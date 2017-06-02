"""
Google trend hot video item crawler

Eason Cao (eason@lenlabs.com)
"""
import urllib, urllib2, json

url = 'https://trends.google.com.tw/trends/hotvideos/hotItems'

param = { 'hvd' : '', 'geo' : 'US', 'mob' :0, 'hvsm' :1 }

req = urllib2.Request(url, urllib.urlencode(param))
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
req.add_header('origin', 'https://trends.google.com.tw')
req.add_header('referer', 'https://trends.google.com.tw/trends/hotvideos')
data = urllib2.urlopen(req)

raw_json = json.loads(data.read())


"""
Fetch the trending video data

{
    channelUrl : "https://www.youtube.com/channel/UC8gKWMFvVenlVjgysNojYQg"
    commentCount : "68,581"
    dailyViewCount : "1,000,000"
    id : "YAJWK40qahg"
    imgUrl : "https://i.ytimg.com/vi/YAJWK40qahg/mqdefault.jpg"
    length : "9:41"
    publishedTime : "today"
    shareUrl : "https://www.google.com/trends/hotvideos?svt=SML+Movie:+Jeffys+Fidget+Spinner!&hvd=20170601&geo=US#a=YAJWK40qahg"
    title : "SML Movie: Jeffy's Fidget Spinner!"
    totalViewCount : "3,311,117"
    url : "https://www.youtube.com/watch?v=YAJWK40qahg"
    username : "SuperMarioLogan
}
"""

if 'videoList' in raw_json:

    for video in raw_json['videoList']:
        print "%s : " % video['title']

    print "[INFO] Total has %s items." % len(raw_json['videoList'])
