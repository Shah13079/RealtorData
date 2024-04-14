# from textwrap import indent
# import scrapy
# from ..utilities import headers_req, homeTown_pages, hometown_property, find_association, find_association_monthly, find_building_and_construction
# import json


# class FileSpider(scrapy.Spider):
#     name = 'hometown'

#     allowed_domains = ['www.realtor.com']

#     def start_requests(self):
#         page_num = 1
#         offset = 0
#         total_pages = 0
#         state = "Vermont"
#         code = "VT"

#         yield scrapy.Request(
#             url="https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
#                 body=json.dumps(homeTown_pages(state, page_num, offset, code)),
#             callback=self.parse_page,
#             method="POST",
#             dont_filter=True,

#             meta={
#                     "state_location": state,
#                     "state_code": code,
#                     "page_num": page_num,
#                     "offset": offset,
#                     "total_pages": total_pages
#             }            ,
#             headers=req_headers
#         )

#     def parse_page(self, response):
#         page_num = response.request.meta['page_num']
#         offset = response.request.meta['offset']
#         total_pages = response.request.meta['total_pages']

#         state_location = response.request.meta['state_location']
#         state_code = response.request.meta['state_code']

#         json_response = json.loads(response.body)

#         total_count = json_response.get("data").get('home_search').get("total")
#         print(f"total count for {state_location}:", total_count)

#         # count total pages
#         pages_calculation = (int(total_count)//42)+1

#         page_listings = json_response.get(
#             "data").get('home_search').get("results")

#         for property in page_listings:
#             property_id = property.get('property_id')
#             listing_id = property.get('listing_id')
#             if listing_id is None:
#                 listing_id = ''

#             yield scrapy.Request(
#                 url="https://www.realtor.com/api/v1/hulk?client_id=rdc-x&schema=vesta",
#                 body=json.dumps(hometown_property(property_id, listing_id)),
#                 callback=self.parse_property_page,
#                 method="POST",
#                 headers=req_headers,
#                 meta={"property_id": property_id,
#                       "listing_id": listing_id},

#             )

#         page_num += 1
#         offset += 42
#         total_pages += 1

#         if total_pages < pages_calculation:

#             yield scrapy.Request(
#                 url="https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
#                 body=json.dumps(homeTown_pages(
#                     state_location, page_num, offset, state_code)),
#                 callback=self.parse_page,
#                 dont_filter=True,
#                 method="POST",
#                 headers=req_headers,
#                 meta={
#                     "state_location": state_location,
#                     "state_code": state_code,
#                     "page_num": page_num,
#                     "offset": offset,
#                     "total_pages": total_pages
#                 }
#             )

#     def parse_property_page(self, response):
#         pro_id = response.meta['property_id']
#         lis_id = response.meta['listing_id']

#         hoa_fee = beds = baths = baths_consolidated = baths_full = data_source_copy_right = ''
#         json_response = json.loads(response.body)

#         # try:
#         #     buyer_details = json_response.get("data").get("home").get("buyers")[0]
#         # except (TypeError,AttributeError):
#         #     pass

#         # property_details

#         prop_details = json_response.get("data").get("home")
#         try:
#             list_price = prop_details.get("list_price")
#         except AttributeError:
#             pass

#         property_details = json_response.get('data').get("home")

#         try:

#             location = json_response.get('data').get("home").get("location")
#         except (AttributeError):
#             pass

#         try:
#             baths = prop_details.get("description").get("baths")
#         except (AttributeError):
#             pass
#             # with open("see_to_property",'a+') as e:
#             #     e.write(f"property id:{pro_id},listing_id:{lis_id}\n")
#             #     e.close()

#         try:
#             baths_consolidated = prop_details.get(
#                 "description").get("baths_consolidated")
#         except (AttributeError):
#             pass

#         try:
#             baths_full = prop_details.get("description").get("baths_full")
#         except (AttributeError):
#             pass

#         try:
#             baths_half = prop_details.get("description").get("baths_half")
#         except (AttributeError):
#             pass

#         try:

#             beds = prop_details.get("description").get("beds")
#         except (AttributeError):
#             pass

#         try:
#             garage = prop_details.get("description").get("garage")
#         except (AttributeError):
#             pass

#         try:
#             lot_sqft = prop_details.get("description").get("lot_sqft")
#         except (AttributeError):
#             pass

#         try:
#             sqft = prop_details.get("description").get("sqft")
#         except (AttributeError):
#             pass

#         try:
#             type = prop_details.get("description").get("type")
#         except (AttributeError):
#             pass

#         try:
#             property_details_text = prop_details.get("description").get("text")
#         except (AttributeError):
#             property_details_text = ''

#         try:
#             year_built = prop_details.get("description").get("year_built")
#         except (AttributeError):
#             year_built = ''

#         try:
#             hoa_fee = json_response.get('data').get(
#                 "home").get("hoa").get("fee")
#         except (AttributeError):
#             hoa_fee = ''

#         try:
#             price_per_sqft = json_response.get(
#                 'data').get("home").get("price_per_sqft")
#         except (AttributeError):
#             price_per_sqft = ''

#         try:
#             property_url = prop_details.get("permalink")
#             abs_url = 'https://www.realtor.com/realestateandhomes-detail/'+property_url
#         except (AttributeError):
#             property_url = ''

