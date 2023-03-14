import requests
from bs4 import BeautifulSoup

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>Test</title>

</head>
<body>
    <h1>Ronaldo Information: {}</h1>
<body>
</html>

'''


response = requests.get("https://en.wikipedia.org/wiki/Cristiano_Ronaldo")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table" ,class_="infobox vcard") 
    ronaldo = tables[0]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(ronaldo))
else:
    print('Request Failed')



