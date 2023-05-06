# import mysql.connector

# try:
#     db = mysql.connector.connect(
#         host='us-cdbr-east-06.cleardb.net',
#         user='ba22761bd77f18',
#         password='843e35b3',
#         database='heroku_3b513f8347c686c',
#         # reconnect=True
#     )
#     print("Conexão bem sucedida!")
# except mysql.connector.Error as error:
#     print("Erro ao tentar conectar ao banco de dados:", error)

#     from mysql.connector import connect

# def obtemConexaoComMySQL (servidor, usuario, senha, bd):
#     if obtemConexaoComMySQL.conexao==None:
#     obtemConexaoComMySQL.conexao = connect(host=servidor, user=usuario, passwd=senha, database=bd)
#     return obtemConexaoComMySQL.conexao

# obtemConexaoComMySQL.conexao=None

# comando="insert into Alunos (RA,Nome) values (23232323,'Neusa Reis')"
# conexao=obtemConexaoComMySQL('us-cdbr-east-06.cleardb.net','ba22761bd77f18','843e35b3','heroku_3b513f8347c686c')
# cursor=conexao.cursor()
# cursor.execute(comando)