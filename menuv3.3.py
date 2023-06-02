from tkinter import messagebox  # o messagebox é um módulo do tkinter
import tkinter as tk
from funcoes import inserirDados, excluirDados, analisarDados, obtemConexaoComMySQL
import mysql.connector

class Application(tk.Frame): # application representa a aplicação principal (ela vem da tk.Frame, que é um widget da biblioteca Tkinter)
    def __init__(self, master=None):  # init inicializa a janela e chama o create widget
        self.quit_called = False
        self.fontePadrao = ("Arial", "11")
        super().__init__(master)
        self.master = master
        self.master.title("Sistema de Controle de Qualidade do Ar e Efeitos à Saúde")
        self.pack()
        self.create_widgets()

    def popup_mensagem(self, mensagem):
        messagebox.showinfo("Mensagem", mensagem)

    def quit(self):
        self.quit_called = True
        self.master.destroy()

    def create_widgets(self):
        self.espaco = tk.Label(self, text="")
        self.espaco.pack(pady=5)

        self.label1 = tk.Label(
            self, text="Sistema de Controle de Qualidade do Ar e Efeitos à Saúde\n\n")
        self.label1["font"] = ("bold")
        self.label1.pack()

        self.label2 = tk.Label(self, text="Menu\n")
        self.label2["font"] = ("Arial", "15", "italic", "bold")
        self.label2.pack()

        self.inserirDados = inserirDados

        self.button1 = tk.Button(
            self, text="Inserir dados", command=self.popup_inserir_dados)
        self.button1["width"] = 20
        self.button1["font"] = self.fontePadrao
        self.button1.pack()

        self.button2 = tk.Button(
            self, text="Alterar dados", command=self.VerificaData)
        self.button2["width"] = 20
        self.button2["font"] = self.fontePadrao
        self.button2.pack()

        self.button3 = tk.Button(
            self, text="Excluir dados", command=self.VerificaDataExcluir)
        self.button3["width"] = 20
        self.button3["font"] = self.fontePadrao
        self.button3.pack()

        self.button4 = tk.Button(
            self, text="Analisar dados", command=analisarDados)
        self.button4["width"] = 20
        self.button4["font"] = self.fontePadrao
        self.button4.pack()

        self.button5 = tk.Button(self, text="Sair", command=self.quit)
        self.button5["width"] = 20
        self.button5["font"] = self.fontePadrao
        self.button5.pack()

        self.espaco = tk.Label(self, text="")
        self.espaco.pack(pady=15)

    def popup_inserir_dados(self):  # inserir
        self.popup = tk.Toplevel(self)
        self.popup.title("Inserir Dados")
        self.popup.geometry("400x350")
        self.popup.focus_set()

        tk.Label(self.popup, text="Insira os valores a seguir:").grid(
            row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.popup, text="Partículas Inaláveis (MP10):").grid(
            row=1, column=0, padx=10, pady=10)
        self.varMP10 = tk.Entry(self.popup)
        self.varMP10.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.popup, text="Partículas Inaláveis Finas (MP2.5):").grid(
            row=2, column=0, padx=10, pady=10)
        self.varMP25 = tk.Entry(self.popup)
        self.varMP25.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.popup, text="Ozônio (O3):").grid(
            row=3, column=0, padx=10, pady=10)
        self.varO3 = tk.Entry(self.popup)
        self.varO3.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.popup, text="Monóxido de Carbono (CO):").grid(
            row=4, column=0, padx=10, pady=10)
        self.varCO = tk.Entry(self.popup)
        self.varCO.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.popup, text="Dióxido de Nitrogênio (NO2):").grid(
            row=5, column=0, padx=10, pady=10)
        self.varNO2 = tk.Entry(self.popup)
        self.varNO2.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self.popup, text="Dióxido de Carbono (SO2):").grid(
            row=6, column=0, padx=10, pady=10)
        self.varSO2 = tk.Entry(self.popup)
        self.varSO2.grid(row=6, column=1, padx=10, pady=10)

        tk.Button(self.popup, text="Cancelar", command=self.popup.destroy).grid(
            row=7, column=0, padx=10, pady=10)
        tk.Button(self.popup, text="Salvar", command=self.salvar_dados_and_fechar_popup).grid(
            row=7, column=1, padx=10, pady=10)

    def salvar_dados_and_fechar_popup(self):
        self.salvar_dados()
        self.popup.destroy()

    def salvar_dados(self):  # insert no bd
        try:
            varMP10 = int(self.varMP10.get())
            varMP25 = int(self.varMP25.get())
            varO3 = int(self.varO3.get())
            varCO = int(self.varCO.get())
            varNO2 = int(self.varNO2.get())
            varSO2 = int(self.varSO2.get())

            if varMP10 >= 0 and varMP25 >= 0 and varO3 >= 0 and varCO >= 0 and varNO2 >= 0 and varSO2 >= 0:
                comando = "INSERT INTO PARAMETROS(DADO_DATA,MP10, MP25, O3, CO, NO2, SO2) VALUES (curdate(),%i,%i,%i,%i,%i,%i)" % (
                    varMP10, varMP25, varO3, varCO, varNO2, varSO2)
                conexao = obtemConexaoComMySQL(
                    'us-cdbr-east-06.cleardb.net', 'ba22761bd77f18', '843e35b3', 'heroku_3b513f8347c686c')
                cursor = conexao.cursor()
                cursor.execute(comando)
                conexao.commit()
                self.popup_mensagem("Dados inseridos com sucesso.")
            else:
                self.popup_mensagem(
                    "Digite valores iguais ou maiores que zero!")
        except ValueError:
            self.popup_mensagem("Valor inválido, tente novamente!")

    class VerificaData:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Verificar Data")

            dia_label = tk.Label(self.root, text="Dia:")
            dia_label.grid(row=0, column=0)
            self.dia_entry = tk.Entry(self.root)
            self.dia_entry.grid(row=0, column=1)

            mes_label = tk.Label(self.root, text="Mês:")
            mes_label.grid(row=1, column=0)
            self.mes_entry = tk.Entry(self.root)
            self.mes_entry.grid(row=1, column=1)

            ano_label = tk.Label(self.root, text="Ano:")
            ano_label.grid(row=2, column=0)
            self.ano_entry = tk.Entry(self.root)
            self.ano_entry.grid(row=2, column=1)

            submit_button = tk.Button(
                self.root, text="Verificar", command=self.verificaData)
            submit_button.grid(row=3, column=0, columnspan=2)

            self.result_label = tk.Label(self.root, text="")
            self.result_label.grid(row=4, column=0, columnspan=2)

            self.data_label = tk.Label(self.root, text="")
            self.data_label.grid(row=5, column=0, columnspan=2)

            self.ids_label = tk.Label(self.root, text="")
            self.ids_label.grid(row=6, column=0, columnspan=2)

            self.root.mainloop()

        def verificaData(self):
            try:
                dia = int(self.dia_entry.get())
                mes = int(self.mes_entry.get())
                ano = int(self.ano_entry.get())

                if ano < 2000:
                    messagebox.showerror(
                        "Erro", "Este programa não lida com datas anteriores a 2000!")
                elif dia < 1 or dia > 31:
                    messagebox.showerror("Erro", "Dia inválido!")
                elif mes < 1 or mes > 12:
                    messagebox.showerror("Erro", "Mês inválido!")
                elif mes in [4, 6, 9, 11] and dia > 30:
                    messagebox.showerror(
                        "Erro", "Este mês não pode ter mais que 30 dias!")
                elif mes == 2 and dia > 29:
                    messagebox.showerror(
                        "Erro", "Fevereiro nunca tem mais que 29 dias")
                elif ano > 1582 and not (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0) and mes == 2 and dia > 28:
                    messagebox.showerror(
                        "Erro", "Fevereiro não tem mais que 28 dias em um ano que não seja bissexto!")
                else:
                    conexao = obtemConexaoComMySQL(
                        'us-cdbr-east-06.cleardb.net', 'ba22761bd77f18', '843e35b3', 'heroku_3b513f8347c686c')
                    try:
                        with conexao.cursor() as cursor:
                            comando = "SELECT * FROM PARAMETROS WHERE DADO_DATA = '%i-%i-%i'" % (
                                ano, mes, dia)
                            cursor.execute(comando)
                            dadosSelecionados = cursor.fetchall()

                            if len(dadosSelecionados) == 0:
                                messagebox.showinfo(
                                    "Informação", "Não existem dados na data solicitada. Tente novamente com outra data.")
                            else:
                                self.abreJanelaDados(dadosSelecionados)
                    except Exception as e:
                        print(f"Ocorreu um erro: {e}")
                    finally:
                        conexao.close()
            except:
                messagebox.showerror(
                    "Erro", "Dia, mês e ano devem ser números!")

            self.root.destroy()

        def abreJanelaDados(self, data):
            janelaDados(data)

    class VerificaDataExcluir:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Verificar Data")

            dia_label = tk.Label(self.root, text="Dia:")
            dia_label.grid(row=0, column=0)
            self.dia_entry = tk.Entry(self.root)
            self.dia_entry.grid(row=0, column=1)

            mes_label = tk.Label(self.root, text="Mês:")
            mes_label.grid(row=1, column=0)
            self.mes_entry = tk.Entry(self.root)
            self.mes_entry.grid(row=1, column=1)

            ano_label = tk.Label(self.root, text="Ano:")
            ano_label.grid(row=2, column=0)
            self.ano_entry = tk.Entry(self.root)
            self.ano_entry.grid(row=2, column=1)

            submit_button = tk.Button(
                self.root, text="Verificar", command=self.VerificaDataExcluir)
            submit_button.grid(row=3, column=0, columnspan=2)

            self.result_label = tk.Label(self.root, text="")
            self.result_label.grid(row=4, column=0, columnspan=2)

            self.data_label = tk.Label(self.root, text="")
            self.data_label.grid(row=5, column=0, columnspan=2)

            self.ids_label = tk.Label(self.root, text="")
            self.ids_label.grid(row=6, column=0, columnspan=2)

            self.root.mainloop()

        def VerificaDataExcluir(self):
            try:
                dia = int(self.dia_entry.get())
                mes = int(self.mes_entry.get())
                ano = int(self.ano_entry.get())

                if ano < 2000:
                    messagebox.showerror(
                        "Erro", "Este programa não lida com datas anteriores a 2000!")
                elif dia < 1 or dia > 31:
                    messagebox.showerror("Erro", "Dia inválido!")
                elif mes < 1 or mes > 12:
                    messagebox.showerror("Erro", "Mês inválido!")
                elif mes in [4, 6, 9, 11] and dia > 30:
                    messagebox.showerror(
                        "Erro", "Este mês não pode ter mais que 30 dias!")
                elif mes == 2 and dia > 29:
                    messagebox.showerror(
                        "Erro", "Fevereiro nunca tem mais que 29 dias")
                elif ano > 1582 and not (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0) and mes == 2 and dia > 28:
                    messagebox.showerror(
                        "Erro", "Fevereiro não tem mais que 28 dias em um ano que não seja bissexto!")
                else:
                    conexao = obtemConexaoComMySQL(
                        'us-cdbr-east-06.cleardb.net', 'ba22761bd77f18', '843e35b3', 'heroku_3b513f8347c686c')
                    try:
                        with conexao.cursor() as cursor:
                            comando = "SELECT * FROM PARAMETROS WHERE DADO_DATA = '%i-%i-%i'" % (
                                ano, mes, dia)
                            cursor.execute(comando)
                            dadosSelecionados = cursor.fetchall()

                            if len(dadosSelecionados) == 0:
                                messagebox.showinfo(
                                    "Informação", "Não existem dados na data solicitada. Tente novamente com outra data.")
                            else:
                                self.abreJanelaDadosExcluir(dadosSelecionados)
                    except Exception as e:
                        print(f"Ocorreu um erro: {e}")
                    finally:
                        conexao.close()
            except:
                messagebox.showerror(
                    "Erro", "Dia, mês e ano devem ser números!")

            self.root.destroy()

        def abreJanelaDadosExcluir(self, data):
            janelaDadosExcluir(data)


