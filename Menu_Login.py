import Login

#login adm
#testeadm@gmail.com
#senhaadm
#login cliente
#testecliente@gmail.com
#senhacliente
#login func
#testefunc@gmail.com
#senhatestefunc

def funcao_login():
    """
    Função responsável pelo processo de login do usuário.

    Esta função solicita ao usuário que insira seu email e senha. 
    Em seguida, valida se os campos foram preenchidos corretamente. 
    Se o usuário não fornecer um email ou senha, a função levanta uma exceção ValueError.
    Caso contrário, a função chama a função `login_adm` do módulo `codigo_login` para validar as credenciais do usuário.

    Retorno:
    - Chama a função `codigo_login.login_adm(senha, usuario)` que retorna o resultado do processo de login.
    """
    try: 
        usuario=str(input("\nDigite o email do usuário: "))
        if not usuario:
            raise ValueError("Erro Usuario")
        else:
            senha=str(input("\nDigite sua senha aqui: "))
            if not senha:
                raise ValueError("Erro Senha")
                
        return codigo_login.login_adm(senha, usuario)

    except ValueError as error:
        if str(error) == "Erro Usuario":
            print("Erro: Usuario Inválido")
        elif str(error) == "Erro Senha":
            print("Erro, Senha Invalida")