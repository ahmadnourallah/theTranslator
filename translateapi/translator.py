# -*- coding: utf-8 -*-
import sys, re, json
if (sys.version_info[0] < 3):
    import urllib2
    import urllib
    import HTMLParser
else:
    import html.parser
    import urllib.request
    import urllib.parse

agent = {'User-Agent':
"Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}

def unescape(text):
    if (sys.version_info[0] < 3):
        parser = HTMLParser.HTMLParser()
    else:
        parser = html.parser.HTMLParser()
    return (parser.unescape(text))

def Googletranslate(string, to_language="auto", from_language="auto"):

    base_link = "https://translate.google.com/m?hl=%s&sl=%s&q=%s"
    if (sys.version_info[0] < 3):
        string = urllib.quote_plus(string)
        link = base_link % (to_language, from_language, string)
        request = urllib2.Request(link, headers=agent)
        raw_data = urllib2.urlopen(request).read()
    else:
        string = urllib.parse.quote(string)
        link = base_link % (to_language, from_language, string)
        request = urllib.request.Request(link, headers=agent)
        raw_data = urllib.request.urlopen(request).read()
    data = raw_data.decode("utf-8")
    expr = r'class="t0">(.*?)<'
    re_result = re.findall(expr, data)
    if (len(re_result) == 0):
        result = ""
    else:
        result = unescape(re_result[0])
    return (result)

def Yandextranslate(string, to_language):
    if (sys.version_info[0] < 3):
        json_data = urllib2.urlopen("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170804T224557Z.3f816f7720547557.409b857bfccf5acb026d292a796a93cff350f936&text={0}&lang={1}".format(urllib.quote(string),to_language))
    else:
        json_data = urllib.request.urlopen("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170804T224557Z.3f816f7720547557.409b857bfccf5acb026d292a796a93cff350f936&text={0}&lang={1}".format(urllib.request.quote(string),to_language))
    python_obj = json.loads(json_data.read().decode('utf-8'))
    return python_obj['text'][0]

def LanguageDetect(string):
    url = urllib.request.urlopen("https://translate.yandex.net/api/v1.5/tr.json/detect?key=trnsl.1.1.20170804T224557Z.3f816f7720547557.409b857bfccf5acb026d292a796a93cff350f936&text={0}".format(urllib.parse.quote(string)))
    python_obj = json.loads(url.read().decode('utf-8'))
    return python_obj['lang']
