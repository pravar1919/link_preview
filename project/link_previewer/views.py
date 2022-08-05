from django.http import JsonResponse
from django.shortcuts import render
import requests, extraction, json


def home(request):
    if request.is_ajax():
        url=request.GET.get('url')
        print(url)
        if not url.startswith("https://") or url.startswith("http://"):
            print("inside not https")
            return JsonResponse({"status":400, "detail":"Invalid Url Try using https:// before link"})

        ext = extraction.Extractor()
        x = ext.extract(requests.get(url).text, source_url=url)
        print("x", x)
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
        print(json.dumps(data))
        return JsonResponse({"detail":json.dumps(data), "status":200})
    return render(request,"index.html")

    # https://cxgmuuirzz6lnjrxcbckgt5uaq0fqbwy.lambda-url.ap-south-1.on.aws/