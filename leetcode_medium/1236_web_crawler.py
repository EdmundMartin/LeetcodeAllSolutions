from typing import List


class HtmlParser:
    def getUrls(self, url) -> List[str]:
        ...


class URL:
    def __init__(self, protocol: str, host: str):
        self.protocol = protocol
        self.host = host

    def __eq__(self, other):
        return self.protocol == other.protocol and self.host == other.host


def parse_url(url: str) -> URL:
    url = url.split('/')
    return URL(url[0][:-1], url[2])


class Solution:
    def __init__(self):
        self.start_url: URL = None
        self.seen = set()

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.start_url = parse_url(startUrl)

        queue = [startUrl]
        self.seen.add(startUrl)
        while queue:
            url = queue.pop(0)

            potential_urls = htmlParser.getUrls(url)
            for potential_url in potential_urls:
                if parse_url(potential_url) == self.start_url and potential_url not in self.seen:
                    self.seen.add(potential_url)
                    queue.append(potential_url)

        return list(self.seen)


if __name__ == '__main__':
    parse_url("http://news.yahoo.com/news")
