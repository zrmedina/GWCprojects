# Imports

import tweepy
# Keys and Access Tokens

CONSUMER_KEY    = 'ROtKGoH34N4kUOX5IxBOjnZGX'
CONSUMER_SECRET = '1AVhqg1zvnrf6n6xR323Fa5Z4oX2ZGuU3zAvrNwnqcbMIopoCn'

ACCESS_TOKEN    = '1017154683746390016-DutDRxeqlB6LPJGpXB2GlMwY0rpcyq'
ACCESS_SECRET   = '5WHclQZQz89Cd9XT6KEyTq7gdUFN2Uy3v2cEOPOH2RQxN'

# Authentication

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status

api.update_status("In hoc signo vinces")
