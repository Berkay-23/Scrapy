from cmath import inf
import scrapy


class MarketSpider(scrapy.Spider):
    name = 'market'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for i in response.css('.lister-list tr'):

            popularity = i.css('td:nth-child(2)::text').get().strip()
            name = i.css('td:nth-child(2) a::text').get().strip()
            info = i.css('td:nth-child(2) .secondaryInfo::text').get().strip()
            rating = i.css('td:nth-child(3) strong::text').get().strip()

            yield {
                'popularity': popularity,
                'name': name,
                'info': info,
                'rating': rating
            }
