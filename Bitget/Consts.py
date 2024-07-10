
# http header
CONTENT_TYPE = 'Content-Type'
ACCESS_KEY = 'ACCESS-KEY'
ACCESS_SIGN = 'ACCESS-SIGN'
ACCESS_TIMESTAMP = 'ACCESS-TIMESTAMP'
ACCESS_PASSPHRASE = 'ACCESS-PASSPHRASE'
APPLICATION_JSON = 'application/json'

# header key
ACEEPT = 'Accept'
COOKIE = 'Cookie'
LOCALE = 'locale='

KLINE_INTERVAL_1MINUTE = 60
KLINE_INTERVAL_3MINUTE = 180
KLINE_INTERVAL_5MINUTE = 300
KLINE_INTERVAL_15MINUTE = 900
KLINE_INTERVAL_30MINUTE = 1800
KLINE_INTERVAL_1HOUR = 3600
KLINE_INTERVAL_2HOUR = '2h'
KLINE_INTERVAL_4HOUR = '4h'
KLINE_INTERVAL_6HOUR = '6h'
KLINE_INTERVAL_8HOUR = '8h'
KLINE_INTERVAL_12HOUR = '12h'
KLINE_INTERVAL_1DAY = '1d'
KLINE_INTERVAL_3DAY = '3d'
KLINE_INTERVAL_1WEEK = '1w'
KLINE_INTERVAL_1MONTH = '1M'

# method
GET = "GET"
POST = "POST"
DELETE = "DELETE"

# Base Url
API_URL = 'https://api.bitget.com'

# ws Url
CONTRACT_WS_URL = 'wss://ws.bitget.com/mix/v1/stream'



# ########################################
# ##############【spot url】###############
# ########################################

SPOT_PUBLIC_V1_URL = '/api/spot/v1/public'
SPOT_MARKET_V1_URL = '/api/spot/v1/market'
SPOT_ACCOUNT_V1_URL = '/api/spot/v1/account'
SPOT_ORDER_V1_URL = '/api/spot/v1/trade'
SPOT_WALLET_V1_URL = '/api/spot/v1/wallet'

# ########################################
# ##############【mix url】################
# ########################################

MIX_MARKET_V1_URL = '/api/mix/v1/market'
MIX_ACCOUNT_V1_URL = '/api/mix/v1/account'
MIX_POSITION_V1_URL = '/api/mix/v1/position'
MIX_ORDER_V1_URL = '/api/mix/v1/order'
MIX_PLAN_V1_URL = '/api/mix/v1/plan'
MIX_TRACE_V1_URL = '/api/mix/v1/trace'


BROKER_ACCOUNT_V1_URL = '/api/broker/v1/account'
BROKER_MANAGE_V1_URL = '/api/broker/v1/manage'

SUBSCRIBE = 'subscribe'
UNSUBSCRIBE = 'unsubscribe'
LOGIN = 'login'

GET = 'GET'
REQUEST_PATH = '/user/verify'

SERVER_TIMESTAMP_URL='/api/spot/v1/public/time'