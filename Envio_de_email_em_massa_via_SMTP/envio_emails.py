import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Carregar lista de e-mails
emails = pd.read_csv('emails.csv')

# Configurações do servidor SMTP
smtp_server = 'smtp.zoho.com'
smtp_port = 587
username = ''
password = ''

# Criar conexão com o servidor SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

# Preparar e enviar e-mails
for index, row in emails.iterrows():
    name = row['name']
    email = row['email']
    
    # Criar o objeto de e-mail
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = email
    msg['Subject'] = 'Assunto do E-mail'
    
    # Corpo do e-mail
    body = f'Olá {name},\n\nEsta é uma mensagem de teste.'
    msg.attach(MIMEText(body, 'html'))
    
    # Enviar o e-mail
    server.sendmail(username, email, msg.as_string())
    print(f'E-mail enviado para {name} ({email})')

# Fechar conexão com o servidor SMTP
server.quit()
