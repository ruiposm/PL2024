import re

TOKENS = [
    ('SELECT', r'SELECT'),
    ('FROM', r'FROM'),
    ('WHERE', r'WHERE'),
    ('ID', r'[a-zA-Z_]\w*'), 
    ('NUMBER', r'\d+'), 
    ('VIRGULA', r','),
    ('GREATER_EQUAL', r'>='),
    ('ERROR', r'.')
]


def tokenns(query):
    tokens = []
    query = query.strip()

    while query:
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(query)
            if match:
                value = match.group(0)
                if token_type != 'ERROR':
                    tokens.append((token_type, value))
                query = query[len(value):].strip()
                break
        if not match:
            raise ValueError('Erro de sintaxe: {}'.format(query))
    
    return tokens

def main():
    query = "Select id, nome, salario From empregados Where salario >= 820"
    tokens = tokenns(query)
    print(tokens)

if __name__ == "__main__":
    main()

