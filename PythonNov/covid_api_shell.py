Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> import urllib.request as url
>>> response = url.urlopen("https://data.covid19india.org/states_daily.json")
>>> data = json.load(response)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['states_daily'])
>>> states = data['states_daily']
>>> type(states)
<class 'list'>
>>> states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
>>> len(states)
1563
>>> 1563 / 3
521.0
>>> states[100]
{'an': '1', 'ap': '0', 'ar': '0', 'as': '3', 'br': '8', 'ch': '0', 'ct': '6', 'date': '16-Apr-20', 'dateymd': '2020-04-16', 'dd': '0', 'dl': '11', 'dn': '0', 'ga': '0', 'gj': '9', 'hp': '3', 'hr': '8', 'jh': '0', 'jk': '2', 'ka': '2', 'kl': '27', 'la': '2', 'ld': '0', 'mh': '5', 'ml': '0', 'mn': '0', 'mp': '6', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '2', 'py': '0', 'rj': '17', 'sk': '0', 'status': 'Recovered', 'tg': '68', 'tn': '62', 'tr': '0', 'tt': '258', 'un': '0', 'up': '11', 'ut': '0', 'wb': '5'}
>>> states[200]
{'an': '0', 'ap': '2', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '19-May-20', 'dateymd': '2020-05-19', 'dd': '0', 'dl': '6', 'dn': '0', 'ga': '0', 'gj': '25', 'hp': '1', 'hr': '0', 'jh': '0', 'jk': '2', 'ka': '3', 'kl': '0', 'la': '0', 'ld': '0', 'mh': '76', 'ml': '0', 'mn': '0', 'mp': '6', 'mz': '0', 'nl': '0', 'or': '1', 'pb': '1', 'py': '0', 'rj': '5', 'sk': '0', 'status': 'Deceased', 'tg': '4', 'tn': '3', 'tr': '0', 'tt': '146', 'un': '0', 'up': '5', 'ut': '0', 'wb': '6'}
>>> states[1000]
{'an': '0', 'ap': '121', 'ar': '0', 'as': '17', 'br': '60', 'ch': '26', 'ct': '312', 'date': '10-Feb-21', 'dateymd': '2021-02-10', 'dd': '0', 'dl': '131', 'dn': '0', 'ga': '64', 'gj': '495', 'hp': '49', 'hr': '107', 'jh': '42', 'jk': '32', 'ka': '322', 'kl': '5745', 'la': '3', 'ld': '25', 'mh': '2421', 'ml': '4', 'mn': '39', 'mp': '175', 'mz': '3', 'nl': '3', 'or': '81', 'pb': '180', 'py': '32', 'rj': '89', 'sk': '3', 'status': 'Recovered', 'tg': '163', 'tn': '493', 'tr': '0', 'tt': '11796', 'un': '0', 'up': '166', 'ut': '110', 'wb': '283'}
>>> states[1000]['dl']
'131'
>>> states[1000]['up']
'166'
>>> states[1000]['hr']
'107'
>>> 