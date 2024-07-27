from BancodeDados.Banco_de_Dados import conectar_bd
from BancodeDados.Criptografia import cripto
from Listar import listar_login, listar_prato_adm, listar_forn, listar_fab, listar_func, listar_adm, listar_clientes, listar_ing

def alterar_ing():
    """
    Altera os dados de um ingrediente no banco de dados.

    Funções chamadas:
    - listar_ing(): Lista todos os ingredientes existentes.

    Etapas:
    - Exibe o layout para alterar dados de ingredientes.
    - Solicita ao usuário o ID do ingrediente a ser alterado.
    - Solicita os novos dados do ingrediente.
    - Conecta ao banco de dados e atualiza o registro com os novos dados.
    - Confirma a alteração e fecha a conexão com o banco.
    """
    print("*********************************************************")
    print("Alterar dados - Ingredientes")
    listar_ing()#lista ingredientes para escolher qual alterar

    id_ing_alt = int(input("Digite o id do ingrediente que deseja alterar: "))

    #pega os dados
    novo_id = input("Novo id do ingrediente: ")
    novo_nome = input("Novo nome do ingrediente: ")
    novo_preco = input("Novo preço do ingrediente: ")
    novo_forn = input("Novo fornecedor do ingrediente: ")
    novo_fab = input("Novo fabricante do ingrediente: ")
    novo_min = input("Nova quantidade minima do ingrediente: ")
    novo_max = input("Nova quantidade máxima do ingrediente: ")
    novo_est = input("Nova quantidade estoque do ingrediente: ")
    novo_categoria = input("Nova categoria do ingrediente: ")
    novo_data_fab = input("Nova data fabricação do ingrediente: ")
    novo_data_val = input("Nova data validade do ingrediente: ")

    #adiciona ao banco
    connection = conectar_bd()#conecta no banco
    cursor = connection.cursor()

    #altera todos os dados do ingrediente escolhido
    cursor.execute('''
        UPDATE Ingredientes 
        SET id_ing = :novo_id, nome_ing = :novo_nome, preco_ing = :novo_preco,
        fornecedor = :novo_forn, fabricante = :novo_fab, quant_min = :novo_min,
        quant_max = :novo_max, quant_est = :novo_est, categoria = :nova_categoria,
        data_fab = :novo_data_fab, data_val = :novo_data_val 
        WHERE id_ing = :id_ing_alt
    ''', {'novo_id': novo_id, 'novo_nome': novo_nome, 'novo_preco': novo_preco, 
          'novo_forn': novo_forn, 'novo_fab': novo_fab, 'novo_min': novo_min,
           'novo_max': novo_max, 'novo_est': novo_est, 'nova_categoria': novo_categoria,
            'novo_data_fab': novo_data_fab, 'novo_data_val': novo_data_val , 'id_ing_alt': id_ing_alt})

    print("Alterado com sucesso!")

    connection.commit()#salva alterações
    connection.close()#fecha conecxão

def alterar_prato():
    """
    Altera os dados de um prato no banco de dados.

    Funções chamadas:
    - listar_prato_adm(): Lista todos os pratos existentes.

    Etapas:
    - Exibe o layout para alterar dados de pratos.
    - Solicita ao usuário o ID do prato a ser alterado.
    - Solicita os novos dados do prato.
    - Conecta ao banco de dados e atualiza o registro com os novos dados.
    - Confirma a alteração e fecha a conexão com o banco.
    """
    print("****************************************************************************")
    print("Pratos")
    listar_prato_adm()#lista pratos para escolher qual alterar

    id_prato_alt = int(input("Digite o id do prato que deseja alterar: "))

    #novos dados do prato
    novo_id = input("Novo id do prato: ")
    novo_nome = input("Novo nome do prato: ")
    nova_descricao = input("Nova descrição do prato: ")
    nova_desc_cripto = cripto(nova_descricao)
    nova_categoria = input("Nova categoria do prato: ")
    novo_custo = float(input("Novo preço do prato: "))

    #alterar dados no banco de dados
    connection = conectar_bd()#conecta no banco
    cursor = connection.cursor()

    #altera todos os dados do prato escolhido
    cursor.execute('''
        UPDATE Pratos 
        SET id_prato = :novo_id, nome_prato = :novo_nome, desc_prato = :nova_descricao, categoria = :nova_categoria, custo_prato = :novo_custo 
        WHERE id_prato = :id_prato_alt
    ''', {'novo_id': novo_id, 'novo_nome': novo_nome, 'nova_descricao': nova_desc_cripto, 'nova_categoria': nova_categoria, 'novo_custo': novo_custo, 'id_prato_alt': id_prato_alt})

    print("Alterado com sucesso!")

    connection.commit()#salva alterações
    connection.close()#fecha conecxão

