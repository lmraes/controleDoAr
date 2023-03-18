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
    
    

    continuar = input('\nDeseja continuar? (S/N)    ')
    