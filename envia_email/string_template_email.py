# Criar uma string sendo um template.
# Criar um template HTML e subistituir alguns placeholdes nele.
from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

# Biblioteca de envio de emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

caminho_base = 'D:\\Cursos\\Luiz_Otavio_Miranda\\Python\\Modulos\\' 
nome_arquivo = 'template.html'
img = 'imagem.jpg'

full_path = caminho_base + nome_arquivo
print(full_path)

with open(full_path, 'r', encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Elias Rodrigues', data=data_atual)
    # corpo_msg = template.safe_substitute(nome='Elias Rodrigues', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Elias Antonio Rodrigues'
msg['to'] = meu_email  # Cliente
msg['subject'] = 'Atenção este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')

msg.attach(corpo)

with open(caminho_base + img, 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso.')
