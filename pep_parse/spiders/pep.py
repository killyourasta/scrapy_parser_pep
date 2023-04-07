import scrapy

SPIDER_MODULES = ['peps.python.org']
START_URLS = ['https://peps.python.org/']


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = SPIDER_MODULES
    start_urls = START_URLS

    def parse(self, response):
        for link in response.css(
            'tbody tr a[href^="pep-"]'
        ):
            yield response.follow(
                link, callback=self.parse_pep
            )

    def parse_pep(self, response):
        full_pep_name = response.css('.page-title::text').get().split()
        number = full_pep_name[1]
        name_pep = ' '.join(full_pep_name[3:])
        yield {
            'number': int(number),
            'name': name_pep,
            'status': response.css('abbr::text').get()
        }
