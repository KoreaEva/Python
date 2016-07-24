########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b64b37b5dd5a49689d492a01a36435e8',
}

params = urllib.parse.urlencode({
    # Request parameters
    'numberOfLanguagesToDetect': '1',
})

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/languages?%s" % params, "{'documents': [{'id': 'test001','text': 'I Love You'}]}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################