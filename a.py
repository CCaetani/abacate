''''''''''''''''''''''
receita1 = float(input("Digite sua primeira receita"))
receita2 = float(input("Digite sua segunda receita"))
receita3 = float(input("Digite sua terceira receita"))
despesa1 = float(input("Digite sua primeira despesa"))
despesa2 = float(input("Digite sua primeira despesa"))
despesa3 = float(input("Digite sua primeira despesa"))

receita_geral = receita1 + receita2 + receita3
despesa_geral = despesa1 + despesa2 + despesa3
saldo = receita_geral - despesa_geral

total_receita1 = receita1 / receita_geral * 100
total_receita2 = receita2 / receita_geral * 100
total_receita3 = receita3 / receita_geral * 100

total_despesa1 = despesa1 / despesa_geral * 100
total_despesa2 = despesa2 / despesa_geral * 100
total_despesa3 = despesa3 / despesa_geral * 100


print("Bem-vindo ao sistema de gerenciamento de finanças pessoas!\n")

print("Você irá cadastrar receitas e despesas, calcular o saldo e gerar um relatorio detalhado\n")

print("Seu saldo total é\n", saldo)
input("Deseja receber as despesas?, clique qualquer numero")
print("despesa de receita", total_receita1,"%", total_receita2,"%", total_receita3, "%")
print("despesa de despesa", total_despesa1,"%", total_despesa2,"%", total_despesa3, "%")

input("Deseja receber o relatorio completo?")
print("total de reseita", receita_geral, "total de despesas", despesa_geral, "saldo", saldo, "despesa de receita",  total_receita1,"%" , total_receita2,"%", total_receita3,"%", "despesa de despesa", total_despesa1,"%", total_despesa2,"%", total_despesa3, "%")
'''''''''''