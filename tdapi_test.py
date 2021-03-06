from tdapi import TDAmeritradeAPI
import getpass
import argparse
import pandas as pd
import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sourceid', help="API key provided by TD Ameritrade")
    parser.add_argument('userid')
    parser.add_argument('ticker', default='AMZN')
    args = parser.parse_args()

    #print args.sourceid
    #print args.userid

    if not (args.sourceid and args.userid):
        parser.print_help()

    pwd = getpass.getpass()
    td = TDAmeritradeAPI(args.sourceid)
    td.login(args.userid, pwd)
    print('Getting snapshot quote for %s' % args.ticker)
    quoteList = td.getSnapshotQuote([args.ticker],'stock',True)
    print(quoteList[args.ticker])

    print('Getting price history')
    dt = datetime.datetime.now()
    df = td.getPriceHistory(args.ticker, intervalType='DAILY', intervalDuration='1', periodType='MONTH',
        period='6', startdate=None, enddate=dt.strftime('%Y%m%d'), extended=None)
    print(df)

    print('Getting binary option chain for %s' % args.ticker)
    chain = td.getBinaryOptionChain(args.ticker)
    print('Returned %d contracts. First 10:' % len(chain))
    for option in chain[:10]:
        print(option)

    td.logout()


if __name__ == '__main__':
    main()
