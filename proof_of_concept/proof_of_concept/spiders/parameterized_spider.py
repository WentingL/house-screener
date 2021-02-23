import pandas as pd
import scrapy


class ParameterizedSpider(scrapy.Spider):
    name = "myownspider"

    def start_requests(self):
        urls = [
            "file:///E:/Github/web-scraper/proof_of_concept/attempt-zillow.html",
            # 'https://www.zillow.com/homes/for_sale/',
            # 'https://www.point2homes.com/CA/Real-Estate-Listings/BC/Kelowna.html',
            # 'https://www.realtor.ca/map#ZoomLevel=4&Center=54.920828%2C-99.316406&LatitudeMax=67.40327&LongitudeMax=-53.96484&LatitudeMin=36.87083&LongitudeMin=-144.66797&Sort=6-D&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        home_data = {}
        filter_xpath = '//div[@class="list-card-info"]/div[@class="list-card-heading"]/ul[count(li)>2]/../..'
        address = response.xpath(filter_xpath + '/a /address /text()').extract()
        home_data["address"] = address

        detail_info  = filter_xpath + '/div[@class="list-card-heading"]'
        prices = response.xpath(detail_info + '/div[@class="list-card-price"] /text()').extract()
        for index, price in enumerate(prices):
            prices[index] = price.replace("C$", "").replace("$", "").replace(",","")

        bds = response.xpath(detail_info + '/ul[@class="list-card-details"] /li[1] /text()').extract()
        bds = list(filter(lambda a: a != ",", bds))

        bath = response.xpath(detail_info + '/ul[@class="list-card-details"] /li[2] /text()').extract()
        bath = list(filter(lambda a: a != ",", bath))
        # Assume the unit of area is sqft
        area = response.xpath(detail_info + '/ul[@class="list-card-details"] /li[3] /text()').extract()
        for i, a in enumerate(area):
            area[i] = area[i].replace(",", "")

        home_data["price"] = prices
        home_data["beds"]= bds
        home_data["bath"] = bath
        home_data["area"] = area

        # self.logger.info(home_data)
        df = pd.DataFrame.from_dict(home_data)
        df.to_csv("extracted_data.csv")