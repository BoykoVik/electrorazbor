import urllib.parse
import urllib.request

def tgsandmsg(msgForTg):
    url = u'https://api.telegram.org/bot6153857947:AAEFXlzH983Nnudmlu5KBl4THxTh4t94STQ/sendMessage'
    admins = ('628257666',)
    for admin in admins:
            try:
                data = {'chat_id': admin, 'text': msgForTg, 'parse_mode': 'HTML'}
                url_values = urllib.parse.urlencode(data)
                full_url = url + '?' + url_values
                data = urllib.request.urlopen(full_url)
            except:
                 pass