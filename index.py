import requests
from bs4 import BeautifulSoup

def main(url):
    url=url
    r = requests.get(url).text
    soup = BeautifulSoup(r, features="html.parser")

    title = soup.title.string
    # print ('TITLE IS :', title)

    image = soup.find('meta', attrs={'property': 'og:image'})
    image = image['content']
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

main("https://www.ambitionbox.com/overview/trootech-business-solutions-overview?utm_campaign=share_overview_header&utm_medium=company_header&utm_source=ambitionbox")