def alterar_fab():
    """
    Altera os dados de um fabricante no banco de dados.

    Funções chamadas:
    - listar_fab(): Lista todos os fabricantes existentes.

    Etapas:
    - Exibe o layout para alterar dados de fabricantes.
    - Solicita ao usuário o ID do fabricante a ser alterado.
    - Solicita os novos dados do fabricante.
    - Conecta ao banco de dados e atualiza o registro com os novos dados.
    - Confirma a alteração e fecha a conexão com o banco.
    """
    print("****************************************************************************")
    print("Fabricantes")
    listar_fab()#lista fabricantes para escolher qual alterar

    id_fab_alt = int(input("Digite o id do fabricante que deseja alterar: "))

    #novos dados do fabricante
    novo_id = input("Novo id do fabricante: ")
    novo_nome = input("Novo nome do fabricante: ")
    novo_email = input("Novo email do fabricante: ")
    novo_tel = input("Novo telefone do fabricante: ")

    #alterar dados no banco de dados
    connection = conectar_bd()#conecta no banco
    cursor = connection.cursor()

    #altera todos os dados do fabricante escolhido
    cursor.execute('''
        UPDATE Fabricantes 
        SET id_fab = :novo_id, nome_fab = :novo_nome, email_fab = :novo_email, tel_fab = :novo_tel 
        WHERE id_fab = :id_fab_alt
    ''', {'novo_id': novo_id, 'novo_nome': novo_nome, 'novo_email': novo_email, 'novo_tel': novo_tel, 'id_fab_alt': id_fab_alt})

    print("Alterado com sucesso!")

    connection.commit()#salva alterações
    connection.close()#fecha conecxão

def alterar_forn():
    """
    Altera os dados de um fornecedor no banco de dados.

    Funções chamadas:
    - listar_forn(): Lista todos os fornecedores existentes.

    Etapas:
    - Exibe o layout para alterar dados de fornecedores.
    - Solicita ao usuário o ID do fornecedor a ser alterado.
    - Solicita os novos dados do fornecedor.
    - Conecta ao banco de dados e atualiza o registro com os novos dados.
    - Confirma a alteração e fecha a conexão com o banco.
    """
    print("****************************************************************************")
    print("Fornecedores")
    listar_forn()#lista fornecedores para escolher qual alterar

    id_forn_alt = int(input("Digite o id do fornecedor que deseja alterar: "))

    #novos dados do fabricante
    novo_id = input("Novo id do fornecedor: ")
    novo_nome = input("Novo nome do fornecedor: ")
    novo_email = input("Novo email do fornecedor: ")
    novo_tel = input("Novo telefone do fornecedor: ")

    #alterar dados no banco de dados
    connection = conectar_bd()#conecta no banco
    cursor = connection.cursor()

    #altera todos os dados do fornecedor escolhido
    cursor.execute('''
        UPDATE Fornecedores 
        SET id_forn = :novo_id, nome_forn = :novo_nome, email_forn = :novo_email, tel_forn = :novo_tel 
        WHERE id_forn = :id_forn_alt
    ''', {'novo_id': novo_id, 'novo_nome': novo_nome, 'novo_email': novo_email, 'novo_tel': novo_tel, 'id_forn_alt': id_forn_alt})

    print("Alterado com sucesso!")

    connection.commit()#salva alterações
    connection.close()#fecha conecxão

def alterar_func():
    """
    Altera os dados de um funcionário no banco de dados.

    Funções chamadas:
    - listar_func(): Lista todos os funcionários existentes.

    Etapas:
    - Exibe o layout para alterar dados de funcionários.
    - Solicita ao usuário o ID do funcionário a ser alterado.
    - Solicita os novos dados do funcionário.
    - Conecta ao banco de dados e atualiza o registro com os novos dados.
    - Confirma a alteração e fecha a conexão com o banco.
    """
    print("****************************************************************************")
    print("Funcionários")
    listar_func()#lista funcionarios para escolher qual alterar

    id_func_alt = int(input("Digite o id do funcionário que deseja alterar: "))

    #novos dados do fabricante
    novo_id = input("Novo id do funcionário: ")
    novo_nome = input("Novo nome do funcionário: ")
    novo_data_nasc = input("Nova data nascimento do funcionário: ")
    novo_sal = input("Novo salário do funcionário: ")
    novo_data_cont = input("Nova data contrato do funcionário: ")
    novo_categoria = input("Nova categoria do funcionário: ")

    #alterar dados no banco de dados
    connection = conectar_bd()#conecta no banco
    cursor = connection.cursor()

    #altera todos os dados do funcionario escolhido
    cursor.execute('''
        UPDATE Funcionários 
        SET id_func = :novo_id, nome_func = :novo_nome, data_nasc_func = :novo_data_nasc, sal_func = :novo_sal, data_contrato = :novo_data_cont, categoria_func = :novo_categoria
        WHERE id_func = :id_func_alt
    ''', {'novo_id': novo_id, 'novo_nome': novo_nome, 'novo_data_nasc': novo_data_nasc, 'novo_sal': novo_sal, 'novo_data_cont': novo_data_cont, 'novo_categoria': novo_categoria, 'id_func_alt': id_func_alt})

    print("Alterado com sucesso!")

    connection.commit()#salva alterações
    connection.close()#fecha conecxão