class janelaDados:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title("Dados")

        self.ids_label = tk.Label(self.root, text="IDs e Valores:")
        self.ids_label.pack()

        for linha in data:
            var_id = int(linha[0])
            var_MP10 = int(linha[2])
            var_MP25 = int(linha[3])
            var_O3 = int(linha[4])
            var_CO = int(linha[5])
            var_NO2 = int(linha[6])
            var_SO2 = int(linha[7])

            label_text = "ID: %d - MP10: %d, MP25: %d, O3: %d, CO: %d, NO2: %d, SO2: %d" % (
                var_id, var_MP10, var_MP25, var_O3, var_CO, var_NO2, var_SO2
            )

            label = tk.Label(self.root, text=label_text)
            label.pack()

        confirm_button = tk.Button(
            self.root, text="Confirmar", command=self.alterar)
        confirm_button.pack()

    def alterar(self):
        def on_confirm():
            escolhaId = int(id_entry.get())

            var_MP10 = int(mp10_entry.get())
            var_MP25 = int(mp25_entry.get())
            var_O3 = int(o3_entry.get())
            var_CO = int(co_entry.get())
            var_NO2 = int(no2_entry.get())
            var_SO2 = int(so2_entry.get())

            try:
                conexao = obtemConexaoComMySQL(
                    'us-cdbr-east-06.cleardb.net', 'ba22761bd77f18', '843e35b3', 'heroku_3b513f8347c686c')
                conexao.reconnect()
                cursor = conexao.cursor()
                comando = ("UPDATE PARAMETROS SET MP10 = %i, MP25 = %i, O3 = %i, CO = %i, NO2 = %i, SO2 = %i WHERE ID = %i") % (
                    var_MP10, var_MP25, var_O3,
                    var_CO, var_NO2, var_SO2, escolhaId
                )
                cursor.execute(comando)
                conexao.commit()
                messagebox.showinfo(
                    "Informação", "Dados alterados com sucesso.")
                window.destroy()
                self.root.destroy()
            except Exception as e:
                messagebox.showerror(
                    "Erro", "Erro ao alterar os dados. Tente novamente!")
                print(e)
        
        window = tk.Tk()
        window.title("Alterar Dados")

        id_label = tk.Label(
            window, text="Digite o número do ID para alterar seus dados:")
        id_label.pack()

        id_entry = tk.Entry(window)
        id_entry.pack()

        mp10_label = tk.Label(window, text="Digite o novo valor de MP10:")
        mp10_label.pack()

        mp10_entry = tk.Entry(window)
        mp10_entry.pack()

        mp25_label = tk.Label(window, text="Digite o novo valor de MP25:")
        mp25_label.pack()

        mp25_entry = tk.Entry(window)
        mp25_entry.pack()

        o3_label = tk.Label(window, text="Digite o novo valor de O3:")
        o3_label.pack()

        o3_entry = tk.Entry(window)
        o3_entry.pack()

        co_label = tk.Label(window, text="Digite o novo valor de CO:")
        co_label.pack()

        co_entry = tk.Entry(window)
        co_entry.pack()

        no2_label = tk.Label(window, text="Digite o novo valor de NO2:")
        no2_label.pack()

        no2_entry = tk.Entry(window)
        no2_entry.pack()

        so2_label = tk.Label(window, text="Digite o novo valor de SO2:")
        so2_label.pack()

        so2_entry = tk.Entry(window)
        so2_entry.pack()

        confirm_button = tk.Button(
            window, text="Confirmar", command=on_confirm)
        confirm_button.pack()

        window.mainloop()

