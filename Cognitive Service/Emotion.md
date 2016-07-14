#Recognize Emotions in Images  

The Emotion API takes an facial expression in an image as an input, and returns the confidence across a set of emotions for each face in the image, as well as bounding box for the face, using the Face API. If a user has already called the Face API, they can submit the face rectangle as an optional input.   The emotions detected are anger, contempt, disgust, fear, happiness, neutral, sadness, and surprise. These emotions are understood to be cross-culturally and universally communicated with particular facial expressions.  For the demo below please click the image samples to see how Emotion API uses world-class machine learning techniques to provide these results. You can also click the open image button or drag-and-drop to upload your own images, or input a URL for a remote image. We don’t keep your images for this demo.

[API Key Reference](https://dev.projectoxford.ai/docs/services/5639d931ca73072154c1ce89/operations/563b31ea778daf121cc3a5fa)

~~~~
############ Python 2.7 #############
#import httplib2, urllib, base64

#headers = {
#    # Request headers
#    'Content-Type': 'application/json',
#    'Ocp-Apim-Subscription-Key': '1e6a0214e8e243f69825e35b19270bbc',
#}

#params = urllib.parse.urlencode({
#})

#try:
#    conn = httplib.HTTPSConnection('api.projectoxford.ai')
#    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, "{'url': 'https://lh3.googleusercontent.com/WjhiG9DDttW7V4Iamd4XwQIVQTjgQ8fV9ElCYeNBTpIYVcO7sZM3PySqHJ0BOrla9XwoGLbGdBgFtyFplueX3mdjsw71j4pzgVYY3UbDIzxqhbAEKPTwkN3h-PhleQ'}", headers)
#    response = conn.getresponse()
#    data = response.read()
#    print(data)
#    conn.close()
#except Exception as e:
#    #print("[Errno {0}] {1}".format(e.arg)
#    print("Error");

####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '1e6a0214e8e243f69825e35b19270bbc',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, "{'url': 'http://postfiles6.naver.net/20160530_117/warit_1464561113138dr7yL_JPEG/IMG_1094.jpg?type=w3'}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~