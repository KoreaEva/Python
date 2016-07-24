#Bing Search API
The Search API provides a similar (but not exact) experience to Bing.com/Search by returning search results that Bing determines are relevant to the specified query. The results also identify the order that you must display the content in (see Using Ranking to Display Results). The response may also include related search links and suggest a query string that may more accurately represent the user's intent. Typically, you will call this API instead of calling the other APIs in the Bing API family, such as the Image API or News API.

[API Key Reference](https://dev.cognitive.microsoft.com/docs/services/56b43eeccf5ff8098cef3807/operations/56b4447dcf5ff8098cef380d)

Request parameters

- q string The user's search query string
- count (optional) number The number of search results to return in the response. The actual number delivered may be less than requested.
- offset (optional) number The zero-based offset that indicates the number of search results to skip before returning results.
- mkt (optional) string The market where the results come from. Typically, this is the country where the user is making the request from; however, it could be a different country if the user is not located in a country where Bing delivers results. The market must be in the form {language code}-{country code}. For example, en-US. 

Full list of supported markets: 
es-AR,en-AU,de-AT,nl-BE,fr-BE,pt-BR,en-CA,fr-CA,es-CL,da-DK,fi-FI,fr-FR,de-DE,zh-HK,en-IN,en-ID,en-IE,it-IT,ja-JP,ko-KR,en-MY,es-MX,nl-NL,en-NZ,no-NO,zh-CN,pl-PL,pt-PT,en-PH,ru-RU,ar-SA,en-ZA,es-ES,sv-SE,fr-CH,de-CH,zh-TW,tr-TR,en-GB,en-US,es-US
safesearch (optional) string A filter used to filter results for adult content.

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
    'model': '{string}',
    'text': '{string}',
    'order': '{number}',
    'maxNumOfCandidatesReturned': '{number}',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/text/weblm/v1.0/breakIntoWords?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
~~~~