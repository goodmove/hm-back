import bs4
import requests
from polyglot.text import Text
import json

def get_text_by_url(link = "https://en.wikipedia.org/wiki/French_invasion_of_Russia"):
    response = requests.get(link)
    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')
        title = html.select("#firstHeading")[0].text
        paragraphs = html.select("p")
        intro = ''
        for i, para in enumerate(paragraphs):
            intro+= para.text
            if i==2:
                break
        return intro

def get_text_by_idea(idea="French invasion of Russia"):
    session = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": idea,
        "prop": "links",
        "pllimit": "max"
    }

    response = session.get(url=url, params=params)
    data = response.json()
    pages = data["query"]["pages"]
    pg_count = 1

    page_titles = []
    for key, val in pages.items():
        for link in val["links"]:
            page_titles.append(link["title"])
            break
    url = 'https://en.wikipedia.org/wiki/'+str(page_titles[0])
    return get_text_by_url(url)
    

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees.label(filter=lambda t: t.node == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: 
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)    
    

def get_meme(name, text):

    url = "http://2276.lnsigo.mipt.ru/v1/squad"
    q = "Who is "
    for n in name:
        q+=n
        q+=' '
    q+="?"
    print(q)
    data = {
    "questions": [q],
        "secret": "GBEjUo7SSaQDljj9lsZZukUIUl9gr1cc",
        "text": text}
    
    response = requests.post(url=url, data=json.dumps(data))
    
    return response.text

def name_from_text(text):
    text_new = Text(text)
    for el in text_new.entities:
        if el.tag == 'I-PER':
            return el
            
if __name__ == "__main__":
    text = get_text_by_idea("Winston Churchill")
    name = name_from_text(text)
    print(get_meme(name, text))
