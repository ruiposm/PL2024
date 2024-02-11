def ler_dataset(file_path):
    with open("emd.csv", 'r') as file:
        # Lê todas as linhas do arquivo e armazena em uma lista
        lines = file.readlines()
        # Remove o cabeçalho do arquivo e armazena em uma variável
        header = lines.pop(0)
        # Inicializa uma lista para armazenar os dados processados
        data = []
        # Itera sobre as linhas restantes no arquivo
        for line in lines:
            # Divide cada linha em colunas usando a vírgula como separador
            columns = line.strip().split(',')
            # Cria um dicionário para representar cada entrada de dados
            dict = {
                '_id': columns[0],
                'index': int(columns[1]),
                'dataEMD': columns[2],
                'nome_primeiro': columns[3],
                'nome_ultimo': columns[4],
                'idade': int(columns[5]),
                'genero': columns[6],
                'morada': columns[7],
                'modalidade': columns[8],
                'clube': columns[9],
                'email': columns[10],
                'federado': columns[11],
                'resultado': columns[12]
            }
            # Adiciona o dicionário à lista de dados
            data.append(dict)
    # Retorna a lista de dados processados
    return data

def modalidades_ordenadas(data):
    modalidades = set(dict['modalidade'] for dict in data)
    return sorted(modalidades)

def calcular_percentagens_aptidao(data):
    total_atletas = len(data)
    aptos = sum(1 for dict in data if dict['resultado'] == 'true')
    inaptos = total_atletas - aptos
    percent_aptos = (aptos / total_atletas) * 100
    percent_inaptos = (inaptos / total_atletas) * 100
    return percent_aptos, percent_inaptos

def distribuicao_escalao_etario(data):
    distribuicao = {}
    for dict in data:
        idade = dict['idade']
        escalao = (idade // 5) * 5
        if escalao not in distribuicao:
            distribuicao[escalao] = 0
        distribuicao[escalao] += 1
    return distribuicao
# Nome do arquivo
file_name = "emd.csv"

# Ler o dataset
data = ler_dataset(file_name)

# Obter os resultados
modalidades = modalidades_ordenadas(data)
percent_aptos, percent_inaptos = calcular_percentagens_aptidao(data)
distribuicao_escalao = distribuicao_escalao_etario(data)

print("Modalidades ordenadas alfabeticamente:", modalidades)
print("Percentagem de atletas aptos:", percent_aptos)
print("Percentagem de atletas inaptos:", percent_inaptos)
print("Distribuição de atletas por escalão etário:", distribuicao_escalao)