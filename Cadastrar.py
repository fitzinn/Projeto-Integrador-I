from BancodeDados.Banco_de_Dados import conectar_bd
from BancodeDados.Criptografia import cripto

#cadastrar ingrediente
def cadastrar_ing():
    print("*********************************************************")
    print("Cadastro de Ingredientes")
    #pega os dados
    nome_ing = str(input("Digite o nome do ingrediente: "))
    preco_ing = int(input("Digite o preço do ingrediente: "))
    fornecedor = int(input("Digite o id do fornecedor do ingrediente: "))
    fabricante = int(input("Digite o id do fabricante do ingrediente: "))
    quant_min = int(input("Digite a quantidade minima de estoque do ingrediente: "))
    quant_max = int(input("Digite a quantidade maxima de estoque do ingrediente: "))
    quant_est = int(input("Digite a quantidade do estoque do ingrediente: "))
    categoria = str(input("Digite a categoria do ingrediente: "))
    data_fab = input("Digite a data de fabricação do ingrediente: ")
    data_val = input("Digite a data de validade do ingrediente: ")

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Ingredientes (id_ing, nome_ing, preco_ing, fornecedor, fabricante, quant_min, quant_max, quant_est, categoria, data_fab, data_val) VALUES (seq_id_ing.NEXTVAL, :1, :2, :3, :4, :5, :6, :7, :8, :9, :10)', (nome_ing, preco_ing, fornecedor, fabricante, quant_min, quant_max, quant_est, categoria, data_fab, data_val))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#cadastrar prato
def cadastrar_prato():
    print("*********************************************************")
    print("Cadastro de Pratos")
    # Pega os dados
    nome_prato = str(input("Digite o nome do prato: "))
    desc_prato = str(input("Digite a descrição do prato: "))
    categoria_prato = str(input("Digite a categoria do prato: "))
    custo_prato = float(input("Digite o custo do prato: "))

    # Criptografa a descrição do prato
    desc_prato_cripto = cripto(desc_prato)

    # Adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Pratos (id_prato, nome_prato, desc_prato, categoria, custo_prato) VALUES (seq_id_prato.NEXTVAL, :1, :2, :3, :4)', (nome_prato, desc_prato_cripto, categoria_prato, custo_prato))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

    # Obtém o ID do prato cadastrado
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT id_prato FROM Pratos WHERE nome_prato = :1 AND desc_prato = :2 AND categoria = :3 AND custo_prato = :4', (nome_prato, desc_prato_cripto, categoria_prato, custo_prato))
    id_prato = cursor.fetchone()[0]

    connection.close()

    calcular_margem(id_prato, custo_prato)

#calcular margem
def calcular_margem(id_prato, custo_produto):
    # Custos fixos
    custo_fixo = 3050

    # Preço de venda
    preco_venda = float(input("PREÇO DE VENDA DESEJADO: "))

    # Cálculo específico para este produto
    custo_fixo_prato = custo_fixo / 225
    imposto = 0.1 * preco_venda
    outros_custos = custo_fixo_prato + imposto + custo_produto
    lucro = preco_venda - outros_custos
    margem = (lucro / preco_venda) * 100

    # Classificação do lucro
    if margem > 20:
        classificacao_lucro = "Alto"
    elif margem > 10:
        classificacao_lucro = "Lucro médio"
    elif margem > 0:
        classificacao_lucro = "Lucro baixo"
    else:
        classificacao_lucro = "Prejuízo"

    inserir_resultados(id_prato, preco_venda, custo_fixo_prato, imposto, margem)
    exibir_tabela_resultados(preco_venda, imposto, outros_custos, margem, classificacao_lucro)

# Funções adicionais para manipulação do banco de dados e exibição dos resultados
def obter_dados_produto():
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT id_prato, nome_prato, desc_prato, custo_prato FROM Pratos')
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

#inserir resultados
def inserir_resultados(id_prato, preco_venda, custo_fixo, imposto, margem):
    connection = conectar_bd()
    cursor = connection.cursor()

    # Inserir na tabela
    cursor.execute('UPDATE Pratos SET preco_venda = :1, custo_fixo = :2, impostos = :3, margem_lucro = :4 WHERE id_prato = :5', (preco_venda, custo_fixo, imposto, margem, id_prato))

    # Commit da transação
    connection.commit()

    cursor.close()
    connection.close()

