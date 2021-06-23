import pymysql

#conexao ao banco de dados do MYSQL
Conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='banco'
)
Cursor = Conexao.cursor()   # pega ferramentas do Mysql

class Conecta_Com_Banco():

    def conectando(self):
        try:
            Cursor.execute("select database();")            # Essa linha pega o nome do banco para checar que esta realmente conecatado com banco
            self.banco = Cursor.fetchone()                  # A Variavel Banco recebe o nome do banco
            print("Conecatado na DataBase:",self.banco)

        except ConnectionError :
            print("Conexão falhou")
        finally:
           print("Conectado MySQL")

    # a funsao instertTabela recebe os valores de cada coluna do Json e a hora e data do computador
    def insertTabela(self,valor_Bateria,estado_Bateria,temperatura,frequencia,horario,data):
            self.dado = (valor_Bateria,estado_Bateria,temperatura,frequencia,horario,data)
            insert = "INSERT INTO Dados (Valor_bateria, Estado_bateria, Temperatura, Frequencia, Horario, Data) " \
                     "VALUES (%s, %s, %s, %s, %s, %s)"

            Cursor.execute(insert,self.dado)  # executa o comando para inserir no banco
            Conexao.commit()                #Se um transação for concluída com sucesso (todas as operações bem-sucedidas), o banco de dados será alterado permanentemente, com os dados alterados persistidos (salvos em disco); essa operação é chamada de COMMIT.
            print("Inserido com SUCESSO")

    def selectTABELA(self):
            select = "SELECT * FROM Dados"
            Cursor.execute(select)                  # executa o comando select
            self.tabela = Cursor.fetchall()         # fetchall percorrer toda tabela passando tudo para variavel
            return self.tabela

    # na funsao deletaTABELA passamos o ID do elemento que queremos DELETAR
    def deletaTABELA(self,id):
        delete = "DELETE FROM `Dados` WHERE `Dados`.`id` = "
        self.deletar = delete + id
        print( str(self.deletar))

        Cursor.execute(self.deletar)                  # executa o comando DELETE
        Conexao.commit()
        print(id , " Deletado com SUCESSO")

    def selecionarCOLUNA(self,coluna):
        select = "SELECT "+coluna+" FROM Dados"
        Cursor.execute(select)  # executa o comando select
        self.tabela = Cursor.fetchall()  # fetchall percorrer toda tabela passando tudo para variavel
        return self.tabela

    # a funsao Maior_E_Menor precisa passar a coluna que iremos analizar o maior e menor dessa coluna
    def Maior_E_Menor(self,coluna):
        maior_Temperatura= "SELECT MAX("+coluna+") FROM Dados;"   # pega o maior valor da coluna
        menor_Temperatura= "SELECT MIN("+coluna+") FROM Dados;"   # pega o menor valor da coluna

        Cursor.execute(maior_Temperatura)                              # execura comando do Maior da coluna
        self.maiorTABELA = Cursor.fetchall()                           # fetchall percorrer toda tabela passando tudo para variavel

        Cursor.execute(menor_Temperatura)                              # execura comando do MENOR da coluna
        self.menorTABELA = Cursor.fetchall()                           # fetchall percorrer toda tabela passando tudo para variavel

        return self.maiorTABELA,self.menorTABELA
