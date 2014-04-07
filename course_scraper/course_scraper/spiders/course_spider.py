from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from course_scraper.items import Course

class CourseSpider(CrawlSpider):
    name = "course_spider"
    allowed_domains = ["registrar.princeton.edu"]
    start_urls = [
        "http://registrar.princeton.edu/course-offerings/search_results.xml?term=1152&subject=COS"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=('course_details.xml')), callback='parse_details'),
    )

    def parse_details(self, response):
        sel = Selector(response)

        course = Course()
        course['title'] = sel.xpath('//*[@id="timetable"]/h2/text()').extract()
        course['code'] = sel.xpath('//*[@id="timetable"]/strong[2]/text()').extract()
        course['desc'] = sel.xpath('//*[@id="descr"]/text()').extract()

        return [course]