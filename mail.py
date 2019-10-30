import smtplib
from email.message import EmailMessage


def sendMail():

    sender = 'xxxxxxxxxxx@gmail.com'
    password = 'xxxxxxxxxxxxxxxxx'
    to = 'xxxxxxxxxxxxxx@gmail.com'

    msg = EmailMessage()
    msg['Subject'] = 'Mail Subject '
    msg['From'] = sender
    msg['To'] = to
    msg.set_content('mail content in plain text')
    msg.add_alternative("""\
        <html>
            <body>
                <h1>Hello World</h1>
            </body>
        </html>
        """,subtype = 'html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #login 
        smtp.login(sender,password)
        #send message
        smtp.send_message(msg)

sendMail()