class janelaDadosExcluir:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title("Dados")

        self.ids_label = tk.Label(self.root, text="IDs e Valores:")
        self.ids_label.pack()

        for linha in data:
            var_id = int(linha[0])
            var_MP10 = int(linha[2])
            var_MP25 = int(linha[3])
            var_O3 = int(linha[4])
            var_CO = int(linha[5])
            var_NO2 = int(linha[6])
            var_SO2 = int(linha[7])

            label_text = "ID: %d - MP10: %d, MP25: %d, O3: %d, CO: %d, NO2: %d, SO2: %d" % (
                var_id, var_MP10, var_MP25, var_O3, var_CO, var_NO2, var_SO2)

            label = tk.Label(self.root, text=label_text)
            label.pack()

        confirm_button = tk.Button(self.root, text="Confirmar", command=self.excluir)
        confirm_button.pack()

    def excluir(self):
            window = tk.Tk()
            window.title("Excluir Dados")

            id_label = tk.Label(window, text="Digite o número do ID para excluir seus dados:")
            id_label.pack()

            id_entry = tk.Entry(window)
            id_entry.pack()

            def on_confirm():
                escolhaId = int(id_entry.get())
                conexao = obtemConexaoComMySQL('us-cdbr-east-06.cleardb.net', 'ba22761bd77f18', '843e35b3', 'heroku_3b513f8347c686c')
                conexao.reconnect()
                cursor = conexao.cursor()
                try:
                    comando = "DELETE FROM PARAMETROS WHERE ID= '%s'" % (escolhaId)
                    cursor.execute(comando)
                    conexao.commit()
                    messagebox.showinfo("Informação", "Dados excluídos com sucesso.")
                except Exception as e:
                    messagebox.showerror("Erro", "Erro ao excluir os dados. Tente novamente!")
                    print(e)

                cursor.close()
                conexao.close()
                window.destroy()
                self.root.destroy()
                        
            confirm_button = tk.Button(window, text="Confirmar", command=on_confirm)
            confirm_button.pack()

            window.mainloop()

