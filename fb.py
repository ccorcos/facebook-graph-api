import urllib2
import json

token = "CAACEdEose0cBACAFJb5jHvsv3xNl2d2dJNsuhtJSSu1crFdntFLt6ZC2SgIjl4clfmssASZBTHrbUK6dScM2gJxZCPxMasZAsTcTjdJ3UI2BmTu9HRoc06SW6XXMMHuFBza471FcyeO1w9OrFLxN6qtQGRUPGNF41iLIdoZApZA3P5KZAwvLsQAdV8YcKLRm0UZD"

def getAll(url):
    resp = json.loads(urllib2.urlopen(url).read())
    if 'data' in resp:
        if len(resp['data']) == 0:
            return []
        elif 'next' in resp['paging']:
            rest = getAll(resp['paging']['next'])
            return resp['data'] + rest
        else:
            return resp['data']
    else:
        return resp

def fb(query):
    pre = "https://graph.facebook.com/v1.0/"
    # query = "me/friends"
    post = "?access_token="
    url = pre + query + post + token
    return getAll(url)