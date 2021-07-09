import smtplib
server = server.SMTP('smpt.Your Sever of Mail(Like for example gmail, Mail, Yahoo, etc.',Server port)
server.starttls()
server.login('Your Gmail ID', 'Password')
server.sendmail('Your Gmail ID'
                'Recievers Gmail ID'
                'Your Message To the Reciver')