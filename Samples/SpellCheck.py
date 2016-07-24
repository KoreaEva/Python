########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': '5144df8ca57b42daa970dda97ee8e7e0',
}

params = urllib.parse.urlencode({
    # Request parameters
    'mode': 'spell',
})

try:
    conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("POST", "/bing/v5.0/spellcheck/?%s" % params, "Text=Bill+Gatas", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
