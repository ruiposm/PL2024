Construir um programa que simule uma máquina de vending.
A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.
stock = [
 {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
 ...
]
Podes persistir essa lista num ficheiro em JSON que é carregado no arranque do programa e é atulizado
quando o programa termina.
A seguir apresenta-se um exemplo de uma interação com a máquina, assim que esta é ligada, para que
possas perceber o tipo de comandos que a máquina aceita:
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade |  preço
---------------------------------
A23 água 0.5L 8 0.7
...
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SELECIONAR A23
maq: Saldo insufuciente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c
>> ...
...
maq: Saldo = 74c
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
maq: Até à próxima

