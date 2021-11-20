from bs4 import BeautifulSoup
import requests
import smtplib
import email.message

URL = "https://www.brasiltronic.com.br/camera-sony-alpha-a6400-com-lente-16-50mm-f-35-56-lente-oss-p1324121"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('h1', class_ = 'name').get_text()
price = soup.find('strong', class_='sale-price').get_text().strip()

num_price = price[3:8]
num_price = num_price.replace('.','')
num_price = float(num_price)


def send_email():
    email_content = """
    https://www.brasiltronic.com.br/camera-sony-alpha-a6400-com-lente-16-50mm-f-35-56-lente-oss-p1324121
    """
    msg = email.message.Message()
    msg['Subject'] = 'Preço Camera Sony A6400 BAIXOU!!!!'

    msg['From'] = 'web.scrapper6@gmail.com'
    msg['To'] = 'web.scrapper6@gmail.com'
    password = 'beautifulsoup'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    print("Sucesso ao enviar email")



if (num_price < 8000):
    send_email()















