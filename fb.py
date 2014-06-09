import urllib2
import json

token = "CAACEdEose0cBACOPH1Tmrks9A66GehBIvVKSw7Lz3EL3cA3IGZBCIkTVuWxJ9RsJMKouzvHkWDG7MLslobfAb0gil5ItvPADXOXfew1MmZAzolMzFZBKZCnQUroXeSyC5tW4iXLZAkGPNSDZAbjzEEvZBlpcMpaEZBoddTZBZBeJUpMBVNlRZBsCLT2q2VcNVbblcMZD"

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