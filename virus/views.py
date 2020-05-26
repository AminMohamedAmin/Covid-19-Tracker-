from django.shortcuts import render, HttpResponse
import requests
from .models import Assure
from datetime import datetime
from django.views.generic import ListView

# Create your views here.
class All(ListView):
    alldata = requests.get('https://corona.lmao.ninja/v2/all').json()
    allcases = alldata['cases']
    allrecoveries = alldata['recovered']
    alldeaths = alldata['deaths']
    allactive = alldata['active']
    allaffectedCountries = alldata['affectedCountries']

    cnum = []
    for i in range(1, allaffectedCountries + 1):
        cnum.append(i)

class Egypt(ListView):
    locationdata = requests.get('https://corona.lmao.ninja/v2/countries/egypt').json()
    locationcases = locationdata['cases']
    locationrecoveries = locationdata['recovered']
    locationdeaths = locationdata['deaths']
    locationactive = locationdata['active']
    locationtodaycases = locationdata['todayCases']
    locationtodaydeaths = locationdata['todayDeaths']
    locationcritical = locationdata['critical']
    locationcasesPerOneMillion = locationdata['casesPerOneMillion']
    locationdeathsPerOneMillion = locationdata['deathsPerOneMillion']

class HistAll(ListView):
    res1 = requests.get('https://corona.lmao.ninja/v2/historical/all').json()['cases']
    res2 = requests.get('https://corona.lmao.ninja/v2/historical/all').json()['deaths']
    res3 = requests.get('https://corona.lmao.ninja/v2/historical/all').json()['recovered']

class CountryData(ListView):
    casesarr1 = []
    casesarr2 = []
    res1 = requests.get('https://corona.lmao.ninja/v2/countries').json()
    for i in res1:
        casesarr1.append(i['country'])
    for ii in res1:
        casesarr2.append(ii['cases'])

    activearr1 = []
    activearr2 = []
    res2 = requests.get('https://corona.lmao.ninja/v2/countries').json()
    for i in res2:
        activearr1.append(i['country'])
    for ii in res2:
        activearr2.append(ii['active'])

    recovarr1 = []
    recovarr2 = []
    res3 = requests.get('https://corona.lmao.ninja/v2/countries').json()
    for i in res3:
        recovarr1.append(i['country'])
    for ii in res3:
        recovarr2.append(ii['recovered'])

    deathsarr1 = []
    deathsarr2 = []
    res4 = requests.get('https://corona.lmao.ninja/v2/countries').json()
    for i in res4:
        deathsarr1.append(i['country'])
    for ii in res4:
        deathsarr2.append(ii['deaths'])



def Home(request):
    all = All()
    egy = Egypt()
    hist = HistAll()
    countrydata = CountryData()

    drate = zip(countrydata.casesarr2, countrydata.deathsarr2)
    crate = zip(countrydata.casesarr2, countrydata.recovarr2)


    context = {
        'allcases': all.allcases,
        'allrecoveries': all.allrecoveries,
        'alldeaths': all.alldeaths,
        'allactive':all.allactive,
        'allaffectedCountries':all.allaffectedCountries,

        'locationcases': egy.locationcases,
        'locationrecoveries': egy.locationrecoveries,
        'locationdeaths': egy.locationdeaths,
        'locationactive': egy.locationactive,
        'locationtodaycases': egy.locationtodaycases,
        'locationtodaydeaths': egy.locationtodaydeaths,
        'locationcritical': egy.locationcritical,
        'locationcasesPerOneMillion': egy.locationcasesPerOneMillion,
        'locationdeathsPerOneMillion': egy.locationdeathsPerOneMillion,

        'res1': hist.res1,
        'res2': hist.res2,
        'res3': hist.res3,

        'casesarr1': countrydata.casesarr1,
        'casesarr2': countrydata.casesarr2,
        'activearr1': countrydata.activearr1,
        'activearr2': countrydata.activearr2,
        'recovarr1': countrydata.recovarr1,
        'recovarr2': countrydata.recovarr2,
        'deathsarr1': countrydata.deathsarr1,
        'deathsarr2': countrydata.deathsarr2,
        'drate': drate,
        'crate': crate,
        'cnum': all.cnum,
    }
    return render(request, 'home.html', context)

