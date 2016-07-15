########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '02669de042544b1e8a2bdfccfbf30a4f',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Categories',
    'details': '',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, "{url:'http://postfiles6.naver.net/20160530_117/warit_1464561113138dr7yL_JPEG/IMG_1094.jpg?type=w3'}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################