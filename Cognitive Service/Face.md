#Face API  

Face API도 상당히 유용한 서비스 중의 하나이다. 기본적으로 Detect, Find Similar, Group, Identify, Verify 등의 기능을 제공한다. 


##Detect
Detect human faces in an image and returns face locations, and optionally with face ID, landmarks, and attributes.


[API Key Reference](https://dev.projectoxford.ai/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236)
Optional parameters for returning face ID, landmarks, and attributes. Attributes include age, gender, smile intensity, facial hair and head-pose. Face ID is for other APIs use including Face - Identify, Face - Verify, and Face - Find Similar. The face ID will expire in 24 hours after detection call.

- JPEG, PNG, GIF(the first frame), and BMP are supported. The image file size should be no larger than 4MB.
- The detectable face size is between 36x36 to 4096x4096 pixels. The faces out of this range will not be detected.
- A maximum of 64 faces could be returned for an image. The returned faces are ranked by face rectangle size in descending order.
- Some faces may not be detected for technical challenges, e.g. very large face angles (head-pose) or large occlusion. Frontal and near-frontal faces have the best results.
- Attributes (age, gender, headPose, smile and facialHair, and glasses) are still experimental and may not be very accurate. HeadPose's pitch value is reserved as 0.

여기서 반드시 설정해 주어야 하는 것이 바로 returnFaceAttributes 인데 돌려 받기를 원하는 속성들을 나열하면 된다.

Face Attributes:
- age: an age number in years.
- gender: male or female.
- smile: smile intensity, a number between [0,1]
- facialHair: consists of lengths of three facial hair areas: moustache, beard and sideburns.
- headPose: 3-D roll/yew/pitch angles for face direction. Pitch value is reserved to 0.
- glasses: glasses type. Possible values are 'noGlasses', 'readingGlasses', 'sunglasses', 'swimmingGoggles'.

~~~~
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{Subscription Key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~

