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