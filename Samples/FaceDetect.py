########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '22583463d6cb490d866c5ac76aeb50f3',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    #'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,facialHair,glasses',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{url:'http://postfiles14.naver.net/20160530_253/warit_1464560752259sBYzQ_JPEG/IMG_1100.jpg?type=w3'}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)

    f = open('c:/result.json', 'w')
    f.write('test')
    f.close()

    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################