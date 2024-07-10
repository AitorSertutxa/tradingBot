import Bitget.Futures.Market_Api as Market
import Bitget.Futures.Account_Api as accounts
import Bitget.Futures.Order_Api as order
import Bitget.Consts as c
import Config
import TecIndicators as tec
import Objetos as ob
import datetime
import winsound as wi
import time
#--------------------------------------------
# #Variables Globales
cliente = Market.MarketApi(Config.GILTZA_BIT, Config.GILTZA_IXILA_BIT, Config.PASSAPI_BIT, use_server_time=False, first=False)
accountApi = accounts.AccountApi(Config.GILTZA_BIT, Config.GILTZA_IXILA_BIT, Config.PASSAPI_BIT, use_server_time=False, first=False)
orderApi = order.OrderApi(Config.GILTZA_BIT, Config.GILTZA_IXILA_BIT, Config.PASSAPI_BIT, use_server_time=False, first=False)
dataCandles = 100
emaShort = 2
emaLarge = 22
dBeneficios = 0
strPreviPair = ''
#--------------------------------------------
def Get_PareDatuak():
    apareGuztiak = []   

    apareGuztiak = cliente.tickers('umcbl')

    return apareGuztiak['data']

def Get_PareakETHBTCKenduta(pair):
    aPareak = []

    for i in range(0, len(pair)):        
        aPareak.append(pair[i])
    
    return aPareak

def Get_GainetikoPareak(pair , beheLanga):
    aAuxGain = []
    aGainetikoak = []

    for i in range(0, len(pair)):
        aAuxGain.append([pair[i]['symbol'], float(pair[i]['priceChangePercent']), float(pair[i]['last'])])

    aAuxGain = sorted(aAuxGain, key=lambda x: x[1], reverse = True)      
    for i in range(0, beheLanga):       
        aGainetikoak.append(aAuxGain[i])

    return aGainetikoak

def Get_PareDefinitiboak(pair, iTipoVela):
    aPareDefProv = []
    aPareDef = []
    ema2 = []
    ema22 = []
    ordena = 0
    iEma2 = 0
    iEma22 = 0

    for i in range(0, len(pair)):
        klines = Get_DatosKlines(pair[i][0], dataCandles, iTipoVela)
        if (klines != None):
            df = ob.Get_DataFrameSoloCandlestick(klines)        
            if(df.empty == False):                                                    
                ema2 = tec.calculate_ema(df['close'], emaShort)
                ema22 = tec.calculate_ema(df['close'], emaLarge)  
                rsi, stochrsiK, stochrsiD = tec.stoch_rsi_tradingview(df)
                iEma2 = len(ema2) -1
                iEma22 = len(ema22) - 1                                 
                if(ema2[iEma2 - 1] < ema22[iEma22 - 1] and ema2[iEma2] > ema22[iEma22]):
                    #if(stochrsiK[99] < 80):
                        ordena = ema2[iEma2] - ema22[iEma22]
                        aPareDefProv.append([pair[i][0], pair[i][1], ema22[iEma22], ema2[iEma2], pair[i][2], round(ordena, 5), 'BERDEA'])
                elif(ema2[iEma2 - 1] > ema22[iEma22 - 1] and ema2[iEma2] < ema22[iEma22]):
                    #if(stochrsiK[99] > 20):
                        ordena = ema22[iEma22] - ema2[iEma2] 
                        aPareDefProv.append([pair[i][0], pair[i][1], ema22[iEma22], ema2[iEma2], pair[i][2], round(ordena, 5), 'GORRIA'])      
    aPareDef = sorted(aPareDefProv, key=lambda x: x[5], reverse = True) 

    return aPareDef

def Get_DatosKlines(pair, dataCandles, iTipoVela):   
    klines = []

    nowDatetime = datetime.datetime.now()
    nowDatetime100 = nowDatetime - datetime.timedelta(hours=dataCandles)     
    miliNowDatetime = round(nowDatetime.timestamp() * 1000)
    nowDatetime100 = round(nowDatetime100.timestamp() * 1000)  

    if(iTipoVela == 1):
        klines = cliente.candles(pair, granularity=c.KLINE_INTERVAL_1HOUR, startTime=nowDatetime100, endTime=miliNowDatetime)
    elif(iTipoVela == 15):
        klines = cliente.candles(pair, granularity=c.KLINE_INTERVAL_15MINUTE, startTime=nowDatetime100, endTime=miliNowDatetime)
    elif(iTipoVela == 30):
        klines = cliente.candles(pair, granularity=c.KLINE_INTERVAL_30MINUTE, startTime=nowDatetime100, endTime=miliNowDatetime)
   
    return klines

