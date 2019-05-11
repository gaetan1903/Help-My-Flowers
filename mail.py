import smtplib
from email.mime.text import MIMEText

message = MIMEText('je suis un test')
message['Subject'] = 'hey object '

message['From'] = 'gaetan.jonathan.bakary@esti.mg'
message['To'] = 'gaetan.s118@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('gaetan.jonathan.bakary@esti.mg','*********')
server.send_message(message)
server.quit()
