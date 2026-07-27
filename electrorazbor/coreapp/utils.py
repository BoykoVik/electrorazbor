import urllib.parse
import urllib.request
import threading

def tgsandmsg(msgForTg):
    """
    Отправка сообщения в Telegram асинхронно (не блокирует)
    """
    def _send():
        url = u'https://api.telegram.org/bot8187379981:AAEBI3xGSMfrYqtCJONoT4bKVT3dQQRcqc8/sendMessage'
        admins = ('628257666', '596900780',)
        for admin in admins:
            try:
                data = {'chat_id': admin, 'text': msgForTg, 'parse_mode': 'HTML'}
                url_values = urllib.parse.urlencode(data)
                full_url = url + '?' + url_values
                # Таймаут 2 секунды
                urllib.request.urlopen(full_url, timeout=2)
            except:
                pass
    
    # Запускаем в фоновом потоке
    thread = threading.Thread(target=_send, daemon=True)
    thread.start()