import datetime
import base64
import httplib
import urllib
import getpass
import binascii
import time
import array
import string
import math, types
from struct import pack, unpack
from xml.etree import ElementTree
import logging
import pandas

class StockQuote():
    symbol = None
    description = None
    bid = None
    ask = None
    bidAskSize = None
    last = None
    lastTradeSize = None
    lastTradeDate = None
    openPrice = None
    highPrice = None
    lowPrice = None
    closePrice = None
    volume = None
    yearHigh = None
    yearLow = None
    realTime = None
    exchange = None
    assetType = None
    change = None
    changePercent = None

    def __init__(self, elementTree):
        i = elementTree
        self.symbol = i.findall('symbol')[0].text
        self.description = i.findall('description')[0].text
        self.bid = float(i.findall('bid')[0].text)
        self.ask = float(i.findall('ask')[0].text)
        self.bidAskSize = i.findall('bid-ask-size')[0].text
        self.last = float(i.findall('last')[0].text)
        self.lastTradeSize = i.findall('last-trade-size')[0].text
        self.lastTradeDate = i.findall('last-trade-date')[0].text
        self.openPrice = float(i.findall('open')[0].text)
        self.highPrice = float(i.findall('high')[0].text)
        self.lowPrice = float(i.findall('low')[0].text)
        self.closePrice = float(i.findall('close')[0].text)
        self.volume = float(i.findall('volume')[0].text)
        self.yearHigh = float(i.findall('year-high')[0].text)
        self.yearLow = float(i.findall('year-low')[0].text)
        self.realTime = i.findall('real-time')[0].text
        self.exchange = i.findall('exchange')[0].text
        self.assetType = i.findall('asset-type')[0].text
        self.change = float(i.findall('change')[0].text)
        self.changePercent = i.findall('change-percent')[0].text


    def __str__(self):
        s = ''
        for key in dir(self):
            if key[0] != '_':
                s += '%s: %s\n' % (key, getattr(self, key))
        return s

class OptionChainElement():

    quoteDateTime = None

    # Option Date Length - Short - 2
    # Option Date - String - Variable
    date = None
    # Expiration Type Length - Short - 2
    # Expiration Type - String - Variable (R for Regular, L for LEAP)
    expirationType = None
    # Strike Price - Double - 8
    strike = None

    # Standard Option Flag - Byte - 1 (1 = true, 0 = false)
    standardOptionFlag = None

    # Put/Call Indicator - Char - 2 (P or C in unicode)
    pcIndicator = None

    # Option Symbol Length - Short - 2
    # Option Symbol - String - Variable
    optionSymbol = None

    # Option Description Length - Short - 2
    # Option Description - String - Variable
    optionDescription = None

    # Bid - Double - 8
    bid = None

    # Ask - Double - 8
    ask = None

    # Bid/Ask Size Length - Short - 2
    # Bid/Ask Size - String - Variable
    baSize = None

    # Last - Double - 8
    last = None

    # Last Trade Size Length - Short - 2
    # Last Trade Size - String - Variable
    lastTradeSize = None

    # Last Trade Date Length - short - 2
    # Last Trade Date - String - Variable
    lastTradeDate = None

    # Volume - Long - 8
    volume = None

    # Open Interest - Integer - 4
    openInterest = None

    # RT Quote Flag - Byte - 1 (1=true, 0=false)
    rtQuoteFlag = None

    # Underlying Symbol length - Short 2
    # Underlying Symbol - String - Variable
    underlyingSymbol = None

    # Delta - Double- 8
    # Gamma - Double - 8
    # Theta - Double - 8
    # Vega - Double - 8
    # Rho - Double - 8
    delta = None
    gamma = None
    theta = None
    vega = None
    rho = None

    # Implied Volatility - Double - 8
    impliedVolatility = None

    # Time Value Index - Double - 8
    timeValueIndex = None

    # Multiplier - Double - 8
    multiplier = None

    # Change - Double - 8
    change = None

    # Change Percentage - Double - 8
    changePercentage = None

    # ITM Flag - Byte - 1 (1 = true, 0 = false)
    itmFlag = None

    # NTM Flag - Byte - 1 (1 = true, 0 = false)
    ntmFlag = None

    # Theoretical value - Double - 8
    theoreticalValue = None

    # Deliverable Note Length - Short - 2
    # Deliverable Note - String - Variable
    deliverableNote = None

    # CIL Dollar Amount - Double - 8
    cilDollarAmoubt = None

    # OP Cash Dollar Amount - Double - 8
    opCashDollarAmount = None

    # Index Option Flag - Byte - 1 (1 = true, 0 = false)
    indexOptionFlag = None

    # Number of Deliverables - Integer - 4
    deliverables = []   # (symbol, shares)
    # REPEATING block for each Deliverable
    #    Deliverable Symbol Length - Short - 2
    #    Deliverable Symbol - String - Variable
    #    Deliverable Shares - Integer - 4
    # END

    def setQuoteDateTime(self, quoteTime):
        #self.quoteDateTime = datetime.datetime.now()
        self.quoteDateTime = quoteTime

    def __str__(self):
        s = self.optionDescription
        if self.last != None:
            s += ' Last: $%.2f' % self.last
        else:
            s += ' Last: N/A'

        s += " (d: %f g: %f t: %f v: %f r: %f)" % \
            (self.delta, self.gamma, self.theta, self.vega, self.rho)
        #         date
        #         expirationType
        #         strike
        #         standardOptionFlag
        #         pcIndicator
        #         optionSymbol
        #         optionDescription
        #         bid
        #         ask
        #         baSize
        #         last
        #         lastTradeSize
        #         lastTradeDate
        #         volume
        #         openInterest
        #         rtQuoteFlag
        #         underlyingSymbol
        #         delta
        #         gamma
        #         theta
        #         vega
        #         rho
        #         impliedVolatility
        #         timeValueIndex
        #         multiplier
        #         change
        #         changePercentage
        #         itmFlag
        #         ntmFlag
        #         theoreticalValue
        #         deliverableNote
        #         cilDollarAmoubt
        #         opCashDollarAmount
        #         indexOptionFlag
        #         deliverables = []   # (symbol, shares)
        # REPEATING block for each Deliverable
        #    Deliverable Symbol Length - Short - 2
        #    Deliverable Symbol - String - Variable
        #    Deliverable Shares - Integer - 4
        return s

