import numpy as np
import pandas as pd

#--------------------------------------------------------------------
#------------------ EHLER INSTANTANEOUS TRENDLINE  ------------------
#--------------------------------------------------------------------
def ehlers_instantaneous_trendline_v2(data, alpha=0.07):
    itrend = pd.Series(0.0, index=data.index)
    trigger = pd.Series(0.0, index=data.index)
    
    for i in range(2, len(data)):
        if i < 7:
            itrend[i] = (data[i] + (2 * data[i-1]) + data[i-2]) / 4
        else:
            itrend[i] = ((alpha - (alpha ** 2 / 4)) * data[i]) + (0.5 * alpha ** 2 * data[i-1]) - \
                        ((alpha - (0.75 * alpha ** 2)) * data[i-2]) + (2 * (1 - alpha) * itrend[i-1]) - \
                        ((1 - alpha) ** 2 * itrend[i-2])
            
        trigger[i] = 2 * itrend[i] - itrend[i-2]
        
    sig = np.where(trigger > itrend, 1, np.where(trigger < itrend, -1, 0))
    itColor = np.where(sig > 0, 'g', np.where(sig < 0, 'r', 'k'))
    
    return itrend, trigger, sig, itColor
 
#--------------------------------------------------------------------
#------------------ MEDIA MOVIL EXPONENCIAL  ------------------------
#--------------------------------------------------------------------
def calculate_ema(prices, days, smoothing=2):
    ema = [sum(prices[:days]) / days]
    for price in prices[days:]:
        ema.append((price * (smoothing / (1 + days))) + ema[-1] * (1 - (smoothing / (1 + days))))
    return ema

#--------------------------------------------------------------------
#------------------ RSI ESTOCASTICO ---------------------------------
#--------------------------------------------------------------------

def stoch_rsi_tradingview(ohlc: pd.DataFrame, period=14, smoothK=3, smoothD=3):  
    # Calculate RSI
    rsi = rsi_tradingview(ohlc, period=period)
    #-------------------------------------------
    # Calculate StochRSI
    rsi = pd.Series(rsi)
    stochrsi  = (rsi - rsi.rolling(period).min()) / (rsi.rolling(period).max() - rsi.rolling(period).min())
    stochrsi_K = stochrsi.rolling(smoothK).mean()
    stochrsi_D = stochrsi_K.rolling(smoothD).mean()
    #-------------------------------------------
    return rsi, stochrsi_K * 100, stochrsi_D * 100

#--------------------------------------------------------------------
#------------------ RSI ---------------------------------------------
#--------------------------------------------------------------------

def rsi_tradingview(ohlc: pd.DataFrame, period: int = 14) -> pd.Series:
    delta = ohlc["close"].diff()
    up, down = delta.copy(), delta.copy() 
    #-------------------------------------------
    up[up < 0] = 0
    down[down > 0] = 0
    #-------------------------------------------
    _gain = up.ewm(com=(period - 1), min_periods=period).mean()
    _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()
    #-------------------------------------------
    RS = _gain / _loss
    #-------------------------------------------
    return pd.Series(100 - (100 / (1 + RS)), name="RSI")