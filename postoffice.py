import smtplib
from email.message import EmailMessage

password = 'bcdonnfrcftufncu'
sender_email = 'dd05tsvetkov@yandex.ru'
recipient_email = ['ddtsvetkov2005@gmail.com', 'dd05tsvetkov@yandex.ru']
subject = 'Проверка связи'
body = 'текст проверочного сообщения '

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email


server = None
try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(sender_email,password)
    server.send_message(msg)
    print('Письмо отправлено')
except Exception as e:
    print(f'Ошибка {e}')

finally:
    if server:
        server.quit()