class HistoricalPriceBar():
    close = None
    high = None
    low = None
    open = None
    volume = None
    timestamp = None

    def __init__(self):
        pass

    def __str__(self):
        return '%f,%f,%f,%f,%f,%s' % (self.close, self.high, self.low, self.open, self.volume, self.timestamp)

class TDAmeritradeAPI():
    _sourceID = None    # Note - Source ID must be provided by TD Ameritrade
    _version = '0.1'
    _active = False
    _sessionID = ''

    def __init__(self, sourceID):
        self._sourceID = sourceID

    def isActive(self, confirm=False):
        if self._active == True:
            # Confirm with server by calling KeepAlive
            if confirm:
                if self.keepAlive() == False:
                    self.login()
                    # TODO: add more robust checking here to make sure we're really logged in
            return True
        else:
            return False

    def keepAlive(self):
        conn = httplib.HTTPSConnection('apis.tdameritrade.com')
        conn.request('POST', '/apps/100/KeepAlive?source=%s' % self._sourceID)
        response = conn.getresponse()
        #print response.status, response.reason

        #print 'Getting response data...'
        data = response.read()
        #print 'Data:',data
        conn.close()

        if data.strip() == 'LoggedOn':
            return True
        elif data.strip() == 'InvalidSession':
            return False
        else:
            #print 'Unrecognized response: %s' % data
            pass

    def login(self, login, password):
        logging.debug('[tdapi] Entered login()')
        params = urllib.urlencode({'source': self._sourceID, 'version': self._version})
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = urllib.urlencode({'userid': login,
                                 'password': password,
                                 'source': self._sourceID,
                                 'version': self._version})
        conn = httplib.HTTPSConnection('apis.tdameritrade.com')
        #conn.set_debuglevel(100)
        conn.request('POST', '/apps/100/LogIn?'+params, body, headers)

        response = conn.getresponse()
        if response.status == 200:
            self._active = True
        else:
            self._active = False
            return False

        # The data response is an XML fragment. Log it.
        data = response.read()
        logging.debug('Login response:\n--------'+data+'\n--------')
        conn.close()

        # Make sure the login succeeded. First look for <result>OK</result>
        element = ElementTree.XML(data)
        try:
            result = element.findall('result')[0].text
            if result == 'FAIL':
                self._active = False
                return False
            elif result == 'OK':
                self._active = True
            else:
                logging.error('Unrecognized login result: %s' % result)
                return False

            # Now get the session ID
            self._sessionID = element.findall('xml-log-in')[0].findall('session-id')[0].text

        except:
            logging.error('Failed to parse login response.')
            return False


    def logout(self):
        conn = httplib.HTTPSConnection('apis.tdameritrade.com')
        conn.request('POST', '/apps/100/LogOut?source=%s' % self._sourceID)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        self._active = False


    def getSessionID(self):
        return self._sessionID

    def getStreamerInfo(self, accountID=None):

        arguments = {'source': self._sourceID}
        if accountID != None:
            arguments['accountid'] = accountID
        params = urllib.urlencode(arguments)

        conn = httplib.HTTPSConnection('apis.tdameritrade.com')
        #conn.set_debuglevel(100)
        conn.request('GET', '/apps/100/StreamerInfo?'+params)
        response = conn.getresponse()
        #print response.status, response.reason
        data = response.read()
        conn.close()
        #print 'Read %d bytes' % len(data)

        # We will need to create an ElementTree to process this XML response
        # TODO: handle exceptions
        element = ElementTree.XML(data)
        # Process XML response
        streamerInfo = {}
        try:
            children = element.findall('streamer-info')[0].getchildren()
            for c in children:
                streamerInfo[c.tag] = c.text
        except e:
            #print 'Error: failed to parse streamer-info response: %s', e
            return False

        #print 'Received streamer-info properties: %s' % streamerInfo

        return streamerInfo


    def getSnapshotQuote(self, tickers, assetType, detailed=False):
        logging.info('[tdapi.getSnapshotQuote] Enter')
        if len(tickers) > 300:
            logging.error('TODO: divide in batches of 300')

        if assetType not in ['stock','option','index','mutualfund']:
            logging.error('getSnapshotQuote: Unrecognized asset type %s' % assetType)
            return []

        arguments = {'source': self._sourceID,
                        'symbol': string.join(tickers, ',')}
        params = urllib.urlencode(arguments)
        #print 'Arguments: ', arguments
        conn = httplib.HTTPSConnection('apis.tdameritrade.com')

        #conn.set_debuglevel(100)
        conn.request('GET', ('/apps/100/Quote;jsessionid=%s?' % self.getSessionID()) +params)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        logging.info('[tdapi.getSnapshotQuote] Read %d bytes' % len(data))

        quotes = {}
        # Perform basic processing regardless of quote type
        element = ElementTree.XML(data)
        try:
            result = element.findall('result')[0].text
            if result == 'FAIL':
                self._active = False
                return False
            elif result == 'OK':
                self._active = True
            else:
                logging.error('[tdapi.getSnapshotQuote] Unrecognized result: %s' % result)
                return {}

            # Now get the session ID
            #self._sessionID = element.findall('xml-log-in')[0].findall('session-id')[0].text

        except:
            logging.error('[tdapi.getSnapshotQuote] Failed to parse snapshot quote response.')
            return False
        if assetType == 'stock':
            try:
                quoteElements = element.findall('quote-list')[0].findall('quote')
                for i in quoteElements:
                    symbol = i.findall('symbol')[0].text
                    if detailed:
                        q = StockQuote(i)  # Create a quote object from etree
                        quotes[symbol] = q
                    else:
                        last = float(i.findall('last')[0].text)
                        quotes[symbol] = last

            except:
                logging.error('Failed to parse snapshot quote response')
                return {}

        else:
            logging.error('[tdapi.getSnapshotQuote] Asset type not supported: %s' % assetType)
        return quotes


    def getBinaryOptionChain(self, ticker):

        arguments = {'source': self._sourceID,
                        'symbol': ticker,
                        'range': 'ALL',
                        'quotes': 'true'
                    }
        params = urllib.urlencode(arguments)
        #print 'Arguments: ', arguments
        conn = httplib.HTTPSConnection('apis.tdameritrade.com')

        #conn.set_debuglevel(100)
        conn.request('GET', ('/apps/200/BinaryOptionChain;jsessionid=%s?' % self.getSessionID()) +params)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        #print 'Read %d bytes' % len(data)

        cursor = 0
        error =         unpack('b',  data[cursor:cursor+1])[0]
        cursor += 1
        # If there is an error, there will be an error length and corresponding error text
        if error != 0:
            errorLength =   unpack('>h', data[cursor:cursor+2])[0]
            cursor += 2
            #print 'Error length:', errorLength
            if errorLength > 0:
                errorText = data[cursor:cursor+errorLength]
                cursor += errorLength
                raise ValueError, '[getBinaryOptionChain] Error: %s' % errorText
        symbolLength = unpack('>h', data[cursor:cursor+2])[0]
        cursor += 2
        symbol = data[cursor:cursor+symbolLength]
        cursor += symbolLength
        #print 'Symbol: %s' % symbol
        symbolDescriptionLength = unpack('>h', data[cursor:cursor+2])[0]
        cursor += 2
        symbolDescription = data[cursor:cursor+symbolDescriptionLength]
        cursor += symbolDescriptionLength
        #print 'Symbol description: %s' % symbolDescription

        bid = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        ask = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        baSizeLength = unpack('>h', data[cursor:cursor+2])[0]
        cursor += 2
        baSize = data[cursor:cursor+baSizeLength]
        cursor += baSizeLength
        #print 'Bid: %f' % bid
        #print 'Ask: %f' % ask
        #print 'Bid/Ask Size: %s' % baSize

        last = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        #print 'Last: %f' % last
        open = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        #print 'Open: %f' % open
        high = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        #print 'High: %f' % high
        low = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        #print 'Low: %f' % low
        close = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        #print 'Close: %f' % close
        volume = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        #print 'Volume: %f' % volume
        change = unpack('>d', data[cursor:cursor+8])[0]
        cursor += 8
        #print 'Change: %f' % change

        rtFlag = unichr(unpack('>H', data[cursor:cursor+2])[0])
        cursor += 2
        #print 'Realtime/Delayed Flag: %s' % rtFlag

        qtLength = unpack('>H', data[cursor:cursor+2])[0]
        cursor += 2
        #print 'qtLength: %d' % qtLength
        quoteTime = data[cursor:cursor+qtLength]
        cursor += qtLength
        #print 'Quote time: %s' % quoteTime
        rowCount = unpack('>i', data[cursor:cursor+4])[0]
        cursor += 4
        #print 'Row count: %d' % rowCount

        optionChain = []
        for i in range(rowCount):
            #print 'Reading row %d' % i
            if cursor > len(data):
                print('Error! Read too much data')
                break

            o = OptionChainElement()
            optionChain.append(o)
            # Option Date Length - Short - 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Option Date - String - Variable
            o.optionDate = data[cursor:cursor+l]; cursor += l

            # Expiration Type Length - Short - 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Expiration Type - String - Variable (R for Regular, L for LEAP)
            o.expirationType = data[cursor:cursor+l]; cursor += l

            # Strike Price - Double - 8
            o.strike = unpack('>d', data[cursor:cursor+8])[0]; cursor += 8

            # Standard Option Flag - Byte - 1 (1 = true, 0 = false)
            o.standardOptionFlag = unpack('b',  data[cursor:cursor+1])[0]; cursor += 1

            # Put/Call Indicator - Char - 2 (P or C in unicode)
            o.pcIndicator = unichr(unpack('>H', data[cursor:cursor+2])[0]); cursor += 2

            # Option Symbol Length - Short - 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Option Symbol - String - Variable
            o.optionSymbol = data[cursor:cursor+l]; cursor += l

            # Option Description Length - Short - 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Option Description - String - Variable
            o.optionDescription = data[cursor:cursor+l]; cursor += l
            # Bid - Double - 8
            o.bid = unpack('>d', data[cursor:cursor+8])[0]; cursor += 8
            # Ask - Double - 8
            o.ask = unpack('>d', data[cursor:cursor+8])[0]; cursor += 8
            # Bid/Ask Size Length - Short - 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Bid/Ask Size - String - Variable
            o.baSize = data[cursor:cursor+l]; cursor += l
            # Last - Double - 8
            o.last = unpack('>d', data[cursor:cursor+8])[0]; cursor += 8

            # Last Trade Size Length - Short - 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Last Trade Size - String - Variable
            o.lastTradeSize = data[cursor:cursor+l]; cursor += l
            # Last Trade Date Length - short - 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Last Trade Date - String - Variable
            o.lastTradeDate = data[cursor:cursor+l]; cursor += l
            # Volume - Long - 8
            o.volume = unpack('>Q',data[cursor:cursor+8])[0]; cursor += 8

            # Open Interest - Integer - 4
            o.openInterest = unpack('>i', data[cursor:cursor+4])[0]; cursor += 4

            # RT Quote Flag - Byte - 1 (1=true, 0=false)
            o.rtQuoteFlag = unpack('b',  data[cursor:cursor+1])[0]; cursor += 1
            o.setQuoteDateTime(quoteTime)

            # Underlying Symbol length - Short 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Underlying Symbol - String - Variable
            o.underlyingSymbol = data[cursor:cursor+l]; cursor += l

            # Delta - Double- 8
            # Gamma - Double - 8
            # Theta - Double - 8
            # Vega - Double - 8
            # Rho - Double - 8
            # Implied Volatility - Double - 8
            # Time Value Index - Double - 8
            # Multiplier - Double - 8
            # Change - Double - 8
            # Change Percentage - Double - 8
            (o.delta, o.gamma, o.theta, o.vega, o.rho, o.impliedVolatility, o.tvIndex,
             o.multiplier, o.change, o.changePercentage) = \
                unpack('>10d', data[cursor:cursor+80]); cursor += 80


            # ITM Flag - Byte - 1 (1 = true, 0 = false)
            # NTM Flag - Byte - 1 (1 = true, 0 = false)
            (o.itmFlag, o.ntmFlag) = unpack('2b', data[cursor:cursor+2]); cursor += 2

            # Theoretical value - Double - 8
            o.theoreticalValue = unpack('>d', data[cursor:cursor+8])[0]; cursor += 8

            # Deliverable Note Length - Short - 2
            l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
            # Deliverable Note - String - Variable
            o.deliverableNote = data[cursor:cursor+l]; cursor += l

            # CIL Dollar Amount - Double - 8
            # OP Cash Dollar Amount - Double - 8
            (o.cilDollarAmount, o.opCashDollarAmount) = \
                unpack('>2d', data[cursor:cursor+16]); cursor += 16
            # Index Option Flag - Byte - 1 (1 = true, 0 = false)
            o.indexOptionFlag = unpack('b', data[cursor:cursor+1])[0]; cursor += 1
            # Number of Deliverables - Integer - 4
            numDeliverables = unpack('>i', data[cursor:cursor+4])[0]; cursor += 4

            for j in range(numDeliverables):
                # REPEATING block for each Deliverable
                #    Deliverable Symbol Length - Short - 2
                l = unpack('>h', data[cursor:cursor+2])[0]; cursor += 2
                #    Deliverable Symbol - String - Variable
                s = data[cursor:cursor+l]; cursor += l
                #    Deliverable Shares - Integer - 4
                o.deliverables.append((s, unpack('>i', data[cursor:cursor+4])[0])); cursor += 4
            # END
            #print o

            # Change all "nan" to None to make sure the oce is serializable
            for k in o.__dict__.keys():
                if (type(o.__dict__[k]) == types.FloatType) and math.isnan(o.__dict__[k]):
                    logging.info('[tdapi.getBinaryOptionChain] Converting o[%s]=nan to None' % (k))
                    o.__dict__[k] = None

        return optionChain



    def getPriceHistory(self, ticker, intervalType='DAILY', intervalDuration='1', periodType='MONTH',
                        period='1', startdate=None, enddate=None, extended=None):


        validPeriodTypes = [
            'DAY',
            'MONTH',
            'YEAR',
            'YTD'
            ]

        validIntervalTypes = {
            'DAY':      ['MINUTE'],
            'MONTH':    ['DAILY', 'WEEKLY'],
            'YEAR':     ['DAILY', 'WEEKLY', 'MONTHLY'],
            'YTD':      ['DAILY', 'WEEKLY']
            }

        arguments = {'source': self._sourceID,
                        'requestidentifiertype': 'SYMBOL',
                        'requestvalue': ticker,
                        'intervaltype': intervalType,
                        'intervalduration': intervalDuration,
                        'period': period,
                        'periodtype':periodType,
                        'startdate':startdate,
                        'enddate':enddate
                    }
        # TODO: build params conditionally based on whether we're doing period-style request
        # TODO: support start and end dates
        validArgs = {}
        for k in arguments.keys():
            if arguments[k] != None:
                validArgs[k] = arguments[k]
        params = urllib.urlencode(validArgs)
        #print 'Arguments: ', validArgs

        logging.getLogger("requests").setLevel(logging.WARNING)
        conn = httplib.HTTPSConnection('apis.tdameritrade.com')
        conn.set_debuglevel(0)

        conn.request('GET', '/apps/100/PriceHistory?'+params)
        response = conn.getresponse()
        if response.status != 200:
            raise ValueError, response.reason
        #print response.status, response.reason
        data = response.read()
        conn.close()
        #print 'Read %d bytes' % len(data)

        # The first 15 bytes are the header
        # DATA              TYPE        DESCRIPTION
        # 00 00 00 01       4 bytes     Symbol Count =1
        # 00 04             2 bytes     Symbol Length = 4
        # 41 4D 54 44       4 bytes     Symbol = AMTD
        # 00                1 byte      Error code = 0 (OK)
        # 00 00 00 02       4 bytes     Bar Count = 2

        cursor = 0
        symbolCount =   unpack('>i', data[0:4])[0]
        #print('Symbol count =0x%x' % symbolCount)
        if symbolCount > 1:
            fp = open('tdapi_debug_dump','w')
            fp.write(data)
            fp.close()
            raise ValueError, 'Error - see tdapi_debug_dump'

        symbolLength =  unpack('>h', data[4:6])[0]
        #print 'Symbol length:', symbolLength
        cursor = 6
        symbol =        data[cursor:cursor+symbolLength]
        #print 'Symbol: ', symbol
        cursor += symbolLength
        error =         unpack('b',  data[cursor:cursor+1])[0]
        cursor += 1
        # If there is an error, there will be an error length and corresponding error text
        if error != 0:
            errorLength =   unpack('>h', data[cursor:cursor+2])[0]
            # TODO: verify that this is correct below -- advance cursor for error length
            cursor += 2
            #print 'Error length:', errorLength
            if errorLength > 0:
                errorText = data[cursor:cursor+errorLength]
                cursor += errorLength
                #print '[PriceHistory] Error:', errorText
                raise ValueError, '[getPriceHistory] Error: %s' % errorText

        barCount =      unpack('>i', data[cursor:cursor+4])[0]
        cursor += 4
        #print 'Bar count:', barCount
        #print 'Trying to read %d bars starting at byte %d' % (barCount, cursor)

        # TODO: Add more rigorous checks on header data

        # Now we need to extract the bars
        bars = []

        for i in range(barCount):
            # Make sure we still have enough data for a bar and a terminator (note only one terminator at the end)
            if cursor + 28 > len(data):
                raise ValueError, 'Trying to read %d bytes from %d total!' % (cursor+58, len(data))
            C     = unpack('>f', data[cursor:cursor+4])[0]
            cursor += 4
            H      = unpack('>f', data[cursor:cursor+4])[0]
            cursor += 4
            L       = unpack('>f', data[cursor:cursor+4])[0]
            cursor += 4
            O      = unpack('>f', data[cursor:cursor+4])[0]
            cursor += 4
            V    = unpack('>f', data[cursor:cursor+4])[0] * 100.0
            cursor += 4
            #T = time.gmtime(float(unpack('>Q',data[cursor:cursor+8])[0]) / 1000.0) # Returned in ms since the epoch
            T = datetime.datetime.utcfromtimestamp(float(unpack('>Q',data[cursor:cursor+8])[0]) / 1000.0) # Returned in ms since the epoch
            cursor += 8
            bars.append((O,H,L,C,V,T))

        # Finally we should see a terminator of FF
        if data[cursor:cursor+2] != '\xff\xff':
            raise ValueError, 'Did not find terminator at hexdata[%d]!' % cursor

        df = pandas.DataFrame(data=bars, columns=['open','high','low','close','volume','timestamp'])

        return df
