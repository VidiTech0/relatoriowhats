import pywhatkit as kit
from datetime import datetime, timedelta
import time

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    return texto

def calcular_tempo_ate_envio(hora, minuto):
    agora = datetime.now()
    horario_envio = agora.replace(hour=hora, minute=minuto, second=0, microsecond=0)

    # Se o horário de envio for antes do horário atual, agenda para o próximo dia
    if horario_envio < agora:
        horario_envio += timedelta(days=1)

    return (horario_envio - agora).total_seconds()

def agendar_envio(numero, mensagem, hora, minuto):
    while True:
        # Calcula o tempo até o envio
        segundos_ate_envio = calcular_tempo_ate_envio(hora, minuto)
        print(f"Mensagem agendada para {numero} às {hora}:{minuto}. Aguardando...")

        # Aguarda até o horário de envio
        time.sleep(segundos_ate_envio)

        # Envia a mensagem instantaneamente sem precisar apertar Enter
        try:
            kit.sendwhatmsg_instantly(numero, mensagem)
            print(f"Mensagem enviada para {numero}")
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

        # Aguarda 24 horas para o próximo envio
        time.sleep(24 * 60 * 60)

if __name__ == "__main__":
    # Configurações
    nome_arquivo = 'mensagem_para_joao.txt'  # Nome do arquivo a ser lido
    numero_whatsapp = '+5588997917773'  # Número do WhatsApp com código do país, por exemplo: +5511999999999
    hora_envio = 11  # Hora de envio (24 horas)
    minuto_envio = 5  # Minuto de envio

    # Ler o arquivo
    mensagem = ler_arquivo(nome_arquivo)

    # Agendar o envio
    agendar_envio(numero_whatsapp, mensagem, hora_envio, minuto_envio)
