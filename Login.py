from BancodeDados.Banco_de_Dados import conectar_bd
from Administrador import menu_adm
from Funcionario import menu_func
from Cliente import menu_cliente
from BancodeDados.Criptografia import descripto
from Logs import log_auditoria, log_accesso

def login_adm(senha, usuario):
    """
    Verifica o login do usuário como administrador, funcionário ou cliente e direciona ao menu apropriado.

    Args:
        senha (str): A senha fornecida pelo usuário.
        usuario (str): O email do usuário.

    Funções chamadas:
    - log_auditoria(connection, tipo_user, id_user, acao): Registra um log de auditoria.
    - log_accesso(connection, tipo_user, id_user, email, acao): Registra um log de acesso.
    - funcao_login(): Exibe a função de login.
    - menu_adm(): Exibe o menu de administrador.
    - menu_func(): Exibe o menu de funcionário.
    - menu_cliente(): Exibe o menu de cliente.
    """
    from menu_login import funcao_login
    try:
        email = usuario
        senhaver = senha.upper()
        connection = conectar_bd()
        #verifica se é adm
        cursor = connection.cursor()
        cursor.execute('SELECT id_adm, senha_adm FROM Login_ADM login WHERE email_adm = :email', {'email': email})
        resultadoadm = cursor.fetchone()
        #verifica se tem no banco
        if resultadoadm:
            id_adm, senha_adm_cripto = resultadoadm
            senha_adm = descripto(senha_adm_cripto)
            #verifica se senha está correta
            if senhaver == senha_adm:
                print("Login de administrador bem-sucedido!")
                log_auditoria(connection, "admin", id_adm, "login")
                cursor.close()
                connection.close()
                menu_adm()
            else:
                print("Senha de administrador incorreta.")
                cursor.close()
                connection.close()
                funcao_login()
        else:
            #verifica se é funcionario
            cursor.execute('SELECT id_login, senha_login FROM Login_Func WHERE email_login = :email', {'email': email})
            resultadofunc = cursor.fetchone()
            #verifica se tem no banco
            if resultadofunc:
                id_func, senha_func_cripto = resultadofunc
                senha_func = descripto(senha_func_cripto)
                #verifica se senha está correta
                if senhaver == senha_func:
                    print("Login de funcionário bem-sucedido!")
                    log_auditoria(connection, "funcionario", id_func, "login")
                    cursor.close()
                    connection.close()
                    menu_func()
                else:
                    print("Senha de funcionário incorreta.")
                    cursor.close()
                    connection.close()
                    funcao_login()
            else:
                #verifica se é cliente
                cursor.execute('SELECT id_cliente, senha_cliente, nome_cliente FROM login_clientes WHERE email_cliente = :email', {'email': email})
                resultadocliente = cursor.fetchone()
                #verifica se tem no banco
                if resultadocliente:
                    id_cliente, senha_cli_cripto, nome_cliente = resultadocliente
                    senha_cli = descripto(senha_cli_cripto)
                    #verifica se senha está correta
                    if senhaver == senha_cli:
                        print(f"Login bem-sucedido! Bem-vindo, {nome_cliente}")
                        log_accesso(connection, "cliente", id_cliente, email, "login")
                        cursor.close()
                        connection.close()
                        menu_cliente()
                    else:
                        print("Senha de cliente incorreta.")
                        cursor.close()
                        connection.close()
                        funcao_login()
                #caso n ache nenhum cadastro imprime mensagem
                else:
                    print("Nenhum cadastro encontrado com esse email, tente novamente.")
                    cursor.close()
                    connection.close()
                    funcao_login()
    except ValueError as error:
        print("Erro ao verificar login:", error)