from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from subprocess import Popen, PIPE
 
html = MIMEText("<html><head><title></title> \
</head><body></body>", "html")
msg = MIMEMultipart("alternative")
 
msg["From"] = "root@virtual"
msg["To"] = "assistenza@gartour.net"
msg["Subject"] = " $USER Disconnesso da Openvpn 10.3"
 
msg.attach(html)
 
p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
p.communicate(msg.as_string()) 