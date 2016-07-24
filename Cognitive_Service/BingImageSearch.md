#Bing Image Search API
The Image Search API lets partners send a search query to Bing and get back a list of relevant images. Note you should call the Image API if you need image content only. If you need other content such as news and webpages in addition to images, you must call the Search API which includes images in the response. You must display the images in the order provided in the response.

Image Insights
Get insights for an image sent in the POST body. 

[API Key Reference](https://dev.cognitive.microsoft.com/docs/services/56b43f0ccf5ff8098cef3808/operations/571fab09dbe2d933e891028f)

Request URL

https://api.cognitive.microsoft.com/bing/v5.0/images/search
Request headers

Content-Type (optional) string Media type of the body sent to the API.
Ocp-Apim-Subscription-Key string Subscription key which provides access to this API. Found in your subscriptions.

~~~~
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("POST", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~