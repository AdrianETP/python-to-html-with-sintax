import re
import webbrowser
import time

code = """
def main():
    x = 2
    print(x)
"""


def py_to_html(value, kind):
    html_content = f"<a class = \"{kind}\" > {value} </a> \n"
    return html_content


html_file = open("index.html", "w")

html_file.write("<link rel=" + "stylesheet" +
                " href=" + "\"style.css\"" + "/>")

html_file.write("<p>")


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
        ('EQUALITY', r'[=]'),
        ('INEQUALITY', r'[!=]|[<=]|[>=]|[<]|[>]'),
        ('OPERATOR', r'[+]|[-]|[*]|[/]'),
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*'),
        ('PARENTHESIS', r'([(]|[)])',),
        ('BRACKETS', r'[{]|[}]|[\[][\]]'),
        ('NEWLINE', r'\n'),
        ('WHITESPACE', r'\s'),
    ]
    x = True
    # regex de busqueda con identificadores de cada regex
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_especifications)
    print("kind, value , Start, End")
    print("---------------------------------")
    # iteracion de cada palabra para encontrar que tipo de palabra es
    for mo in re.finditer(tok_regex, text):
        # el tipo de la palabra
        kind = mo.lastgroup
        # el valor de la palabra
        value = mo.group()
        # donde inicia de todo el texto
        start = mo.start()
        # donde termina
        end = mo.end()
        if (kind == "IDENTIFIER" and value in keywords):
            print("RESERVED", value, start, end)
            html_content = py_to_html(value, "RESERVED")
            html_file.write(html_content)
        elif (kind == "NEWLINE"):
            print("NEWLINE", value, start, end)
            html_file.write("<br>")
        elif (kind == "WHITESPACE"):
            print("WHITESPACE", value, start, end)
            html_file.write("&nbsp;")
        else:
            print(kind, value, start, end)
            htmls_content = py_to_html(value, kind)
            html_file.write(htmls_content)


tokenize(code)
html_file.write("</p>")
