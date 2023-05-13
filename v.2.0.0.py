# Código da versão v2.0.0
# Instalar no terminal: pip install mysql-connector-python

from mysql.connector import connect
def obtemConexaoComMySQL (servidor, usuario, senha, bd):
    if obtemConexaoComMySQL.conexao == None:
        obtemConexaoComMySQL.conexao = \
        connect(host = servidor, user = usuario, passwd = senha, database = bd)
    return obtemConexaoComMySQL.conexao
obtemConexaoComMySQL.conexao = None

print('\n\nSistema de Controle de Qualidade do Ar e Efeitos à Saúde\n')
retornaLinha = 0
while True:
    while True:
        comando = "SELECT * FROM PARAMETROS"
        conexao = obtemConexaoComMySQL('us-cdbr-east-06.cleardb.net','ba22761bd77f18','843e35b3','heroku_3b513f8347c686c')
        cursor = conexao.cursor()
        cursor.execute(comando)
        dadosSelecionados = cursor.fetchall()
        tamanho = len(dadosSelecionados) - 1
        array = [dadosSelecionados[retornaLinha]]
        try:
            for linha in array:
                particulasInalaveis_MP10 = int(linha[2])
                particulasInalaveisFinas_MP25 = int(linha[3])
                ozonio_o3 = int(linha[4])
                monoxidoDeCarbono_co = int(linha[5])
                dioxidoDeNitrogenio_no2 = int(linha[6])
                dioxidoDeEnxofre_so2 = int(linha[7])
        except ValueError:
            print('\nVerifique se os valores digitados são válidos e tente novamente!')
        else:
            if particulasInalaveis_MP10 >= 0  and particulasInalaveisFinas_MP25 >= 0 and ozonio_o3 >= 0 and monoxidoDeCarbono_co >= 0 and dioxidoDeNitrogenio_no2 >= 0 and dioxidoDeEnxofre_so2 >= 0: break
            print("\nDigite valores iguais ou maiores que zero!")
          
    qualidadeDoAr = []

    if (particulasInalaveis_MP10 >= 0 and particulasInalaveis_MP10 <= 50):
       indice_mp10 = 0 + ((40 - 0) / (50 - 0)) * (particulasInalaveis_MP10 - 0)
       qualidadeDoAr.append('N1')
        
    elif (particulasInalaveis_MP10 > 50 and particulasInalaveis_MP10 <= 100): 
       indice_mp10 = 41 + ((80 - 41) / (100 - 50)) * (particulasInalaveis_MP10 - 50)
       qualidadeDoAr.append('N2')

    elif (particulasInalaveis_MP10 > 100 and particulasInalaveis_MP10 <= 150):  
        indice_mp10 = 81 + ((120 - 81) / (150 - 100)) * (particulasInalaveis_MP10 - 100)
        qualidadeDoAr.append('N3')

    elif (particulasInalaveis_MP10 > 150 and particulasInalaveis_MP10 <= 250): 
        indice_mp10 = 121 + ((200 - 121) / (250 - 150)) * (particulasInalaveis_MP10 - 150)
        qualidadeDoAr.append('N4')

    elif (particulasInalaveis_MP10 > 250):
        indice_mp10 = 200 + ((250 - 200) / (350 - 250)) * (particulasInalaveis_MP10 - 250)
        qualidadeDoAr.append('N5')

    if (particulasInalaveisFinas_MP25 >= 0 and particulasInalaveisFinas_MP25 <= 25):
        indice_mp25 = 0 + ((40 - 0) / (25 - 0)) * (particulasInalaveisFinas_MP25 - 0)
        qualidadeDoAr.append('N1')

    elif (particulasInalaveisFinas_MP25 > 25 and particulasInalaveisFinas_MP25 <= 50):
        indice_mp25 = 41 + ((80 - 41) / (50 - 25)) * (particulasInalaveisFinas_MP25 - 25)
        qualidadeDoAr.append('N2')

    elif (particulasInalaveisFinas_MP25 > 50 and particulasInalaveisFinas_MP25 <= 75):
        indice_mp25 = 81 + ((120 - 81) / (75 - 50)) * (particulasInalaveisFinas_MP25 - 50)
        qualidadeDoAr.append('N3')

    elif (particulasInalaveisFinas_MP25 > 75 and particulasInalaveisFinas_MP25 <= 125):
        indice_mp25 = 121 + ((200 - 121) / (125 - 75)) * (particulasInalaveisFinas_MP25 - 75)
        qualidadeDoAr.append('N4')

    elif (particulasInalaveisFinas_MP25 > 125):
        indice_mp25 = 200 + ((250 - 200) / (225 - 125)) * (particulasInalaveisFinas_MP25 - 125)
        qualidadeDoAr.append('N5')
   
    if (ozonio_o3 >= 0 and ozonio_o3 <= 100):
        indice_o3 = 0 + ((40 - 0)/(100-0))*(ozonio_o3 - 0)
        qualidadeDoAr.append('N1') 

    elif (ozonio_o3 > 100 and ozonio_o3 <= 130):
        indice_o3 = 41 + ((80 - 41)/(130 - 100))*(ozonio_o3 - 100) 
        qualidadeDoAr.append('N2')

    elif (ozonio_o3 > 130 and ozonio_o3 <= 160):
        indice_o3 = 81 + ((120 - 81)/(160 - 130))*(ozonio_o3 - 130) 
        qualidadeDoAr.append('N3')

    elif (ozonio_o3 > 160 and ozonio_o3 <= 200): 
        indice_o3= 121 + ((200 - 121)/(200 - 160))*(ozonio_o3 - 160) 
        qualidadeDoAr.append('N4')

    elif (ozonio_o3 > 200): 
        indice_o3= 200 + ((250 - 200)/(250 - 200))*(ozonio_o3 - 200) 
        qualidadeDoAr.append('N5')
 
    if (monoxidoDeCarbono_co >= 0 and monoxidoDeCarbono_co <= 9):
        indice_co = 0 + ((40 - 0)/(9 - 0))*(monoxidoDeCarbono_co - 0) 
        qualidadeDoAr.append('N1')
    
    elif (monoxidoDeCarbono_co > 9 and monoxidoDeCarbono_co <= 11):
        indice_co = 41 + ((80 - 41)/(11 - 9))*(monoxidoDeCarbono_co - 9) 
        qualidadeDoAr.append('N2')

    elif (monoxidoDeCarbono_co > 11 and monoxidoDeCarbono_co <= 13):
        indice_co = 81 + ((120 - 81)/(13 - 11))*(monoxidoDeCarbono_co - 11) 
        qualidadeDoAr.append('N3')

    elif (monoxidoDeCarbono_co > 13 and monoxidoDeCarbono_co <= 15):
        indice_co = 121 + ((200 - 121)/(15 - 13)) * (monoxidoDeCarbono_co - 13) 
        qualidadeDoAr.append('N4')

    elif(monoxidoDeCarbono_co > 15):
        indice_co = 200 + ((250 - 200)/(15 - 20)) * (monoxidoDeCarbono_co - 15) 
        qualidadeDoAr.append('N5')

    if (dioxidoDeNitrogenio_no2 >= 0 and dioxidoDeNitrogenio_no2 <= 200 ):
        indice_no2 = 0 + ((40 - 0) / (200 - 0)) * (dioxidoDeNitrogenio_no2 - 0)
        qualidadeDoAr.append('N1')

    elif (dioxidoDeNitrogenio_no2 > 200 and dioxidoDeNitrogenio_no2 <= 240):
        indice_no2 = 41 + ((80 - 41) / (240 - 200)) * (dioxidoDeNitrogenio_no2 - 200)
        qualidadeDoAr.append('N2')

    elif (dioxidoDeNitrogenio_no2 > 240 and dioxidoDeNitrogenio_no2 <= 320):
        indice_no2 = 81 + ((120 - 81) / (320 - 240)) * (dioxidoDeNitrogenio_no2 - 320)
        qualidadeDoAr.append('N3')

    elif (dioxidoDeNitrogenio_no2 > 320 and dioxidoDeNitrogenio_no2 <= 1130):
        indice_no2 = 121 + ((200 - 121) / (1130 - 320)) * (dioxidoDeNitrogenio_no2 - 320)
        qualidadeDoAr.append('N4')

    elif (dioxidoDeNitrogenio_no2 > 1130):
        indice_no2 = 200 + ((250 - 200) / (1260 - 1130)) * (dioxidoDeNitrogenio_no2- 1130)
        qualidadeDoAr.append('N5')

    if (dioxidoDeEnxofre_so2 >= 0 and dioxidoDeEnxofre_so2 <= 20):
        indice_so2 = 0 + ((40 - 0) / (20 - 0)) * (dioxidoDeEnxofre_so2 - 0)
        qualidadeDoAr.append('N1')

    elif (dioxidoDeEnxofre_so2 > 20 and dioxidoDeEnxofre_so2 <= 40):
        indice_so2 = 41 + ((80 - 41) / (40 - 20)) * (dioxidoDeNitrogenio_no2 - 20)
        qualidadeDoAr.append('N2')

    elif (dioxidoDeEnxofre_so2 > 40 and dioxidoDeEnxofre_so2 <= 365):
        indice_so2 = 81 + ((120 - 81) / (365 - 40)) * (dioxidoDeEnxofre_so2 - 40)
        qualidadeDoAr.append('N3')

    elif (dioxidoDeEnxofre_so2 > 365 and dioxidoDeEnxofre_so2 <= 800):
        indice_so2 = 121 + ((200 - 121) / (800 - 365)) * (dioxidoDeEnxofre_so2 - 365)
        qualidadeDoAr.append('N4')

    elif (dioxidoDeEnxofre_so2 > 800):
        indice_so2 = 200 + ((250 - 200) / (1000 - 800)) * (dioxidoDeEnxofre_so2 - 800) 
        qualidadeDoAr.append('N5')

    print("\nÍndice MP10:",indice_mp10,"\n\nÍndice MP25:",indice_mp25,"\n\nÍndice Ozônio(O3):",indice_o3,"\n\nÍndice Monóxido de Carbono(CO):",indice_co,"\n\nÍndice Dióxido de Nitrogênio(NO2):",indice_no2,"\n\nÍndice Dióxido de Enxofre(SO2):",indice_so2,"\n")

    if 'N5' in qualidadeDoAr:
        print("\nQualidade do ar: N5 - Péssima\n\nToda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares.\n Aumento de mortes prematuras em pessoas de grupos sensíveis.\n\n")
    elif 'N4' in qualidadeDoAr:
        print("\nQualidade do ar: N4 - Muito Ruim\n\nToda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, \nnariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis\n (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n\n")
    elif 'N3' in qualidadeDoAr:
        print("\nQualidade do ar: N3 - Ruim\n\nToda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. \nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n\n")
    elif 'N2' in qualidadeDoAr:
        print("\nQualidade do ar: N2 - Moderada\n\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço.\n A população, em geral, não é afetada.\n\n")
    elif 'N1' in qualidadeDoAr:
        print("\nQualidade do ar: N1 - Boa\n\n")

    while True:
        resposta = input("\n\nDeseja verificar novamente a qualidade do ar? (S/N)").upper()
        if resposta in ["S","N"]: break
        print("\nDeve-se digitar S ou N. Tente novamente!")
    if resposta == "S": 
        if retornaLinha == tamanho:
            print("\nNão existem mais parâmetros para análise")
            break
        else:
            retornaLinha+=1
    if resposta == "N": break

print("\n\nObrigada por usar este programa. Finalizando...\n\n")

            


    
