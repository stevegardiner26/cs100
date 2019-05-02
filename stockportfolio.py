class StockPortfolio:
    # A stock Portfolio is able to track investments held by a person using two pieces of information

    def __init__(self, name, stocks={}):
        self.name = name
        self.stocks = stocks

    def buyMore(self, ticker, shares):
        if ticker in self.stocks:
            self.stocks[ticker] += shares
        else:
            self.stocks[ticker] = shares

    def sellOff(self, ticker, shares):
        if ticker in self.stocks:
            if shares <= self.stocks[ticker]:
                self.stocks[ticker] -= shares