def classificacaoQualidadeDoAr(lista):

    if 'N5' in lista:
        varn5 = ("\nQualidade do ar: N5 - Péssima\n\nToda a população pode apresentar sérios riscos \nde manifestações de doenças respiratórias e cardiovasculares.\n Aumento de mortes prematuras em pessoas de grupos sensíveis.\n\n")
        return varn5
    elif 'N4' in lista:
        varn4 = ("\nQualidade do ar: N4 - Muito Ruim\n\nToda a população pode apresentar agravamento dos sintomas como tosse seca,\n cansaço, ardor nos olhos, \nnariz e garganta e ainda falta de ar e respiração ofegante.\nEfeitos ainda mais graves à saúde de grupos sensíveis\n(crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n\n")
        return varn4
    elif 'N3' in lista:
        varn3 = ("\nQualidade do ar: N3 - Ruim\n\nToda a população pode apresentar sintomas como tosse seca,\ncansaço, ardor nos olhos, nariz e garganta.\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças\n respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n\n")
        return varn3
    elif 'N2' in lista:
        varn2 = ("\nQualidade do ar: N2 - Moderada\n\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças\nrespiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço.\n A população, em geral, não é afetada.\n\n")
        return varn2
    elif 'N1' in lista:
        varn1 = ("\nQualidade do ar: N1 - Boa\n\n")
        return varn1

