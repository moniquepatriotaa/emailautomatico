from email.message import EmailMessage
import ssl
import smtplib

meu_email = "" #seu email
senha_gerada = "sua_senha"  # Substitua pela sua senha de aplicativo
destinatarios = [" ", "outro_email@gmail.com", "mais_um_email@gmail.com"]
assunto = "Olá, testando Python"
body = """
Seu corpo de e-mail aqui.
"""

em = EmailMessage()

em['From'] = meu_email
em['To'] = ", ".join(destinatarios)  # Converte a lista de destinatários em uma única string separada por vírgulas
em['Subject'] = assunto
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meu_email, senha_gerada)
    smtp.sendmail(meu_email, destinatarios, 
                  em.as_string())


#Agora você pode mandar emails para muitas pessoas ao mesmo tempo 