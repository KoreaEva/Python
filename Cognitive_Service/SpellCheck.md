#Spell Check API 

mode (optional) string Mode of spellcheck:
Proof - Meant to provide Office Word like spelling corrections. It can correct long queries, provide casing corrections and suppresses aggressive corrections.
Spell - Meant to provide Search engine like spelling corrections. It will correct small queries(up to length 9 tokens) without any casing changes and will be more optimized (perf and relevance) towards search like queries.
or this demo.

[API Key Reference](https://dev.cognitive.microsoft.com/docs/services/56e73033cf5ff80c2008c679/operations/56e73036cf5ff81048ee6727)

~~~~
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'mode': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("POST", "/bing/v5.0/spellcheck/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~