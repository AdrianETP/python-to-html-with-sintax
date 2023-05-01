import re

code = """
def main():
    x = 2
    print(x)
"""


def tokenize(text):
    # palabras reservadas
    keywords = {'if', 'raise', 'None', 'del', 'import',
                'return', 'elif', 'in', 'try', 'and', 'else', 'is',
                'while', 'as', 'except', 'lambda',
                'with', 'assert', 'finally', 'nonlocal', 'yield',
                'break', 'for', 'not', 'class', 'form', 'or',
                'continue', 'global', 'pass', 'async', 'defer', 'finally',
                'print', 'def', 'if', 'else'
                }
    # expresiones regulares
    token_especifications = [
        ('NUMBER', r'\b\d+'),
        ('STRING', r'"[^"]*"|\'[^\']*\''),
        ('BOOL', r'True|False'),
        ('FLOAT', r'\d+\.\d+'),
        ('EQUALITY', r'='),
        ('INEQUALITY', r'[!=]|[<=]|[>=]|[<]|[>]'),
        ('OPERATOR', r'[+]|[-]|[*]|[/]'),
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*'),
        ('PARENTHESIS', r'([(]|[)])',)
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_especifications)
    print("kind, value , Start, End")
    print("---------------------------------")
    for mo in re.finditer(tok_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        start = mo.start()
        end = mo.end()
        if (kind == "IDENTIFIER" and value in keywords):
            print("RESERVED", value, start, end)
        else:
            print(kind, value, start, end)


tokenize(code)
