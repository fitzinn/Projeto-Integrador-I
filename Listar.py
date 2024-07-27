from BancodeDados.Banco_de_Dados import conectar_bd
from BancodeDados.Criptografia import descripto

def listar_ing():
    print("****************************************************************************")
    print("Ingredientes")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Ingredientes ORDER BY id_ing')

    resultados = cursor.fetchall()

    for ing in resultados:
        print("ID do Ingrediente: ", ing[0])
        print("Nome do Ingrediente: ", ing[1])
        print("Preço do Ingrediente: ", ing[2])
        print("Fornecedor do Ingrediente: ", ing[3])
        print("Fabricante do Ingrediente: ", ing[4])
        print("Quantidade minima do Ingrediente: ", ing[5])
        print("Quantidade maxima do Ingrediente: ", ing[6])
        print("Quantidade estoque do Ingrediente: ", ing[7])
        print("Categoria do Ingrediente: ", ing[8])
        print("Data de fabricação do Ingrediente: ", ing[9])
        print("Data de validade do Ingrediente: ", ing[10])
    
    cursor.close()
    connection.close()

def listar_prato_adm():
    print("****************************************************************************")
    print("Pratos")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Pratos ORDER BY id_prato')

    resultados = cursor.fetchall()

    for prato in resultados:
        print("ID do Prato: ", prato[0])
        print("Nome do Prato: ", prato[1])
        desc_descripto = descripto(prato[2])
        print("Descrição do Prato: ", desc_descripto)
        print("Categoria do Prato: ", prato[3])
        print("Preço Custo do Prato: ", prato[4])
    
    cursor.close()
    connection.close()

def listar_fab():
    print("****************************************************************************")
    print("Fabricante")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Fabricantes ORDER BY id_fab')
    resultados = cursor.fetchall()

    for fab in resultados:
        print("ID do Fabricante: ", fab[0])
        print("Nome do Fabricante: ", fab[1])
        print("Email do Fabricante: ", fab[2])
        print("Telefone do Fabricante: ", fab[3])
    
    cursor.close()
    connection.close()

def listar_forn():
    print("****************************************************************************")
    print("Fornecedor")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Fornecedores ORDER BY id_forn')
    resultados = cursor.fetchall()

    for forn in resultados:
        print("ID do Fornecedor: ", forn[0])
        print("Nome do Fornecedor: ", forn[1])
        print("Email do Fornecedor: ", forn[2])
        print("Telefone do Fornecedor: ", forn[3])
    
    cursor.close()
    connection.close()

def listar_func():
    print("****************************************************************************")
    print("Funcionario")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Funcionarios ORDER BY id_func')
    resultados = cursor.fetchall()

    for func in resultados:
        print("ID do Funcionário: ", func[0])
        print("Nome do Funcionário: ", func[1])
        print("Data do Nascimento do Funcionário: ", func[2])
        print("Salário do Funcionário: ", func[3])
        print("Data de Contrato do Funcionário: ", func[4])
        print("Categoria do Funcionário: ", func[5])
    
    cursor.close()
    connection.close()

def listar_login():
    print("****************************************************************************")
    print("Login Funcionários")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Login_Func ORDER BY id_login')
    resultados = cursor.fetchall()

    for func in resultados:
        print("ID Login do Funcionário: ", func[0])
        print("Email do Funcionário: ", func[1])
        senha_func_desc = descripto(func[2])
        print("Senha do Funcionário: ", senha_func_desc)
        print("ID do Funcionário: ", func[3])
    
    cursor.close()
    connection.close()

def listar_clientes():
    print("****************************************************************************")
    print("Usuários")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Login_Clientes ORDER BY id_cliente')
    resultados = cursor.fetchall()

    for cli in resultados:
        print("ID do Cliente: ", cli[0])
        print("Nome do Cliente: ", cli[1])
        print("Email do Cliente: ", cli[2])
        senha_cli_desc = descripto(cli[3])
        print("Senha do Cliente: ", senha_cli_desc)
    
    cursor.close()
    connection.close()

def listar_adm():
    print("****************************************************************************")
    print("Administradores")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Login_ADM ORDER BY id_adm')
    resultados = cursor.fetchall()

    for adm in resultados:
        print("ID do Administrador: ", adm[0])
        print("Email do Administrador: ", adm[1])
        senha_adm_desc = descripto(adm[2])
        print("Senha do Administrador: ", senha_adm_desc)
        print("ID Funcionário do Administrador: ", adm[3])
    
    cursor.close()
    connection.close()