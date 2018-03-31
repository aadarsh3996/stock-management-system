from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from stockapp.models import CompanyList
import json
import requests

# Create your views here.

app_name='stockapp'


#/stock/market/batch?symbols=aapl,fb,tsla&types=quote,news,chart&range=1m&last=5
def detailed(request):

    print('hi')
    return render(request,'templates/detailed.html')


def movement(request):

    logistic_regression_url="http://127.0.0.1:8500/logistics?symbol="

    registered=0
    dictionary={}
    # dictionary["registered"]=registered



    print('hi')

    query=request.GET.get('q')

    print(query)

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




def home(request):

    batch_quotes_url="https://api.iextrading.com/1.0//stock/market/batch?symbols="

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
