import json

class VendingMachine:
    def __init__(self):
        self.stock = self.load_stock()
        self.saldo = 0

    def load_stock(self):
        try:
            with open("stock.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Erro: Ficheiro de stock não encontrado.")
            return []

    def update_stock(self):
        with open("stock.json", "w") as file:
            json.dump(self.stock, file)

    def listar_produtos(self):
        print("cod | nome | quantidade | preço")
        print("-" * 35)
        for produto in self.stock:
            print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}")

    def adicionar_moeda(self, moeda):
        try:
            valor = self.parse_moeda(moeda)
            self.saldo += valor
            print(f"Saldo = {self.format_moeda(self.saldo)}")
        except ValueError:
            print("Erro: Moeda inválida.")

    def selecionar_produto(self, codigo):
        produto = next((p for p in self.stock if p['cod'] == codigo), None)
        if produto:
            if self.saldo >= produto['preco'] and produto['quant'] > 0:
                self.saldo -= produto['preco']
                produto['quant'] -= 1
                print(f"Pode retirar o produto dispensado \"{produto['nome']}\"")
                print(f"Saldo = {self.format_moeda(self.saldo)}")
            elif self.saldo < produto['preco']:
                print(f"Saldo insuficiente para satisfazer o seu pedido")
                print(f"Saldo = {self.format_moeda(self.saldo)}; Pedido = {self.format_moeda(produto['preco'])}")
            else:
                print("Produto esgotado.")
        else:
            print("Produto não encontrado.")

    def sair(self):
        troco = self.saldo
        moedas = []
        while troco > 0:
            if troco >= 100:
                moedas.append("1€")
                troco -= 100
            elif troco >= 50:
                moedas.append("50c")
                troco -= 50
            elif troco >= 20:
                moedas.append("20c")
                troco -= 20
            elif troco >= 10:
                moedas.append("10c")
                troco -= 10
            elif troco >= 5:
                moedas.append("5c")
                troco -= 5
            elif troco >= 2:
                moedas.append("2c")
                troco -= 2
            elif troco >= 1:
                moedas.append("1c")
                troco -= 1

        print("Pode retirar o troco:", ", ".join(moedas))
        print("Até à próxima")

    def parse_moeda(moeda_str):
        valores = {'1e': 100, '50c': 50, '20c': 20, '10c': 10, '5c': 5, '2c': 2, '1c': 1}
        return valores[moeda_str]

        def format_moeda(valor):
        return f"{valor // 100}e{valor % 100}c"

if __name__ == "__main__":
    maquina = VendingMachine()
    print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ").strip().upper()
        if comando == "LISTAR":
            maquina.listar_produtos()
        elif comando.startswith("MOEDA"):
            moeda = comando.split()[1]
            maquina.adicionar_moeda(moeda)
        elif comando.startswith("SELECIONAR"):
            codigo = comando.split()[1]
            maquina.selecionar_produto(codigo)
        elif comando == "SAIR":
            maquina.sair()
            maquina.update_stock()
            break
        else:
            print("Erro.")
