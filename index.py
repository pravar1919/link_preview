import httpx, json
from bs4 import BeautifulSoup

def lambda_handler(event):
    # print(event['queryStringParameters']['url'])
    url=event#['queryStringParameters']['url']
    if not url.startswith("https://") or url.startswith("http://"):
        return {"status":400, "detail":"Invalid Url Try using https:// before link"}
    with httpx.Client() as client:
        r = client.get(url).text
        soup = BeautifulSoup(r, features="html.parser")
    
        # print("soup: ",soup)
        
        title = soup.find('meta', attrs={'title': 'og:title'})
        if title:
            title = title['content']
        else:
            title = ""
        # print ('TITLE IS :', title)

        image = soup.find('meta', attrs={'property': 'og:image'})
        if image:
            image = image['content']
        else:
            image = ""
        # print("IMAGE IS: ", image['content'])
        meta = soup.find_all('meta')
        print(soup.find('meta', attrs={'name': 'description'}))
        for tag in meta:
            if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
                # print ('NAME    :',tag.attrs['name'].lower())
                desc = tag.attrs['content']
                # print ('CONTENT :',tag.attrs['content'])
        try:
            desc = desc
        except:
            desc = ""
        print("desc",desc)
        # if not desc:
        #     desc = ""
        data = {
            "title":title,
            "description":desc,
            "image":image,
            "url":url
        }
        print(data)
        return {"detail":json.dumps(data), "status":200}

# lambda_handler('https://app.minstein.com')
lambda_handler('https://www.facebook.com')