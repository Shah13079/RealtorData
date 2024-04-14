
def find_association(detail):
    if detail:
        for each in detail:
            a = each.get("category").lower()
            if a == "homeowners association":
                each_list_text = each.get("text")
                for each_text in each_list_text:
                    if "Association:" in each_text:
                        Association = each_text.split("Association:")[-1]
                        return Association.strip()
    else:
        return ''


def find_association_monthly(detail):
    if detail:
        for each in detail:
            a = each.get("category").lower()
            if a == "homeowners association":
                each_list_text = each.get("text")
                for each_text in each_list_text:
                    if 'Calculated Total Monthly Association Fees:' in each_text:
                        association_monthly_fee = each_text.split(
                            "Calculated Total Monthly Association Fees:")[-1]
                        return association_monthly_fee.strip()
    else:
        return ''


def find_building_and_construction(detail):
    if detail:
        for each in detail:
            cat_is = each.get("category").lower()
            if "building and construction" in cat_is:
                each_list_text = each.get("text")
                return each_list_text
    else:
        return ''


##############################################################################################################################
##########################################[ Condos and Single Family Home] ###################################################

def headers_req(location):
    return {"authority": "www.realtor.com",
               "method": "POST",
               "path": "/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
               "scheme": "https",
               "accept": "application/json",
               "accept-encoding": "gzip, deflate, br",
               "accept-language": "en-US,en;q=0.9",
               "content-type": "application/json",
               "referer": f"https://www.realtor.com/realestateandhomes-search/{location}/type-condo,single-family-home,townhome/pnd-hide",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    

def condos_cities(location, page_num, offset, state_code=''):
    for_url = location.split(',')[0].replace(" ", '-') + \
        '_'+location.split(",")[-1].replace(" ", '')
    updated_payload = {
        "query": "\n  query ConsumerSearchQuery(\n    $query: HomeSearchCriteria!\n    $limit: Int\n    $offset: Int\n    $search_promotion: SearchPromotionInput\n    $sort: [SearchAPISort]\n    $sort_type: SearchSortType\n    $client_data: JSON\n    $bucket: SearchAPIBucket\n  ) {\n    home_search: home_search(\n      query: $query\n      sort: $sort\n      limit: $limit\n      offset: $offset\n      sort_type: $sort_type\n      client_data: $client_data\n      bucket: $bucket\n      search_promotion: $search_promotion\n    ) {\n      count\n      total\n      search_promotion {\n        name\n        slots\n        promoted_properties {\n          id\n          from_other_page\n        }\n      }\n      properties: results {\n        property_id\n        list_price\n        search_promotions {\n          name\n          asset_id\n        }\n        primary_photo(https: true) {\n          href\n        }\n        rent_to_own {\n          right_to_purchase\n          rent\n        }\n        listing_id\n        matterport\n        virtual_tours {\n          href\n          type\n        }\n        status\n        products {\n          products\n          brand_name\n        }\n        source {\n          id\n          type\n          spec_id\n          plan_id\n          agents {\n            office_name\n          }\n        }\n        lead_attributes {\n          show_contact_an_agent\n          opcity_lead_attributes {\n            cashback_enabled\n            flip_the_market_enabled\n          }\n          lead_type\n          ready_connect_mortgage {\n            show_contact_a_lender\n            show_veterans_united\n          }\n        }\n        community {\n          description {\n            name\n          }\n          property_id\n          permalink\n          advertisers {\n            office {\n              hours\n              phones {\n                type\n                number\n                primary\n                trackable\n              }\n            }\n          }\n          promotions {\n            description\n            href\n            headline\n          }\n        }\n        permalink\n        price_reduced_amount\n        description {\n          name\n          beds\n          baths_consolidated\n          sqft\n          lot_sqft\n          baths_max\n          baths_min\n          beds_min\n          beds_max\n          sqft_min\n          sqft_max\n          type\n          sub_type\n          sold_price\n          sold_date\n        }\n        location {\n          street_view_url\n          address {\n            line\n            postal_code\n            state\n            state_code\n            city\n            coordinate {\n              lat\n              lon\n            }\n          }\n          county {\n            name\n            fips_code\n          }\n        }\n        open_houses {\n          start_date\n          end_date\n        }\n        branding {\n          type\n          name\n          photo\n        }\n        flags {\n          is_coming_soon\n          is_new_listing(days: 14)\n          is_price_reduced(days: 30)\n          is_foreclosure\n          is_new_construction\n          is_pending\n          is_contingent\n        }\n        list_date\n        photos(limit: 2, https: true) {\n          href\n        }\n        advertisers {\n          type\n          builder {\n            name\n            href\n            logo\n          }\n        }\n      }\n    }\n  }\n",
        "variables": {
            "geoSupportedSlug": f"{for_url}",
            "query": {
                "primary": True,
                "status": ["for_sale", "ready_to_build"],
                "search_location": {"location": f"{location}"},
                "type": [
                    "condos",
                    "condo_townhome_rowhome_coop",
                    "condo_townhome",
                    "single_family",
                    "townhomes",
                    "duplex_triplex",
                ],
                "pending": False,
                "contingent": False,
            },
            "client_data": {"device_data": {"device_type": "tablet"}},
            "limit": 42,
            "offset": offset,
            "sort_type": "relevant",
            "bucket": {"sort": "fractal_v2.1.3"},
            "search_promotion": {"name": "CITY", "slots": [], "promoted_properties": [[]]},
        },
        "seoPayload": {
            "asPath": f"/realestateandhomes-search/{for_url}/pg-{page_num}",
            "pageType": {"silo": "search_result_page", "status": "for_sale"},
            "county_needed_for_uniq": False,
            "isFaqSupport": True,
        },
        "isClient": True,
        "visitor_id": "08531dff-eff5-4ea2-a079-3034f83021a4" }
    return updated_payload


def states_new_page_query(state_name, state_code, page_num, offset):
    state_name_url = state_name.strip().replace(" ", "-")
    updated_payload = {
    "query": "\n  query ConsumerSearchQuery(\n    $query: HomeSearchCriteria!\n    $limit: Int\n    $offset: Int\n    $search_promotion: SearchPromotionInput\n    $sort: [SearchAPISort]\n    $sort_type: SearchSortType\n    $client_data: JSON\n    $bucket: SearchAPIBucket\n  ) {\n    home_search: home_search(\n      query: $query\n      sort: $sort\n      limit: $limit\n      offset: $offset\n      sort_type: $sort_type\n      client_data: $client_data\n      bucket: $bucket\n      search_promotion: $search_promotion\n    ) {\n      count\n      total\n      search_promotion {\n        name\n        slots\n        promoted_properties {\n          id\n          from_other_page\n        }\n      }\n      properties: results {\n        property_id\n        list_price\n        search_promotions {\n          name\n          asset_id\n        }\n        primary_photo(https: true) {\n          href\n        }\n        rent_to_own {\n          right_to_purchase\n          rent\n        }\n        listing_id\n        matterport\n        virtual_tours {\n          href\n          type\n        }\n        status\n        products {\n          products\n          brand_name\n        }\n        source {\n          id\n          type\n          spec_id\n          plan_id\n          agents {\n            office_name\n          }\n        }\n        lead_attributes {\n          show_contact_an_agent\n          opcity_lead_attributes {\n            cashback_enabled\n            flip_the_market_enabled\n          }\n          lead_type\n          ready_connect_mortgage {\n            show_contact_a_lender\n            show_veterans_united\n          }\n        }\n        community {\n          description {\n            name\n          }\n          property_id\n          permalink\n          advertisers {\n            office {\n              hours\n              phones {\n                type\n                number\n                primary\n                trackable\n              }\n            }\n          }\n          promotions {\n            description\n            href\n            headline\n          }\n        }\n        permalink\n        price_reduced_amount\n        description {\n          name\n          beds\n          baths_consolidated\n          sqft\n          lot_sqft\n          baths_max\n          baths_min\n          beds_min\n          beds_max\n          sqft_min\n          sqft_max\n          type\n          sub_type\n          sold_price\n          sold_date\n        }\n        location {\n          street_view_url\n          address {\n            line\n            postal_code\n            state\n            state_code\n            city\n            coordinate {\n              lat\n              lon\n            }\n          }\n          county {\n            name\n            fips_code\n          }\n        }\n        open_houses {\n          start_date\n          end_date\n        }\n        branding {\n          type\n          name\n          photo\n        }\n        flags {\n          is_coming_soon\n          is_new_listing(days: 14)\n          is_price_reduced(days: 30)\n          is_foreclosure\n          is_new_construction\n          is_pending\n          is_contingent\n        }\n        list_date\n        photos(limit: 2, https: true) {\n          href\n        }\n        advertisers {\n          type\n          builder {\n            name\n            href\n            logo\n          }\n        }\n      }\n    }\n  }\n",
    "variables": {
        "geoSupportedSlug": state_name_url,
        "query": {
            "primary": True,
            "status": ["for_sale", "ready_to_build"],
            "search_location": {"location": state_name},
            "type": [
                "condos",
                "condo_townhome_rowhome_coop",
                "condo_townhome",
                "single_family",
                "townhomes",
                "duplex_triplex",
            ],
            "pending": False,
            "contingent": False,
        },
        "client_data": {"device_data": {"device_type": "tablet"}},
        "limit": 42,
        "offset": offset,
        "sort_type": "relevant",
        "bucket": {"sort": "fractal_v2.1.3"},
    },
    "seoPayload": {
        "asPath": f"/realestateandhomes-search/{state_name_url}/pg-{page_num}",
        "pageType": {"silo": "search_result_page", "status": "for_sale"},
        "county_needed_for_uniq": False,
        "isFaqSupport": False,
    },
    "isClient": True,
    "visitor_id": "08531dff-eff5-4ea2-a079-3034f83021a4"     }

    return updated_payload