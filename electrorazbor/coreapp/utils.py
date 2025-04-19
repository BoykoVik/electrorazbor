import urllib.parse
import urllib.request

def tgsandmsg(msgForTg):
    url = u'https://api.telegram.org/bot8187379981:AAEBI3xGSMfrYqtCJONoT4bKVT3dQQRcqc8/sendMessage'
    admins = ('628257666', '596900780',)
    for admin in admins:
            try:
                data = {'chat_id': admin, 'text': msgForTg, 'parse_mode': 'HTML'}
                url_values = urllib.parse.urlencode(data)
                full_url = url + '?' + url_values
                data = urllib.request.urlopen(full_url)
            except:
                 pass