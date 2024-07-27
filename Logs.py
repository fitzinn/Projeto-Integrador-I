from datetime import datetime
import pytz
from BancodeDados.Banco_de_Dados import conectar_bd

fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')

def obter_horario_brasilia():
    return datetime.now(fuso_horario_brasilia)

def log_auditoria(connection, tipo_user, id_user, acao):
    """
    Registra um log de auditoria no banco de dados.

    Funções chamadas:
    - conectar_bd(): Estabelece a conexão com o banco de dados.
    - obter_horario_brasilia(): Obtém o horário atual em Brasília.
    """
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            timestamp = obter_horario_brasilia()
            query = 'INSERT INTO log_auditoria (tipo_user, id_user, acao, timestamp) VALUES (:1, :2, :3, :4)'
            cursor.execute(query, (tipo_user, id_user, acao, timestamp))
            connection.commit()
        print("Log de auditoria registrado com sucesso.")
    except Exception as error:
        print(f"Ocorreu um erro ao registrar o log de auditoria: {error}")

def log_accesso(connection, tipo_user, id_user, email, acao):
    """
    Registra um log de acesso no banco de dados.

    Funções chamadas:
    - conectar_bd(): Estabelece a conexão com o banco de dados.
    - obter_horario_brasilia(): Obtém o horário atual em Brasília.
    """
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            timestamp = obter_horario_brasilia()
            query = 'INSERT INTO log_acesso (tipo_user, id_user, email, acao, timestamp) VALUES (:1, :2, :3, :4, :5)'
            cursor.execute(query, (tipo_user, id_user, email, acao, timestamp))
            connection.commit()
        print("Log de acesso registrado com sucesso.")
    except Exception as error:
        print(f"Ocorreu um erro ao registrar o log de acesso: {error}")

def log_compra(connection, celular, preco_prato, pgto, nome_prato, endereco):
    """
    Registra um log de compra no banco de dados.

    Funções chamadas:
    - conectar_bd(): Estabelece a conexão com o banco de dados.
    - obter_horario_brasilia(): Obtém o horário atual em Brasília.
    """
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            data_pagamento = obter_horario_brasilia()
            query_select_id_prato = 'SELECT id_prato FROM pratos WHERE nome_prato = :1'
            cursor.execute(query_select_id_prato, (nome_prato,))
            id_prato = cursor.fetchone()[0]
            query = 'INSERT INTO pagamentos (id_pagamento, celular_cliente, data_pagamento, valor_pagamento, tipo_pagamento, prato_vendido, endereco_entrega, id_prato) VALUES (seq_id_pag.NEXTVAL, :1, :2, :3, :4, :5, :6, :7)'
            cursor.execute(query, (celular, data_pagamento, preco_prato, pgto, nome_prato, endereco, id_prato))
            connection.commit()
        print("Log de compra registrado com sucesso.")
    except Exception as error:
        print(f"Ocorreu um erro ao registrar o log de compra: {error}")

def print_logs_auditoria():
    """
    Recupera e imprime os logs de auditoria do banco de dados.
    """
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = '''SELECT log_id, tipo_user, id_user, acao, 
                       TO_CHAR((timestamp AT TIME ZONE 'UTC') AT TIME ZONE 'America/Sao_Paulo', 'YYYY-MM-DD HH24:MI:SS') AS formatted_timestamp 
                       FROM log_auditoria 
                       ORDER BY log_id DESC'''
            cursor.execute(query)
            linhas = cursor.fetchall()
            for linha in linhas:
                log_id, tipo_user, id_user, acao, timestamp = linha
                print(f"Log ID: {log_id}, \nTipo de Usuário: {tipo_user}, \nID do Usuário: {id_user}, \nAção: {acao}, \nAno-Mês-Dia - Hora:Minuto:Segundo: {timestamp}\n")
    except Exception as error:
        print(f"Ocorreu um erro ao recuperar os logs de auditoria: {error}")
    finally:
        connection.close()

def print_logs_acesso():
    """
    Recupera e imprime os logs de acesso do banco de dados.
    """
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = '''SELECT log_id, tipo_user, id_user, email, acao, 
                       TO_CHAR((timestamp AT TIME ZONE 'UTC') AT TIME ZONE 'America/Sao_Paulo', 'YYYY-MM-DD HH24:MI:SS') AS formatted_timestamp 
                       FROM log_acesso 
                       ORDER BY log_id DESC'''
            cursor.execute(query)
            linhas = cursor.fetchall()
            for linha in linhas:
                id_acesso, tipo_user, id_user, email, acao, timestamp = linha
                print(f"ID de Acesso: {id_acesso}, \nTipo de Usuário: {tipo_user}, \nID do Usuário: {id_user}, \nEmail: {email}, \nAção: {acao}, \nAno-Mês-Dia - Hora:Minuto:Segundo: {timestamp}\n")
    except Exception as error:
        print(f"Ocorreu um erro ao recuperar os logs de acesso: {error}")
    finally:
        connection.close()

def print_logs_compras():
    """
    Recupera e imprime os logs de compras do banco de dados.
    """
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = '''SELECT 
                    id_pagamento, 
                    celular_cliente, 
                    TO_CHAR((data_pagamento AT TIME ZONE 'UTC') AT TIME ZONE 'America/Sao_Paulo', 'YYYY-MM-DD HH24:MI:SS') AS formatted_date, 
                    valor_pagamento, tipo_pagamento, prato_vendido, endereco_entrega 
                FROM pagamentos
                ORDER BY id_pagamento DESC'''
            cursor.execute(query)
            linhas = cursor.fetchall()
            for linha in linhas:
                id_pagamento, celular_cliente, formatted_date, valor_pagamento, tipo_pagamento, prato_vendido, endereco_entrega = linha
                print(f"ID da Compra: {id_pagamento}, \nCelular do Cliente: {celular_cliente}, \nData: {formatted_date}, \nValor do Pagamento: {valor_pagamento}, \nTipo de Pagamento: {tipo_pagamento}, \nPrato Vendido: {prato_vendido}, \nEndereço de Entrega: {endereco_entrega}\n")
    except Exception as error:
        print(f"Ocorreu um erro ao recuperar os logs de compras: {error}")
    finally:
        connection.close()