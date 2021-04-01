from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Thread
from datetime import datetime,timedelta
from time import sleep
import csv


class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def historicalData(self, reqId, bar):
        s = 'test1'
        with open(s + '.csv', 'a+') as outfile:

            writer = csv.writer(outfile)
            output = [bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume]
            writer.writerow(output)


        print(bar)

def main(ib_app):
    contract = Contract()
    contract.symbol = "ACC"
    contract.secType = "STK"
    contract.exchange = "NSE"
    contract.currency = "INR"
    #contact.lastTradeDateOrContractMonth="201912

    #ib_app.reqHistoricalData(1, contact, '20191230 15:30:00', "1 D", "1 min", "MIDPOINT", 0, 1, False, {})


    stime = datetime(year=2017, month=1, day=2)      # enter the starting date 

    etime = stime.replace(year=2017, month=1, day=27)                    # enter the last date
    #print(stime)
    #print(etime)

    holiday_list = ['26-Jan-2017','24-Feb-2017','13-Mar-2017','04-Apr-2017', '14-Apr-2017', '01-May-2017', '26-Jun-2017',
                    '15-Aug-2017','25-Aug-2017', '02-Oct-2017','20-Oct-2017', '25-Dec-2017', '26-Jan-2018','13-Feb-2018',
                    '02-Mar-2018', '29-Mar-2018', '30-Mar-2018','01-May-2018','15-Aug-2018', '22-Aug-2018', '13-Sep-2018',
                    '20-Sep-2018','02-Oct-2018','18-Oct-2018','08-Nov-2018', '23-Nov-2018','25-Dec-2018','04-Mar-2019',
                    '21-Mar-2019','17-Apr-2019','19-Apr-2019', '29-Apr-2019', '01-May-2019', '05-Jun-2019', '12-Aug-2019',
                    '15-Aug-2019', '02-Sep-2019', '10-Sep-2019', '02-Oct-2019', '08-Oct-2019',  '21-Oct-2019', '28-Oct-2019',
                    '12-Nov-2019', '25-Dec-2019'
                    ]

    while etime >= stime:
        dt = stime.strftime('%Y%m%d %H:%M:%S')
        weekend = stime.strftime('%A')
        holiday_dt = stime.strftime('%d-%b-%Y')

        if weekend == 'Friday':
            #print(weekend)
            stime = stime + timedelta(days=2)
        elif holiday_dt in holiday_list:
            #print(holiday_dt)
            stime = stime + timedelta(days=1)
        else:
            ib_app.reqHistoricalData(1, contract, dt, "1 D", "1 min", "MIDPOINT", 0, 1, False, {})
            #or app.reqHistoricalData(1, contract, dt, length, barSize, "TRADES", 1, 1, False, [])
            sleep(5)
            stime = stime + timedelta(days=1)
            


if __name__ == "__main__":
    app = TestApp()
    app.connect("127.0.0.1", xxxx, 0)           # port number 
    t = Thread(target=app.run)
    t.start()
    main(app)
