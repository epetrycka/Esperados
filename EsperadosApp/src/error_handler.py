import re
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

class ErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if str(msg).count('no viable alternative at input'):
            if match := re.search(r"['].*[']", msg):
                error_msg = f"\033[91mERRORE: linea {line}:{column} - syntax error at {match.group()}\033[0m"
            else:
                error_msg = f"\033[91mERRORE: linea {line}:{column} - {msg}\033[0m"
        elif re.search(r"extraneous input.*Saluton.*", msg):
            error_msg = f"\033[91mERRORE: linea {line}:{column} - program must begin with Saluton\033[0m"
        elif re.search(r"extraneous input.*Adiau.*", msg):
            error_msg = f"\033[91mERRORE: linea {line}:{column} - program must end with Adiau\033[0m"
        elif re.search(r"token recognition error at: '\".*\\n'", msg):
            error_msg = f"\033[91mERRORE: linea {line}:{column} - missing (\")\033[0m"
        elif re.search(r"mismatched input '.*' expecting \{.*\}", msg):
            error_msg = f"\033[91mERRORE: linea {line}:{column} - incomplete or incorrect sentence\033[0m"
        else:
            error_msg = f"\033[91mERRORE: linea {line}:{column} - {msg}\033[0m"

        raise Exception(error_msg)