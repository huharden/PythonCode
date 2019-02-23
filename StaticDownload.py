'''
如下是使用 Python3 内置模块实现的一个比上一篇稍微健壮一点点的下载器。
通过内置 urllib 进行 header 设置或者代理设置或者启用会话，支持简单的 HTTP CODE 5XX 重试机制，支持 GET\POST。
（实际项目考虑和封装的要比这更加健壮）
'''
from http import cookiejar
from urllib import request, error
from urllib.parse import urlparse

class HtmlDownLoader(object):
    def download(self, url, retry_count=3, headers=None, proxy=None, data=None):
        if url is None:
            return None
        try:
            req = request.Request(url, headers=headers, data=data)
            cookie = cookiejar.CookieJar()
            cookie_process = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener()
            if proxy:
                proxies = {urlparse(url).scheme: proxy}
                opener.add_handler(request.ProxyHandler(proxies))
            content = opener.open(req).read()
        except error.URLError as e:
            print('HtmlDownLoader download error:', e.reason)
            content = None
            if retry_count > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    #说明是 HTTPError 错误且 HTTP CODE 为 5XX 范围说明是服务器错误，可以尝试再次下载
                    return self.download(url, retry_count-1, headers, proxy, data)
        return content