#Bing News Search API
The News API lets partners send a search query to Bing and get back a list of relevant news articles. Note you should call the News API if you need news content only. If you need other content such as images and webpages in addition to images, you must call the Search API which includes news articles in the response. You must display the news articles in the order provided in the response.

Search
Get news articles relevant for a given query.

[API Key Reference](https://dev.cognitive.microsoft.com/docs/services/56b43f72cf5ff8098cef380a/operations/56b449fbcf5ff81038d15cdf)

Request URL

https://api.cognitive.microsoft.com/bing/v5.0/news/search[?q][&count][&offset][&mkt][&safeSearch]
Request parameters

- q string The user's search query string
- count (optional) string The number of news results to return in the response. The actual number delivered may be less than requested.
- offset (optional) string The zero-based offset that indicates the number of news results to skip before returning results.
- mkt (optional) string The market where the results come from. Typically, this is the country where the user is making the request from; however, it could be a different country if the user is not located in a country where Bing delivers results. The market must be in the form {language code}-{country code}. For example, en-US. 

Full list of supported markets: 
es-AR,en-AU,de-AT,nl-BE,fr-BE,pt-BR,en-CA,fr-CA,es-CL,da-DK,fi-FI,fr-FR,de-DE,zh-HK,en-IN,en-ID,en-IE,it-IT,ja-JP,ko-KR,en-MY,es-MX,nl-NL,en-NZ,no-NO,zh-CN,pl-PL,pt-PT,en-PH,ru-RU,ar-SA,en-ZA,es-ES,sv-SE,fr-CH,de-CH,zh-TW,tr-TR,en-GB,en-US,es-US
- safeSearch (optional) string A filter used to filter results for adult content.

Request headers

Ocp-Apim-Subscription-Key string Subscription key which provides access to this API. Found in your subscriptions.
~~~~
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'q': 'microsoft',
    'count': '10',
    'offset': '0',
    'mkt': 'en-us',
    'safeSearch': 'Moderate',
})

try:
    conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("GET", "/bing/v5.0/news/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~