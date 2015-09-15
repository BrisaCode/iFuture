#usr/bin/env python
# coding: utf-8
# By Thiago Silva

from yfinancefetcher import *;

def main():
    stockList = ["GOOG", "PETR3.SA", "ARZZ3.SA", "CIEL3.SA", "BTOW3.SA", "ELPL3.SA", "GFSA3.SA", "CMIG4.SA", "CMIG3.SA"]
    fetcher = YFinanceFetcher();
    
    for stock in stockList:
        #stock+='.bvmf'
        print stock
        print "Day High :" + str(fetcher.getStock(stock, 'h'))
        print "Day Low: " + str(fetcher.getStock(stock, 'l'))
        print "Previous Close: " + str(fetcher.getStock(stock, 'p'))
        print "P/E Ratio " + str(fetcher.getStock(stock, 'r'))
        print "BAV (Bid, Ask, Volume): " + str(fetcher.getStock(stock, 'bav'))
        print ""

if __name__ == '__main__':
    main()
