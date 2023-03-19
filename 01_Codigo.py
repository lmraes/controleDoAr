# O sistema deverá conter a leitura dos valores de parâmetros utilizados pela CETESB
print('\n\nSistema de Controle de Qualidade do Ar e Efeitos à Saúde\n')

#Variável de controle de fim do programa
continuar = 'S'

while continuar == 'S' or continuar == 's':

    #Entradas
    particulasInalaveis_MP10 = int(input('\nInsira o valor das Partículas inaláveis (MP10): '))

    particulasInalaveisFinas_MP25 = int(input('\nInsira o valor das Partículas inaláveis finas (MP2,5): '))

    ozonio_o3 = int(input('\nInsira o valor do Ozônio (O³): '))

    monoxidoDeCarbono_co = int(input('\nInsira o valor do Monóxido de Carbono (CO): '))

    dioxidoDeNitrogenio_no2 = int(input('\nInsira o valor do Dióxido de Nitrogênio (NO²): '))

    DioxidoDeEnxofre_so2 = int(input('\nInsira o valor do Dióxido de Enxofre (SO²): '))

    # Condicionais
    if particulasInalaveis_MP10 < 0 or particulasInalaveisFinas_MP25 < 0 or ozonio_o3 < 0 or monoxidoDeCarbono_co < 0 or dioxidoDeNitrogenio_no2 < 0 or DioxidoDeEnxofre_so2 < 0:
        print('\nValores menores que zero são inválidos!')
        
    elif (particulasInalaveis_MP10 >= 0 and particulasInalaveis_MP10 <= 50) and (particulasInalaveisFinas_MP25 >= 0 and particulasInalaveisFinas_MP25 <= 25) and (ozonio_o3 >= 0 and ozonio_o3 <= 100) and (monoxidoDeCarbono_co >= 0 and monoxidoDeCarbono_co <= 9) and (dioxidoDeNitrogenio_no2 >= 0 and dioxidoDeNitrogenio_no2 <= 200) and (DioxidoDeEnxofre_so2 >= 0 and DioxidoDeEnxofre_so2 <= 20):
        print('\nA qualidade do ar é boa!')

    elif (particulasInalaveis_MP10 >= 50 and particulasInalaveis_MP10 <= 100) and (particulasInalaveisFinas_MP25 >= 25 and particulasInalaveisFinas_MP25 <= 50) and (ozonio_o3 >= 100 and ozonio_o3 <= 130) and (monoxidoDeCarbono_co >= 9 and monoxidoDeCarbono_co <= 11) and (dioxidoDeNitrogenio_no2 >= 200 and dioxidoDeNitrogenio_no2 <= 240) and (DioxidoDeEnxofre_so2 >= 20 and DioxidoDeEnxofre_so2 <= 40):
        print('\nA qualidade do ar é moderada!')

    elif (particulasInalaveis_MP10 >= 100 and particulasInalaveis_MP10 <= 150) and (particulasInalaveisFinas_MP25 >= 50 and particulasInalaveisFinas_MP25 <= 75) and (ozonio_o3 >= 130 and ozonio_o3 <= 160) and (monoxidoDeCarbono_co >= 11 and monoxidoDeCarbono_co <= 13) and (dioxidoDeNitrogenio_no2 >= 240 and dioxidoDeNitrogenio_no2 <= 320) and (DioxidoDeEnxofre_so2 >= 40 and DioxidoDeEnxofre_so2 <= 365):
        print('\nA qualidade do ar é ruim!')

    elif (particulasInalaveis_MP10 >= 150 and particulasInalaveis_MP10 <= 250) and (particulasInalaveisFinas_MP25 >= 75 and particulasInalaveisFinas_MP25 <= 125) and (ozonio_o3 >= 160 and ozonio_o3 <= 200) and (monoxidoDeCarbono_co >= 13 and monoxidoDeCarbono_co <= 15) and (dioxidoDeNitrogenio_no2 >= 320 and dioxidoDeNitrogenio_no2 <= 1130) and (DioxidoDeEnxofre_so2 >= 365 and DioxidoDeEnxofre_so2 <= 800):
        print('\nA qualidade do ar é muito ruim!')
    
    elif (particulasInalaveis_MP10 > 250) and (particulasInalaveisFinas_MP25 > 125) and (ozonio_o3 > 200) and (monoxidoDeCarbono_co > 15) and (dioxidoDeNitrogenio_no2 > 1130) and (DioxidoDeEnxofre_so2 > 800):
        print('\nA qualidade do ar é péssima!')
    
   

    continuar = input('\nDeseja continuar? (S/N)    ')
    
