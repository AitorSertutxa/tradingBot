import numpy as np
import pandas as pd

def Get_DataFrameSoloCandlestick(klines):
    df = pd.DataFrame()    
    ValorTiempo = []
    ValorBajo = []
    ValorAlto = []
    ValorApertura = []
    ValorCierre = []
    ValorVolumen = []    
    #-------------------------------
    df = pd.DataFrame(columns=['time', 'low', 'high', 'open', 'close', 'volume'])  
    for i in range(0, len(klines)):
        ValorTiempo.append(klines[i][0])
        ValorBajo.append(klines[i][3])
        ValorAlto.append(klines[i][2])
        ValorApertura.append(klines[i][1])
        ValorCierre.append(klines[i][4])
        ValorVolumen.append(klines[i][5])    
    #-------------------------------    
    df['time'] = np.array(ValorTiempo)   
    df['low'] = np.array(ValorBajo).astype(np.float64)   
    df['high'] = np.array(ValorAlto).astype(np.float64)   
    df['open'] = np.array(ValorApertura).astype(np.float64)   
    df['close'] =np.array(ValorCierre).astype(np.float64)
    df['volume'] = np.array(ValorVolumen).astype(np.float64)    
    #-------------------------------
    return df