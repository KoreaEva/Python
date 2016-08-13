########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '819d088fe5dd4613978973a618731ebb',
}

params = urllib.parse.urlencode({
})

body = "{url:'http://postfiles8.naver.net/20160811_247/warit_1470912730734NnC7q_JPEG/1.jpg?type=w3'}" #쯔위
#body = "{url:'http://postfiles15.naver.net/20160811_206/warit_1470912730966kjw5g_JPEG/5.jpg?type=w3'}" #빵꾸똥꾸
#body = "{url:'http://postfiles14.naver.net/20160811_221/warit_1470912731141wUul4_GIF/1443426009_88.gif?type=w3'}" #먹방
#body = "{url:'http://postfiles7.naver.net/20160811_102/warit_1470912731567lH2Uo_JPEG/WP_20130801_005.jpg?type=w3'}" #주애
#body = "{url:'http://postfiles1.naver.net/20160811_272/warit_1470912731783dbr4q_JPEG/IMG_1905.JPG?type=w3'}" #예진
#body = "{url:'http://postfiles11.naver.net/20160811_154/warit_1470912731919rt1Fj_JPEG/01_7.jpg?type=w3'}" #사티아

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################