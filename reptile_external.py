import requests

url = "https://www.youtube.com"
headers = {'user-agent': 'Mozilla/5.0'} 

# If the client of ss/ssr is local, you can omit 'user:pass@'.
# host is usually 127.0.0.1
# port is usually 1080 (we can find this in v2ray or shadowsocks)
proxies = {'http':'socks5://user:pass@host:port',
           'https':'socks5://user:pass@host:port'}

# If your agent is http, you can replace the above two lines of codes with the following code:
# proxies = {'http':'http://user:pass@host:port',
#            'https':'https://user:pass@host:port'}
try:
    r = requests.get(url, proxies=proxies, headers=headers)
    
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
    
except:
    print("error")