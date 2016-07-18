import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '02669de042544b1e8a2bdfccfbf30a4f',
}

params = urllib.parse.urlencode({
    # Request parameters
    'language': 'unk',
    'detectOrientation ': 'true',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/ocr?%s" % params, "{url:'https://i-msdn.sec.s-msft.com/dynimg/IC847457.jpeg'}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))