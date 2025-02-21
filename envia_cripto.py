import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import mimetypes

# Configuração do servidor SMTP do Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL = "marco.edit01@gmail.com"
SENHA_DE_APP = "nsts mlhf ldjy stcy"

# Conectar ao servidor SMTP
servidor_email = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
servidor_email.starttls()
servidor_email.login(EMAIL, SENHA_DE_APP)

# Configuração do e-mail
remetente = EMAIL
destinatarios = ["marcolopee70@gmail.com"]
assunto = "Relatório de Cripto Moedas"
conteudo = "Segue em anexo o relatório de valorização de criptomoedas."

mensagem = MIMEMultipart()
mensagem["From"] = remetente
mensagem["To"] = ", ".join(destinatarios)
mensagem["Subject"] = assunto

mensagem.attach(MIMEText(conteudo, "plain"))

# Anexar arquivo
documento = "relatorio_criptomoedas.csv"

with open(documento, "rb") as anexo:
    tipo_mimetype, _ = mimetypes.guess_type(documento)
    parte_anexo = MIMEApplication(anexo.read(), Name=documento)
    parte_anexo["Content-Disposition"] = f'attachment; filename="{documento}"'
    parte_anexo["Content-Type"] = tipo_mimetype or "application/octet-stream"
    mensagem.attach(parte_anexo)

# Enviar e-mail
servidor_email.sendmail(remetente, destinatarios, mensagem.as_string())

# Fechar conexão
servidor_email.quit()

print("E-mail enviado com sucesso!")
