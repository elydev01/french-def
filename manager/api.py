import requests as req
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

from manager.const import connection_error_page

USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"

HEADERS = {"User-Agent": USERAGENT}

NOT_RESULT = "<h1 style='color:#ff0422;text-align:center'>Aucun résultat trouvé</h1>"


def get_definition(word):
    """
    :param word: The word whose definition you are looking for
    :return: A list containing all the definitions of word
    """
    try:
        URL = "https://www.larousse.fr/dictionnaires/francais/" + word.lower()
        response = req.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        div = soup.find("div", attrs={"id": "definition"})
        if div:
            return str(div)
        else:
            content = soup.find("section", attrs={"class": "corrector"})
            if content:
                return NOT_RESULT + str(content)
        return NOT_RESULT
    except ConnectionError:
        return connection_error_page
