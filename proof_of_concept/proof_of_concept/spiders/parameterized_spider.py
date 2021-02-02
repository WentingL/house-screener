import scrapy


class ParameterizedSpider(scrapy.Spider):
    name = "myownspider"

    def start_requests(self):
        urls = [
            'https://www.zillow.com/homes/for_sale/',
            'https://www.point2homes.com/CA/Real-Estate-Listings/BC/Kelowna.html',
            'https://www.realtor.ca/map#ZoomLevel=4&Center=54.920828%2C-99.316406&LatitudeMax=67.40327&LongitudeMax=-53.96484&LatitudeMin=36.87083&LongitudeMin=-144.66797&Sort=6-D&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split(".")[1]
        filename = f'attempt-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')