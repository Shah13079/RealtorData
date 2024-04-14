
import scrapy
from time import sleep
import json
from ..utilities import *
import os


class CondosSpider(scrapy.Spider):
    name = 'condos'
    allowed_domains = ['www.realtor.com']

    def __init__(self, state_code=None, state_name=None, *args, **kwargs):
        super(CondosSpider, self).__init__(*args, **kwargs)
        self.state_code = state_code
        self.state_name = state_name
        self.statepath = os.path.join('statesfiles',self.state_name)
    
    def start_requests(self):
        page_num = 1
        offset = 0
        total_pages = 0
        state_code = self.state_code
        file1 = open(f'{self.statepath}.txt', 'r')

        address_lines = file1.readlines()
        for line in address_lines:
            state = line.strip()
            slug_for_headers = state.replace(' ', '-') + "_" + state_code

            if state is not None and state != "" and state != ' ':
                state_with_abbrevation = state+", "+"%s" % (state_code)

                yield scrapy.Request(
                    url="https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
                    body=json.dumps(condos_cities(
                        state_with_abbrevation, page_num, offset)),
                    callback=self.parse_page,
                    method="POST",
                    dont_filter=True,

                    meta={
                        "state_name": state,
                        "state_location": state_with_abbrevation,
                        # "state_code":code,
                        "page_num": page_num,
                        "offset": offset,
                        "total_pages": total_pages,
                        'pages_calculation': 0,
                        "slug_for_headers": slug_for_headers
                    },
                    headers=headers_req(slug_for_headers)
                )

    def parse_page(self, response):
        slug_for_headers = response.meta['slug_for_headers']
        page_num = response.request.meta['page_num']
        offset = response.request.meta['offset']
        total_pages = response.request.meta['total_pages']
        pages_calculation = response.request.meta['pages_calculation']

        state_location = response.request.meta['state_location']
        # state_code = response.request.meta['state_code']

        # page response
        json_response = json.loads(response.body)

        try:
            total_count = json_response.get(
                "data").get('home_search').get("properties")
        except AttributeError:
            pass
        else:

            total_count = json_response.get(
                "data").get('home_search').get("total")

            print(f"total count for {state_location}:", total_count)

            # count total pages
            pages_calculation = (int(total_count)//42)+1
            self.pages_calculation = pages_calculation

            page_listings = json_response.get(
                "data").get('home_search').get("properties")
            
            

            for property in page_listings:
                try:
                    property_id = property.get('property_id')
                except:
                    property_id = ''
                listing_id = property.get('listing_id')
                if listing_id is None:
                    listing_id = ''

                yield scrapy.Request(
                    url=f"https://www.realtor.com/api/v1/ldp?client_id=rdc-x&property_id={property_id}&listing_id=&status=FOR_SALE",
                    callback=self.parse_property_page,
                    headers=headers_req(slug_for_headers),
                    meta={"property_id": property_id,
                          "listing_id": listing_id,
                          "slug_for_headers": slug_for_headers}
                )

        page_num += 1
        offset += 42
        print("offset is:", offset, "page is:", total_pages)
        total_pages += 1

        if total_pages < pages_calculation:
            yield scrapy.Request(
                url="https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
                body=json.dumps(condos_cities(
                    state_location, page_num, offset)),
                callback=self.parse_page,
                dont_filter=True,
                method="POST",
                headers=headers_req(slug_for_headers),
                meta={
                    "state_location": state_location,
                    # "state_code":state_code,
                    "page_num": page_num,
                    "offset": offset,
                    "total_pages": total_pages,
                    "pages_calculation": pages_calculation,
                    "slug_for_headers": slug_for_headers
                }
            )

    def parse_property_page(self, response):
        list_price = lat = lon = adv_office_name = abs_url = hoa_fee = price_per_sqft = data_source_copy_right = photos = source_property_id = data_source = building_and_construction = broker_location = adv_office_phone = beds = beds = baths_consolidated = baths_full = garage = year_built = sqft = lot_sqft = type = city = country = line = postal_code = adv_name = state_code = street_name = association = Calculated_Total_Monthly_Association_Fee = property_details_text = ''

        data_source = source_property_id = data_source_copy_right = baths = ''

        pro_id = response.meta['property_id']
        lis_id = response.meta['listing_id']

        hoa_fee = beds = baths = baths_consolidated = baths_full = ''
        json_response = json.loads(response.body)

        # property_details
        prop_details = json_response.get("data").get("home")
        try:
            list_price = prop_details.get("list_price")
        except AttributeError:
            pass
        
        try:
            property_id = prop_details.get("property_id")
        except AttributeError:
            property_id = ''

        try:

            address = json_response.get('data').get("home").get("location").get("address")
        except AttributeError:
            pass
        
        try:
            baths = prop_details.get("description").get("baths")
        except (AttributeError):
            baths = ''

        try:
            baths_consolidated = prop_details.get(
                "description").get("baths_consolidated")
        except (AttributeError):
            baths_consolidated = ''

        try:
            baths_full = prop_details.get("description").get("baths_full")
        except (AttributeError):
            baths_full = ''

        try:
            baths_half = prop_details.get("description").get("baths_half")
        except (AttributeError):
            baths_half = ''

        try:

            beds = prop_details.get("description").get("beds")
        except (AttributeError):
            beds = ''

        try:
            garage = prop_details.get("description").get("garage")
        except (AttributeError):
            garage = ''

        try:
            lot_sqft = prop_details.get("description").get("lot_sqft")
        except (AttributeError):
            lot_sqft = ''

        try:
            sqft = prop_details.get("description").get("sqft")
        except (AttributeError):
            sqft = ''

        try:
            type = prop_details.get("description").get("type")
        except (AttributeError):
            type = ''

        try:
            property_details_text = prop_details.get("description").get("text")
        except (AttributeError):
            property_details_text = ''

        try:
            year_built = prop_details.get("description").get("year_built")
        except (AttributeError):
            year_built = ''

        try:
            hoa_fee = json_response.get('data').get(
                "home").get("hoa").get("fee")
        except (AttributeError):
            hoa_fee = ''

        try:
            price_per_sqft = json_response.get(
                'data').get("home").get("price_per_sqft")
        except (AttributeError):
            price_per_sqft = ''

        try:
            property_url = prop_details.get("permalink")
            if property_url:
                abs_url = 'https://www.realtor.com/realestateandhomes-detail/'+property_url
            else:
                abs_url = prop_details.get("href")
        except (AttributeError):
            property_url = ''
        


        try:
            lat = address.get("coordinate").get('lat')
        except (AttributeError, UnboundLocalError):
            lat = ''

        try:
            lon = address.get("coordinate").get('lon')
        except (AttributeError, UnboundLocalError):
            lon = ''

        try:
            city = address.get("city")
        except (AttributeError, UnboundLocalError):
            city = ''

        try:
            country = address.get("country")
        except (AttributeError, UnboundLocalError):
            country = ''

        try:
            line = address.get("line")
        except (AttributeError, UnboundLocalError):
            line = ''

        try:
            postal_code = address.get("postal_code")
        except (AttributeError, UnboundLocalError):
            postal_code = ''

        try:
            state = address.get("state")
        except (AttributeError, UnboundLocalError):
            state = ''

        try:
            state_code = address.get("state_code")
        except (AttributeError, UnboundLocalError):
            state_code = ''

        try:
            street_name = address.get("street_name")
        except (AttributeError, UnboundLocalError):
            street_name = ''

        try:

            association = find_association(prop_details.get("details"))
        except (AttributeError):
            association = ''
        try:

            Calculated_Total_Monthly_Association_Fee = find_association_monthly(
                prop_details.get("details"))
        except (AttributeError):
            Calculated_Total_Monthly_Association_Fee = ''
        try:

            building_and_construction = find_building_and_construction(
                prop_details.get("details"))
        except (AttributeError):
            building_and_construction = ''

        try:
            adv_details = json_response.get("data").get(
                "home").get("advertisers")[0]
        except (TypeError, AttributeError, AttributeError, IndexError):
            pass

        try:
            adv_office_phone = adv_details.get(
                "office")['phones'][0].get("number")
        except (TypeError, UnboundLocalError, AttributeError, IndexError):
            adv_office_phone = ''

        try:
            adv_name = json_response.get("data").get(
                'home').get("branding")[0].get("name")
        except (TypeError, UnboundLocalError, AttributeError, IndexError):
            adv_name = ''

        try:
            if lis_id == '':
                adv_office_name = json_response.get("data").get(
                    'home').get("branding")[0].get("name")
            else:
                adv_office_name = json_response.get("data").get(
                    'home').get("branding")[1].get("name")
        except (TypeError, UnboundLocalError, AttributeError, IndexError):
            try:
                adv_office_name = json_response.get("data").get(
                    'home').get("branding")[0].get("name")
            except:
                adv_office_name = ''

        try:
            broker_city = json_response.get("data").get('home').get(
                "consumer_advertisers")[1].get("address").get('city')
            broker_state = json_response.get("data").get('home').get(
                "consumer_advertisers")[1].get("address").get('state_code')

            if broker_city is not None and broker_state is None:
                broker_location = broker_city

            elif broker_city and broker_state:

                broker_location = broker_city+","+broker_state
            else:
                broker_location = ''

        except (TypeError, AttributeError, UnboundLocalError, IndexError):

            broker_location = ''

        try:
            source = prop_details.get("source")
        except (AttributeError, UnboundLocalError, TypeError, IndexError):
            pass
        else:

            try:
                data_source = source.get('name')
            except (AttributeError, UnboundLocalError, TypeError, IndexError):
                data_source = ''

            try:
                source_property_id = source.get('listing_id')
            except (AttributeError, UnboundLocalError, TypeError, IndexError):
                source_property_id = ''

            try:

                if lis_id != '':
                    data_source_copy_right = source.get(
                        "disclaimer").get('text')
                else:
                    data_source_copy_right = source.get("disclaimer")
            except (TypeError, AttributeError, UnboundLocalError, IndexError):
                data_source_copy_right = ''

        try:
            photos = prop_details.get("photos")
        except (AttributeError, UnboundLocalError, TypeError):
            pass
        else:
            try:
                photos = [each.get("href").replace(
                    '.jpg', '-w1024_h768_x1')+'.jpg' for each in photos]
            except (TypeError, AttributeError):
                photos = ''

        yield {
            # details
            "beds": beds,
            "baths": baths,
            "baths_consolidated": baths_consolidated,
            "baths_full": baths_full,
            "baths_half": baths_half,
            "garage": garage,
            "year_built": year_built,
            "sqft": sqft,
            "lot_sqft": lot_sqft,
            "type": type,

            # location details
            "city": city,
            "country": country,
            "line": line,
            "postal_code": postal_code,
            "state": state,
            "state_code": state_code,
            "street_name": street_name,
            'latitute': lat,
            "longitude": lon,

            "property_details_text": property_details_text,

            # associations
            'association': association,
            "Calculated_Total_Monthly_Association_Fee": Calculated_Total_Monthly_Association_Fee,
            
            # building and construction
            "building_and_construction": building_and_construction,

            # advertiser info
            "represented_agent_name": adv_name,
            'agent_office_name': adv_office_name,
            'agent_office_phone': adv_office_phone,
            "broker_location": broker_location,

            # source
            'data_source': data_source,
            "source_property_id": source_property_id,
            'data_source_copy_right': data_source_copy_right,


            "price": list_price,
            "hoa_fee": hoa_fee,
            "price_per_sqft": price_per_sqft,
            "property_url": abs_url,
            "property_id":property_id,
            "photos": photos
        }
        print("\n")

    def process_response(self, response, request, spider):
        if response.status == 403:
            # Add a delay of at least 3 minutes (180 seconds)
            self.logger.warning(f"Received a 403 response. Adding a 3-minute delay.")
            sleep(60)
            # Resend the request
            return request
        return response