def calculoIndice(listaDados):
    qualidadeDoAr = []

    particulasInalaveis_MP10 = listaDados[0]
    particulasInalaveisFinas_MP25 = listaDados[1]
    ozonio_o3 = listaDados[2]
    monoxidoDeCarbono_co = listaDados[3]
    dioxidoDeNitrogenio_no2 = listaDados[4]
    dioxidoDeEnxofre_so2 = listaDados[5]

    if (particulasInalaveis_MP10 >= 0 and particulasInalaveis_MP10 <= 50):
        indice_mp10 = 0 + ((40 - 0) / (50 - 0)) * \
            (particulasInalaveis_MP10 - 0)
        qualidadeDoAr.append('N1')

    elif (particulasInalaveis_MP10 > 50 and particulasInalaveis_MP10 <= 100):
        indice_mp10 = 41 + ((80 - 41) / (100 - 50)) * \
            (particulasInalaveis_MP10 - 50)
        qualidadeDoAr.append('N2')

    elif (particulasInalaveis_MP10 > 100 and particulasInalaveis_MP10 <= 150):
        indice_mp10 = 81 + ((120 - 81) / (150 - 100)) * \
            (particulasInalaveis_MP10 - 100)
        qualidadeDoAr.append('N3')

    elif (particulasInalaveis_MP10 > 150 and particulasInalaveis_MP10 <= 250):
        indice_mp10 = 121 + ((200 - 121) / (250 - 150)) * \
            (particulasInalaveis_MP10 - 150)
        qualidadeDoAr.append('N4')

    elif (particulasInalaveis_MP10 > 250):
        indice_mp10 = 200 + ((250 - 200) / (350 - 250)) * \
            (particulasInalaveis_MP10 - 250)
        qualidadeDoAr.append('N5')

    if (particulasInalaveisFinas_MP25 >= 0 and particulasInalaveisFinas_MP25 <= 25):
        indice_mp25 = 0 + ((40 - 0) / (25 - 0)) * \
            (particulasInalaveisFinas_MP25 - 0)
        qualidadeDoAr.append('N1')

    elif (particulasInalaveisFinas_MP25 > 25 and particulasInalaveisFinas_MP25 <= 50):
        indice_mp25 = 41 + ((80 - 41) / (50 - 25)) * \
            (particulasInalaveisFinas_MP25 - 25)
        qualidadeDoAr.append('N2')

    elif (particulasInalaveisFinas_MP25 > 50 and particulasInalaveisFinas_MP25 <= 75):
        indice_mp25 = 81 + ((120 - 81) / (75 - 50)) * \
            (particulasInalaveisFinas_MP25 - 50)
        qualidadeDoAr.append('N3')

    elif (particulasInalaveisFinas_MP25 > 75 and particulasInalaveisFinas_MP25 <= 125):
        indice_mp25 = 121 + ((200 - 121) / (125 - 75)) * \
            (particulasInalaveisFinas_MP25 - 75)
        qualidadeDoAr.append('N4')

    elif (particulasInalaveisFinas_MP25 > 125):
        indice_mp25 = 200 + ((250 - 200) / (225 - 125)) * \
            (particulasInalaveisFinas_MP25 - 125)
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
        indice_o3 = 121 + ((200 - 121)/(200 - 160))*(ozonio_o3 - 160)
        qualidadeDoAr.append('N4')

    elif (ozonio_o3 > 200):
        indice_o3 = 200 + ((250 - 200)/(250 - 200))*(ozonio_o3 - 200)
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

    elif (monoxidoDeCarbono_co > 15):
        indice_co = 200 + ((250 - 200)/(15 - 20)) * (monoxidoDeCarbono_co - 15)
        qualidadeDoAr.append('N5')

    if (dioxidoDeNitrogenio_no2 >= 0 and dioxidoDeNitrogenio_no2 <= 200):
        indice_no2 = 0 + ((40 - 0) / (200 - 0)) * (dioxidoDeNitrogenio_no2 - 0)
        qualidadeDoAr.append('N1')

    elif (dioxidoDeNitrogenio_no2 > 200 and dioxidoDeNitrogenio_no2 <= 240):
        indice_no2 = 41 + ((80 - 41) / (240 - 200)) * \
            (dioxidoDeNitrogenio_no2 - 200)
        qualidadeDoAr.append('N2')

    elif (dioxidoDeNitrogenio_no2 > 240 and dioxidoDeNitrogenio_no2 <= 320):
        indice_no2 = 81 + ((120 - 81) / (320 - 240)) * \
            (dioxidoDeNitrogenio_no2 - 320)
        qualidadeDoAr.append('N3')

    elif (dioxidoDeNitrogenio_no2 > 320 and dioxidoDeNitrogenio_no2 <= 1130):
        indice_no2 = 121 + ((200 - 121) / (1130 - 320)) * \
            (dioxidoDeNitrogenio_no2 - 320)
        qualidadeDoAr.append('N4')

    elif (dioxidoDeNitrogenio_no2 > 1130):
        indice_no2 = 200 + ((250 - 200) / (1260 - 1130)) * \
            (dioxidoDeNitrogenio_no2 - 1130)
        qualidadeDoAr.append('N5')

    if (dioxidoDeEnxofre_so2 >= 0 and dioxidoDeEnxofre_so2 <= 20):
        indice_so2 = 0 + ((40 - 0) / (20 - 0)) * (dioxidoDeEnxofre_so2 - 0)
        qualidadeDoAr.append('N1')

    elif (dioxidoDeEnxofre_so2 > 20 and dioxidoDeEnxofre_so2 <= 40):
        indice_so2 = 41 + ((80 - 41) / (40 - 20)) * \
            (dioxidoDeNitrogenio_no2 - 20)
        qualidadeDoAr.append('N2')

    elif (dioxidoDeEnxofre_so2 > 40 and dioxidoDeEnxofre_so2 <= 365):
        indice_so2 = 81 + ((120 - 81) / (365 - 40)) * \
            (dioxidoDeEnxofre_so2 - 40)
        qualidadeDoAr.append('N3')

    elif (dioxidoDeEnxofre_so2 > 365 and dioxidoDeEnxofre_so2 <= 800):
        indice_so2 = 121 + ((200 - 121) / (800 - 365)) * \
            (dioxidoDeEnxofre_so2 - 365)
        qualidadeDoAr.append('N4')

    elif (dioxidoDeEnxofre_so2 > 800):
        indice_so2 = 200 + ((250 - 200) / (1000 - 800)) * \
            (dioxidoDeEnxofre_so2 - 800)
        qualidadeDoAr.append('N5')

    return [[str(indice_mp10), str(indice_mp25), str(indice_o3), str(indice_co), str(indice_no2), str(indice_so2)], qualidadeDoAr]

