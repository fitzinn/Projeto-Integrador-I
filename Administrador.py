from Cadastrar import cadastrar_ing, cadastrar_adm, cadastrar_prato, cadastrar_fab, cadastrar_forn, cadastrar_func, cadastrar_cliente
from Alterar import alterar_login, alterar_ing, alterar_cliente, alterar_prato, alterar_fab, alterar_forn, alterar_func, alterar_adm
from Excluir import deletar_clientes, deletar_prato, deletar_fab, deletar_forn, deletar_func, deletar_login, deletar_ing, deletar_adm
from Listar import listar_login, listar_adm, listar_clientes, listar_fab, listar_forn, listar_func, listar_ing, listar_prato_adm
from Relatorios import main, validar_data, gerar_relatorio_vendas
from Logs import print_logs_auditoria, print_logs_acesso, print_logs_compras

def menu_adm():
    from Restaurante import home
    """INTERFACE MENU ADMINISTRADOR
    
    RETORNA:
    (menu_adm_cadastro) = PAGINA DE CADASTRO GERAL PARA ADMIN
    (menu_adm_altero) = PAGINA DE ALTERACAO GERAL PARA ADMIN
    (menu_adm_deleto) = PAGINA DE EXCLUSAO GERAL PARA ADMIN
    (menu_adm_listo) = PAGINA DE LISTAGEM GERAL PARA ADMIN
    (ger_logs) = PAGINA DE GERENCIAMENTO DE LOGS
    (menu_adm_relatorio) = PAGINA DE GERAR RELATORIO
    (home) = VOLTA PARA A PAGINA INICIAL
    """

    while True:
      print("*********************************************************")
      print("        JungKooking Food - Estoque Administrador         ")
      print("                                                         ")
      print("                  |    1-Cadastrar    |                  ")
      print("                  |     2-Alterar     |                  ")
      print("                  |     3-Excluir     |                  ")
      print("                  |      4-Listar     |                  ")
      print("                  |  5-Gerenciar Logs |")
      print("                  | 6-Gerar Relatório |                  ")
      print("                  |       7-Home      |                  ")
      print("*********************************************************")
      opcao = str(input("Digite a opção desejada: "))
      op = opcao.upper()

      if opcao == "1" or op == "CADASTRAR":
        menu_adm_cadastro()
      elif opcao == "2" or op == "ALTERAR":
        menu_adm_altero()
      elif opcao == "3" or op == "EXCLUIR":
        menu_adm_deleto()
      elif opcao == "4" or op == "LISTAR":
        menu_adm_listo()
      elif opcao == "5" or op == "GERENCIAR LOGS" or op == "LOGS":
        ger_logs()
      elif opcao == "6" or op == "GERAR RELATÓRIO" or op == "RELATÓRIO" or op == "RELATORIO" or op == "GERAR RELATORIO":
        main()
      elif opcao == "7" or op == "HOME" or op == "SAIR":
        home()
      else:
        print("Opção inexistente.")

