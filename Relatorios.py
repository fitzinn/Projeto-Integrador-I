import datetime
from tabulate import tabulate
from BancodeDados.Banco_de_Dados import conectar_bd

def consultar_estoque():
    try:
        connection = conectar_bd()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id_ing, nome_ing, quant_est, data_fab, data_val
            FROM Ingredientes
            """)
        estoque = cursor.fetchall()
        
        cursor.close()
        connection.close()

        # Adicionando depuração para verificar os dados recuperados
        print("\nDados recuperados do estoque:\n\n")
        print(tabulate(estoque, headers=["ID", "Nome", "Quantidade", "Data de Fabricação", "Data de Validade"], tablefmt="grid"))
        
    except Exception as e:
        print("\nErro ao consultar o estoque:\n", e)

def gerar_relatorio_vendas(data_venda):
    try:
        connection = conectar_bd()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT TO_CHAR(pa.data_pagamento, 'YYYY-MM-DD') as data_pagamento, 
                   p.nome_prato, 
                   pa.valor_pagamento 
            FROM pratos p 
            JOIN pagamentos pa ON pa.id_prato = p.id_prato 
            WHERE TRUNC(pa.data_pagamento) = TO_DATE(:data_venda, 'YYYY-MM-DD')
            """, {'data_venda': data_venda})
        vendas = cursor.fetchall()
        
        cursor.close()
        connection.close()

        if not vendas:
            print(f"\nNão há lançamentos de vendas para a data: {data_venda}\n")
            return

        # Definindo cabeçalho e linhas
        headers = ["Data", "Prato", "Valor"]
        
        # Calculando o total das vendas
        total_vendas = sum(venda[2] for venda in vendas)

        # Adicionando uma linha para o total na tabela
        vendas.append(("Total", "", total_vendas))

        # Exibindo o relatório
        print(f"\nRelatório de Vendas - Data: {data_venda}\n")
        print(tabulate(vendas, headers=headers, tablefmt="grid"))
    except Exception as e:
        print("\nErro ao gerar relatório de vendas:\n", e)

def calcular_lucro_periodo(data_inicio, data_fim):
    try:
        connection = conectar_bd()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT TO_CHAR(pa.data_pagamento, 'YYYY-MM-DD') as data_pagamento, 
                   LISTAGG(p.nome_prato, ', ') WITHIN GROUP (ORDER BY p.nome_prato) as pratos_vendidos, 
                   SUM(pa.valor_pagamento) as total_vendas 
            FROM pratos p 
            JOIN pagamentos pa ON pa.id_prato = p.id_prato 
            WHERE pa.data_pagamento BETWEEN TO_DATE(:data_inicio, 'YYYY-MM-DD') AND TO_DATE(:data_fim, 'YYYY-MM-DD')
            GROUP BY pa.data_pagamento
            """, {'data_inicio': data_inicio, 'data_fim': data_fim})
        vendas = cursor.fetchall()

        cursor.close()
        connection.close()

        if not vendas:
            print(f"\nNão há vendas registradas no período de {data_inicio} a {data_fim}.\n")
            return

        # Definindo cabeçalho e linhas para as vendas
        headers_vendas = ["Data", "Pratos Vendidos", "Total Vendas"]
        
        # Adicionando o total de vendas ao final da lista de vendas
        total_vendas = sum(venda[2] for venda in vendas)
        vendas.append(("Total", "", total_vendas))
        
        # Exibindo as vendas em uma tabela
        print("\nRelatório de Vendas no Período:")
        print(tabulate(vendas, headers=headers_vendas, tablefmt="grid"))

    except Exception as e:
        print("\nErro ao calcular lucro no período:\n", e)

def validar_data(data):
    try:
        datetime.datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def menu():
    print("\nMENU:")
    print("1. Consultar Estoque")
    print("2. Gerar Relatório de Vendas por Data")
    print("3. Calcular Lucro em um Período")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = str(input("\nEscolha uma opção: "))
        op = opcao.upper()

        if opcao == "1" or op == "CONSULTAR" or op == "CONSULTAR ESTOQUE" or op == "ESTOQUE":
            consultar_estoque()
        elif opcao == "2" or op == "VENDAS" or op == "RELATORIO VENDAS":
            while True:
                data = str(input("\n\nQual a data a ser consultada?\nDigite no formato YYYY-MM-DD: "))
                saida = data.upper()
                if saida == "SAIR":
                    break
                else:
                    if validar_data(data):
                        gerar_relatorio_vendas(data)
                    else:
                        print("Data inválida. Por favor, insira a data no formato YYYY-MM-DD.\n")
        elif opcao == "3" or op == "CALCULAR LUCRO" or op == "LUCRO":
            data_inicio = str(input("\n\nQual a data de início do período a ser consultado?\nDigite no formato YYYY-MM-DD: "))
            sair = data_inicio.upper()
            if sair == "SAIR":
                break
            else:
                data_fim = str(input("\nQual a data de término do período a ser consultado?\nDigite no formato YYYY-MM-DD: "))
                sairdois = data_fim.upper()
                if sairdois == "SAIR":
                    break
                else:
                    if validar_data(data_inicio) and validar_data(data_fim):
                        calcular_lucro_periodo(data_inicio, data_fim)
                    else:
                        print("Data inválida. Por favor, insira as datas no formato YYYY-MM-DD.\n")
        elif opcao == "0" or op == "SAIR":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")