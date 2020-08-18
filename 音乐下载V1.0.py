import requests
import pprint
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
url = 'https://cloud.ccswust.org/'
print('请输入你要的音乐网站')
print('1.网易 2.QQ 3.酷狗 4.酷我')
a = int(input())
if a == 1:
    t = 'netease'
elif a == 2:
    t = 'qq'
elif a == 3:
    t = 'kugou'
elif a == 4:
    t = 'kuwo'
else:
    print("输入错误!!!")
song_n = input('请输入你需要下载的歌曲:')
song_name = str(song_n)
files = {
    'input': (None, song_name),
    'filter': (None, 'name'),
    'type': (None, t),
    'page': (None, 1)
 }
response = requests.post(url, files=files, headers=headers)
# pprint.pprint(response.json())
json_data = response.json()['data']
# print(json_data)
for i in json_data:
    j = i['link']
    t = i['title']
    a = i['author']
    url_1 = i['url']
    res = requests.get(url_1).content
    print(str(a) + '    ' + str(t) + '      歌曲地址 ' + str(j))
    with open('song/' + t + '.mp3', 'wb')as f:
        f.write(res)
    break