def menu_adm_cadastro():
  """INTERFACE MENU DE CADASTRO ADMINISTRADOR

    EXIBE O MENU DE CADASTRO E REDIRECIONA PARA AS FUNÇÕES ESPECÍFICAS DE CADASTRO.

    RETORNA:
    (cadastrar_ing) = PAGINA DE CADASTRO DE INGREDIENTES
    (cadastrar_prato) = PAGINA DE CADASTRO DE PRATOS
    (cadastrar_fab) = PAGINA DE CADASTRO DE FABRICANTES
    (cadastrar_forn) = PAGINA DE CADASTRO DE FORNECEDORES
    (cadastrar_func) = PAGINA DE CADASTRO DE FUNCIONÁRIOS
    (cadastrar_cliente) = PAGINA DE CADASTRO DE CLIENTES
    (cadastrar_adm) = PAGINA DE CADASTRO DE ADMINISTRADORES
    (menu_adm) = RETORNA AO MENU PRINCIPAL DO ADMINISTRADOR
    """

  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                     Menu Cadastros                      ")
    print("                                                         ")
    print("           |      1-Cadastrar Ingrediente    |           ")
    print("           |        2-Cadastrar Prato        |           ")
    print("           |      3-Cadastrar Fabricante     |           ")
    print("           |      4-Cadastrar Fornecedor     |           ")
    print("           |     5-Cadastrar Funcionário     |           ")
    print("           |        6-Cadastrar Cliente      |           ")
    print("           |    7-Cadastrar  Administrador   |           ")
    print("           |       8-Menu Administrador      |           ")
    print("*********************************************************")
    opcao = str(input("Digite a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "INGREDIENTE" or op == "ING":
      cadastrar_ing()
    elif opcao == "2" or op == "PRATO":
      cadastrar_prato()
    elif opcao == "3" or op == "FABRICANTE" or op == "FAB":
      cadastrar_fab()
    elif opcao == "4" or op == "FORNECEDOR" or op == "FORN":
      cadastrar_forn()
    elif opcao == "5" or op == "FUNCIONARIO" or op == "FUNC" or op == "FUNCIONÁRIO":
      cadastrar_func()
    elif opcao == "6" or op == "CLIENTE" or op == "CLI":
      cadastrar_cliente()
    elif opcao == "7" or op == "ADMINISTRADOR" or op == "ADM":
      cadastrar_adm()
    elif opcao == "8" or op == "HOME" or op == "SAIR":
      menu_adm()
    else:
      print("Opção inexistente.")

def menu_adm_altero():

  """INTERFACE MENU DE ALTERAÇÃO ADMINISTRADOR

    EXIBE O MENU DE ALTERAÇÃO E REDIRECIONA PARA AS FUNÇÕES ESPECÍFICAS DE ALTERAÇÃO.

    RETORNA:
    (alterar_ing) = PAGINA DE ALTERAÇÃO DE INGREDIENTES
    (alterar_prato) = PAGINA DE ALTERAÇÃO DE PRATOS
    (alterar_fab) = PAGINA DE ALTERAÇÃO DE FABRICANTES
    (alterar_forn) = PAGINA DE ALTERAÇÃO DE FORNECEDORES
    (alterar_func) = PAGINA DE ALTERAÇÃO DE FUNCIONÁRIOS
    (alterar_cliente) = PAGINA DE ALTERAÇÃO DE CLIENTES
    (alterar_adm) = PAGINA DE ALTERAÇÃO DE ADMINISTRADORES
    (alterar_login) = PAGINA DE ALTERAÇÃO DE LOGIN DE FUNCIONÁRIOS
    (menu_adm) = RETORNA AO MENU PRINCIPAL DO ADMINISTRADOR
    """
  
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                      Menu Alterar                       ")
    print("                                                         ")
    print("            |      1-Alterar Ingrediente    |            ")
    print("            |        2-Alterar Prato        |            ")
    print("            |      3-Alterar Fabricante     |            ")
    print("            |      4-Alterar Fornecedor     |            ")
    print("            |     5-Alterar Funcionário     |            ")
    print("            |        6-Alterar Cliente      |            ")
    print("            |    7-Alterar  Administrador   |            ")
    print("            |  8-Alterar Login Funcionário  |            ")
    print("            |      9-Menu Administrador     |            ")
    print("*********************************************************")
    opcao = str(input("Digite a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "INGREDIENTE" or op == "ING":
      alterar_ing()
    elif opcao == "2" or op == "PRATO":
      alterar_prato()
    elif opcao == "3" or op == "FABRICANTE" or op == "FAB":
      alterar_fab()
    elif opcao == "4" or op == "FORNECEDOR" or op == "FORN":
      alterar_forn()
    elif opcao == "5" or op == "FUNCIONARIO" or op == "FUNC" or op == "FUNCIONÁRIO":
      alterar_func()
    elif opcao == "6" or op == "CLIENTE" or op == "CLI":
      alterar_cliente()
    elif opcao == "7" or op == "ADMINISTRADOR" or op == "ADM":
      alterar_adm()
    elif opcao == "8" or op == "LOGIN" or op == "LOGIN FUNCIONARIO" or op == "LOGIN FUNCIONÁRIO" or op == "LOGIN FUNC":
      alterar_login()
    elif opcao == "9" or op == "HOME" or op == "SAIR":
      menu_adm()
    else:
      print("Opção inexistente.")

def menu_adm_deleto():
  """INTERFACE MENU DE EXCLUSÃO ADMINISTRADOR

    EXIBE O MENU DE EXCLUSÃO E REDIRECIONA PARA AS FUNÇÕES ESPECÍFICAS DE EXCLUSÃO.

    RETORNA:
    (deletar_ing) = PAGINA DE EXCLUSÃO DE INGREDIENTES
    (deletar_prato) = PAGINA DE EXCLUSÃO DE PRATOS
    (deletar_fab) = PAGINA DE EXCLUSÃO DE FABRICANTES
    (deletar_forn) = PAGINA DE EXCLUSÃO DE FORNECEDORES
    (deletar_func) = PAGINA DE EXCLUSÃO DE FUNCIONÁRIOS
    (deletar_clientes) = PAGINA DE EXCLUSÃO DE CLIENTES
    (deletar_adm) = PAGINA DE EXCLUSÃO DE ADMINISTRADORES
    (deletar_login) = PAGINA DE EXCLUSÃO DE LOGIN DE FUNCIONÁRIOS
    (menu_adm) = RETORNA AO MENU PRINCIPAL DO ADMINISTRADOR
    """
  
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                      Menu Excluir                       ")
    print("                                                         ")
    print("            |      1-Excluir Ingrediente    |            ")
    print("            |        2-Excluir Prato        |            ")
    print("            |      3-Excluir Fabricante     |            ")
    print("            |      4-Excluir Fornecedor     |            ")
    print("            |     5-Excluir Funcionário     |            ")
    print("            |        6-Excluir Cliente      |            ")
    print("            |    7-Excluir  Administrador   |            ")
    print("            |  8-Excluir Login Funcionário  |            ")
    print("            |      9-Menu Administrador     |            ")
    print("*********************************************************")
    opcao = str(input("Digite a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "INGREDIENTE" or op == "ING":
      deletar_ing()
    elif opcao == "2" or op == "PRATO":
      deletar_prato()
    elif opcao == "3" or op == "FABRICANTE" or op == "FAB":
      deletar_fab()
    elif opcao == "4" or op == "FORNECEDOR" or op == "FORN":
      deletar_forn()
    elif opcao == "5" or op == "FUNCIONARIO" or op == "FUNC" or op == "FUNCIONÁRIO":
      deletar_func()
    elif opcao == "6" or op == "CLIENTE" or op == "CLI":
      deletar_clientes()
    elif opcao == "7" or op == "ADMINISTRADOR" or op == "ADM":
      deletar_adm()
    elif opcao == "8" or op == "LOGIN" or op == "LOGIN FUNCIONARIO" or op == "LOGIN FUNCIONÁRIO" or op == "LOGIN FUNC":
      deletar_login()
    elif opcao == "9" or op == "HOME" or op == "SAIR":
      menu_adm()
    else:
      print("Opção inexistente.")

def menu_adm_listo():
  """INTERFACE MENU DE LISTAGEM ADMINISTRADOR

    EXIBE O MENU DE LISTAGEM E REDIRECIONA PARA AS FUNÇÕES ESPECÍFICAS DE LISTAGEM.

    RETORNA:
    (listar_ing) = PAGINA DE LISTAGEM DE INGREDIENTES
    (listar_prato_adm) = PAGINA DE LISTAGEM DE PRATOS PARA ADMINISTRADOR
    (listar_fab) = PAGINA DE LISTAGEM DE FABRICANTES
    (listar_forn) = PAGINA DE LISTAGEM DE FORNECEDORES
    (listar_func) = PAGINA DE LISTAGEM DE FUNCIONÁRIOS
    (listar_clientes) = PAGINA DE LISTAGEM DE CLIENTES
    (listar_adm) = PAGINA DE LISTAGEM DE ADMINISTRADORES
    (listar_login) = PAGINA DE LISTAGEM DE LOGIN DE FUNCIONÁRIOS
    (menu_adm) = RETORNA AO MENU PRINCIPAL DO ADMINISTRADOR
    """
  
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                      Menu Listar                        ")
    print("                                                         ")
    print("            |      1-Listar Ingrediente    |             ")
    print("            |        2-Listar Prato        |             ")
    print("            |      3-Listar Fabricante     |             ")
    print("            |      4-Listar Fornecedor     |             ")
    print("            |     5-Listar Funcionário     |             ")
    print("            |        6-Listar Cliente      |             ")
    print("            |    7-Listar  Administrador   |             ")
    print("            |  8-Listar Login Funcionário  |             ")
    print("            |     9-Menu Administrador     |             ")
    print("*********************************************************")
    opcao = str(input("Digite a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "INGREDIENTE" or op == "ING":
      listar_ing()
    elif opcao == "2" or op == "PRATO":
      listar_prato_adm()
    elif opcao == "3" or op == "FABRICANTE" or op == "FAB":
      listar_fab()
    elif opcao == "4" or op == "FORNECEDOR" or op == "FORN":
      listar_forn()
    elif opcao == "5" or op == "FUNCIONARIO" or op == "FUNC" or op == "FUNCIONÁRIO":
      listar_func()
    elif opcao == "6" or op == "CLIENTE" or op == "CLI":
      listar_clientes()
    elif opcao == "7" or op == "ADMINISTRADOR" or op == "ADM":
      listar_adm()
    elif opcao == "8" or op == "LOGIN" or op == "LOGIN FUNCIONARIO" or op == "LOGIN FUNCIONÁRIO" or op == "LOGIN FUNC":
      listar_login()
    elif opcao == "9" or op == "HOME" or op == "SAIR":
      menu_adm()
    else:
      print("Opção inexistente.")

#menu para o relatorio de vendas que esta no arquivo relatorios
def menu_adm_relatorio():
  """INTERFACE MENU DE RELATÓRIO ADMINISTRADOR

    PERMITE AO ADMINISTRADOR GERAR RELATÓRIOS DE VENDAS.

    FUNCIONALIDADES:
    - Solicita ao usuário se deseja gerar o relatório de vendas.
    - Se o usuário confirmar, solicita a data desejada para o relatório.
    - Verifica se a data inserida é válida.
    - Gera o relatório de vendas para a data especificada.

    RETORNO:
    - Caso o usuário opte por não gerar o relatório, encerra a função.
    """
  
  while True:
    opcao=str(input("Deseja gerar o relatorio de vendas? (S/N): "))
    if opcao.upper()=='S':
      while True:
        data_venda=input("Digite a data que deseja acessar ao relatorio no formato AAAA-MM-DD: ")
        if validar_data(data_venda):
          gerar_relatorio_vendas(data_venda)
          break
        else:
        
          print("Formato de data invalido. pOR favor, digite a data no formato AAAA-MM-DD.")
    elif opcao.upper()=='N':
      print("Operação cancelada...")
      break
    else:
      print("Opção inválida. Por favor digite 'S' para sim ou 'N' para nao")

def ger_logs():

    """
    EXIBE PAGINA DE GERENCIAMENTO DE LOGS

    RETORNA:
    (print_logs_auditoria) = PRINTA PAGINA DE LOGS DE AUDITORIA
    (print_logs_acesso) = PRINTA PAGINA DE LOGS DE ACESSO DE CLIENTE

    """

    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("")
    print("               |   1-Log De Auditoria   |")
    print("               |    2-Log De Acessos    |")
    print("               |     3-Log de Compras   |")
    print("               |  4-Menu Administrador  |")
    print("**********************************************************")
    opcao=str(input("Escolha a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "AUDITORIA" or op == "LOG AUDITORIA" or op == "LOG DE AUDITORIA":
        print_logs_auditoria()
    elif opcao == "2" or op == "ACESSOS" or op == "LOG ACESSOS" or op == "LOG DE ACESSOS":
        print_logs_acesso()
    elif opcao == "3" or op == "COMPRAS" or op == "LOG COMPRAS" or op == "LOG DE COMPRAS":
        print_logs_compras()
    elif opcao == "4" or op == "MENU" or op == "SAIR":
        menu_adm()