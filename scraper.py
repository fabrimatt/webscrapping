import requests
from bs4 import BeautifulSoup



#pagina que vamos trabalhar
url ='https://www.pichau.com.br/hardware/placa-de-video'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_='product details product-item-details')
ultima_pagina= soup.find('span', class_='text-page last').get_text().strip()




for i in range(1,int(ultima_pagina)):
        url_pag =f'https://www.pichau.com.br/hardware/placa-de-video?p={i}'
        site = requests.get(url_pag, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        placas = soup.find_all('div', class_='product details product-item-details')
        
        with open ('precos_placas.csv','a',newline='', encoding='utf-8') as f:
                for placa in placas:
                        
                        marca = placa.find('a', class_='product-item-link').get_text().strip()
                        try:
                                preco = placa.find('span', class_='price').get_text().strip()
                                num_preco = preco[2:]
                                num_preco = num_preco[:-3]
                                                                
                        except:
                                num_preco = '0'
                        
                        try:
                                preco_boleto = placa.find('span', class_='price-boleto').get_text().strip()
                                index= preco_boleto.find(',')
                                num_preco_boleto = preco_boleto[10:index]
                                                        
                        except:
                                num_preco_boleto = '0'
                        
                        linha = marca + ';' + num_preco + ';' + num_preco_boleto + '\n'
                        print(linha)
                        f.write(linha)
        print(url_pag)





