import Menu_Login
from Cliente import listar_prato_cliente
from Cadastrar import cadastrar_cliente
#pagina inicial
def home():
    """
    Exibe a interface principal da JungKooking Food e permite a navegação para
    outras seções do sistema, como cardápio, sobre nós e login.

    Opções:
        - HOME: Recarrega a página inicial.
        - CARDAPIO / CARDÁPIO: Lista os pratos disponíveis.
        - SOBRE NOS / SOBRE: Exibe informações sobre o restaurante.
        - LOGIN: Redireciona para a página de login ou cadastro.
        - SAIR: Sai do programa.

    Esta função chama outras funções conforme a opção escolhida pelo usuário.
    """
    while True:
        print("**********************************************************")
        print("                   JungKooking Food                       ")
        print("|    |        |        |        |         |        |     |")
        print("|HOME|        |CARDÁPIO|        |SOBRE NÓS|        |LOGIN|")
        print("|    |        |        |        |         |        |     |")
        print("                                                          ")
        print("EXPLORE SEU #MOMENTO COREANO                              ")
        print("                                                          ")
        print("      Pratos Principais           Porções(Acompanhamentos)")
        print("**********************************************************")
        opcao = str(input("Digite a opção desejada ou sair: ")).strip().upper()

        if opcao == "HOME":
            continue
        elif opcao in ("CARDAPIO", "CARDÁPIO"):
            listar_prato_cliente()
        elif opcao in ("SOBRE NOS", "SOBRE"):
            sobre()
        elif opcao == "LOGIN":
            login_cadastro()
        elif opcao == "SAIR":
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida, tente novamente.")

#pagina escolha login ou cadastro
def login_cadastro():
    """
        Exibe a interface de escolha para login ou cadastro de clientes na JungKooking Food.

    Opções:
        - 1 / LOGIN: Redireciona para a função de login.
        - 2 / CADASTRO: Redireciona para a função de cadastro de clientes.
        - 3 / HOME: Volta para a página inicial.
        - 4 / SAIR: Sai do programa.

    Esta função chama outras funções conforme a opção escolhida pelo usuário.
    """
    while True:
        print("*********************************************************")
        print("                   JungKooking Food                      ")
        print("|     |               |        |                   |    |")
        print("|LOGIN|               |CADASTRO|                   |HOME|")
        print("|     |               |        |                   |    |")
        print("                                                         ")
        print("                   |    1-Login    |                     ")
        print("                   |  2-Cadastro   |                     ")
        print("                   |     3-Home    |                     ")
        print("                   |     4-Sair    |                     ")
        print("*********************************************************")
        opcao = str(input("Digite a opcao desejada: "))
        op = opcao.upper()

        if opcao == "1" or op == "LOGIN":
            menu_login.funcao_login()
        elif opcao == "2" or op == "CADASTRO":
            cadastrar_cliente()
        elif opcao == "3" or op == "HOME":
            home()
        elif opcao == "4" or op == "SAIR":
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida, tente novamente.")

#pagina sobre o restaurante
def sobre():
    """
    Exibe informações sobre o restaurante JungKooking Food, incluindo uma breve
    descrição do estabelecimento e informações de contato.
    """
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |         |                |     |")
    print("|HOME|                 |SOBRE NÓS|                |LOGIN|")
    print("|    |                 |         |                |     |")
    print("Somos um restaurante de Comida Coreana                   ")
    print("Servimos diferenciados pratos em nosso estabelecimento   ")
    print("O melhor estabelecimento do Brasil de Culinaria Coreana  ")
    print("Para nos contatar utilize o numero de WhatsApp a baixo:  ")
    print("                                             1999999-9999")
    print("*********************************************************")
