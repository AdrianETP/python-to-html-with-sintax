import re

code = open("code.txt", "r").read()


def py_to_html(value, kind):
    html_content = f"<a class = \"{kind}\" > {value} </a> \n"
    return html_content


html_file = open("index.html", "w")

html_file.write("<link rel=" + "stylesheet" +
                " href=" + "\"style.css\"" + "/>")

html_file.write("<p>")


def syntax(text):
    # palabras reservadas
    reserved_words = {'if', 'raise', 'None', 'del', 'import',
                      'return', 'elif', 'in', 'try', 'and', 'else', 'is',
                      'while', 'as', 'except', 'lambda',
                      'with', 'assert', 'finally', 'nonlocal', 'yield',
                      'break', 'for', 'not', 'class', 'form', 'or',
                      'continue', 'global', 'pass', 'async', 'defer', 'finally',
                      'print', 'def', 'if', 'else'
                      }
    # expresiones regulares
    tokens = [
        ('COMMENT', r'#\s.*'),
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
    regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
    # iteracion de cada palabra para encontrar que tipo de palabra es
    for mo in re.finditer(regex, text):
        # el tipo de la palabra
        kind = mo.lastgroup
        # el valor de la palabra
        value = mo.group()
        if (kind == "IDENTIFIER" and value in reserved_words):
            html_content = py_to_html(value, "RESERVED")
            html_file.write(html_content)
        elif (kind == "NEWLINE"):
            html_file.write("<br>")
        elif (kind == "WHITESPACE"):
            html_file.write("&nbsp;")
        else:
            htmls_content = py_to_html(value, kind)
            html_file.write(htmls_content)


syntax(code)
html_file.write("</p>")
print("Html generado con exito!")
