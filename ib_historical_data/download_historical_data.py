from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def historicalData(self, reqId, bar):

        print("HistoricalData: ", reqId,
              "Date ;", bar.date,
             "open: ", bar.open,
              "High :", bar.high,
              "low :", bar.low,
             "Close :", bar.close,
             "Volume :", bar.volume,
             "Count :", bar.barCount,
             "WAP:", bar.average)


def main():
    app = TestApp()
    app.connect("127.0.0.1", 7499, 0)
    contact = Contract()
    contact.symbol = "ACC"
    contact.secType = "STK"
    contact.exchange = "NSE"
    contact.currency = "INR"
    app.reqHistoricalData(1, contact, "20191230 15:30:00", "1 M", "1 min", "MIDPOINT", 0, 1, False, []) # user specific date and time
    app.run()


if __name__ == "__main__":
    main()