def analisarDados():
    window = tk.Toplevel(master=root)
    window.title("Analisar Dados")
    window.geometry("450x450")

    try:
        comando = "SELECT * FROM PARAMETROS"
        conexao = obtemConexaoComMySQL(
            'us-cdbr-east-06.cleardb.net', 'ba22761bd77f18', '843e35b3', 'heroku_3b513f8347c686c')
        cursor = conexao.cursor()
        cursor.execute(comando)
        dadosSelecionados = cursor.fetchall()
        tamanho = len(dadosSelecionados) - 1
        retornaLinha = 0
        analise_label = None
    except Exception as e:
            messagebox.showerror(
                "Erro", "Erro ao analisar os dados. Tente novamente!")
            print(e)
    while True:
        linha = dadosSelecionados[retornaLinha]
        particulasInalaveis_MP10 = int(linha[2])
        particulasInalaveisFinas_MP25 = int(linha[3])
        ozonio_o3 = int(linha[4])
        monoxidoDeCarbono_co = int(linha[5])
        dioxidoDeNitrogenio_no2 = int(linha[6])
        dioxidoDeEnxofre_so2 = int(linha[7])

        if particulasInalaveis_MP10 >= 0 and particulasInalaveisFinas_MP25 >= 0 and ozonio_o3 >= 0 and monoxidoDeCarbono_co >= 0 and dioxidoDeNitrogenio_no2 >= 0 and dioxidoDeEnxofre_so2 >= 0:
            listaDados = [particulasInalaveis_MP10, particulasInalaveisFinas_MP25,
                        ozonio_o3, monoxidoDeCarbono_co, dioxidoDeNitrogenio_no2, dioxidoDeEnxofre_so2]
            calculoIndice(listaDados)
            respostaIndice = calculoIndice(listaDados)
            respostaQualidade = classificacaoQualidadeDoAr(respostaIndice[1])
            resultado = ("Índice MP10:", respostaIndice[0][0], "\nÍndice MP25:", respostaIndice[0][1], "\nÍndice O3:", respostaIndice[0]
                        [2], "\nÍndice CO:", respostaIndice[0][3], "\nÍndice NO2:", respostaIndice[0][4], "\nÍndice SO2:", respostaIndice[0][5])
            resultado += ("\n\n", respostaQualidade)
            
            if analise_label is None:
                analise_label = tk.Label(
                    window, text='\n'.join(str(item) for item in resultado))
                analise_label.pack()
            else:
                analise_label.config(text='\n'.join(str(item)
                                    for item in resultado))
        else:
            messagebox.showinfo(
                "Erro", "Digite valores iguais ou maiores que zero!")

        resposta = messagebox.askquestion(
            "Verificar Novamente", "Deseja verificar novamente?",parent=window)
        if resposta == 'no':
            window.destroy()
            break
        else:
            if retornaLinha == tamanho:
                messagebox.showinfo(
                    "Erro", "\nNão existem mais parâmetros para análise",parent=window)
                window.destroy()
                break
            else:
                analise_label.config(text="")
                retornaLinha += 1
    window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

while True:
    app.mainloop()

    if app.quit_called:
        break