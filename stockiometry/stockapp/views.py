from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from stockapp.models import CompanyList,Order,Track
import json
import requests
from django.contrib.auth import authenticate, login, logout

# Create your views here.

app_name='stockapp'


#/stock/market/batch?symbols=aapl,fb,tsla&types=quote,news,chart&range=1m&last=5
def detailed(request):

    quote= None
    news= None
    peers= None
    logo= None
    stats= None
    financials= None
    company= None
    competitors = None


    registered = 0

    print('hi')
    print(request.session.get('username'))

    company_list = CompanyList.objects.all()
    print(len(company_list))

    query=request.GET.get('q')

    if query is not None:

        company_object = CompanyList.objects.filter(company_name=query).first()
        symbol = company_object.company_symbol

        url = "https://api.iextrading.com/1.0/stock/" + symbol + "/batch?types=quote,news,peers,logo,stats,financials,company"
        registered=1

        resp = requests.get(url)

        detail_dict = resp.json()

        quote= detail_dict.get("quote")
        news= detail_dict.get("news")
        peers= detail_dict.get("peers")
        logo= detail_dict.get("logo")
        stats= detail_dict.get("stats")
        financials= detail_dict.get("financials")
        company= detail_dict.get("company")

        # print(quote)
        # print(news)
        # print(peers)
        # print(logo)
        # print(stats)
        # print(financials)
        # print(company)

        competitors =[]

        for x in peers:
            company_object = CompanyList.objects.filter(company_symbol=x).first()
            if company_object is not None:
                competitors.append(company_object.company_name)

        print(competitors)

        # print(resp.json())


    return render(request,'templates/detailed.html',{'company_list':company_list,'quote':quote,'news':news,'logo':logo,'stats':stats,'financials':financials,'company':company,'competitors':competitors,'registered':registered})

def buy(request):

    print('hi')
    print(request.session.get('username'))




    company_list = CompanyList.objects.all()
    print(len(company_list))

    #print(company_list[0].company_name)

    query=request.GET.get('q')

    if query is None:
        query = request.GET.get('quantity')
    print(request.GET)

    registered = 0

    temp=0

    stock_dict=None

    if query is not None:
        print('bitch')
        if  'q' in request.GET.keys():
            print('hello')

            print(query)

            company_object = CompanyList.objects.filter(company_name=query).first()
            symbol = company_object.company_symbol
            url = "https://api.iextrading.com/1.0/stock/"+symbol+"/quote"


            resp = requests.get(url)
            print(resp.json())

            stock_dict = resp.json()

            registered = 1

            temp = 1

        if 'quantity' in request.GET.keys():
            print('inside second form')
            username = request.session['username']
            bs = "BUY"
            sname= request.GET.get('name')
            ssymbol = request.GET.get('symbol')
            sprice = request.GET.get('price')
            squantity = request.GET.get('quantity')
            print(int(float(sprice)))
            print(username)
            total_worth = int(float(sprice)) * int(squantity)
            print(total_worth)

            c_order = Order(username=username,bs=bs,sname=sname,sprice=sprice,squantity=squantity,ssymbol=ssymbol,total_worth=str(total_worth))
            c_order.save()

            c_track = Track(username=username,squantity=squantity,ssymbol=ssymbol,sname=sname)
            c_track.save()


    return render(request,'templates/buy.html',{"company_list":company_list,"stock_dict":stock_dict,"registered": registered,"temp":temp})

def sell(request):

    print(request.session.get('username'))
    print('hi')
    return render(request,'templates/sell.html')












def movement(request):

    print(request.session.get('username'))

    logistic_regression_url="http://127.0.0.1:8500/logistics?symbol="

    registered=0
    dictionary={}
    # dictionary["registered"]=registered



    print('hi')

    query=request.GET.get('q')

    #print(query)

    if query is not None:
        logistic_regression_url=logistic_regression_url+query
        print(logistic_regression_url)

        logistic_request=requests.get(logistic_regression_url)
        predicted_dict=logistic_request.json()
        #predicted_dict=json.loads(predict_json)

        print(predicted_dict)

        dictionary["c_name"]=predicted_dict["company_name"]
        dictionary["c_primary"]=predicted_dict["company_primary_exchange"]
        dictionary["c_label"]=predicted_dict["predicted_label"]
        dictionary["c_symbol"]=predicted_dict["company_symbol"]
        # dictionary["registered"]=1

        registered=1

        print(dictionary)





    return render(request,'templates/movement.html',{'registered':registered, 'dictionary' : dictionary})

def forest(request):

    stock_dict = None
    company_list = CompanyList.objects.all()
    print(len(company_list))

    registered = 0

    #print(company_list[0].company_name)

    query=request.GET.get('q')

    if query is not None:
        registered = 1
        random_forest_url= "http://127.0.0.1:8500/forest?symbol="

        company_object = CompanyList.objects.filter(company_name=query).first()
        symbol = company_object.company_symbol
        random_forest_url = random_forest_url + symbol

        resp = requests.get(random_forest_url)
        print(resp.json())

        stock_dict = resp.json()



    return render(request,'templates/forest.html',{"company_list":company_list,"registered": registered,"dictionary":stock_dict})


def deep(request):
    stock_dict = None
    company_list = CompanyList.objects.all()
    print(len(company_list))

    registered = 0

    query=request.GET.get('q')

    if query is not None:
        registered = 1
        deep_learning_url="http://127.0.0.1:8500/deep?symbol="
        company_object = CompanyList.objects.filter(company_name=query).first()
        symbol = company_object.company_symbol
        deep_learning_url=deep_learning_url+symbol
        print(deep_learning_url)

        resp = requests.get(deep_learning_url)
        print(resp.json())

        stock_dict = resp.json()


    return render(request,'templates/deep.html',{"company_list":company_list,"registered": registered,"dictionary":stock_dict})




def home(request):

    batch_quotes_url="https://api.iextrading.com/1.0//stock/market/batch?symbols="

    print(request.session.get('username'))

    stocks_dict=None
    registered=0
    print(registered)

    print('hello')

    query=request.GET.get('q')


    if query is not None:
        print(query)
        results=CompanyList.objects.filter(Q(company_symbol__icontains=query))
        #temp=results[0]
        if (len(results) > 40):
            results=results[0:40]

        # for i in results:
        #     print(results[i].company_symbol)
        #print(results)

        print(len(results))

        symbols_string=""

        for i in range(len(results)):
            temp=results[i]
            symbols_string=symbols_string+temp.company_symbol
            symbols_string=symbols_string+","

        print(symbols_string)

        count=len(symbols_string)
        print(count)
        count=count-1
        symbols_string=symbols_string[0:count]

        print(symbols_string)

        batch_quotes_url = batch_quotes_url + symbols_string
        batch_quotes_url= batch_quotes_url + "&types=quote"
        print(batch_quotes_url)

        stocks_request=requests.get(batch_quotes_url)
        print(stocks_request.json)



        stocks_dict=json.loads(stocks_request.text)

        registered=1

        print(registered)

        print(type(stocks_dict))

        # for i,j in stocks_dict.items():
        #     print (i)
        #     for k,l in j.items():
        #         print (k)
        #         for m,n in l.items():
        #             print(m,l[m],sep=" ")

    return render(request,'templates/home.html',{'registered':registered, 'stocks_dict' : stocks_dict})

def user_logout(request):

    print('logout')
    print(request.session.get('username'))
    request.session.clear()
    logout(request)
    print(request.session.get('username'))
    return render(request,"templates/logout.html")
