import re

# Definición de tokens
TOKENS = {
    'NUMBER': r'\d+(\.\d*)?',  # Enteros y decimales
    'PLUS': r'\+',             # Suma
    'MINUS': r'-',             # Resta
    'MULTIPLY': r'\*',         # Multiplicación
    'DIVIDE': r'/',            # División
    'LPAREN': r'\(',           # Paréntesis izquierdo
    'RPAREN': r'\)',           # Paréntesis derecho
}

token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENS.items())

def lex(expression):
    for match in re.finditer(token_re, expression):
        token_type = match.lastgroup
        token_value = match.group()
        yield (token_type, token_value)
