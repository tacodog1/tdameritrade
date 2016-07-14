# tdameritrade
Basic python client implementation of TDAmeritrade API

TD Ameritrade provides a developer API which supports a variety of features including historical pricing data, snapshot and streaming quotes, option chains, historical volatility, etc. This is a basic client implementation in python along with a simple test example for snapshot quotes and option chains.

This is pre-Alpha level code and only implements a small portion of the TDA API. However, it is useful for my needs and I didn't see another python implementation on github, so I'm making it available. Please let me know if you are interested in using it.

Note that in order to access the TDA API you will need to have an API key provided by TDAmeritrade. If you don't have one please contact TDAmeritrade.

To use the tdapi_test.py example, provide your API key, username, and a ticker:
python tdapi_test.py YOUR_API_KEY someuser AMZN

