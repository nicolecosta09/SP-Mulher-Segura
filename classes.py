#PESSOA
class Pessoa:
    def __init__(self, nome, cpf, telefone, senha, servicoDeEmergencia=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.senha = senha
        self.servicoDeEmergencia = servicoDeEmergencia
 
#metodo
 
    def exibirPerfil(self):
      return f"Nome: {self.nome}\nCPF:{self.cpf}\nTelefone:{self.telefone}"  
 
    def autenticar(self,senha):
        return self.senha == senha
 
 
#classe vitima
class Vitima(Pessoa):
    def __init__(self, nome, cpf, telefone,senha, endereco, localizacaoAtual,servicoDeEmergencia=None):
        super().__init__(nome,cpf,telefone,senha,servicoDeEmergencia)
        self.endereco=endereco
        self.localizacaoAtual=localizacaoAtual
        self.ocorrencias= []
 
#metodos
    def solicitarAjuda(self):
        print(f"{self.nome} solicitou ajuda>")
 
    def autorizarLocalizacao(self):
        print("Localização autorizada.")
        return True
 
    def consultarLocais(self):
        print("Consultando locais seguros...")
 
    def cadastrarProtetor(self,protetor):   
     self.protetor = protetor 
     print(f"Protetor:{protetor.nome} cadastrado.")  
 
    def calcularRotas(self,localizacao):
        print("Calculando rota até a localização...")
        return localizacao
 
    def registrarOcorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)
        print(f"Ocorrência {ocorrencia.idOcorrencia} registrada pela vítima {self.nome}.")
 
#classe protetor
class Protetor(Pessoa):
    def __init__(self,nome, cpf,telefone,senha, parentesco,servicoDeEmergencia=None):
        super().__init__(nome,cpf,telefone,senha,servicoDeEmergencia)
        self.parentesco=parentesco
        self.ocorrencias=[]
 
#metodos
 
    def consultarLocais(self):
        print("Protetor consultando locais seguros...")
 
    def ajudarVitima(self):
        print(f"{self.nome} está ajudando a vítima.")
 
    def acompanharOcorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)
        print(f"Protetor {self.nome} está acompanhando a ocorrência {ocorrencia.idOcorrencia}.")
 
 
 
 
#CLASSE SERVIÇOS DE EMERGENCIA
class ServicoDeEmergencia:
    def __init__(self,idServico, tipoServico):
        self.idServico=idServico
        self.tipoServico=tipoServico
#mETODOS
    def acionar(self, local, ocorrencia):
        print(f"Serviço de emergência acionado no local:{local.obterCoordenadas()}")
        ocorrencia.abrir()
        return True
 
    def confirmarAtendimento(self, ocorrencia):
        print("Atendimento confirmado.")
        ocorrencia.atualizarStatus("Em atendimento")
        return True
 
 
 
#CLASSE POLICIA
class Policia(ServicoDeEmergencia):
    def __init__(self,idServico, tipoServico, posto,disponibilidade):
        super().__init__(idServico, tipoServico)
        self.posto=posto
        self.disponibilidade=disponibilidade
 
    def atenderOcorrencia(self,ocorrencia):
        if self.disponibilidade:
         print("Polícia atendendo a ocorrencia ")
         ocorrencia.atualizarStatus("Atendida pela Polícia")
        else:
            print("Polícia indisponível")
 
    def acompanharCaso(self,ocorrencia):
        print("POlícia acompanhando o caso.")
        ocorrencia.atualizarStatus("Caso sendo acompanhado")
 
    def registrarBoletim(self):
        print("Boletim de ocorrencia registrado.")
        return "Boletim registrado com sucesso"
 
 
 
#CLASSE OCORRENCIA
class Ocorrencia:
    def __init__(self, idOcorrencia, tipoViolencia, dataHora, status):
        self.idOcorrencia = idOcorrencia
        self.tipoViolencia = tipoViolencia
        self.dataHora = dataHora
        self.status = status
        self.localizacao = Localizacao(0, 0)
        self.alertas = []
 
    def abrir(self):
        self.status = "Aberta"
        print("Ocorrência aberta.")
 
    def atualizarStatus(self, novoStatus="Atualizada"):
        self.status = novoStatus
        print(f"Status atualizado para: {self.status}")
 
    def encerrar(self):
        self.status = "Encerrada"
        print("Ocorrência encerrada.")
 
    def adicionarAlerta(self, alerta):
        self.alertas.append(alerta)
        print(f"Alerta {alerta.idAlerta} vinculado à ocorrência {self.idOcorrencia}.")
 
 
 
#CLASSE LOCALIZAÇÃO
class Localizacao:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
 
    def compartilhar(self):
        print(f"Localização compartilhada: {self.obterCoordenadas()}")
        return self.obterCoordenadas()
 
    def obterCoordenadas(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"
 
 
    
# CLASSE ALERTA
class Alerta:
    def __init__(self, idAlerta, mensagem, dataHora, lido=False):
        self.idAlerta = idAlerta
        self.mensagem = mensagem
        self.dataHora = dataHora
        self.lido = lido
 
    def enviar(self):
        print(f"Alerta enviado: {self.mensagem}")
 