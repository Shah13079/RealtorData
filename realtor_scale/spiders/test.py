# import scrapy
# import json

# class Test(scrapy.Spider):
#     name = 'test'

#     def start_requests(self):
#         yield scrapy.Request(
#             # "https://www.realtor.com/api/v1/ldp?client_id=rdc-x&property_id=9566459484&listing_id=&status=FOR_SALE",
            
#             callback=self.parse
#         )
#     def parse(self,response):
#         response = json.loads(response.body)
#         location = response.get('data').get("home").get("location")
#         yield{
#             "location": location
#         }
        
       