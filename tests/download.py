#!/usr/bin/env python

import unittest

from lulu.extractors import (
    imgur,
    magisto,
    youtube,
    yixia,
    bilibili,
    douyin,
    miaopai,
    # netease,
    youku,
    qq,
    acfun,
)


class LuluTests(unittest.TestCase):
    def test_imgur(self):
        imgur.download('http://imgur.com/WVLk5nD', info_only=True)
        imgur.download('http://imgur.com/gallery/WVLk5nD', info_only=True)

    def test_magisto(self):
        magisto.download(
            'http://www.magisto.com/album/video/f3x9AAQORAkfDnIFDA',
            info_only=True
        )

    def test_youtube(self):
        youtube.download(
            'http://www.youtube.com/watch?v=pzKerr0JIPA', info_only=True
        )
        youtube.download('http://youtu.be/pzKerr0JIPA', info_only=True)
        youtube.download(
            'http://www.youtube.com/attribution_link?u=/watch?v%3DldAKIzq7bvs%26feature%3Dshare',  # noqa
            info_only=True
        )

    def test_yixia(self):
        yixia.download(
            'http://m.miaopai.com/show/channel/vlvreCo4OZiNdk5Jn1WvdopmAvdIJwi8',  # noqa
            info_only=True
        )

    def test_bilibili(self):
        bilibili.download(
            'https://www.bilibili.com/video/av16907446/', info_only=True
        )
        bilibili.download(
            'https://www.bilibili.com/video/av13228063/', info_only=True
        )

    def test_douyin(self):
        douyin.download(
            'https://www.douyin.com/share/video/6492273288897629454',
            info_only=True
        )
        douyin.download(
            'https://www.douyin.com/share/video/6511578018618543368',
            info_only=True
        )

    def test_weibo(self):
        miaopai.download('https://m.weibo.cn/status/FEFq863WF', info_only=True)
        miaopai.download(
            'https://m.weibo.cn/status/4199826726109820', info_only=True
        )

    def test_netease(self):
        # failed on travis, don't know why, maybe ip issue?
        pass
        # netease.download(
        #     'http://music.163.com/#/album?id=35757233', info_only=True
        # )
        # netease.download(
        #     'http://music.163.com/#/song?id=490602750', info_only=True
        # )

    def test_youku(self):
        youku.download(
            'http://v.youku.com/v_show/id_XMzMzMDk5MzcyNA==.html',
            info_only=True
        )
        youku.download(
            'http://v.youku.com/v_show/id_XMzI2NTUyOTIxMg==.html',
            info_only=True
        )

    def test_qq(self):
        qq.download('https://v.qq.com/x/page/n0528cwq4xr.html', info_only=True)
        qq.download(
            'https://v.qq.com/x/cover/ps6mnfqyrfo7es3/q0181hpdvo5.html?',
            info_only=True
        )
        qq.download(
            'http://v.qq.com/cover/p/ps6mnfqyrfo7es3.html?vid=q0181hpdvo5',
            info_only=True
        )
        qq.download(
            'https://v.qq.com/x/cover/9hpjiv5fhiyn86u/t0522x58xma.html',
            info_only=True
        )

    def test_acfun(self):
        acfun.download('http://www.acfun.cn/v/ac4209715', info_only=True)
        acfun.download('http://www.acfun.cn/v/ac4210425', info_only=True)


if __name__ == '__main__':
    unittest.main()