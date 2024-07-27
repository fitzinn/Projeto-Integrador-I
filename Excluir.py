from BancodeDados.Banco_de_Dados import conectar_bd
from Listar import listar_login, listar_ing, listar_prato_adm, listar_forn, listar_fab, listar_func, listar_adm, listar_clientes

def deletar_ing():
    """
    Deleta um ingrediente do banco de dados com base no ID fornecido pelo usuário.

    Funções chamadas:
    - listar_ing(): Lista os ingredientes disponíveis.

    Etapas:
    - Lista os ingredientes disponíveis.
    - Solicita ao usuário o ID do ingrediente a ser deletado.
    - Executa a exclusão do ingrediente no banco de dados.
    """
    print("****************************************************************************")
    print("Ingredientes")
    listar_ing()

    id_ing_del = input("Digite o id do ingrediente que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Ingredientes WHERE id_ing = :id_ing_del', {'id_ing_del': id_ing_del})

    print("Deletado com sucesso!")

    connection.commit()
    connection.close()

def deletar_prato():
    """
    Deleta um prato do banco de dados com base no ID fornecido pelo usuário.

    Funções chamadas:
    - listar_prato_adm(): Lista os pratos disponíveis.

    Etapas:
    - Lista os pratos disponíveis.
    - Solicita ao usuário o ID do prato a ser deletado.
    - Executa a exclusão do prato no banco de dados.
    """
    print("****************************************************************************")
    print("Pratos")
    listar_prato_adm()

    id_prato_del = input("Digite o id do prato que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Pratos WHERE id_prato = :id_prato_del', {'id_prato_del': id_prato_del})

    print("Deletado com sucesso!")

    connection.commit()
    connection.close()

def deletar_fab():
    """
    Deleta um fabricante do banco de dados com base no ID fornecido pelo usuário.

    Funções chamadas:
    - listar_fab(): Lista os fabricantes disponíveis.
    Etapas:
    - Lista os fabricantes disponíveis.
    - Solicita ao usuário o ID do fabricante a ser deletado.
    - Executa a exclusão do fabricante no banco de dados.
    """
    print("****************************************************************************")
    print("Fabricantes")
    listar_fab()

    id_fab_del = input("Digite o id do fabricante que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Fabricantes WHERE id_fab = :id_fab_del', {'id_fab_del': id_fab_del})

    print("Deletado com sucesso!")

    connection.commit()
    connection.close()

def deletar_forn():
    """
    Deleta um fornecedor do banco de dados com base no ID fornecido pelo usuário.

    Funções chamadas:
    - listar_forn(): Lista os fornecedores disponíveis.
    - conectar_bd(): Estabelece a conexão com o banco de dados.

    Etapas:
    - Lista os fornecedores disponíveis.
    - Solicita ao usuário o ID do fornecedor a ser deletado.
    - Executa a exclusão do fornecedor no banco de dados.
    """
    print("****************************************************************************")
    print("Fornecedores")
    listar_forn()

    id_forn_del = input("Digite o id do fornecedor que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Fornecedores WHERE id_forn = :id_forn_del', {'id_forn_del': id_forn_del})

    print("Deletado com sucesso!")

    connection.commit()
    connection.close()

def deletar_func():
    """
    Deleta um funcionário do banco de dados com base no ID fornecido pelo usuário.

    Funções chamadas:
    - listar_func(): Lista os funcionários disponíveis.
    - conectar_bd(): Estabelece a conexão com o banco de dados.

    Etapas:
    - Lista os funcionários disponíveis.
    - Solicita ao usuário o ID do funcionário a ser deletado.
    - Executa a exclusão do funcionário no banco de dados.
    """
    print("****************************************************************************")
    print("Funcionários")
    listar_func()

    id_func_del = input("Digite o id do funcionário que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Funcionarios WHERE id_func = :id_func_del', {'id_func_del': id_func_del})

    print("Deletado com sucesso!")

    connection.commit()
    connection.close()

def deletar_clientes():
    """
    Deleta um cliente do banco de dados com base no ID fornecido pelo usuário.

    Funções chamadas:
    - listar_clientes(): Lista os clientes disponíveis.
    - conectar_bd(): Estabelece a conexão com o banco de dados.

    Etapas:
    - Lista os clientes disponíveis.
    - Solicita ao usuário o ID do cliente a ser deletado.
    - Executa a exclusão do cliente no banco de dados.
    """
    print("****************************************************************************")
    print("Usuários")
    listar_clientes()

    id_cli_del = input("Digite o id do cliente que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Login_Clientes WHERE id_cliente = :id_cli_del', {'id_cli_del': id_cli_del})

    print("Deletado com sucesso!")

    connection.commit()
    connection.close()

def deletar_login():
    """
    Deleta um login de funcionário do banco de dados com base no ID fornecido pelo usuário.

    Funções chamadas:
    - listar_login(): Lista os logins de funcionários disponíveis.
    - conectar_bd(): Estabelece a conexão com o banco de dados.

    Etapas:
    - Lista os logins de funcionários disponíveis.
    - Solicita ao usuário o ID do login a ser deletado.
    - Executa a exclusão do login no banco de dados.
    """
    print("****************************************************************************")
    print("Login Funcionários")
    listar_login()

    id_func_del = input("Digite o id do login que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Login_Func WHERE id_login = :id_func_del', {'id_func_del': id_func_del})

    print("Deletado com sucesso!")

    connection.commit()
    connection.close()

def deletar_adm():
    """
    Deleta um administrador do banco de dados com base no ID fornecido pelo usuário.

    Funções chamadas:
    - listar_adm(): Lista os administradores disponíveis.
    - conectar_bd(): Estabelece a conexão com o banco de dados.

    Etapas:
    - Lista os administradores disponíveis.
    - Solicita ao usuário o ID do administrador a ser deletado.
    - Executa a exclusão do administrador no banco de dados.
    """
    print("****************************************************************************")
    print("Administradores")
    listar_adm()

    id_adm_del = input("Digite o id do administrador que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Login_ADM WHERE id_adm = :id_adm_del', {'id_adm_del': id_adm_del})

    print("Deletado com sucesso!")

    connection.commit()
    connection.close()