#exibir tabela
def exibir_tabela_resultados(preco_venda, imposto, outros_custos, margem, classificacao_lucro):
    # Dicionário de cores para classificação de lucro
    cores = {
        "Alto": "\033[92m",  # Verde
        "Lucro médio": "\033[93m",  # Amarelo
        "Lucro baixo": "\033[91m",  # Vermelho
        "Prejuízo": "\033[91m"  # Vermelho
    }

    # Reseta a cor após o texto ser exibido
    reset_cor = "\033[0m"

    print("\n    ****** Tabela de Resultados ******\n")
    print("+-------------------------------------------------+")
    print("| {:<15} | {:<13} | {:<11} |".format("Preço de Venda", "Impostos", "Outros Custos"))
    print("+-------------------------------------------------+")
    print("| R$ {:<12.2f} | R$ {:<10.2f} | R$ {:<10.2f} |".format(preco_venda, imposto, outros_custos))
    print("+-------------------------------------------------+")
    print("| {:<47} |".format("            Margem de Lucro"))
    print("+-------------------------------------------------+")
    print("| {:<45.1f}%  |".format(margem))
    print("+-------------------------------------------------+")
    print("| {:<47} |".format("           Classificação do Lucro"))
    print("+-------------------------------------------------+")
    print("| {:<56} |".format(cores.get(classificacao_lucro, "") + classificacao_lucro + reset_cor))
    print("+-------------------------------------------------+")

#cadastrar fabricante
def cadastrar_fab():
    print("*********************************************************")
    print("Cadastro de Fabricante")
    #pega os dados
    nome_fab = str(input("Digite o nome do fabricante: "))
    tel_fab = int(input("Digite o telefone do fabricante: "))
    email_fab = str(input("Digite o email do fabricante: "))

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Fabricantes (id_fab, nome_fab, tel_fab, email_fab) VALUES (seq_id_fab.NEXTVAL, :1, :2, :3)', (nome_fab, tel_fab, email_fab))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#cadastrar fornecedor
def cadastrar_forn():
    print("*********************************************************")
    print("Cadastro de Fornecedor")
    #pega os dados
    nome_forn = str(input("Digite o nome do fornecedor: "))
    tel_forn = int(input("Digite o telefone do fornecedor: "))
    email_forn = str(input("Digite o email do fornecedor: "))
    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Fornecedores (id_forn, nome_forn, tel_forn, email_forn) VALUES (seq_id_forn.NEXTVAL, :1, :2, :3)', (nome_forn, tel_forn, email_forn))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#cadastrar funcionario e login funcionario
def cadastrar_func():
    print("*********************************************************")
    print("Cadastro de Funcionário")
    #pega os dados
    nome_func = str(input("Digite o nome do funcionario: "))
    data_nasc_func = str(input("Digite a data de nascimento do funcionario: "))
    sal_func = float(input("Digite o salario do funcionario: "))
    data_contrato = str(input("Digite a data do contrato com o funcionario: "))
    categoria_func = str(input("Digite a categoria do funcionario: "))

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Funcionarios (id_func, nome_func, data_nasc_func, sal_func, data_contrato, categoria_func) VALUES (seq_id_func.NEXTVAL, :1, :2, :3, :4, :5)', (nome_func, data_nasc_func, sal_func, data_contrato, categoria_func))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

    email_login = str(input("Digite o email de login do funcionario: "))
    senha_login = str(input("Digite a senha de login do funcionario: "))
    id_func = int(input("Digite o id do funcionário do login a ser cadastrado:"))

    #senha funcionario criptografada
    senha_func_cripto = cripto(senha_login)

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Login_Func (id_login, email_login, senha_login, id_func) VALUES (seq_id_login.NEXTVAL, :1, :2, :3)', (email_login, senha_func_cripto, id_func))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#cadastrar cliente
def cadastrar_cliente():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |         |                |     |")
    print("|HOME|                 |SOBRE NÓS|                |LOGIN|")
    print("|    |                 |         |                |     |")
    print("                                                         ")
    print("                 Cadastro de Cliente                     ")
    print("")
    print("Nome:                                                    ")
    print("Email:                                                   ")
    print("Senha:                                                   ")
    print("*********************************************************")
    nome_cliente = str(input("Digite seu nome: "))
    email_cliente = str(input("Digite seu email: "))
    senha_cliente = str(input("Digite sua senha: "))
    senha_ver = str(input("Digite sua senha mais uma vez: "))
    if senha_cliente != senha_ver:
        print("Senhas nao batem, digite suas informacoes novamente.")
        return cadastrar_cliente()
    else:
        senha_cripto = cripto(senha_cliente)
        connection = conectar_bd()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO login_clientes (id_cliente, nome_cliente, email_cliente, senha_cliente) VALUES (seq_id_cliente.NEXTVAL, :1, :2, :3)', (nome_cliente, email_cliente, senha_cripto))
        print("Cliente Cadastrado com sucesso!")

        connection.commit()
        connection.close()

#cadastrar administrador
def cadastrar_adm():
    print("****************************************************************************")
    print("Cadastro de Administrador")
    #pega os dados
    id_func = int(input("Digite o id do funcionario a virar administrador: "))
    email_adm = str(input("Digite o email do administrador: "))
    senha_adm = str(input("Digite a senha do administrador: "))
    senha_cripto_adm = cripto(senha_adm)

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Login_ADM (id_adm, email_adm, senha_adm, id_func) VALUES (seq_id_adm.NEXTVAL, :1, :2, :3)', (email_adm, senha_cripto_adm, id_func))
    id_func_del = id_func
    cursor.execute('DELETE FROM Login_Func WHERE id_func = :id_func_del', {'id_func_del': id_func_del})
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()