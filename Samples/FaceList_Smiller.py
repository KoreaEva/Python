########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '22583463d6cb490d866c5ac76aeb50f3',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/findsimilars?%s" % params, "{'faceId':'e10cc8a8-f292-43a8-ac0e-84255728be92','faceListId':'test1','maxNumOfCandidatesReturned':10}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################