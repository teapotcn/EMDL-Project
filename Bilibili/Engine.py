import requests, json
from tqdm import tqdm


def wyydownloader(name, ID):
    print('正在加载网易云音乐下载器：')
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; rv:11.0) like Gecko"}
    data = requests.get(r'http://music.163.com/api/song/detail/?id=114514&ids=%5B114514%5D', headers=headers)
    n = json.loads(data.content)
    name = n['songs']['name']
    creator = n['songs']['artists'][0]['name']
    chunk_size = 1024
    response = requests.get('http://music.163.com/song/media/outer/url?id=%s.mp3' % ID, headers=headers)
    print(response)
    # 文件大小，以 B 为单位
    file_size = response.headers.get('Content-Length')
    print(file_size)
    if file_size is not None:
        file_size = int(file_size)
    #部分代码Copy自 https://zhuanlan.zhihu.com/p/369531344
    bar = tqdm(total=file_size, desc=f'下载文件: {name}')
    with open('{name}-{creator}.mp3', mode='wb') as f:
    # 写入分块文件
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            bar.update(chunk_size)
    return 0
def bilibiliDownloader(url):
    pass