def Get_HoraValida(iRangoVela):
    date = datetime.datetime.now()
    #-----------------------------------
    if(iRangoVela == 1):
        if(date.minute == 57 or date.minute == 58 or date.minute == 59):        
            return 1
        else:
            return 0
    elif(iRangoVela == 15):
        if(date.minute == 12 or date.minute == 13 or date.minute == 14):        
            return 1
        else:
            return 0
    else:
        if(date.minute == 27 or date.minute == 28 or date.minute == 29):        
            return 1
        else:
            return 0
    
def ErosketaTxanpona(pair, iLeverage,dTakeProf, dStop, dUsdtSim):
    dCantidad = 0
    dProfit = 0
    dLost = 0
    dBalance = 0
    dResultado1 = 0
    dResultado2 = 0
    global dBeneficios 
    global strPreviPair

    if(pair == strPreviPair):
        return 0
    strPreviPair = pair    
    if(dBeneficios == 0):
        dBeneficios = dUsdtSim
    resultLeverage = accountApi.leverage(pair[0], marginCoin='USDT', leverage=iLeverage)    
    if(resultLeverage['msg'] != 'success'):
        return 0
    else:
        aPairData = cliente.ticker(pair[0])
        if(aPairData['msg'] != 'success'):
            return 0
        else:
            dCantidad = (dUsdtSim * iLeverage) / float(aPairData['data']['last'])            
            if(pair[6] == 'BERDEA'):
                dProfit =  float(aPairData['data']['last'])   + ((float(aPairData['data']['last'])  * dTakeProf) / 100)
                dLost = float(aPairData['data']['last'])  - ((float(aPairData['data']['last'])   * dStop) / 100)
                # result = orderApi.place_order(pair[0], marginCoin='USDT', size=1, side='open_long', orderType='market')
                # Hasta que se cumpla condicion de venta dando vueltas
                while 1:
                    aPairData = cliente.ticker(pair[0])
                    print(pair[0] + ' **** ' +'Precio Activo: ' + aPairData['data']['last'] + ' / T.PROFIT: ' + str(dProfit) + ' S.LOSS:  ' + str(dLost) + ' **** ' + 'LONG'  + ' GANANCIAS TOTALES: ' +  str(dBeneficios))
                    print('.........................................................................')   
                    if(float(aPairData['data']['last'])  > dProfit or dLost > float(aPairData['data']['last'])):
                        dBalance = (dUsdtSim * iLeverage) / float(aPairData['data']['last'])  
                        if(dBalance > dCantidad):
                            dResultado1 = dBalance - dCantidad
                            dResultado2 = dResultado1 * float(aPairData['data']['last'])  
                            dBeneficios = dBeneficios - dResultado2
                        else:
                            dResultado1 = dCantidad - dBalance    
                            dResultado2 = dResultado1 * float(aPairData['data']['last'])  
                            dBeneficios = dBeneficios + dResultado2                            
                        break                      
                    #------------------------------------------------------
                    time.sleep(1)        
            else:
                dProfit =  float(aPairData['data']['last'])  - ((float(aPairData['data']['last']) * dTakeProf) / 100)
                dLost = float(aPairData['data']['last'])   + ((float(aPairData['data']['last']) * dStop) / 100)
                # result = orderApi.place_order(pair[0], marginCoin='USDT', size=1, side='open_short', orderType='market')       
                while 1:
                    aPairData = cliente.ticker(pair[0])
                    print(pair[0] + ' **** ' +'Precio Activo: ' + aPairData['data']['last'] + ' / T.PROFIT: ' + str(dProfit) + ' S.LOSS:  ' + str(dLost) + ' **** ' + 'SHORT'  + ' GANANCIAS TOTALES: ' +  str(dBeneficios))
                    print('.........................................................................')   
                    if(float(aPairData['data']['last']) < dProfit or dLost < float(aPairData['data']['last'])):
                        dBalance = (dUsdtSim * iLeverage) / float(aPairData['data']['last'])  
                        if(dBalance > dCantidad):
                            dResultado1 = dBalance - dCantidad
                            dResultado2 = dResultado1 * float(aPairData['data']['last'])  
                            dBeneficios = dBeneficios + dResultado2
                        else:
                            dResultado1 = dCantidad - dBalance    
                            dResultado2 = dResultado1 * float(aPairData['data']['last'])  
                            dBeneficios = dBeneficios - dResultado2                            
                        break
                    #------------------------------------------------------
                    time.sleep(1)                              
            print('Beneficios dia: ' + str(dBeneficios))
            print('.........................................................................')                        
        return 1
