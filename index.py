import requests, extraction, json


def lambda_handler(event, x):
    print(event, x)
    url=event['queryStringParameters']['url']
    if not url.startswith("https://") or url.startswith("http://"):
        return {"status":400, "detail":"Invalid Url Try using https:// before link"}

    ext = extraction.Extractor()
    x = ext.extract(requests.get(url).text, source_url=url)
    print("x",x)
    if x.image:
        image = x.images[0]
    else:
        image = ""
    title = x.title
    desc = x.description
    
    data = {
        "title":title,
        "description":desc,
        "image":image,
        "url":url
    }
    print(data)
    return {"detail":json.dumps(data), "status":200}