from Cadastrar import cadastrar_ing, cadastrar_prato, cadastrar_fab, cadastrar_forn
from Alterar import alterar_ing, alterar_prato, alterar_fab, alterar_forn
from Excluir import deletar_prato, deletar_fab, deletar_forn, deletar_ing
from Listar import listar_fab, listar_forn, listar_ing, listar_prato_adm

def menu_func():
  """
  Exibe o menu principal para os funcionários, permitindo cadastrar, alterar,
  excluir ou listar itens do estoque, ou voltar para a página inicial.

  Funções chamadas:
  - menu_func_cadastro(): Exibe o submenu de cadastro.
  - menu_func_altero(): Exibe o submenu de alteração.
  - menu_func_deleto(): Exibe o submenu de exclusão.
  - menu_func_listo(): Exibe o submenu de listagem.
  - home(): Volta para a página inicial.

  Etapas:
  - Exibe o layout do menu principal.
  - Solicita a opção desejada do funcionário.
  - Direciona para a função correspondente com base na opção escolhida.
  """
  from interface_restaurante import home
  while True:
      print("*********************************************************")
      print("        JungKooking Food - Estoque Funcionário           ")
      print("                                                         ")
      print("                  |    1-Cadastrar    |                  ")
      print("                  |     2-Alterar     |                  ")
      print("                  |     3-Excluir     |                  ")
      print("                  |      4-Listar     |                  ")
      print("                  |       5-Home      |                  ")
      print("*********************************************************")
      opcao = str(input("Digite a opção desejada: "))
      op = opcao.upper()

      if opcao == "1" or op == "CADASTRAR":
        menu_func_cadastro()
      elif opcao == "2" or op == "ALTERAR":
        menu_func_altero()
      elif opcao == "3" or op == "EXCLUIR":
        menu_func_deleto()
      elif opcao == "4" or op == "LISTAR":
        menu_func_listo()
      elif opcao == "5" or opcao == "HOME" or op == "SAIR":
        home()
      else:
        print("Opção inexistente.")

def menu_func_cadastro():
  """
  Exibe o submenu de cadastro para os funcionários, permitindo cadastrar
  ingredientes, pratos, fabricantes ou fornecedores, ou voltar para o menu
  principal do funcionário.

  Funções chamadas:
  - cadastrar_ing(): Cadastra um ingrediente.
  - cadastrar_prato(): Cadastra um prato.
  - cadastrar_fab(): Cadastra um fabricante.
  - cadastrar_forn(): Cadastra um fornecedor.
  - menu_func(): Volta para o menu principal do funcionário.

  Etapas:
  - Exibe o layout do submenu de cadastro.
  - Solicita a opção desejada do funcionário.
  - Direciona para a função correspondente com base na opção escolhida.
  """
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Funcionário           ")
    print("                                                         ")
    print("                     Menu Cadastros                      ")
    print("                                                         ")
    print("           |      1-Cadastrar Ingrediente    |           ")
    print("           |        2-Cadastrar Prato        |           ")
    print("           |      3-Cadastrar Fabricante     |           ")
    print("           |      4-Cadastrar Fornecedor     |           ")
    print("           |        5-Menu Funcionário       |           ")
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
    elif opcao == "5" or op == "HOME" or op == "SAIR":
      menu_func()
    else:
      print("Opção inexistente.")

def menu_func_altero():
  """
  Exibe o submenu de alteração para os funcionários, permitindo alterar
  ingredientes, pratos, fabricantes ou fornecedores, ou voltar para o menu
  principal do funcionário.

  Funções chamadas:
  - alterar_ing(): Altera um ingrediente.
  - alterar_prato(): Altera um prato.
  - alterar_fab(): Altera um fabricante.
  - alterar_forn(): Altera um fornecedor.
  - menu_func(): Volta para o menu principal do funcionário.

  Etapas:
  - Exibe o layout do submenu de alteração.
  - Solicita a opção desejada do funcionário.
  - Direciona para a função correspondente com base na opção escolhida.
  """
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Funcionário           ")
    print("                                                         ")
    print("                      Menu Alterar                       ")
    print("                                                         ")
    print("            |      1-Alterar Ingrediente    |            ")
    print("            |        2-Alterar Prato        |            ")
    print("            |      3-Alterar Fabricante     |            ")
    print("            |      4-Alterar Fornecedor     |            ")
    print("            |       5-Menu Funcionário      |            ")
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
    elif opcao == "5" or op == "HOME" or op == "SAIR":
      menu_func()
    else:
      print("Opção inexistente.")

def menu_func_deleto():
  """
  Exibe o submenu de exclusão para os funcionários, permitindo excluir
  ingredientes, pratos, fabricantes ou fornecedores, ou voltar para o menu
  principal do funcionário.

  Funções chamadas:
  - deletar_ing(): Exclui um ingrediente.
  - deletar_prato(): Exclui um prato.
  - deletar_fab(): Exclui um fabricante.
  - deletar_forn(): Exclui um fornecedor.
  - menu_func(): Volta para o menu principal do funcionário.

  Etapas:
  - Exibe o layout do submenu de exclusão.
  - Solicita a opção desejada do funcionário.
  - Direciona para a função correspondente com base na opção escolhida.
  """
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Funcionário           ")
    print("                                                         ")
    print("                      Menu Excluir                       ")
    print("                                                         ")
    print("            |      1-Excluir Ingrediente    |            ")
    print("            |        2-Excluir Prato        |            ")
    print("            |      3-Excluir Fabricante     |            ")
    print("            |      4-Excluir Fornecedor     |            ")
    print("            |       5-Menu Funcionário      |            ")
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
    elif opcao == "5" or op == "HOME" or op == "SAIR":
      menu_func()
    else:
      print("Opção inexistente.")

def menu_func_listo():
  """
  Exibe o submenu de listagem para os funcionários, permitindo listar
  ingredientes, pratos, fabricantes ou fornecedores, ou voltar para o menu
  principal do funcionário.

  Funções chamadas:
  - listar_ing(): Lista os ingredientes.
  - listar_prato_adm(): Lista os pratos para o administrador.
  - listar_fab(): Lista os fabricantes.
  - listar_forn(): Lista os fornecedores.
  - menu_func(): Volta para o menu principal do funcionário.

  Etapas:
  - Exibe o layout do submenu de listagem.
  - Solicita a opção desejada do funcionário.
  - Direciona para a função correspondente com base na opção escolhida.
  """
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Funcionário           ")
    print("                                                         ")
    print("                      Menu Listar                        ")
    print("                                                         ")
    print("            |      1-Listar Ingrediente    |             ")
    print("            |        2-Listar Prato        |             ")
    print("            |      3-Listar Fabricante     |             ")
    print("            |      4-Listar Fornecedor     |             ")
    print("            |       5-Menu Funcionário     |            ")
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
    elif opcao == "5" or op == "HOME" or op == "SAIR":
      menu_func()
    else:
      print("Opção inexistente.")