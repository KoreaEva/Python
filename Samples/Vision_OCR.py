import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '4a13d8c8170c4388932571752f455e13',
}

params = urllib.parse.urlencode({
    # Request parameters
    'language': 'unk',
    'detectOrientation ': 'true',
})

body = "{url:'http://postfiles12.naver.net/20160811_203/warit_1470918044092RofNM_JPEG/1_XjHSP02.jpg?type=w3'}"

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))