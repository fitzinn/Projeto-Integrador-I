from BancodeDados.Criptografia import descripto
from BancodeDados.Banco_de_Dados import conectar_bd
from Logs import log_compra
def menu_cliente():
    """
    Exibe o menu principal para o cliente, listando os pratos disponíveis e 
    permitindo a seleção de pratos para adicionar ao carrinho.

    Funções chamadas:
    - listar_prato_cliente(): Lista os pratos disponíveis.
    - escolher_prato(): Permite ao cliente escolher um prato para adicionar ao carrinho.

    Etapas:
    - Exibe o layout do menu.
    - Chama a função para listar os pratos disponíveis.
    - Chama a função para escolher um prato.
    """
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARDAPIO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("CARDAPIO                                                 ")
    print("                                                         ")
    listar_prato_cliente()
    escolher_prato()
    print("*********************************************************")

#pagina da comida do cardapio para adicionar ao carrinho
def escolher_prato():
    """
    Permite ao cliente escolher um prato do cardápio para adicionar ao carrinho e processar o pagamento.

    Funções chamadas:
    - descripto(): Descriptografa a descrição do prato.
    - pagamento(prato, preco): Processa o pagamento para o prato escolhido.

    Etapas:
    - Solicita ao cliente o nome do prato desejado ou a opção de sair.
    - Verifica se o prato existe no banco de dados.
    - Exibe os detalhes do prato escolhido.
    - Chama a função para processar o pagamento.
    """
    while True:
        prato_escolhido = str(input("Digite o nome do prato que deseja adicionar ao carrinho ou SAIR para voltar: ")).strip()
        prato_esc = prato_escolhido.upper()

        if prato_esc == "SAIR":
            print("Voltando ao inicio...")
            break

        connection = conectar_bd()
        
        try:
            cursor = connection.cursor()
            query = 'SELECT * FROM PRATOS WHERE nome_prato = :nome_prato'
            cursor.execute(query, {"nome_prato": prato_esc})
            prato = cursor.fetchone()

            if prato:
                print("\nPrato escolhido:")
                print("Nome do Prato: ", prato[1])
                desc_descripto = descripto(prato[2])
                print("Descrição do Prato: ", desc_descripto)
                print("Categoria do Prato: ", prato[3])
                print("Valor do Prato: ", prato[5])
                print("")
                pagamento(prato[1], prato[5])
                break
            else:
                print("Prato não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            cursor.close()
            connection.close()

#pagina do pagamento
def pagamento(prato, preco):
    """
    Processa o pagamento de um prato escolhido pelo cliente.

    Parâmetros:
    - prato (str): Nome do prato escolhido.
    - preco (int): Preço do prato escolhido.

    Funções chamadas:
    - log_compra(connection, celular, preco_prato, pag, nome_prato, endereco): Registra a compra no banco de dados.

    Etapas:
    - Solicita ao cliente as informações necessárias para o pagamento.
    - Valida a forma de pagamento.
    - Registra a compra no banco de dados.
    - Exibe uma mensagem de confirmação.
    """
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("Endereço de entrega:                   Forma De Pagamento")
    print("CEP:                                                  Pix")
    print("Nome completo:                                     Cartao")
    print("Numero de Celular:                                       ")
    print("                                      Finalizar Pagamento")
    print("*********************************************************")
    
    celular = int(input("Digite aqui seu numero de celular: "))
    endereco = str(input("Digite aqui o endereco de entrega: "))
    preco_prato = int(preco)
    nome_prato = prato
    pgto = str(input("Digite a forma de pagamento acima desejada (Pix ou Cartao): "))
    pag = pgto.upper()

    if pag == "PIX" or "CARTAO":
        
        connection = conectar_bd()
        
        try:
            log_compra(connection, celular, preco_prato, pag, nome_prato, endereco)
            print(f"Pagamento finalizado via {pag} com entrega no endereço {endereco}. Você receberá um SMS de confirmação no número {celular}")
        except Exception as error:
            print(f"Ocorreu um erro ao processar o pagamento: {error}")
        finally:
            connection.close()
    else:
        print("Forma de pagamento inválida. Por favor, escolha entre Pix ou Cartao.")

def listar_prato_cliente():
    """
    Lista todos os pratos disponíveis no cardápio para o cliente.

    Funções chamadas:
    - descripto(): Descriptografa a descrição do prato.

    Etapas:
    - Estabelece conexão com o banco de dados.
    - Executa a query para buscar os pratos disponíveis.
    - Exibe os detalhes de cada prato.
    - Fecha a conexão com o banco de dados.
    """
    print("****************************************************************************")
    print("Pratos")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Pratos ORDER BY id_prato')

    resultados = cursor.fetchall()

    for prato in resultados:
        print("Nome do Prato: ", prato[1])
        desc_descripto = descripto(prato[2])
        print("Descrição do Prato: ", desc_descripto)
        print("Categoria do Prato: ", prato[3])
        print("Valor do Prato: ", prato[5])
    
    cursor.close()
    connection.close()
