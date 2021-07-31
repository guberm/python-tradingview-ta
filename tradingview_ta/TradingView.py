import os
from main import TA_Handler, Interval, Exchange


#https://python-tradingview-ta.readthedocs.io/en/latest/usage.html

stock_symb = 'FRII'
intervalO = 'monthly'
market = 'TSX'
intervalN = ''
country = 'canada'

if intervalO == "daily":
    intervalN = Interval.INTERVAL_1_DAY
if intervalO == "weekly":
    intervalN = Interval.INTERVAL_1_WEEK
if intervalO == "monthly":
    intervalN = Interval.INTERVAL_1_MONTH

#if not market:
#    r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol=' + stock_symb + '&token=c1oaehq37fkqrr9sebhg')
#    n = str(r.json())
#    n = n.replace("'","\"")
#    y = json.loads(str(n))
#    e = y['exchange']
#    ee = e.split(' ')
#    market = ee[0]



handler = TA_Handler(
    symbol=stock_symb,
    screener=country,
    exchange=market,
    #interval=Interval.INTERVAL_1_MINUTE
    #interval=Interval.INTERVAL_5_MINUTES
    #interval=Interval.INTERVAL_15_MINUTES
    #interval=Interval.INTERVAL_1_HOUR
    #interval=Interval.INTERVAL_4_HOURS
    #interval=Interval.INTERVAL_1_DAY
    #interval=Interval.INTERVAL_1_WEEK
    #interval=Interval.INTERVAL_1_MONTH
    interval=intervalN
)

analysis = handler.get_analysis()
print(str(analysis.summary))


#print("oscillators: " + str(analysis.oscillators))
#print("moving_averages: " + str(analysis.moving_averages))