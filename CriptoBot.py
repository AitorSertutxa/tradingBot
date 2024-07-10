import FuncUtilesBit as fuB
import FuncUtilesKu as fuK
import winsound as wi
import time
import Config
#--------------------------------------------
#Variables Globales
BitGet = 1
kuCoin = 0
Binance = 0
aPareDatuak = []
aErantzunPareak = []
aGainetikoPareak = []
aErantzunPareak = []
iResponse = 0
iTimeResponse = 1
#---------------------------------------------
#VARIABLES A INTRODUCIR AL GUSTO
iNumMonedas = 30                        #Cantidad de Monedas a analizar ordenadas por las ganadoras del dia
iRangoVela = 1                          #Rango de tiempo de cada vela -> 1 / 1 HORA || 15 / 15 MINS. || 30 / 30 MINS. 
iApalancamiento = 10                     #Apalancamiento que se quiera
iApalancamientoBtcEth = 25               #Apalancamiento diferente para BITCOIN Y ETHEREUM
dTakeProfit = 0.7                        #Take Profit que se quiera añadir
dStopLoss = 1                            #Stop loss que se quiera introducir
dUsdtSim = 50                            #Cantidad de USDT para simular y comprobar funcionamiento
#--------------------------------------------
# Bot 
while 1:
    if(BitGet == 1):        
        #iTimeResponse = fuB.Get_HoraValida(iRangoVela)
        if(iTimeResponse == 1):
            aPareDatuak = fuB.Get_PareDatuak()
            aPareak = fuB.Get_PareakETHBTCKenduta(aPareDatuak)
            aGainetikoPareak = fuB.Get_GainetikoPareak(aPareak, iNumMonedas)
            aErantzunPareak = fuB.Get_PareDefinitiboak(aGainetikoPareak, iRangoVela)
            if(len(aErantzunPareak) > 0):
                if(aErantzunPareak[0][0] != 'BTCUSDT_UMCBL' and aErantzunPareak[0][0] != 'ETHUSDT_UMCBL'):
                    iResponse = fuB.ErosketaTxanpona(aErantzunPareak[0], iApalancamiento, dTakeProfit, dStopLoss, dUsdtSim)
                else:
                    iResponse = fuB.ErosketaTxanpona(aErantzunPareak[0], iApalancamientoBtcEth, dTakeProfit, dStopLoss, dUsdtSim)
            else:
                print('NO HAY NINGUNA MONEDA QUE CUMPLA CON LOS REQUISITOS ADECUADOS.')
                print('.........................................................................')    
        else:
            print('NO SE ESTA EN EL RANGO DE HORA REQUERIDO; NADA QUE MOSTRAR.')
            print('.........................................................................')    
            time.sleep(60)
    elif(kuCoin == 1):
        aPareDatuak = fuK.Get_PareDatuak()
        aPareak = fuK.Get_PareakETHBTCKenduta(aPareDatuak)
        aGainetikoPareak = fuK.Get_GainetikoPareak(aPareak, iNumMonedas)
        aErantzunPareak = fuK.Get_PareDefinitiboak(aGainetikoPareak)            
    # Ateratzen ditugu emaitzak
    # for i in range(0, len(aErantzunPareak)):
    #     wi.Beep(2500, 100)
    #     print(str(aErantzunPareak[i][0]) + '---' + str(aErantzunPareak[i][1]) + '---' + str(aErantzunPareak[i][2]) + '---' + str(aErantzunPareak[i][3]) + '---' + str(aErantzunPareak[i][4]) + '---' + str(aErantzunPareak[i][5]) + '---' + str(aErantzunPareak[i][6]))
    # print('.........................................................................')    