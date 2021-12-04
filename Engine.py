import requests, json
from tqdm import tqdm
from you_get import common
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; rv:11.0) like Gecko"}

def wyydownloader(ID):
    '''利用官方API实现。'''
    print('正在加载网易云音乐下载器：')
    data = requests.get('http://music.163.com/api/song/detail/?id='+ID+'&ids=%5B'+ID+'%5D', headers=headers)
    n = json.loads(data.content)
    name = n['songs'][0]['name']
    creator = n['songs'][0]['artists'][0]['name']
    chunk_size = 1024
    response = requests.get('http://music.163.com/song/media/outer/url?id=%s.mp3' % ID, headers=headers)
    file_size = response.headers.get('Content-Length')
    if file_size is not None:
        file_size = int(file_size)
    #部分代码Copy自 https://zhuanlan.zhihu.com/p/369531344
    bar = tqdm(total=file_size, desc=f'下载文件: {name}',leave=True, unit='b', unit_scale=True, colour='#66ccff')
    with open(f'{name} - {creator}.mp3', mode='wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            bar.update(chunk_size)
def bilibiliDownloader(url):
    '''用you-get实现。'''
    common.any_download(url, info_only=False,output_dir=r'保存的目录',merge=True)
def searcher(name):
    f, c, d, k, _ = [], [], [], [], []
    data = requests.get(r'http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={'+name+r'}&type=1&offset=0&total=true&limit=20',headers=headers)
    n = json.loads(data.content)['result']['songs'][0:9]
    for x in range(len(n)):
        f.append(n[x]['name'])
        c.append(n[x]['artists'][0]['name'])
        d.append(n[x]['id'])
    for y in range(len(n)):
        k.append([f[y],c[y],str(d[y])])
    for z in range(len(n)):
        _.append(('['+str(z)+']')+" | ".join(k[z]))
    for __ in range(len(n)):
        print(_[__])
    a = input('请输入你选择下载的歌曲: ')
    wyydownloader(str(d[int(a)]))
def playlist(ID):
    pass