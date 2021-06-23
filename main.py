from Dados_analizados import Dados_estudados
from Conecta_Com_Banco import Conecta_Com_Banco
from datetime import datetime

import tkinter as tk
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

JANELA = tk.Tk()
JANELA.geometry("1360x700")
JANELA.title('Interfaca para ALEX')

style.use('fivethirtyeight')

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(20, 20))
fig.tight_layout(pad=15.0)

def main():


        # lista dos componetes da seleção da coluna
        lista3 = {
            "Valor_Bateria": "0.0",
            "Estado_bateria": "False",
            "Temperatura": "0.0",
            "Frequencia": "0.0",
            "Horario": "False",
            "Data": "0.0"

        }
        json = list(lista3.keys())
        caixaSelecao3 = ttk.Combobox(JANELA, values=json)

        dados = Dados_estudados()  # cria o objeto Dados_estudados para pegar a funsao dessa classe
        banco = Conecta_Com_Banco()  # cria o objeto Conecta_Com_Banco para pegar a funsao dessa classe
        banco.conectando()  # conectando com o banco

        def coordenadas(coluna,s):
            item = ""
            p = 0
            # coloca os valores da coluna Valor_Bateria na String que vai para o Grafico
            for x in coluna:
                item = str(x)
                for a in ['\n', '(', ')', ',', ' ']:
                    item = item.replace(a, " ")

                valor = item + ";" + str(p)
                s.append(valor)
                p += 1
            return s

        def coordenadas2(s,xs,ys,px,py,titulo ):
            # Retirando o sinal de ; das Strings VB e pegando apenas os valores para por nas String de Coordenadas
            for line in s:
                if len(line) > 1:
                    x, y = line.split(';')
                    xs.append(float(y))
                    ys.append(float(x))

            # No grafico da posição 00 vai ter Essas configurações
            axs[px, py].set_title(titulo)     # Titulo do grafico
            axs[px, py].plot(xs, ys, color='C0') # as coordenadas para por cada ponto
            axs[px, py].set_xlabel("Time")             # Titulo para coordenada X do grafico
            axs[px, py].set_ylabel("Amplitude")        # Titulo para coordenada Y do grafico


        def animacoes(colunaVB, colunaEB , colunaT, colunaF):
            #STRINGS que ira receber os valores dos elemento das colunas para por no grafico
            VB = [] # String que recebe o valor do Valor_Bateria
            EB = [] # String que recebe o valor do Estado_Bateria
            T = []  # String que recebe o valor a  Temperatura
            F = []  # String que recebe o valor a  Frequencia


            #coloca os valores da coluna Temperatura na String que vai para o Grafico
            VB = coordenadas(colunaVB,VB)
            EB = coordenadas(colunaEB,EB)
            T = coordenadas(colunaT,T)
            F = coordenadas(colunaF,F)


            #Strings responsaveis pela coordenadas do grafico para Valor_Bateria
            xs_VB = []
            ys_VB = []

            #Strings responsaveis pela coordenadas do grafico para Estado_Bateria
            xs_EB = []
            ys_EB = []

            #Strings responsaveis pela coordenadas do grafico para Temperatura
            xs_T = []
            ys_T = []

            #Strings responsaveis pela coordenadas do grafico para Frequencia
            xs_F = []
            ys_F = []

            coordenadas2(VB,xs_VB,ys_VB,0,0,"Valor_Bateria")
            coordenadas2(EB,xs_EB,ys_EB,0,1,"Estado_Bateria")
            coordenadas2(T,xs_T,ys_T,1,0,"Temperatura")
            coordenadas2(F,xs_F,ys_F,1,1,"Frequencia")


        def animate(coluna):
            valores = dados.atualizaDados()  # pega os valores dos sensores e atualiza no JSON
            horario = datetime.now().time()  # pega Horario do computador
            data = datetime.now().date()  # pega DATA do computador
            banco.insertTabela(valores["Valor_Bateria"], valores["Estado_Bateria"], valores["Temperatura"],
                               valores["Frequencia"], horario, data)

            colunaVB = banco.selecionarCOLUNA("Valor_Bateria")
            colunaEB = banco.selecionarCOLUNA("Estado_Bateria")
            colunaT = banco.selecionarCOLUNA("Temperatura")
            colunaF = banco.selecionarCOLUNA("Frequencia")

            animacoes(colunaVB, colunaEB , colunaT, colunaF)

        def printGRAFICO():

            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()
        def escreverGRAFICO(self, coluna):
            t = banco.selecionarCOLUNA(coluna)

            novo = []
            item = ""
            for x in t:
                item = str(x)
                for a in ['\n', '(', ')', ',', ' ']:
                    item = item.replace(a, " ")
                novo.append(item)

            print(novo)
            #-------------------------------------

        # lista dos componetes da caixa de seleção 1
        lista1 = {  # criando um JSON
            "Insere para o banco": "0.0",
            "Select da tabela do banco": "False",
            "Deleta uma linha da tabela do banco": "0.0"

        }
        # lista dos componetes da caixa de seleção Consulta
        lista2 = {  # criando um JSON
            "Maior e menor valor da coluna": "0.0",
            "Contagem dos valores que são Maior,menor,igual ou diferente a um numero de referencia": "False",
            "ENTRE VALORES": "0.0",
            "ENTRE datas": "False",
            "Maior entre Valores da bateria": "0.0"

        }

        # lista dos componetes da caixa de seleção da Operacoes

        lista4 = {
            "=": "0.0",
            "!=": "False",
            ">": "0.0",
            "<": "0.0",
            "<=": "False",
            ">=": "0.0"

        }

        label = tk.Label(text="Inserido valores:", fg="Blue", anchor="e")
        labelDELETE = tk.Label(text="ID", anchor="e")
        bloco2 = tk.Label(text="Escolha a alternativa do Banco MySQL:", fg='white', bg='BLUE', width=200,
                          height=1)

        labelMaior = tk.Label(text="Inserido valores:", fg="Blue", anchor="e")
        labelMenor = tk.Label(text="Inserido valores:", fg="Blue", anchor="e")
        labelContagem = tk.Label(text="Operacao:", anchor="e")
        labelResultadoContagem = tk.Label(text="Inserido valores:", fg="Blue", anchor="e")
        labelValor = tk.Label(text="Valor:", anchor="e")
        labelResultadoBATERIA = tk.Label(text="Inserido valores:", fg="Blue", anchor="e")

        labelValorI = tk.Label(text="Valor Inicial:", anchor="e")
        labelValorF = tk.Label(text="Valor Final:" , anchor="e")

        labelDataI = tk.Label(text="Data Inicial:",anchor="e")
        labelDataF = tk.Label(text="Data Final:", anchor="e")



        label2 = tk.Label(text="Inserido valores:", fg="Blue")
        labelConsultar = tk.Label(text="Digita o ID:")

        tv = ttk.Treeview(JANELA, columns=(
            'id', 'Valor_Bateria', 'Estado_Bateria', 'Temperatura', 'Frequencia', 'hora', 'data'), show='headings',
                          height=5)
        tv2 = ttk.Treeview(JANELA, columns=(
            'id', 'Valor_Bateria', 'Estado_Bateria', 'Temperatura', 'Frequencia', 'hora', 'data'), show='headings')

        tv3 = ttk.Treeview(JANELA, columns=(
            'id', 'Valor_Bateria', 'Estado_Bateria', 'Temperatura', 'Frequencia', 'hora', 'data'), show='headings')
        caixaTEXTO = tk.Entry()

        bloco1 = tk.Label(text="Escolha a alternativa do Banco MySQL:", fg='white', bg='#7E40C8', width=200,height=1)
        bloco1.grid(row=0, column=0, columnspan=100, sticky="NSEW")

        botaoDELETAR = tk.Button(text="Deletar", command=lambda: deleteITEM(caixaTEXTO.get()))

        botao2 = tk.Button(text="Deletar", command=lambda: deleteITEM(caixaTEXTO.get()))
        botao3 = tk.Button(text="Contar", command=lambda: contar(caixaSelecao4.get(), int(caixaTEXTO2.get())))


        botao4 = tk.Button(text="EntreV",command=lambda:
                                interValores(0,tv2, caixaSelecao3.get(),
                                                 int(caixaTEXTOValorInicial.get()),
                                                 int(caixaTEXTOValorFinal.get())
                                                 ))

        botao5 = tk.Button(text="EntreD", command=lambda: interValores(1,tv3,caixaSelecao3.get(),
            int(caixaTEXTOValorInicial.get()),
            int(caixaTEXTOValorFinal.get())
        ))


        botaoConte = tk.Button(text="Contar", command=lambda: deleteITEM(caixaTEXTO.get()))

        json4 = list(lista4.keys())
        caixaSelecao4 = ttk.Combobox(JANELA, values=json4)
        caixaTEXTO2 = tk.Entry()
        caixaTEXTOValorInicial = tk.Entry()
        caixaTEXTOValorFinal = tk.Entry()

        def interValores(valor_data,tvv,coluna,inicio,final):
            print(inicio)
            print(final)

            if valor_data == 0:
                tabela= banco.entreValores(coluna,str(inicio),str(final))
            else:
                tabela= banco.entreDatas(str(inicio),str(final))

            #tamanho dos tituos da tabela
            tvv.column('id', minwidth=10, width=50)
            tvv.column('Valor_Bateria', minwidth=0, width=150)
            tvv.column('Estado_Bateria', minwidth=0, width=150)
            tvv.column('Temperatura', minwidth=0, width=150)
            tvv.column('Frequencia', minwidth=0, width=150)
            tvv.column('hora', minwidth=0, width=150)
            tvv.column('data', minwidth=0, width=150)

            #Dando titulo de cada Coluna da tabela
            tvv.heading('id', text='ID')
            tvv.heading('Valor_Bateria', text='Valor_Bateria')
            tvv.heading('Estado_Bateria', text='Estado_Bateria')
            tvv.heading('Temperatura', text='Temperatura')
            tvv.heading('Frequencia', text='Frequencia')
            tvv.heading('hora', text='hora')
            tvv.heading('data', text='data')

            # coordenada do local da tabela na interface Grafica
            tvv.grid(row=6, column=0, columnspan=80, sticky="NSEW",padx=10, pady=10, ipadx=10)

           # limpa a tabela inteira
            for i in tvv.get_children():
                tvv.delete(i)

            #preenche a tabela
            for (i, v, e, t, f, h, d) in tabela:  # percorre toda valores na tabela e printa na tela
                tvv.insert('', "end", values=(i, v, e, t, f, h, d))

        def contar(op,valor):
            if op == "=":
                tipo = 0
            elif op == "!=":
                tipo = 1
            elif op == ">":
                tipo = 2
            elif op == "<":
                tipo = 3
            elif op == ">=":
                tipo = 4
            elif op == "<=":
                tipo = 5


            contou = banco.contagem(caixaSelecao3.get(),tipo,valor)
            if tipo == 0:
                labelResultadoContagem["text"] = f'Na {caixaSelecao3.get()} Total de valores IGUAIS é: {str(contou)}'
                labelResultadoContagem.grid(row=14, column=5)
            elif tipo == 1:#pega os valores Diferentes ao valore de referencia da coluna escolida
                labelResultadoContagem["text"] = f'Na {caixaSelecao3.get()} Total de valores DIFERENTES é: {str(contou)}'
                labelResultadoContagem.grid(row=14, column=5)
            elif tipo == 2: #pega os valores MAIOR ao valore de referencia da coluna escolida
                labelResultadoContagem["text"] = f'Na {caixaSelecao3.get()} Total de valores MAIOR é: {str(contou)}'
                labelResultadoContagem.grid(row=14, column=5)
            elif tipo == 3: #pega os valores MENOR ao valore de referencia da coluna escolida
                labelResultadoContagem["text"] = f'Na {caixaSelecao3.get()} Total de valores MENOR é: {str(contou)}'
                labelResultadoContagem.grid(row=14, column=5)
            elif tipo == 4: #pega os valores MAIOR E MENOR ao valore de referencia da coluna escolida
                labelResultadoContagem["text"] = f'Na {caixaSelecao3.get()} Total de valores MAIOR E IGUAL é: {str(contou)}'
                labelResultadoContagem.grid(row=14, column=5)
            elif tipo == 5: #pega os valores MENOR E IGUAL ao valore de referencia da coluna escolida
                labelResultadoContagem["text"] = f'Na {caixaSelecao3.get()} Total de valores MENOR E IGUAL é: {str(contou)}'
                labelResultadoContagem.grid(row=14, column=5)

        def deleteITEM(deletar):
            # deleta do banco
            d = banco.deletaTABELA(deletar)
            # posiciona local da lebal para enviar aviso na tela
            label2.grid(row=4, column=4)
            label2["text"] = f'ID = {deletar} foi Excluido da tabela Dados'

        def selecaoCaixa1():

            if (caixaSelecao1.get() == "Insere para o banco"):
                # Lista dos elemento que ira sumir da tela
                tv3.grid_forget()
                tv2.grid_forget()
                labelContagem.grid_forget()
                caixaSelecao4.grid_forget()
                labelValor.grid_forget()
                caixaTEXTO2.grid_forget()
                botao3.grid_forget()
                caixaTEXTOValorInicial.grid_forget()
                caixaTEXTOValorFinal.grid_forget()
                botao4.grid_forget()
                botao5.grid_forget()
                labelResultadoBATERIA.grid_forget()
                labelDataI.grid_forget()
                labelDataF.grid_forget()
                labelValorI.grid_forget()
                labelValorF.grid_forget()
                labelDELETE.grid_forget()
                label2.grid_forget()

                tv.grid_forget()
                label2.grid_forget()
                caixaTEXTO.grid_forget()
                botaoDELETAR.grid_forget()
                labelDELETE.grid_forget()

                # Lista dos elemento que ira APARECE da tela

                valores = dados.atualizaDados()  # pega os valores dos sensores e atualiza no JSON
                horario = datetime.now().time()  # pega Horario do computador
                data = datetime.now().date()  # pega DATA do computador
                bloco2.grid(row=6, column=0, columnspan=100, sticky="NSEW",padx=10, pady=10, ipadx=10)
                bloco2["text"] = f'inserido:{valores}'
                banco.insertTabela(valores["Valor_Bateria"], valores["Estado_Bateria"], valores["Temperatura"],valores["Frequencia"], horario, data)
                valores = dados.atualizaDados()  # pega os valores dos sensores e atualiza no JSON

            elif (caixaSelecao1.get() == "Select da tabela do banco"):
                # Lista dos elemento que ira sumir da tela

                label.grid_forget()
                tv3.grid_forget()
                tv2.grid_forget()
                labelContagem.grid_forget()
                caixaSelecao4.grid_forget()
                labelValor.grid_forget()
                caixaTEXTO2.grid_forget()
                botao3.grid_forget()
                caixaTEXTOValorInicial.grid_forget()
                caixaTEXTOValorFinal.grid_forget()
                botao4.grid_forget()
                botao5.grid_forget()
                labelResultadoBATERIA.grid_forget()
                labelDataI.grid_forget()
                labelDataF.grid_forget()
                labelValorI.grid_forget()
                labelValorF.grid_forget()
                labelDELETE.grid_forget()
                label2.grid_forget()

                botaoDELETAR.grid_forget()
                labelDELETE.grid_forget()
                caixaTEXTO.grid_forget()
                tabela= banco.selectTABELA()

                # Lista dos elemento que ira APARECER da tela

                tv.column('id',minwidth=10,width=50)
                tv.column('Valor_Bateria',minwidth=0,width=150)
                tv.column('Estado_Bateria',minwidth=0,width=150)
                tv.column('Temperatura',minwidth=0,width=150)
                tv.column('Frequencia',minwidth=0,width=150)
                tv.column('hora',minwidth=0,width=150)
                tv.column('data',minwidth=0,width=150)

                tv.heading('id' , text='ID')
                tv.heading('Valor_Bateria' , text='Valor_Bateria')
                tv.heading('Estado_Bateria' , text='Estado_Bateria')
                tv.heading('Temperatura' , text='Temperatura')
                tv.heading('Frequencia' , text='Frequencia')
                tv.heading('hora' , text='hora')
                tv.heading('data' , text='data')

                tv.grid(row=6, column=0, columnspan=80, sticky="NSEW",padx=10, pady=10, ipadx=10)

                for i in tv.get_children():
                    tv.delete(i)

                for (i,v,e,t,f,h,d) in tabela:  # percorre toda valores na tabela e printa na tela
                    tv.insert('',"end",values=(i,v,e,t,f,h,d))
            else:
                # Lista dos elemento que ira sumir da tela
                tv3.grid_forget()
                tv2.grid_forget()
                labelContagem.grid_forget()
                caixaSelecao4.grid_forget()
                labelValor.grid_forget()
                caixaTEXTO2.grid_forget()
                botao3.grid_forget()
                caixaTEXTOValorInicial.grid_forget()
                caixaTEXTOValorFinal.grid_forget()
                botao4.grid_forget()
                botao5.grid_forget()
                labelResultadoBATERIA.grid_forget()
                labelDataI.grid_forget()
                labelDataF.grid_forget()
                labelValorI.grid_forget()
                labelValorF.grid_forget()
                label2.grid_forget()

                tv.grid_forget()
                label.grid_forget()

                # Lista dos elemento que ira APARECER da tela

                labelDELETE.grid(row=3, column=0)
                caixaTEXTO.grid(row=3, column=1)
                botaoDELETAR.grid(row=4, column=1, padx=10, pady=10, ipadx=20)

                tabela= banco.selectTABELA()
                tv.column('id',minwidth=10,width=50)
                tv.column('Valor_Bateria',minwidth=0,width=150)
                tv.column('Estado_Bateria',minwidth=0,width=150)
                tv.column('Temperatura',minwidth=0,width=150)
                tv.column('Frequencia',minwidth=0,width=150)
                tv.column('hora',minwidth=0,width=150)
                tv.column('data',minwidth=0,width=150)

                tv.heading('id' , text='ID')
                tv.heading('Valor_Bateria' , text='Valor_Bateria')
                tv.heading('Estado_Bateria' , text='Estado_Bateria')
                tv.heading('Temperatura' , text='Temperatura')
                tv.heading('Frequencia' , text='Frequencia')
                tv.heading('hora' , text='hora')
                tv.heading('data' , text='data')
                tv.grid(row=6, column=0, columnspan=200, sticky="NSEW",padx=10, pady=10, ipadx=10)

                for i in tv.get_children():
                    tv.delete(i)
                for (i,v,e,t,f,h,d) in tabela:  # percorre toda valores na tabela e printa na tela
                    tv.insert('',"end",values=(i,v,e,t,f,h,d))

        def selecaoCaixa2():

            if (caixaSelecao2.get() == "Maior e menor valor da coluna"):
                # Lista dos elemento que ira sumir da tela
                bloco2.grid_forget()
                tv.grid_forget()
                labelDELETE.grid_forget()
                caixaTEXTO.grid_forget()
                botaoDELETAR.grid_forget()
                labelDELETE.grid_forget()
                label2.grid_forget()

                tv3.grid_forget()
                tv2.grid_forget()
                labelContagem.grid_forget()
                caixaSelecao4.grid_forget()
                labelValor.grid_forget()
                caixaTEXTO2.grid_forget()
                botao3.grid_forget()
                caixaTEXTOValorInicial.grid_forget()
                caixaTEXTOValorFinal.grid_forget()
                botao4.grid_forget()
                botao5.grid_forget()
                labelResultadoBATERIA.grid_forget()
                labelDataI.grid_forget()
                labelDataF.grid_forget()
                labelValorI.grid_forget()
                labelValorF.grid_forget()

                # Lista dos elemento que ira APARECER da tela

                tabelaM,tabelam = banco.Maior_E_Menor(caixaSelecao3.get())
                labelMaior.grid(row=9, column=0, columnspan=10, sticky="NSEW",padx=10, pady=10, ipadx=10)
                labelMenor.grid(row=10, column=0, columnspan=10, sticky="NSEW",padx=10, pady=10, ipadx=10)

                for minhaTABELA in tabelaM:
                    labelMaior["text"] = f'{caixaSelecao3.get()} MAX {minhaTABELA}'

                for minhaTABELA in tabelam:
                    labelMenor["text"] = f'{caixaSelecao3.get()} MIN {minhaTABELA}'


            elif (caixaSelecao2.get() == "Contagem dos valores que são Maior,menor,igual ou diferente a um numero de referencia"):
                # Lista dos elemento que ira sumir da tela
                bloco2.grid_forget()
                tv.grid_forget()
                labelDELETE.grid_forget()
                caixaTEXTO.grid_forget()
                botaoDELETAR.grid_forget()
                labelDELETE.grid_forget()
                label2.grid_forget()

                tv3.grid_forget()
                tv2.grid_forget()
                labelMaior.grid_forget()
                labelMenor.grid_forget()
                labelResultadoContagem.grid_forget()
                caixaTEXTOValorInicial.grid_forget()
                caixaTEXTOValorFinal.grid_forget()
                botao4.grid_forget()
                botao5.grid_forget()
                labelResultadoBATERIA.grid_forget()
                labelDataI.grid_forget()
                labelDataF.grid_forget()
                labelValorI.grid_forget()
                labelValorF.grid_forget()


                # Lista dos elemento que ira APARECER da tela
                Sep = ttk.Separator(JANELA, orient=VERTICAL)
                Sep.grid(row=1, column=7,rowspan=5, pady=10, padx=10, sticky=(S, N))

                labelContagem.grid(row=1, column=8)
                caixaSelecao4.grid(row=1, column=9)

                labelValor.grid(row=2, column=8)
                caixaTEXTO2.grid(row=2, column=9)
                botao3.grid(row=3, column=9)


            elif (caixaSelecao2.get() == "ENTRE VALORES"):
                # Lista dos elemento que ira sumir da tela
                bloco2.grid_forget()
                tv.grid_forget()
                labelDELETE.grid_forget()
                caixaTEXTO.grid_forget()
                botaoDELETAR.grid_forget()
                labelDELETE.grid_forget()

                labelMaior.grid_forget()
                labelMenor.grid_forget()
                labelContagem.grid_forget()
                caixaSelecao4.grid_forget()
                labelValor.grid_forget()
                caixaTEXTO2.grid_forget()
                botao3.grid_forget()
                botao5.grid_forget()
                labelResultadoBATERIA.grid_forget()
                labelResultadoContagem.grid_forget()
                tv3.grid_forget()
                labelDataI.grid_forget()
                labelDataF.grid_forget()


                # Lista dos elemento que ira APARECER da tela
                Sep = ttk.Separator(JANELA, orient=VERTICAL)
                Sep.grid(row=1, column=7,rowspan=5, pady=10, padx=10, sticky=(S, N))

                labelValorI.grid(row=1, column=8)
                caixaTEXTOValorInicial.grid(row=1, column=9)
                labelValorF.grid(row=2, column=8)
                caixaTEXTOValorFinal.grid(row=2, column=9)
                botao4.grid(row=3, column=9)


            elif (caixaSelecao2.get() == "ENTRE datas"):
                # Lista dos elemento que ira sumir da tela

                bloco2.grid_forget()
                tv.grid_forget()
                labelDELETE.grid_forget()
                caixaTEXTO.grid_forget()
                botaoDELETAR.grid_forget()
                labelDELETE.grid_forget()
                label2.grid_forget()

                labelMaior.grid_forget()
                labelMenor.grid_forget()
                labelContagem.grid_forget()
                caixaSelecao4.grid_forget()
                labelValor.grid_forget()
                caixaTEXTO2.grid_forget()
                botao3.grid_forget()
                botao4.grid_forget()
                labelResultadoBATERIA.grid_forget()
                labelResultadoContagem.grid_forget()
                tv2.grid_forget()
                labelValorI.grid_forget()
                labelValorF.grid_forget()

                # Lista dos elemento que ira APARECER da tela
                labelDataI.grid(row=1, column=8)
                caixaTEXTOValorInicial.grid(row=1, column=9)
                labelDataF.grid(row=2, column=8)
                caixaTEXTOValorFinal.grid(row=2, column=9)
                botao5.grid(row=3, column=9)


            elif (caixaSelecao2.get() == "Maior entre Valores da bateria"):
                # Lista dos elemento que ira sumir da tela
                bloco2.grid_forget()
                tv.grid_forget()
                labelDELETE.grid_forget()
                caixaTEXTO.grid_forget()
                botaoDELETAR.grid_forget()
                labelDELETE.grid_forget()
                label2.grid_forget()

                tv3.grid_forget()
                tv2.grid_forget()
                labelDataI.grid_forget()
                labelDataF.grid_forget()
                labelMaior.grid_forget()
                labelMenor.grid_forget()
                labelContagem.grid_forget()
                caixaSelecao4.grid_forget()
                labelValor.grid_forget()
                caixaTEXTO2.grid_forget()
                botao3.grid_forget()
                caixaTEXTOValorInicial.grid_forget()
                caixaTEXTOValorFinal.grid_forget()
                botao4.grid_forget()
                botao5.grid_forget()
                labelResultadoContagem.grid_forget()
                labelDELETE.grid_forget()

                # Lista dos elemento que ira APARECER da tela

                i,f,m= banco.maiorEntreValores("0", "11")
                i1,f1,m1=banco.maiorEntreValores("11", "21")
                i2,f2,m2=banco.maiorEntreValores("21", "31")
                i3,f3,m3=banco.maiorEntreValores("31", "41")
                i4,f4,m4=banco.maiorEntreValores("41", "51")
                i5,f5,m5=banco.maiorEntreValores("51", "61")
                i6,f6,m6=banco.maiorEntreValores("61", "71")
                i7,f7,m7=banco.maiorEntreValores("71", "81")
                i8,f8,m8=banco.maiorEntreValores("81", "91")
                i9,f9,m9=banco.maiorEntreValores("91", "101")
                labelResultadoBATERIA.grid(row=6, column=0, columnspan=10, sticky="NSEW",padx=10, pady=10, ipadx=10)

                labelResultadoBATERIA["text"] = "Maior entre "+i+" e "+f+" da Frequencia é: "+str(m)+"\n" \
                                                "Maior entre "+i1+" e "+f1+" da Frequencia é: "+str(m1)+"\n" \
                                                "Maior entre "+i2+" e "+f2+" da Frequencia é: "+str(m2)+"\n" \
                                                "Maior entre "+i3+" e "+f3+" da Frequencia é: "+str(m3)+"\n" \
                                                "Maior entre "+i4+" e "+f4+" da Frequencia é: "+str(m4)+"\n" \
                                                "Maior entre "+i5+" e "+f5+" da Frequencia é: "+str(m5)+"\n" \
                                                "Maior entre "+i6+" e "+f6+" da Frequencia é: "+str(m6)+"\n" \
                                                "Maior entre "+i7+" e "+f7+" da Frequencia é: "+str(m7)+"\n" \
                                                "Maior entre "+i8+" e "+f8+" da Frequencia é: "+str(m8)+"\n" \
                                                "Maior entre "+i9+" e "+f9+" da Frequencia é: "+str(m9)+"\n"

        labelSelecionar = tk.Label(text="seleciona")
        labelSelecionar.grid(row=1, column=0, padx=10, pady=10, ipadx=10)
        json = list(lista1.keys())
        caixaSelecao1 = ttk.Combobox(JANELA, values=json)
        caixaSelecao1.grid(row=1, column=1, padx=10, pady=10, ipadx=10)

        botaoSelecionar = tk.Button(text="Selecinar", command=selecaoCaixa1)
        botaoSelecionar.grid(row=2, column=1, padx=10, pady=10, ipadx=10)

        botaoGRAFICO = tk.Button(text="GRAFICO", command=printGRAFICO)
        botaoGRAFICO.grid(row=2, column=0, padx=10, pady=10, ipadx=10)

        ################################################################################################
        Separador = ttk.Separator(JANELA, orient=VERTICAL)
        Separador.grid(row=1, column=3, rowspan=5, pady=10, padx=10, sticky=(S, N))
        ################################################################################################
        labelConsultar= tk.Label(text="Consultar",anchor="e")
        labelConsultar.grid(row=1, column=4)
        json = list(lista2.keys())
        caixaSelecao2 = ttk.Combobox(JANELA, values=json)
        caixaSelecao2.grid(row=1, column=5)

        mensagem3 = tk.Label(text="Coluna", anchor="e")
        mensagem3.grid(row=2, column=4)
        caixaSelecao3.grid(row=2, column=5)

        botaoConsulta = tk.Button(text="Consultar", command=selecaoCaixa2)
        botaoConsulta.grid(row=3, column=5, padx=10, pady=10, ipadx=20)
        ################################################################################################

        JANELA.mainloop()

if __name__ == '__main__':
    main()


