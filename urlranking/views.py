from django.shortcuts import render
from django.http import HttpResponse
from .models import Url_index
from . import tests

def index(request):
    return render(request, "base.html")
    
    
def Gsearch(request):
    count = 0
    url_ranking = 0
    context = []
    content_name = request.POST.get('name')
    url = request.POST.get('search_url')
    ip_detail = tests.get_location()
    user_ip = ip_detail.get('ip')
    user_city = ip_detail.get('city')
    user_country = ip_detail.get('country')
    dataset = Url_index.objects.all().filter(content=content_name,tigger_url=url,system_ip=user_ip,country=user_country,city=user_city)
    try :
        from googlesearch import search
    except ImportError:
        print("No Module named 'google' Found")      
    for i in search(query=content_name,lang='en',num=10,stop=100,pause=2):
        count += 1
        if  url == i:
            context.append("Position : "+ str(count))
            url_ranking = count
            context.append("URL : " + i)
    if url_ranking != 0:
        if not dataset:
            Url_index.objects.create(content=content_name,tigger_url=url,ranking=url_ranking,system_ip=user_ip,country=user_country,city=user_city)
            context.append("Message : " + "This Content Search First time")        
            return HttpResponse(context)
        else:
            ranking_count = [item.ranking for item in dataset][0]
            print(ranking_count)
            if ranking_count > url_ranking:
                context.append("Message : " + "URL Ranking Increase")
            elif ranking_count == url_ranking:
                context.append("Message : " + "URL Ranking Have No Change")            
            else:
                context.append("Message : " + "URL Ranking Decrease")            
            dataset.update(ranking = url_ranking)
            return HttpResponse(context)
    else:
        return HttpResponse("Search combination have no match")