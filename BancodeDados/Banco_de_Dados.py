import oracledb
import os

#Conectar ao banco de dados
def conectar_bd():
    try:
        connection=oracledb.connect(
            config_dir=os.path.dirname(os.path.realpath(__file__)),
            user="ADMIN",#usuario
            password="senha",#senha
            dsn="ProjetoIntegrador1_low",#tipo
            wallet_location=os.path.dirname(os.path.realpath(__file__)),#pega wallet
            wallet_password="senha")#senha da wallet
        return connection
    except Exception as error:
        print("Erro ao conectar no banco: ", error)

connection = conectar_bd()