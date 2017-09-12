import json
import urllib
from pprint import pprint

base_url = 'https://query.yahooapis.com/v1/public/yql?'
query = {
    'q': 'select Ask,Bid,Name,BookValue,TwoHundreddayMovingAverage,Volume,YearHigh, YearLow \
    from yahoo.finance.quotes \
    where symbol in \
    ("MRK.DE", "FRE.DE", "BMW.DE", "EOAN.DE", "CON.DE", "DTE.DE", "VOW3.DE", \
    "HEN3.DE", "LIN.DE", "RWE.DE", "BEI.DE", "VNA.DE", "IFX.DE", "PSM.DE", \
    "FME.DE", "BAYN.DE", "SAP.DE", "TKA.DE", "ADS.DE", "HEI.DE", "DAI.DE", \
    "BAS.DE", "DPW.DE", "LHA.DE", "ALV.DE", "DB1.DE", "DBK.DE", "SIE.DE", \
    "CBK.DE", "MUV2.DE")',
    'format': 'json',
    'env': 'store://datatables.org/alltableswithkeys'
}

url = base_url + urllib.urlencode(query)
response = urllib.urlopen(url)
data = response.read()
quote = json.loads(data)
pprint(quote)

for item in quote['query']['results']['quote']:
    print (item['Name'])
    print (item['Bid'])
