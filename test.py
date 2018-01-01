#!/usr/bin/python3

import os
import sys
import pytube
from urllib.request import urlopen

from pprint import pprint

from distutils.dir_util import mkpath

CWD = os.path.dirname(os.path.abspath(__file__))
YT_DOWNLOAD_PATH = os.path.sep.join([
    CWD, 'download'
])


playlist_beginning = 'https://www.youtube.com/playlist?list='


playlists = [
    ('地下秩序', 'PLuwJy35eAVaL18Lg87FfKet-j7KDlqhqQ'),
    ('街角有樂', 'PLuwJy35eAVaJ_wKgvppYyxD-nXpHTtR9o'),
    ('文化長河－古都行', 'PLuwJy35eAVaIxgNAYL3YMzYhI5wIsSZmt'),
    ('香港故事-自遊香港', 'PLuwJy35eAVaL7ssLU1FA8zuLP3Sv94gYd'),
    ('香港歷史系列 III', 'PLuwJy35eAVaKpGWWgEPNK_-dDLlN8n-1J'),
    ('山水搜記', 'PLuwJy35eAVaIkcvGxeQh7-gN_SNF5uxOZ'),
    ('山水傳奇', 'PLuwJy35eAVaInrY8jNDhWZMDfjYysi2Rl'),
    ('文化長河-大地行', 'PLuwJy35eAVaKb9cptymdxqQHTVbKvgZbL'),
    ('我們的科學家', 'PLuwJy35eAVaJD-ze9wRgtBAoQzhabo5Vl'),
    ('香港歷史系列', 'PL1396B172772C478A'),
    ('天人合一', 'PLuwJy35eAVaJLkfXBGaplXAGWRk5JV8gr'),
    ('RTHK-香港故事', 'PLU18ugb4GweMOJBW_PdjjlHiPa-Z9IFOi'),
    ('香港歷史系例', 'PLFlwfOGHoMCraMmNjQM57RwM_Ruje6NQY'),
    ('長片','PL106E1D13834F287B'),
    ('戰火無情', 'PLVbwECSBScsMBt8cIkMR1QMbvxRlGy_iy')
]


def get_playlist_links(playlist_url):
    """get the playlist links"""
    page_elements = urlopen(playlist_url).readlines()

    page_elements = [temp.decode('utf-8') for temp in page_elements]
    # pprint(page_elements)

    # Filter out unnecessary lines
    video_elements = [
        el for el in page_elements if 'pl-video-title-link' in el]
    # Grab the video urls from the elements
    video_urls = [v.split('href="', 1)[1].split('" ', 1)[0]
                  for v in video_elements]
    return ['http://www.youtube.com' + v for v in video_urls]


def fetch_youtube_link(playlist):
    video_urls = get_playlist_links(playlist)
    output = []
    for u in video_urls:
        try:
            print('creating yt object %s ' % u)
            yt = pytube.YouTube(u)
            output.append(yt.streams.filter(progressive=True, mime_type='video/mp4').order_by('resolution').desc().first())
            pass
        except pytube.exceptions.AgeRestrictionError as e:
            print('exception raised during getting %s ' % u)
        except Exception as e:
            raise e
        else:
            pass
    return output


def download_youtube(yts):
    for yt in yts:
        print('downloading')
        yt.download(output_path='%s/download' % CWD)


def download_all(youtube_lists):
    for dir_name, youtube_list in youtube_lists:
        youtube_list = playlist_beginning + youtube_list
        pprint(download_youtube(fetch_youtube_link(youtube_list)))


download_all(playlists)

# yt= YouTube('https://www.youtube.com/watch?v=0htq8YQJ2wM')
# yt.streams.first().download()
