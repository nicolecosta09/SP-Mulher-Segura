#==========================================================
#                  SP MULHER SEGURA
# ==========================================================
#
#   Curso ......... Técnico em Informática
#   Ano/Turma ..... 2º A Informática
#   Disciplina .... Programação Orientada a Objetos
#   Data .......... 11/09/2026
#
#   Integrantes:
#     - Ana Cecylia
#     - Camile
#     - Esther
#     - Nicole
#     - Larissa Natsumi
#
# ==========================================================

from classes import Pessoa, Vitima, Protetor, ServicoDeEmergencia, Policia, Localizacao, Ocorrencia, Alerta
 
 
if __name__ == "__main__":
 
    print("========== SISTEMA DE EMERGÊNCIA ==========")
 
    # Criando a polícia (que é um ServicoDeEmergencia)
    policia = Policia(
        1,
        "Polícia Militar",
        "Posto Central",
        True
    )
 
    # Criando a vítima já associada a um ServicoDeEmergencia
    vitima = Vitima(
        "Maria",
        12345678900,
        999999999,
        "1234",
        100,
        1,
        servicoDeEmergencia=policia
    )
 
    # Criando o protetor
    protetor = Protetor(
        "João",
        98765432100,
        988888888,
        "5678",
        "Irmão",
        servicoDeEmergencia=policia
    )
 
    vitima.cadastrarProtetor(protetor)
 
    # Criando uma ocorrência 
    ocorrencia = Ocorrencia(
        1,
        "Ameaça",
        "28/08/2026 15:00",
        "Pendente"
    )
 
   
    ocorrencia.localizacao.latitude = -8.7612
    ocorrencia.localizacao.longitude = -63.9004
 
    # Vinculando a ocorrência à vítima e ao protetor
    vitima.registrarOcorrencia(ocorrencia)
    protetor.acompanharOcorrencia(ocorrencia)
 
    # Criando um alerta e vinculando à ocorrência
    alerta = Alerta(1, "Ameaça registrada próxima à sua região", "28/08/2026 15:01")
    ocorrencia.adicionarAlerta(alerta)
 
    print("\n--- PESSOA / VÍTIMA ---")
    print(vitima.exibirPerfil())
    print("Senha correta:", vitima.autenticar("1234"))
 
    print("\n--- VÍTIMA ---")
    vitima.solicitarAjuda()
    vitima.autorizarLocalizacao()
    vitima.consultarLocais()
    vitima.calcularRotas(ocorrencia.localizacao)
 
    print("\n--- PROTETOR ---")
    protetor.consultarLocais()
    protetor.ajudarVitima()
 
    print("\n--- LOCALIZAÇÃO (via composição da Ocorrencia) ---")
    ocorrencia.localizacao.compartilhar()
 
    print("\n--- SERVIÇO DE EMERGÊNCIA / POLÍCIA ---")
    policia.acionar(ocorrencia.localizacao, ocorrencia)
    policia.confirmarAtendimento(ocorrencia)
    policia.atenderOcorrencia(ocorrencia)
    policia.acompanharCaso(ocorrencia)
    policia.registrarBoletim()
 
    print("\n--- ALERTA ---")
    alerta.enviar()
    print("Alerta lido?", alerta.lido)
 
    print("\n--- OCORRÊNCIA ---")
    print("Status atual:", ocorrencia.status)
    ocorrencia.encerrar()
    print("Status final:", ocorrencia.status)
    print("Total de alertas vinculados:", len(ocorrencia.alertas))
 
    print("\n============================================")
 
