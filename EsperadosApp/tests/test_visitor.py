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
False\nFalse\nTrue\nFalse\nTrue\nFalse\n👋 Adiau!\n""" #FIXME
    assert expected == captured.out

def test_operations(capsys):
    with open(f"tests/examples/expressions/all_operations.es") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    expected = """👋 Saluton!\nhe cos
10.8\n2\n11\n6\n4\n5.5\n0.8\n0\n-7
-1.0\n2\n2.2\n7.5\n1\n6\n8.75\n3\n4.5
2.0\n1.0\n4.0\n11.0\n3.0\n2.0
0.5\n0\n2\n2.5\n0\n1.0
3.0\n1\n8\n0.8\n3\n1.0\n👋 Adiau!\n""" #FIXME
    assert expected == captured.out

@pytest.mark.parametrize("filename, expected", [
    ("expressions/compare_except_str_and_int.es", "Can't compare 'str' and 'int'"),
    ("expressions/compare_except_str_and_bool.es", "Can't compare 'str' and 'bool'"), #FIXME
    ("expressions/compare_except_float_and_str.es", "Can't compare 'float' and 'str'"),
    ("expressions/add_exceptions_str_int.es", "Can't add two different types: str + int"),
    ("expressions/add_exceptions_str_float.es", "Can't add two different types: str + float"),
    ("expressions/add_exceptions_str_bool.es", "Can't add two different types: str + bool"),
    ("expressions/sub_exceptions_str_str.es", "Can't substract two string types: str - str"), #FIXME 
    ("expressions/sub_exceptions_str_int.es", "Can't substract two different types: str - int"),
    ("expressions/sub_exceptions_str_float.es", "Can't substract two different types: str - float"),
    ("expressions/sub_exceptions_str_bool.es", "Can't substract two different types: bool - str"),
    ("expressions/multi_exceptions_str_str.es", "Can't multiply non-number types: str * str"),
    ("expressions/multi_exceptions_str_int.es", "Can't multiply non-number types: str * int"),
    ("expressions/multi_exceptions_str_float.es", "Can't multiply non-number types: str * float"),
    ("expressions/multi_exceptions_str_bool.es", "Can't multiply non-number types: str * bool"),
    ("expressions/divide_exceptions_str_str.es", "Can't divide non-number types: str / str"),
    ("expressions/divide_exceptions_str_int.es", "Can't divide non-number types: str / int"),
    ("expressions/divide_exceptions_str_float.es", "Can't divide non-number types: str / float"),
    ("expressions/divide_exceptions_str_bool.es", "Can't divide non-number types: str / bool"),
    ("expressions/divide_exceptions_false.es", "Division by zero is not allowed!"),
    ("expressions/divide_exceptions_zero.es", "Division by zero is not allowed!"),
    ("expressions/mod_exceptions_str_str.es", "Modulo operation requires numbers: str % str"),
    ("expressions/mod_exceptions_str_int.es", "Modulo operation requires numbers: str % int"),
    ("expressions/mod_exceptions_str_float.es", "Modulo operation requires numbers: str % float"),
    ("expressions/mod_exceptions_str_bool.es", "Modulo operation requires numbers: str % bool"),
    ("expressions/mod_exceptions_false.es", "Modulo by zero is not allowed!"),
    ("expressions/mod_exceptions_zero.es", "Modulo by zero is not allowed!"),
    ("expressions/expon_exceptions_bool_str.es", "Cannot exponentiate non-numeric type: str"), #FIXME
    ("expressions/expon_exceptions_int_str.es", "Cannot exponentiate non-numeric type: str"), #FIXME
    ("expressions/expon_exceptions_float_str.es", "Cannot exponentiate non-numeric type: str"), #FIXME
    ("expressions/expon_exceptions_str_int.es", "Cannot exponentiate non-numeric type: str"),
])

def test_invalid_expressions_raise_exception(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        _ = run_code(code)
    assert expected in str(exc_info.value)

# =========================
# Control Structures
# =========================

# =========================
# If-Elif_Else
# =========================

@pytest.mark.parametrize("filename, expected", [
    ("if_statement/correct_if.es", "if"),
    ("if_statement/correct_elif.es", "elif"),
    ("if_statement/correct_else.es", "else"),
])

def test_if_statement(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['result'] == expected

# =========================
# For
# =========================

@pytest.mark.parametrize("filename, expected", [
    ("for_loop/correct_asc_for.es", 6),
    ("for_loop/correct_desc_for.es", 0),
    ("for_loop/for_in_for.es", -20),
    ("for_loop/break_statement.es", 21),
    ("for_loop/continue_statement.es", 15),
])

def test_for_loop(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['sum'] == expected

@pytest.mark.parametrize("filename, expected", [
    ("for_loop/for_exceptions_existing_var.es", "Variable name i is already in use"),
    ("for_loop/for_exceptions_str.es", "Value string Lol is not a numberic type and cannot be used in for loop parameters"),
])

def test_for_exceptions(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        run_code(code)
    assert expected in str(exc_info.value)

def test_for_warnings(capsys):
    with open(f"tests/examples/for_loop/wrong_step.es") as f:
        code = f.read()
    with pytest.warns(RuntimeWarning) as record:
        run_code(code)
    assert any("Params start: 0, end: 5, step: -1 are not executable" in str(w.message) for w in record)

# =========================
# While
# =========================

@pytest.mark.parametrize("filename, expected", [
    ("while_loop/correct_while.es", 66),
    ("while_loop/while_in_while.es", 27),
    ("while_loop/neg_condition.es", 0),
    ("while_loop/break_statement.es", 6),
    ("while_loop/continue_statement.es", 15),
])

def test_while_loop(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['sum'] == expected

# =========================
# For each
# =========================

@pytest.mark.parametrize("filename, expected", [
    ("foreach_loop/correct_foreach.es", 10),
    ("foreach_loop/for_str.es", "string do dodania"),
    ("foreach_loop/for_different_types.es", True),
    ("foreach_loop/break_statement.es", 0),
    ("foreach_loop/continue_statement.es", 0),
])

def test_foreach_loop(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['sum'] == expected

@pytest.mark.parametrize("filename, expected", [
    ("foreach_loop/non_exist_lista.es", "Object lista is not iterable"), #FIXME
])

def test_foreach_exceptions(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        run_code(code)
    assert expected in str(exc_info.value)

# =========================
# Functions
# =========================

@pytest.mark.parametrize("filename, expected", [
    ("functions/function_call.es", 15),
    ("functions/function_without_params.es", "wynik"),
    ("functions/function_one_param.es", "jeden"),
    ("functions/multi_call.es", "czwarty"),
    ("functions/recursion.es", 5040),
    ("functions/fun_in_fun.es", 9),
    ("functions/fun_call_other_fun.es", 15),
    ("functions/first_class_fun.es", "Saluton: Imie"),
    ("functions/loop_fun_call.es", 6),
    ("functions/fun_in_condition.es", "-"),
    ("functions/return_in_loop.es", 0),
])

def test_function_def_call(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_vars['result'] == expected

@pytest.mark.parametrize("filename, expected", [
    ("functions/used_parameter_name.es", "Parameter name 'a' is already used in this function definition"),
    ("functions/non_existing_fun.es", "Function 'fun2' is not defined."),
    ("functions/non_existing_param.es", "Parameter name does not apear in function definition"),
    ("functions/require_arguments.es", "Function require parameters: ['nazwa']"),
    ("functions/redefinition.es", "Function fun1 is already defined"),
])

def test_fun_exceptions(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        run_code(code)
    assert expected in str(exc_info.value)

# =========================
# Lists
# =========================

@pytest.mark.parametrize("filename, expected", [
    ("lists/list_def.es", [1, 2, 3, "4"]),
    ("lists/empty_list.es", []),
    ("lists/add_to_list.es", [1, 2, 4, 9]),
    ("lists/add_list_to_list.es", ['lista', ['kolejna', 'lista']]),
    ("lists/insert_val.es", [1, 2, 3, 4, 4, 5]),
    ("lists/replace_val.es", [1, 2, 3, 1, 5]),
    ("lists/remove_val.es", [1, 2, 4, 5]),
])

def test_list_operations(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    visitor = run_code(code)
    assert visitor.global_lists['result'] == expected

@pytest.mark.parametrize("filename, expected", [
    ("lists/add_to_non_list.es", "List 'result' is not defined"),
    ("lists/insert_str_index.es", "Index in insert function must be numeric"), #FIXME
    ("lists/insert_non_existing_list.es", "List 'result2' is not defined"),
    ("lists/replace_non_list.es", "Struct 'result2' is not defined"),
    ("lists/replace_str_index.es", "Index in replace function must be numeric"), #FIXME
    ("lists/replace_outofrange.es", "List index out of range: -1"),
    ("lists/print_outofrange.es", "List index out of range. result length: 5"),
    ("lists/remove_non_exist_val.es", "Element '0' not found in list 'result'"),
    ("lists/remove_non_exist_list.es", "List 'result2' is not defined"),
])

def test_lists_exceptions(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        run_code(code)
    assert expected in str(exc_info.value)

# dotąd ok
# słowniki

# =========================
# Dictionaries
# =========================