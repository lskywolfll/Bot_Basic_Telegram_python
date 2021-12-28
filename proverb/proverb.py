import requests
from random import choice
from bs4 import BeautifulSoup

urls = [
    {
        "page": "https://psicologiaymente.com/reflexiones/frases-de-exito",
        "count": 56
    }
]

def format_proverb(proverb: str):
    number = proverb[4:6]
    number = number.replace(".", "")
    number = int(number)
    proverb = proverb[7:] if number >= 10 else proverb[6:]
    positionAuthor = proverb.index("(")
    author = proverb[positionAuthor + 1:proverb.index(")")].replace(".", "")
    proverb = proverb[:positionAuthor]
    proverb = proverb.replace(";", "").replace(",", "").replace(".", "").replace(":", "")
    format_txt = f"{proverb} escrito por {author}"
    return format_txt


def get_proverb():
    url = urls[0]
    request = requests.get(url["page"])
    soup = BeautifulSoup(request.content, "html.parser")
    proverb = str(choice(list(soup.findAll("h3"))))
    proverb = format_proverb(proverb)
    return proverb