def Country_Info(request):
    all = All()
    egy = Egypt()
    hist = HistAll()
    countrydata = CountryData()

    try:
        locate = request.POST.get('location')
        location = str(locate)
        locatedata = requests.get('https://corona.lmao.ninja/v2/countries/' + location).json()
        locatename = locatedata['country']
        locatecases = locatedata['cases']
        locaterecoveries = locatedata['recovered']
        locatedeaths = locatedata['deaths']
        locateactive = locatedata['active']
        locatetodaycases = locatedata['todayCases']
        locatetodaydeaths = locatedata['todayDeaths']
        locatecritical = locatedata['critical']
        locatecasesPerOneMillion = locatedata['casesPerOneMillion']
        locatedeathsPerOneMillion = locatedata['deathsPerOneMillion']

        drate = zip(countrydata.casesarr2, countrydata.deathsarr2)
        crate = zip(countrydata.casesarr2, countrydata.recovarr2)

        context = {
            'allcases': all.allcases,
            'allrecoveries': all.allrecoveries,
            'alldeaths': all.alldeaths,
            'allactive':all.allactive,
            'allaffectedCountries':all.allaffectedCountries,

            'locationcases': egy.locationcases,
            'locationrecoveries': egy.locationrecoveries,
            'locationdeaths': egy.locationdeaths,
            'locationactive': egy.locationactive,
            'locationtodaycases': egy.locationtodaycases,
            'locationtodaydeaths': egy.locationtodaydeaths,
            'locationcritical': egy.locationcritical,
            'locationcasesPerOneMillion': egy.locationcasesPerOneMillion,
            'locationdeathsPerOneMillion': egy.locationdeathsPerOneMillion,

            'res1': hist.res1,
            'res2': hist.res2,
            'res3': hist.res3,

            'locatename':locatename,
            'locatecases': locatecases,
            'locaterecoveries': locaterecoveries,
            'locatedeaths': locatedeaths,
            'locateactive': locateactive,
            'locatetodaycases': locatetodaycases,
            'locatetodaydeaths': locatetodaydeaths,
            'locatecritical': locatecritical,
            'locatecasesPerOneMillion': locatecasesPerOneMillion,
            'locatedeathsPerOneMillion': locatedeathsPerOneMillion,

            'locate':locate,

            'casesarr1': countrydata.casesarr1,
            'casesarr2': countrydata.casesarr2,
            'activearr1': countrydata.activearr1,
            'activearr2': countrydata.activearr2,
            'recovarr1': countrydata.recovarr1,
            'recovarr2': countrydata.recovarr2,
            'deathsarr1': countrydata.deathsarr1,
            'deathsarr2': countrydata.deathsarr2,
            'drate': drate,
            'crate': crate,
            'cnum': all.cnum,
        }
        return render(request, 'home.html', context)
    except:
        locate = request.POST.get('location')
        location = str(locate).title()
        rr = requests.get('https://corona.lmao.ninja/v2/countries/' + location).json()
        if rr['message'] == "Country not found or doesn't have any cases":
            if locate:
                text = "Country not found or doesn't have any cases. Check country name carefully and try again."
                return render(request, 'notfound.html', {'locate':locate, 'text':text,})
            else:
                text = "Put your country"
                return render(request, 'notfound.html', {'locate':locate, 'text':text,})
        else:
            text = "Unexpected error, try again"
            return render(request, 'notfound.html', {'locate':locate, 'text':text,})


def Country_History(request):
    all = All()
    egy = Egypt()
    hist = HistAll()
    countrydata = CountryData()
    try:
        locatee = request.POST.get('locationn')
        res = requests.get('https://corona.lmao.ninja/v2/historical/' + str(locatee)).json()['country']
        histname = str(res)

        res1 = requests.get('https://corona.lmao.ninja/v2/historical/' + str(locatee)).json()['timeline']['cases']
        res2 = requests.get('https://corona.lmao.ninja/v2/historical/' + str(locatee)).json()['timeline']['deaths']
        res3 = requests.get('https://corona.lmao.ninja/v2/historical/' + str(locatee)).json()['timeline']['recovered']

        drate = zip(countrydata.casesarr2, countrydata.deathsarr2)
        crate = zip(countrydata.casesarr2, countrydata.recovarr2)

        context = {
            'allcases': all.allcases,
            'allrecoveries': all.allrecoveries,
            'alldeaths': all.alldeaths,
            'allactive':all.allactive,
            'allaffectedCountries':all.allaffectedCountries,

            'locationcases': egy.locationcases,
            'locationrecoveries': egy.locationrecoveries,
            'locationdeaths': egy.locationdeaths,
            'locationactive': egy.locationactive,
            'locationtodaycases': egy.locationtodaycases,
            'locationtodaydeaths': egy.locationtodaydeaths,
            'locationcritical': egy.locationcritical,
            'locationcasesPerOneMillion': egy.locationcasesPerOneMillion,
            'locationdeathsPerOneMillion': egy.locationdeathsPerOneMillion,

            'res1': hist.res1,
            'res2': hist.res2,
            'res3': hist.res3,

            'locatee':locatee,

            'histname':histname,

            'r1':res1,
            'r2': res2,
            'r3': res3,

            'casesarr1': countrydata.casesarr1,
            'casesarr2': countrydata.casesarr2,
            'activearr1': countrydata.activearr1,
            'activearr2': countrydata.activearr2,
            'recovarr1': countrydata.recovarr1,
            'recovarr2': countrydata.recovarr2,
            'deathsarr1': countrydata.deathsarr1,
            'deathsarr2': countrydata.deathsarr2,
            'drate': drate,
            'crate': crate,
            'cnum': all.cnum,
        }
        return render(request, 'home.html', context)
    except:
        locatee = request.POST.get('locationn')
        locationn = str(locatee).title()
        rr = requests.get('https://corona.lmao.ninja/v2/historical/' + locationn).json()
        if rr['message'] == "Country not found or doesn't have any historical data":
            if locatee:
                text = "Country not found or doesn't have any historical data. Check country name carefully and try again."
                return render(request, 'notfound.html', {'locate': locatee, 'text': text, })
            else:
                return HttpResponse('put your country')
        else:
            return HttpResponse('Unexpected error, try again')