# a funsao contagem conta todos os elemento de uma coluna passando nomed da coluna, qual operacao aritimerica que iremos utilizar e passa o valor de referencia
    def contagem(self,coluna,tipo,valor): # (nome_da_coluna , operacao , valor_de_referencia)


        # aqui escolemos a operacao que queremos utilizar
        if tipo == 0:
            op = "="
        elif tipo == 1:
            op = "!="
        elif tipo == 2:
            op = ">"
        elif tipo == 3:
            op = "<"
        elif tipo == 4:
            op = "<="
        elif tipo == 5:
            op = ">="



        self.seleciona = "SELECT "+coluna+" FROM Dados where " + coluna + "  " + op + " " + str(valor)  +" ORDER BY "+coluna+";"
        Cursor.execute(self.seleciona)      # roda comando para selecionar coluna onde tem valores sendo comparacado com Valore de referencia
        self.seleciona = Cursor.fetchall()  # fetchall percorrer toda tabela passando tudo para variavel


        if tipo == 0:  #pega os valores iguais ao valore de referencia da coluna escolida
            self.conta = "SELECT COUNT(*) AS Temp FROM Dados WHERE "+coluna+" = "+ str(valor) +" ORDER BY "+coluna+";"
            Cursor.execute(self.conta)
            self.cotagem = Cursor.fetchone()  # fetchall percorrer toda tabela passando tudo para variavel
            return self.cotagem

        elif tipo == 1:#pega os valores Diferentes ao valore de referencia da coluna escolida
            self.conta = "SELECT COUNT(*) AS Temp FROM Dados WHERE " + coluna + " != " + str(valor) +" ORDER BY "+coluna+";"
            Cursor.execute(self.conta)
            self.cotagem = Cursor.fetchone()  # fetchall percorrer toda tabela passando tudo para variavel
            return self.cotagem

        elif tipo == 2: #pega os valores MAIOR ao valore de referencia da coluna escolida
            self.conta = "SELECT COUNT(*) AS Temp FROM Dados WHERE " + coluna + " > " + str(valor) +" ORDER BY "+coluna+";"
            Cursor.execute(self.conta)
            self.cotagem = Cursor.fetchone()  # fetchall percorrer toda tabela passando tudo para variavel
            return self.cotagem

        elif tipo == 3: #pega os valores MENOR ao valore de referencia da coluna escolida
            self.conta = "SELECT COUNT(*) AS Temp FROM Dados WHERE " + coluna + " < " + str(valor) +" ORDER BY "+coluna+";"
            Cursor.execute(self.conta)
            self.cotagem = Cursor.fetchone()  # fetchall percorrer toda tabela passando tudo para variavel
            return self.cotagem

        elif tipo == 4: #pega os valores MAIOR E MENOR ao valore de referencia da coluna escolida
            self.conta = "SELECT COUNT(*) AS Temp FROM Dados WHERE " + coluna + " >= " + str(valor) +" ORDER BY "+coluna+";"
            Cursor.execute(self.conta)
            self.cotagem = Cursor.fetchone()  # fetchall percorrer toda tabela passando tudo para variavel
            return self.cotagem

        elif tipo == 5: #pega os valores MENOR E IGUAL ao valore de referencia da coluna escolida
            self.conta = "SELECT COUNT(*) AS Temp FROM Dados WHERE " + coluna + " <= " + str(valor) +" ORDER BY "+coluna+";"
            Cursor.execute(self.conta)
            self.cotagem = Cursor.fetchone()  # fetchall percorrer toda tabela passando tudo para variavel
            return self.cotagem




# funsao entreValores encontra valores na tabela entre um intervalor de valores,
    def entreValores(self,coluna,inicio,final): # (nome_da_Coluna, Valor_inicial, Valor_Final)
        self.entrevaloress= "SELECT * FROM Dados WHERE "+coluna+" BETWEEN "+inicio+" AND "+final+" ORDER BY "+coluna+";   "

        Cursor.execute(self.entrevaloress)
        self.entrevaloress = Cursor.fetchall()  # fetchall percorrer toda tabela passando tudo para variavel

        return self.entrevaloress

# funsao entreDatas encontra datas na tabela entre um intervalor de datas,

    def entreDatas(self, inicio,final):  #(data_inicial , data_final)
            print(inicio)
            print(final)
            self.entredata = "SELECT * FROM Dados WHERE data BETWEEN date('"+inicio+"') AND date('"+final+"') ORDER BY data "
            Cursor.execute(self.entredata)
            self.entredata = Cursor.fetchall()  # fetchall percorrer toda tabela passando tudo para variavel

            return self.entredata


    # Encontra Maior da frequencia do valores quando bateria eta entre um determinado periodo
    def maiorEntreValores(self , inicio,final):
            self.media = "SELECT MAX(Frequencia) FROM Dados WHERE Valor_Bateria BETWEEN "+inicio+" AND "+final+" ;"
            Cursor.execute(self.media)
            self.media = Cursor.fetchone()  # fetchall percorrer toda tabela passando tudo para variavel
            return inicio,final,self.media
            print("Maior entre "+inicio+" e "+final+" da Frequencia é: " + str(self.media)  )
