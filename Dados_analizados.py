import psutil
import json

class Dados_estudados:
    # cria o arquivo JSON com as suas colunashttps://meet.google.com/kfe-ozsw-ygt
    def criarArquivoJSON(self):
        self.data = {  # criando um JSON
            "Valor_Bateria": 0.0,
            "Estado_Bateria": False,
            "Temperatura": 0.0,
            "Frequencia": 0.0,

        }
        with open ("DADOS.json",'w') as arquivo_json:  # abre o arquivo em modo de w (escrevre por cima)
            json.dump(self.data,arquivo_json)          #converte uma string em json
        arquivo_json.close()

    def atualizaDados(self):
            with open ("DADOS.json",'r') as arquivo_json:    # abre arquivo em r (modo de leitura)
                self.data = json.load(arquivo_json)

                #atualizar Dados da bateria
                self.valor_bateria = psutil.sensors_battery().percent  # pega o valor da bateria
                self.estado_bateria = psutil.sensors_battery().power_plugged  # pega o valor do estado da bateria

                self.data['Valor_Bateria'] = self.valor_bateria     # passa para o json o valor da bateria
                self.data['Estado_Bateria'] = self.estado_bateria   # passa para o json o valor do estadod da bateria

                #atualiza a temperatura
                self.temperatura = psutil.sensors_temperatures() # passa todas as informacoes da temperatura
                for nome, Todos_itens in self.temperatura.items():
                        for item in Todos_itens:
                            #print("%-20s %s °C" %(item.label or nome, item.current))
                            self.data['Temperatura'] = item.current   # pega o valor da temperatura e passa JSON

                #atualiza a frequencia
                self.frequencia = psutil.cpu_freq().current  # pega o valor da frequencia e passa para JSON
                self.data['Frequencia'] = self.frequencia
            arquivo_json.close()

            with open("DADOS.json", 'w') as arquivo_json:  # abre o arquivo em modo de w (escrevre por cima)
                json.dump(self.data, arquivo_json)  # converte uma string em json
                return self.data
            arquivo_json.close()

    def lerDados(self):
        with open ("DADOS.json",'r') as arquivo_json:    # abre arquivo em r (modo de leitura)
            self.data = json.load(arquivo_json)
            for self.item, self.valor in self.data.items():  # printa coluna e valores do JSON
                print(self.item, self.valor)
        arquivo_json.close()

