from fastapi import FastAPI
from typing import Union
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

@app.get('/')
def hello(url: Union[str, None] = None):
    with httpx.Client() as client:
        print(url)
        r = client.get(url)#.text
        c = client.get(url).content
    soup = BeautifulSoup(r, features="html.parser")
    print("********************",r)
    title = soup.title.string
    # print ('TITLE IS :', title)

    image = soup.find('meta', attrs={'property': 'og:image'})
    if image:
        image = image['content']
    else:
        image = ""
    # image = image.get('content')
    # print("IMAGE IS: ", image['content'])
    meta = soup.find_all('meta')
    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            # print ('NAME    :',tag.attrs['name'].lower())
            desc = tag.attrs['content']
            # print ('CONTENT :',tag.attrs['content'])

    data = {
        "title":title,
        "description":desc,
        "image":image,
        "url":url
    }
    print(data)
    return data

