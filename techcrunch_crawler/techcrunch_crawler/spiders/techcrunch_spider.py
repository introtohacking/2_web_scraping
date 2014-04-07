from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from techcrunch_crawler.items import Article

class TechCrunchSpider(CrawlSpider):
    name = "techcrunch_spider"
    allowed_domains = ["techcrunch.com"]
    start_urls = [
        "http://techcrunch.com/"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=('(.*)/(\d+)/(\d+)/(\d+)/(.*)',)), callback='parse_details'),
    )

    def parse_details(self, response):
        sel = Selector(response)

        article = Article()
        article['title'] = sel.css(".tweet-title").extract()
        article['body'] = sel.css(".article-entry").extract()
        article['url'] = response.url

        return [article]