def Assurance(request):
    all = All()
    egy = Egypt()
    hist = HistAll()
    countrydata = CountryData()

    name = request.POST['name']
    age = request.POST['age']
    gender = request.POST['gender']
    address = request.POST['address']

    if age < '15':
        a = 0
    elif age >= '15' and age < '30':
        a = 1
    elif age >= '30' and age < '50':
        a = 2
    elif age >= '50' and age < '70':
        a = 3
    elif age > '70':
        a = 4
    else:
        a = 0

    if gender == 'Male':
        g = 2
    elif gender == 'Female':
        g = 1
    else:
        g = 0

    agedata = a
    genderdata = g
    level1 = agedata + genderdata

    c1 = request.POST.get('c1', False)
    c2 = request.POST.get('c2', False)
    c3 = request.POST.get('c3', False)
    c4 = request.POST.get('c4', False)
    c5 = request.POST.get('c5', False)
    c6 = request.POST.get('c6', False)
    c7 = request.POST.get('c7', False)
    c8 = request.POST.get('c8', False)
    c9 = request.POST.get('c9', False)
    c10 = request.POST.get('c10', False)

    if c1 == 'on':
        c1 = True
    else:
        c1 = False

    if c2 == 'on':
        c2 = True
    else:
        c2 = False

    if c3 == 'on':
        c3 = True
    else:
        c3 = False

    if c4 == 'on':
        c4 = True
    else:
        c4 = False

    if c5 == 'on':
        c5 = True
    else:
        c5 = False

    if c6 == 'on':
        c6 = True
    else:
        c6 = False

    if c7 == 'on':
        c7 = True
    else:
        c7 = False

    if c8 == 'on':
        c8 = True
    else:
        c8 = False

    if c9 == 'on':
        c9 = True
    else:
        c9 = False

    if c10 == 'on':
        c10 = True
    else:
        c10 = False

    new = Assure()
    new.name = name
    new.age = age
    new.gender =gender
    new.address = address
    new.temperature = c1
    new.cough = c2
    new.throat = c3
    new.vomiting = c4
    new.chronic = c5
    new.travel = c6
    new.respiratory = c7
    new.condition = c8
    new.visiting = c9
    new.worker = c10

    new.save()

    if c1 == True:
        d1 = 2
    else:
        d1 = 0

    if c2 == True:
        d2 = 2
    else:
        d2 = 0

    if c3 == True:
        d3 = 1
    else:
        d3 = 0

    if c4 == True:
        d4 = 1
    else:
        d4 = 0

    if c5 == True:
        d5 = 1
    else:
        d5 = 0

    if c6 == True:
        d6 = 5
    else:
        d6 = 0

    if c7 == True:
        d7 = 4
    else:
        d7 = 0

    if c8 == True:
        d8 = 3
    else:
        d8 = 0

    if c9 == True:
        d9 = 3
    else:
        d9 = 0

    if c10 == True:
        d10 = 2
    else:
        d10 = 0

    level2 = d1 + d2 + d3 + d4 + d5
    level3 = d6 + d7 + d8 + d9 + d10

    data = Assure.objects.filter(name=name)
    new.delete()

    date = datetime.now()

    drate = zip(countrydata.casesarr2, countrydata.deathsarr2)
    crate = zip(countrydata.casesarr2, countrydata.recovarr2)

    context = {
        'allcases': all.allcases,
        'allrecoveries': all.allrecoveries,
        'alldeaths': all.alldeaths,
        'allactive':all.allactive,
        'allaffectedCountries':all.allaffectedCountries,

        'locationcases': egy.locationcases,
        'locationrecoveries': egy.locationrecoveries,
        'locationdeaths': egy.locationdeaths,
        'locationactive': egy.locationactive,
        'locationtodaycases': egy.locationtodaycases,
        'locationtodaydeaths': egy.locationtodaydeaths,
        'locationcritical': egy.locationcritical,
        'locationcasesPerOneMillion': egy.locationcasesPerOneMillion,
        'locationdeathsPerOneMillion': egy.locationdeathsPerOneMillion,

        'res1': hist.res1,
        'res2': hist.res2,
        'res3': hist.res3,

        'data':data,
        'level1': level1,
        'level2': level2,
        'level3':level3,
        'name':name,

        'date':date,

        'casesarr1': countrydata.casesarr1,
        'casesarr2': countrydata.casesarr2,
        'activearr1': countrydata.activearr1,
        'activearr2': countrydata.activearr2,
        'recovarr1': countrydata.recovarr1,
        'recovarr2': countrydata.recovarr2,
        'deathsarr1': countrydata.deathsarr1,
        'deathsarr2': countrydata.deathsarr2,
        'drate': drate,
        'crate': crate,
        'cnum': all.cnum,
    }
    return render(request, 'home.html', context)
