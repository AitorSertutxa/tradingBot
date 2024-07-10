from kucoin_futures.client import Market
import Config
# #Variables Globales
cliente = Market(url='https://api.kucoin.com')
dataCandles = 200
emaShort = 2
#-------------------------------------------------
def Get_PareDatuak():
    apareGuztiak = []   

    apareGuztiak = cliente.get_ticker('XBTUSDM')

    return apareGuztiak
    