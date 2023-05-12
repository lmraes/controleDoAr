# Código da versão v3.0.0
# Instalar no terminal: pip install mysql-connector-python
import funcoes
print('\n\nSistema de Controle de Qualidade do Ar e Efeitos à Saúde\n')
while True:
    opcaoMenu = funcoes.menu()  
    match opcaoMenu:
        case 1:
            funcoes.inserirDados()   
        case 2: 
            funcoes.alterarDados()
        case 3:
            funcoes.excluirDados()
        case 4:
            funcoes.analisarDados()      
        case 5: 
            while True:
                resposta = input("\n\nDeseja sair do programa? (S/N)").upper()
                if resposta in ["S","N"]: break
                print("\nDeve-se digitar S ou N. Tente novamente!")
            if resposta == "S": break
        case _:
            print("\n\nVerifique a opção e tente novamente!")

print("\n\nObrigada por usar este programa. Finalizando...\n\n")

            


    
