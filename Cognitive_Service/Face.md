#Face API  

Face API도 상당히 유용한 서비스 중의 하나이다. 기본적으로 Detect, Find Similar, Group, Identify, Verify 등의 기능을 제공한다. 


##Detect
Detect human faces in an image and returns face locations, and optionally with face ID, landmarks, and attributes.


[API Reference](https://dev.projectoxford.ai/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236)
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

##Face List의 생성

여러 사람들 중 한 명을 찾거나 하기 위해서 필요한 것이 먼저 Person Group을 만드는 것이다. 
[API Reference](https://dev.projectoxford.ai/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524b)

Create an empty face list with user-specified face list ID, name and an optional user-data. 64 face lists are allowed to exist in one subscription.
Face list is a group of faces, and these faces will not expire. Face list is used as a parameter of source faces in Face - Find Similar. Face List is useful when to find similar faces in a fixed face set very often, e.g. to find a similar face in a face list of celebrities, friends, or family members.

A face list can have a maximum of 1000 faces.

Face List를 생성하기 위해서는 아래와 같은 파라메터가 필요하다.
~~~~
{
    "name":"sample_list",
    "userData":"User-provided data attached to the face list" 
}
~~~~

실제로 Face List를 생성하는 코드는 아래와 같다. 
~~~~
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("PUT", "/face/v1.0/facelists/{faceListId}?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~


##Face List에 Face 추가하기

Face List가 생성되고 나면 Face를 여러장 추가해 본다.  
[API Reference](https://dev.projectoxford.ai/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395250)

Face List - Add a Face to a Face List
Add a face to a face list. The input face is specified as an image with a targetFace rectangle. It returns an persistedFaceId representing the added face, and persistedFaceId will not expire.

- The persistedFaceId will be used in output JSON of Face - Find Similar, or in Face List - Delete a Face from a Face List to remove face from a face list.
- JPEG, PNG, GIF(the first frame), and BMP are supported. The image file size should be no larger than 4MB.
- The detectable face size is between 36x36 to 4096x4096 pixels. The faces out of this range will not be detected.
- Rectangle specified by targetFace should contain exactly one face. Zero or multiple faces will be regarded as an error. Out of detectable face size, large head-pose, or very large occlusions will also result in fail to add a person face.
- The given rectangle specifies both face location and face size at the same time. There is no guarantee of corrent result if you are using rectangle which are not returned from Face - Detect.

Face list is a group of faces, and these faces will not expire. Face list is used as a parameter of source faces in Face - Find Similar. Face List is useful when to find similar faces in a fixed face set very often, e.g. to find a similar face in a face list of celebrities, friends, or family members.

A face list can have a maximum of 1000 faces.

이제 얼굴이 들어간 사진들을 Face List에 추가한다. 이때 사진에는 여러사람이 들어가면 오류가 나는데 이럴 경우 추가 옵션으로 영역을 지정해 주면 오류를 해결 할 수 있다.
~~~~
{
    "url":"http://example.com/1.jpg"
}
~~~~

실제로 Face List에 Face를 추가하는 코드는 아래와 같다. 
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
    'userData': '{string}',
    'targetFace': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/facelists/{faceListId}/persistedFaces?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~

##Face List에 Face 목록 확인하기

Face List안에 추가된 Face 목록을 조회해 본다.  
[API Reference](https://dev.projectoxford.ai/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524c/console)

Retrieve a face list's information, including face list ID, name, userData and faces in the face list. Face list simply represents a list of faces, and could be treated as a searchable data source in Face - Find Similar.

리스트를 요청하는 파라메터
~~~~
{
    "faceListId": "sample_list",
    "name": "list1",
    "userData":"User-provided data attached to the face list",
    "persistedFaces":[
        {
            "persistedFaceId":"B8D802CF-DD8F-4E61-B15C-9E6C5844CCBD",
            "userData":"User-provided data attached to the face" 
        },
        …
    ]
}
~~~~

실제로 Face List에서 Face 목록을 조회하는 코드는 아래와 같다. 
~~~~
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("GET", "/face/v1.0/facelists/{faceListId}?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~


##Face List에 Face 조회하기

Face List안에 추가된 Face 목록을 조회해 본다.  
[API Reference](https://dev.projectoxford.ai/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524c/console)

Retrieve a face list's information, including face list ID, name, userData and faces in the face list. Face list simply represents a list of faces, and could be treated as a searchable data source in Face - Find Similar.

리스트를 요청하는 파라메터
~~~~
{
    "faceListId": "sample_list",
    "name": "list1",
    "userData":"User-provided data attached to the face list",
    "persistedFaces":[
        {
            "persistedFaceId":"B8D802CF-DD8F-4E61-B15C-9E6C5844CCBD",
            "userData":"User-provided data attached to the face" 
        },
        …
    ]
}
~~~~

실제로 Face List에서 Face 목록을 조회하는 코드는 아래와 같다. 
~~~~
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("GET", "/face/v1.0/facelists/{faceListId}?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~