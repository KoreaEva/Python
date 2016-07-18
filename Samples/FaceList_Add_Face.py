########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '22583463d6cb490d866c5ac76aeb50f3',
}

params = urllib.parse.urlencode({
    # Request parameters
    #'userData': '{string}',
    #'targetFace': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    #conn.request("POST", "/face/v1.0/facelists/test1/persistedFaces?%s" % params, "{url:'https://scontent-hkg3-1.xx.fbcdn.net/t31.0-8/12068941_10207469425632295_4957511523235867823_o.jpg'}", headers)
    #conn.request("POST", "/face/v1.0/facelists/test1/persistedFaces?%s" % params, "{url:'https://scontent-hkg3-1.xx.fbcdn.net/v/t1.0-9/10613008_10206103705730151_3481211037983654159_n.jpg?oh=0ce3eb2697b70f1b41920d9c43ca7913&oe=57F2410C'}", headers)
    #conn.request("POST", "/face/v1.0/facelists/test1/persistedFaces?%s" % params, "{url:'https://scontent-hkg3-1.xx.fbcdn.net/t31.0-8/10700695_10204641056044823_5842444176578171694_o.jpg'}", headers)
    #conn.request("POST", "/face/v1.0/facelists/test1/persistedFaces?%s" % params, "{url:'https://scontent-hkg3-1.xx.fbcdn.net/t31.0-8/884544_10203491971278422_8237786656142135210_o.jpg'}", headers)
    #conn.request("POST", "/face/v1.0/facelists/test1/persistedFaces?%s" % params, "{url:'https://scontent-hkg3-1.xx.fbcdn.net/v/t1.0-9/1467388_10202312828320585_1732102552_n.jpg?oh=0950b86256357e11b89f6ba9585d8593&oe=581E6F1F'}", headers)
    #conn.request("POST", "/face/v1.0/facelists/test1/persistedFaces?%s" % params, "{url:'https://scontent-hkg3-1.xx.fbcdn.net/v/t1.0-9/406950_4807351380175_280570573_n.jpg?oh=593a834d97d4760331e9341137064c9e&oe=58319FCE'}", headers)
    #conn.request("POST", "/face/v1.0/facelists/test1/persistedFaces?%s" % params, "{url:''}", headers)
    #conn.request("POST", "/face/v1.0/facelists/test1/persistedFaces?%s" % params, "{url:''}", headers)

    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

########################################################################
