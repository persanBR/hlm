#!/usr/bin/python
import requests,sys,datetime

global days
days = '7'

def currentprice(coin,basecurrency):
        curpriceurl = 'https://min-api.cryptocompare.com/data/price?fsym='+coin+'&tsyms='+basecurrency[0:3]+''
        price = requests.get(curpriceurl)
        curprice = price.json()
        return curprice[basecurrency[0:3]]

def getprice(coin,daylimit,basecurrency):
        histurl = 'https://min-api.cryptocompare.com/data/histoday?fsym='+coin+'&tsym='+basecurrency+'&e=BitTrex&limit='+daylimit+''
        price = requests.get(histurl)
        timefrom = datetime.datetime.fromtimestamp(int(price.json().get('TimeFrom'))).strftime('%Y-%m-%d %H:%M:%S')
        timeto = datetime.datetime.fromtimestamp(int(price.json().get('TimeTo'))).strftime('%Y-%m-%d %H:%M:%S')
        listhigh = []
        listlow = []
        print (coin+' - '+basecurrency+' Sumary:')
        for a in price.json().get('Data'):
                #print ('Time: ' + datetime.datetime.fromtimestamp(int(a['time'])).strftime('%Y-%m-%d %H:%M:%S'))
                #print ('High: ' + str(a['high'])),
                #print ('Low: ' + str(a['low']))
                ##print ('Open: ' + str(a['open']))
                ##print ('Close: ' + str(a['close']))
                listhigh.append(a['high'])
                listlow.append(a['low'])
        print ('From '+str(timefrom)+' to '+str(timeto))
        print ('Highest value: ' + str(max(listhigh)))
        print ('Lowest value: ' + str(min(listlow)))
        print ('High Avg: ' + str(sum(listhigh)/len(listhigh)))
        print ('Lowest Avg: ' + str(sum(listlow)/len(listlow)))
        print ('Current price: ' + str(currentprice(coin,basecurrency)))
        print ('')

def basemarket(coin):
        currencies = requests.get('https://bittrex.com/api/v1.1/public/getmarkets')
        for a in currencies.json().get('result'):
                if coin == a['MarketCurrency']:
                        getprice(a['MarketCurrency'],days,a['BaseCurrency'][0:3])

def main():
        currencies = requests.get('https://bittrex.com/api/v1.1/public/getcurrencies')
        for a in currencies.json().get('result'):
               if a['IsActive'] == True:
                       #print a['Currency']
                       basemarket(a['Currency'])
               #sys.exit(0)


if __name__ == "__main__":
        main()
