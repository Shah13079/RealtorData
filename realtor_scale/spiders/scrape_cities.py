import scrapy

URL = 'https://www.Texas-demographics.com/cities_by_population'.lower()


class Cities(scrapy.Spider):
    name = 'city'

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse
        )

    def parse(self, response, **kwargs):
        file_name = response.xpath("//h1/text()").get().split()[0]

        cities = response.xpath('//table[@class="ranklist table"]//td[2]')
        for each_city in cities:
            name = each_city.xpath('.//a/text()').get()

            if name is None:
                name = each_city.xpath('.//text()').get()

            a = name.split(" and ")
            a = ','.join(a).split(',')

            for each in a:
                with open(file_name.strip()+".txt", 'a+') as f:
                    f.write(each.strip()+str("\n"))

            yield {
                'city': name.strip()
            }
