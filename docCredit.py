from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now=datetime.datetime.now()

content = ''

def extract_articles(url):
    print('Extracting Doctor of Credits Articles...')
    cnt = ''
    cnt +=('<b>Doc of Credits articles as of now:</b><br><br>')
    response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(response).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    for i,tag in enumerate(soup.find_all('h2',attrs={'class':'entry-title'})):
        cnt += ((str(i+1))+ ' :: '+tag.text + "\n"+"<br>")

    print(cnt)
    return(cnt)

cnt = extract_articles('https://www.doctorofcredit.com/')
content += cnt
content += '<br>--------<br>'
content += '<br><br>End of Message'

SERVER = 'smtp-mail.outlook.com'
PORT = 587
FROM = 'kwon741@hotmail.com'
TO = 'krnjin94@gmail.com'
PASS = '********'

msg = MIMEMultipart()

msg['Subject'] = "Doctor of Credits New Posts [Automated Emails] " + str(now.month) + "/" + str(now.day) + " - " + str(now.now())
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

server = smtplib.SMTP(SERVER,PORT)

server.set_debuglevel(1)

server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

server.quit()
