import re
import webbrowser
import time

code = r'''
def main():
    x = 2
    print(x)
    y = True
    z = "hola"
    if z != y:
        print("not equal")
    # esto es un comentario
a = {
    "a": 1,
    "b": 2,
    "c": 3
}
if a["a"] >= 1:
    print("greater")

"""
hola esto es otro comentario jalsjda
"""




'''


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
        ('COMMENT', r'#.*'),
        ('LONG_COMMENT', r''),
        ('NUMBER', r'\b\d+'),
        ('STRING', r'"[^"]*"|\'[^\']*\''),
        ('BOOL', r'True|False'),
        ('FLOAT', r'\d+\.\d+'),
        ('EQUALITY', r'[=]'),
        ('INEQUALITY', r'[!=]|[<=]|[>=]|[<]|[>]'),
        ('OPERATOR', r'[+]|[-]|[*]|[/]'),
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*'),
        ('PARENTHESIS', r'([(]|[)])',),
        ('BRACKETS', r'[{]|[}]|[\[]|[\]]'),
        ('COMMA', r'[,]'),
        ('SEMICOLON', r'[;]'),
        ('DOT', r'[.]'),
        ('COLON', r'[:]'),
        ('NEWLINE', r'\n'),
        ('WHITESPACE', r'\s'),
    ]

    # regex de busqueda con identificadores de cada regex
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_especifications)
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
            html_content = py_to_html(value, "RESERVED")
            html_file.write(html_content)
        elif (kind == "NEWLINE"):
            html_file.write("<br>")
        elif (kind == "WHITESPACE"):
            html_file.write("&nbsp;")
        else:
            htmls_content = py_to_html(value, kind)
            html_file.write(htmls_content)


tokenize(code)
html_file.write("</p>")
print("Html generado con exito!")