def alterar_login():
    """
    Altera os dados de login de um funcionário no banco de dados.

    Funções chamadas:
    - listar_login(): Lista todos os logins de funcionários existentes.

    Etapas:
    - Exibe o layout para alterar dados de login.
    - Solicita ao usuário o ID do login a ser alterado.
    - Solicita os novos dados do login.
    - Conecta ao banco de dados e atualiza o registro com os novos dados.
    - Confirma a alteração e fecha a conexão com o banco.
    """
    print("****************************************************************************")
    print("Login Funcionário")
    listar_login()#lista login funcionarios para escolher qual alterar

    id_login_alt = int(input("Digite o id do funcionário que deseja alterar: "))

    #novos dados do fabricante
    novo_id = input("Novo id do login: ")
    novo_email = input("Novo email do login: ")
    nova_senha = input("Nova senha do login: ")
    novo_id_func = input("Novo id do funcionário do login: ")

    #alterar dados no banco de dados
    connection = conectar_bd()#conecta no banco
    cursor = connection.cursor()

    #altera todos os dados do login funcionario escolhido
    cursor.execute('''
        UPDATE Login_Func 
        SET id_login = :novo_id, email_login = :novo_email, senha_login = :nova_senha, id_func = :novo_id_func
        WHERE id_login = :id_login_alt
    ''', {'novo_id': novo_id, 'novo_email': novo_email, 'nova_senha': nova_senha, 'novo_id_func': novo_id_func , 'id_login_alt': id_login_alt})

    print("Alterado com sucesso!")

    connection.commit()#salva alterações
    connection.close()#fecha conecxão

def alterar_cliente():
    print("****************************************************************************")
    print("Usuários")   
    listar_clientes()#lista login clientes para escolher qual alterar

    id_cliente_alt = int(input("Digite o id do cliente que deseja alterar: "))

    #novos dados do fabricante
    novo_id = input("Novo id do cliente: ")
    novo_nome = input("Novo nome do cliente: ")
    novo_email = input("Novo email do cliente: ")
    novo_senha = input("Nova senha do cliente: ")

    #alterar dados no banco de dados
    connection = conectar_bd()#conecta no banco
    cursor = connection.cursor()

    #altera todos os dados do login cliente escolhido
    cursor.execute('''
        UPDATE Login_Clientes 
        SET id_cliente = :novo_id, nome_cliente = :novo_nome, email_cliente = :novo_email, senha_cliente = :novo_senha 
        WHERE id_cliente = :id_cliente_alt
    ''', {'novo_id': novo_id, 'novo_nome': novo_nome, 'novo_email': novo_email, 'novo_senha': novo_senha, 'id_cliente_alt': id_cliente_alt})

    print("Alterado com sucesso!")

    connection.commit()#salva alterações
    connection.close()#fecha conecxão

def alterar_adm():
    print("****************************************************************************")
    print("Administradores")
    listar_adm()#lista administradores para escolher qual alterar

    id_adm_alt = int(input("Digite o id do administrador que deseja alterar: "))

    #novos dados do fabricante
    novo_id = input("Novo id do administrador: ")
    novo_email = input("Novo email do administrador: ")
    novo_senha = input("Nova senha do administrador: ")
    novo_id_func = input("Novo id funcionário do administrador: ")

    #alterar dados no banco de dados
    connection = conectar_bd()#conecta no banco
    cursor = connection.cursor()

    #altera todos os dados do administrador escolhido
    cursor.execute('''
        UPDATE Login_ADM 
        SET id_forn = :novo_id, email_forn = :novo_email, senha_adm = :novo_senha, id_func = :novo_id_func 
        WHERE id_forn = :id_forn_alt
    ''', {'novo_id': novo_id, 'novo_email': novo_email, 'novo_senha': novo_senha, 'novo_id_func': novo_id_func, 'id_adm_alt': id_adm_alt})

    print("Alterado com sucesso!")

    connection.commit()#salva alterações
    connection.close()#fecha conecxão