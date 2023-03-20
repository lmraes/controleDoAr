# O sistema deverá conter a leitura dos valores de parâmetros utilizados pela CETESB
print('\n\nSistema de Controle de Qualidade do Ar e Efeitos à Saúde\n')

#Variável de controle de fim do programa
continuar = True

while continuar == True:

    #Entradas
    try:
        particulasInalaveis_MP10 = int(input('\nInsira o valor das Partículas inaláveis (MP10): '))

        particulasInalaveisFinas_MP25 = int(input('\nInsira o valor das Partículas inaláveis finas (MP2,5): '))

        ozonio_o3 = int(input('\nInsira o valor do Ozônio (O³): '))

        monoxidoDeCarbono_co = int(input('\nInsira o valor do Monóxido de Carbono (CO): '))

        dioxidoDeNitrogenio_no2 = int(input('\nInsira o valor do Dióxido de Nitrogênio (NO²): '))

        DioxidoDeEnxofre_so2 = int(input('\nInsira o valor do Dióxido de Enxofre (SO²): '))
    except:
        print('\nVerifique se os valores digitados são válidos e tente novamente!\nFinalizando o programa...\n\n')
        break
          
    # Condicionais
    if particulasInalaveis_MP10 < 0  or particulasInalaveisFinas_MP25 < 0 or ozonio_o3 < 0 or monoxidoDeCarbono_co < 0 or dioxidoDeNitrogenio_no2 < 0 or DioxidoDeEnxofre_so2 < 0:
        print('\nValores menores que zero são inválidos!')
             
    elif (particulasInalaveis_MP10 >= 0 and particulasInalaveis_MP10 < 50) and (particulasInalaveisFinas_MP25 >= 0 and particulasInalaveisFinas_MP25 < 25) and (ozonio_o3 >= 0 and ozonio_o3 < 100) and (monoxidoDeCarbono_co >= 0 and monoxidoDeCarbono_co < 9) and (dioxidoDeNitrogenio_no2 >= 0 and dioxidoDeNitrogenio_no2 < 200) and (DioxidoDeEnxofre_so2 >= 0 and DioxidoDeEnxofre_so2 < 20):
        print('\nQualidade N1 - BOA\n')

    elif (particulasInalaveis_MP10 >= 50 and particulasInalaveis_MP10 < 100) and (particulasInalaveisFinas_MP25 >= 25 and particulasInalaveisFinas_MP25 < 50) and (ozonio_o3 >= 100 and ozonio_o3 < 130) and (monoxidoDeCarbono_co >= 9 and monoxidoDeCarbono_co < 11) and (dioxidoDeNitrogenio_no2 >= 200 and dioxidoDeNitrogenio_no2 < 240) and (DioxidoDeEnxofre_so2 >= 20 and DioxidoDeEnxofre_so2 < 40):
        print('\nQualidade N2 - MODERADA\n\tPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.')

    elif (particulasInalaveis_MP10 >= 100 and particulasInalaveis_MP10 < 150) and (particulasInalaveisFinas_MP25 >= 50 and particulasInalaveisFinas_MP25 < 75) and (ozonio_o3 >= 130 and ozonio_o3 < 160) and (monoxidoDeCarbono_co >= 11 and monoxidoDeCarbono_co < 13) and (dioxidoDeNitrogenio_no2 >= 240 and dioxidoDeNitrogenio_no2 < 320) and (DioxidoDeEnxofre_so2 >= 40 and DioxidoDeEnxofre_so2 < 365):
        print('\nQualidade N3 - RUIM\n\tToda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.')

    elif (particulasInalaveis_MP10 >= 150 and particulasInalaveis_MP10 < 250) and (particulasInalaveisFinas_MP25 >= 75 and particulasInalaveisFinas_MP25 < 125) and (ozonio_o3 >= 160 and ozonio_o3 < 200) and (monoxidoDeCarbono_co >= 13 and monoxidoDeCarbono_co < 15) and (dioxidoDeNitrogenio_no2 >= 320 and dioxidoDeNitrogenio_no2 < 1130) and (DioxidoDeEnxofre_so2 >= 365 and DioxidoDeEnxofre_so2 < 800):
        print('\nQualidade N4 - MUITO RUIM\n\tToda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).') 

    elif (particulasInalaveis_MP10 > 250) and (particulasInalaveisFinas_MP25 > 125) and (ozonio_o3 > 200) and (monoxidoDeCarbono_co > 15) and (dioxidoDeNitrogenio_no2 > 1130) and (DioxidoDeEnxofre_so2 > 800):
        print('\nQualidade N5 - PÉSSIMA\n\tToda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.') 

    continuar = input('\nDeseja continuar? (S/N)    ')

    if (continuar == 's') or (continuar == 'S'):
        continuar = True
    elif (continuar == 'n') or (continuar == 'N'):
        continuar = False
        print('\nFinalizando o programa...\n\n')
        break
    else:
        print('\nOpção inválida!\nFinalizando o programa...\n\n')
        break
            


    
