import requests, bs4

url = "https://file.wikileaks.org/file/"
wiki = requests.get(url)
bswiki =  bs4.BeautifulSoup(wiki.text, 'html.parser')

atag = bswiki.find_all('a')
href_list = []
for href in atag:
    href_list.append(href.get('href'))
    
pdf_list = []
for link in href_list:
    if '.pdf' in link:
        pdf_list.append(link)

def download_file(pdf_name):
    response = requests.get("https://file.wikileaks.org/file/" + pdf_name)
    with open(pdf_name, 'wb') as file:
        file.write(response.content)
        
i = 0
for pdf in pdf_list:
    download_file(pdf)
    i += 1
    print(i)
