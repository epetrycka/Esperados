from antlr4 import *
from src.generated.EsperadosLexer import EsperadosLexer
from src.generated.EsperadosParser import EsperadosParser
from src.visitor import EsperadosVisitorImpl
from src.error_handler import ErrorListener
import pytest
from unittest.mock import patch

def run_code(code: str, mock_inputs=None):
    input = InputStream(code)
    lexer = EsperadosLexer(input)
    stream = CommonTokenStream(lexer)
    parser = EsperadosParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ErrorListener())
    tree = parser.program()
    visitor = EsperadosVisitorImpl()
    if mock_inputs:
        with patch('builtins.input', side_effect=mock_inputs):
            visitor.visit(tree)
    else:
        visitor.visit(tree)
    return visitor

def test_empty_file(capsys):
    with open("tests/examples/incomplete_files/empty_file.es") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_correct_empty_file(capsys):
    with open(f"tests/examples/incomplete_files/correct_empty_file.es") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    assert captured.out == "👋 Saluton!\n👋 Adiau!\n"

# =========================
# Grammar structure
# =========================

@pytest.mark.parametrize("filename, expected", [
    ("incomplete_files/without_adiau.es", "program must end with Adiau"),
    ("incomplete_files/without_saluton.es", "program must begin with Saluton"),
    ("incomplete_files/adiau_before_saluton.es", "program must begin with Saluton"),
])

def test_saluton_adiau(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        run_code(code)
    assert expected in str(exc_info.value)

# =========================
# Print function
# =========================

@pytest.mark.parametrize("filename, expected", [
    ("print_statement/simple_print.es", "Prosty print"),
    ("print_statement/print_with_few_elements.es", "Print z kilkoma danymi po przecinku"),
    ("print_statement/print_variable_from_memory.es", "Wypisywanie zmiennej 52.8 z pamieci"),
])

def test_print_statements(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    assert expected in captured.out

# =========================
# Variables Definitions
# =========================

@pytest.mark.parametrize("filename, name, expected, type", [
    ("variable_definition/temp_variable_def.es", "x", 42, "t"),
    ("variable_definition/global_variable_def.es", "zmienna", 5.8, "g"),
])

def test_variable_def(filename, name, expected, type, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    visitor = run_code(code)
    if type == "g":
        assert name in visitor.global_vars
        assert visitor.global_vars[name] == expected
    elif type == "t":
        assert name in visitor.temp_vars[-1]
        assert visitor.temp_vars[-1][name] == expected

def test_variable_from_input(capsys):
    with open(f"tests/examples/variable_definition/variable_from_input.es") as f:
        code = f.read()
    visitor = run_code(code, mock_inputs=["Hello!"])
    assert 'input' in visitor.temp_vars[-1]
    assert visitor.temp_vars[-1]['input'] == "Hello!"

def test_first_class_functions(capsys):
    with open(f"tests/examples/variable_definition/first_class_functions.es") as f:
        code = f.read()
    visitor = run_code(code)
    captured = capsys.readouterr()
    assert 'Saluton: Imie' in captured.out
    assert 'x' in visitor.temp_vars[-1]
    assert 'salutu' in visitor.functions

def test_no_access_out_of_scope(capsys):
    with open(f"tests/examples/variable_definition/no_access_outofscope.es") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        _ = run_code(code)
    assert "Variable 'x' is not defined" in str(exc_info.value)

def test_overwritting_variables(capsys):
    with open(f"tests/examples/variable_definition/overwritting_global.es") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        _ = run_code(code)
    assert "Variable name x is already in use" in str(exc_info.value)

# =========================
# Delete Statement
# =========================

@pytest.mark.parametrize("filename, name, expected, type", [
    ("delete_statement/correct_delete_temp.es", "x", "423", "t"),
    ("delete_statement/correct_delete_global.es", "y", "Hej", "g"),
])

def test_delete_statement_correct(filename, name, expected, type, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    visitor = run_code(code)
    captured = capsys.readouterr()
    if type == "g":
        assert name not in visitor.global_vars
        assert expected in captured.out
    elif type == "t":
        assert name not in visitor.temp_vars[-1]
        assert expected in captured.out

def test_delete_statement_incorrect(capsys):
    with open(f"tests/examples/delete_statement/delete_non_exist.es") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        run_code(code)
    assert "Variable 'y' is not defined" in str(exc_info.value)

# =========================
# Expressions
# =========================

def test_logical_expressions(capsys):
    with open(f"tests/examples/expressions/all_expressions.es") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    expected = """👋 Saluton!\nTrue\nTrue\nTrue
True\nTrue\nTrue\nFalse\nTrue\nTrue
True\nTrue\nTrue\nFalse\nTrue\nTrue
True\nFalse\nTrue\nFalse\nTrue\nTrue
True\nFalse\nTrue\n3\n0\n4\n2\nTrue
False\nTrue\nFalse\n0\nTrue\nTrue\nTrue
False\nFalse\nTrue\nFalse\nTrue\nTrue\n👋 Adiau!\n"""
    assert expected == captured.out

def test_operations(capsys):
    with open(f"tests/examples/expressions/all_operations.es") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    expected = """👋 Saluton!\nhe cos
10.8\n2\n11\n6\n4\n👋 Adiau!\n"""
    assert expected == captured.out

@pytest.mark.parametrize("filename, expected", [
    ("expressions/compare_str_and_bool.es", "Can't compare 'str' and 'bool'"),
    ("expressions/compare_str_and_int.es", "Can't compare 'str' and 'int'"),
    ("expressions/compare_float_and_str.es", "Can't compare 'float' and 'str'"),
    ("expressions/add_exceptions_str_int.es", "Can't add two different types: str + int"),
    ("expressions/add_exceptions_str_float.es", "Can't add two different types: str + float"),
    ("expressions/add_exceptions_str_bool.es", "Can't add two different types: str + bool"),
])

def test_invalid_expressions_raise_exception(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        _ = run_code(code)
    assert expected in str(exc_info.value)

# dotąd ok

# =========================
# Control Structures
# =========================

def test_if_statement():
    with open("tests/examples/control_structures/simple_if.es") as f:
        code = f.read()
    visitor = run_code(code)
    assert 'a' not in visitor.temp_vars[-1]
    assert visitor.temp_vars[-1]['b'] == 2

def test_elif_else_statement():
    with open("tests/examples/control_structures/elif_else.es") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['result'] == "if"

def test_for_loop():
    with open("tests/examples/control_structures/for_loop.es") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['sum'] == 10

def test_while_loop():
    with open("tests/examples/control_structures/while_loop.es") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['i'] == 5

def test_foreach_loop():
    with open("tests/examples/control_structures/foreach_loop.es") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['sum'] == 6

# =========================
# Functions
# =========================

def test_function_def_call():
    with open("tests/examples/functions/function_call.es") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.temp_vars[-1]['result'] == 15

# =========================
# Lists
# =========================

# def test_list_operations():
#     with open("tests/examples/lists/list_ops.es") as f:
#         code = f.read()
#     visitor = run_code(code)
#     assert visitor.global_lists['l'][0] == 0
#     assert 1 not in visitor.global_lists['l']