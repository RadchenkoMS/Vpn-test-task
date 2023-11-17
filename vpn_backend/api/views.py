from django.shortcuts import render
import requests
from django.http import HttpResponse


def proxy_view(request, external_url):
    url = f'https://{external_url}'
    response = requests.get(url)
    if response.status_code == 200:
        return HttpResponse(response.content, content_type=response.headers['Content-Type'])
    else:
        return HttpResponse(f'Error proxying content from {url}', status=response.status_code)