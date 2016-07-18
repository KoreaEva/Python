#Vision API 
Computer Vision API - v1.0
The Computer Vision API provides state-of-the-art algorithms to process images and return information. For example, it can be used to determine if an image contains mature content, or it can be used to find all the faces in an image. It also has other features like estimating dominant and accent colors, categorizing the content of images, and describing an image with complete English sentences. Additionally, it can also intelligently generate images thumbnails for displaying large images effectively.

Analyze Image
This operation extracts a rich set of visual features based on the image content. Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL. Within your request, there is an optional parameter to allow you to choose which features to return. By default, image categories are returned in the response. A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

[API Key Reference](https://dev.projectoxford.ai/docs/services/56f91f2d778daf23d8ec6739/operations/56f91f2e778daf14a499e1fa)

Computer Vision API는 두 가지 Parameter을 지정할 수 있는데 두 번째는 필수 사항은 아니다. 

첫 번째 옵션은 분석 종류를 지정한다.  

visualFeatures (optional) string A string indicating what visual feature types to return. Multiple values should be comma-separated. 
Valid visual feature types include: 
1. Categories - categorizes image content according to a taxonomy defined in documentation.
2. Tags - tags the image with a detailed list of words related to the image content.
3. Description - describes the image content with a complete English sentence.
4. Faces - detects if faces are present. If present, generate coordinates, gender and age.
5. ImageType - detects if image is clipart or a line drawing.
6. Color - determines the accent color, dominant color, and whether an image is black&white.
7. Adult - detects if the image is pornographic in nature (depicts nudity or a sex act). Sexually suggestive content is also detected.

두 번쨰 옵션은 디테일에 대한 옵션을 지정하는 것인데 필수요소는 아니다.

details (optional) string A string indicating which domain-specific details to return. Multiple values should be comma-separated. 
Valid visual feature types include: 
Celebrities - identifies celebrities if detected in the image.


~~~~
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Categories',       #이 부분의 값을 변경해서 분석 방법을 변경할 수 있다.
    'details': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~


#Recognize Emotions in Images  

The Emotion API takes an facial expression in an image as an input, and returns the confidence across a set of emotions for each face in the image, as well as bounding box for the face, using the Face API. If a user has already called the Face API, they can submit the face rectangle as an optional input.   The emotions detected are anger, contempt, disgust, fear, happiness, neutral, sadness, and surprise. These emotions are understood to be cross-culturally and universally communicated with particular facial expressions.  For the demo below please click the image samples to see how Emotion API uses world-class machine learning techniques to provide these results. You can also click the open image button or drag-and-drop to upload your own images, or input a URL for a remote image. We don’t keep your images for this demo.

[API Key Reference](https://dev.projectoxford.ai/docs/services/5639d931ca73072154c1ce89/operations/563b31ea778daf121cc3a5fa)

~~~~
############ Python 2.7 #############
#import httplib2, urllib, base64

#headers = {
#    # Request headers
#    'Content-Type': 'application/json',
#    'Ocp-Apim-Subscription-Key': '{Subscription Key}',
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