#         # Its all about location

#         try:
#             city = location.get("address").get("city")
#         except (AttributeError, UnboundLocalError):
#             city = ''

#         try:
#             country = location.get("address").get("country")
#         except (AttributeError, UnboundLocalError):
#             country = ''

#         try:
#             line = location.get("address").get("line")
#         except (AttributeError, UnboundLocalError):
#             line = ''

#         try:
#             postal_code = location.get("address").get("postal_code")
#         except (AttributeError, UnboundLocalError):
#             postal_code = ''

#         try:
#             state = location.get("address").get("state")
#         except (AttributeError, UnboundLocalError):
#             state = ''

#         try:
#             state_code = location.get("address").get("state_code")
#         except (AttributeError, UnboundLocalError):
#             state_code = ''

#         try:
#             street_name = location.get("address").get("street_name")
#         except (AttributeError, UnboundLocalError):
#             street_name = ''

#         try:

#             association = find_association(prop_details.get("details"))
#         except(AttributeError):
#             association = ''
#         try:

#             Calculated_Total_Monthly_Association_Fee = find_association_monthly(
#                 prop_details.get("details"))
#         except(AttributeError):
#             association = ''
#         try:

#             building_and_construction = find_building_and_construction(
#                 prop_details.get("details"))
#         except(AttributeError):
#             association = ''

#         try:
#             adv_details = json_response.get("data").get(
#                 "home").get("advertisers")[0]
#         except (TypeError, AttributeError, AttributeError):
#             pass

#         try:
#             adv_office_phone = adv_details.get(
#                 "office")['phones'][0].get("number")
#         except (TypeError, UnboundLocalError, AttributeError):
#             adv_office_phone = ''

#         try:
#             adv_name = json_response.get("data").get(
#                 'home').get("branding")[0].get("name")
#         except (TypeError, UnboundLocalError, AttributeError):
#             adv_name = ''

#         try:
#             if lis_id == '':
#                 adv_office_name = json_response.get("data").get(
#                     'home').get("branding")[0].get("name")
#             else:
#                 adv_office_name = json_response.get("data").get(
#                     'home').get("branding")[1].get("name")
#         except (TypeError, UnboundLocalError, AttributeError, IndexError):
#             try:
#                 adv_office_name = json_response.get("data").get(
#                     'home').get("branding")[0].get("name")
#             except:
#                 adv_office_name = ''

#         try:
#             broker_city = json_response.get("data").get('home').get(
#                 "consumer_advertisers")[1].get("address").get('city')
#             broker_state = json_response.get("data").get('home').get(
#                 "consumer_advertisers")[1].get("address").get('state_code')

#             if broker_city is not None and broker_state is None:
#                 broker_location = broker_city

#             elif broker_city and broker_state:

#                 broker_location = broker_city+","+broker_state
#             else:
#                 broker_location = ''

#         except (TypeError, AttributeError, UnboundLocalError, IndexError):

#             broker_location = ''

#         try:
#             source = prop_details.get("source")
#         except(AttributeError, UnboundLocalError, TypeError, IndexError):
#             pass
#         else:

#             data_source = source.get('name')
#             source_property_id = source.get('listing_id')

#             try:

#                 if lis_id != '':
#                     data_source_copy_right = source.get(
#                         "disclaimer").get('text')
#                 else:
#                     data_source_copy_right = source.get("disclaimer")
#             except(TypeError, AttributeError, UnboundLocalError, IndexError):
#                 data_source_copy_right = ''

#         try:
#             photos = prop_details.get("photos")
#         except(AttributeError, UnboundLocalError, TypeError):
#             pass
#         else:
#             try:
#                 photos = [each.get("href").replace(
#                     '.jpg', '-w1024_h768_x1')+'.jpg' for each in photos]
#             except (TypeError):
#                 photos = ''

#         yield{
#             # details
#             "beds": beds,
#             "baths": baths,
#             "baths_consolidated": baths_consolidated,
#             "baths_full": baths_full,
#             "baths_half": baths_half,
#             "garage": garage,
#             "year_built": year_built,
#             "sqft": sqft,
#             "lot_sqft": lot_sqft,
#             "type": type,

#             # location details
#             "city": city,
#             "country": country,
#             "line": line,
#             "postal_code": postal_code,
#             "state": state,
#             "state_code": state_code,
#             "street_name": street_name,

#             "property_details_text": property_details_text,

#             # associations
#             'association': association,
#             "Calculated_Total_Monthly_Association_Fee": Calculated_Total_Monthly_Association_Fee,

#             #building and construction
#             "building_and_construction": building_and_construction,

#             # advertiser info
#             "represented_agent_name": adv_name,
#             'agent_office_name': adv_office_name,
#             'agent_office_phone': adv_office_phone,
#             "broker_location": broker_location,

#             # source
#             'data_source': data_source,
#             "source_property_id": source_property_id,
#             'data_source_copy_right': data_source_copy_right,


#             "pirce": list_price,
#             "hoa_fee": hoa_fee,
#             "price_per_sqft": price_per_sqft,
#             "property_url": abs_url,
#             "photos": photos
#         }
