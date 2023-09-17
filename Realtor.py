import getpass
import requests
import json

def get_search_criteria():
    area = input("Enter the area (city, zip, county): ")
    min_price = input("Enter the minimum price: ")
    max_price = input("Enter the maximum price: ")
    min_bedrooms = input("Enter the minimum number of bedrooms: ")
    min_bathrooms = input("Enter the minimum number of bathrooms: ")
    min_garage = input("Enter the minimum number of car garage: ")
    
    return area, min_price, max_price, min_bedrooms, min_bathrooms, min_garage

def build_request(area, min_price, max_price, min_bedrooms, min_bathrooms, min_garage):
    url = "https://realtor.p.rapidapi.com/properties/v3/list"
    querystring = {
        "sort":"relevance",
        "city":area,
        "limit":"200",
        "offset":"0",
        "state_code":"WA",
        "price_min":min_price,
        "price_max":max_price,
        "beds_min":min_bedrooms,
        "baths_min":min_bathrooms,
        "garage":min_garage
    }
    headers = {
        'x-rapidapi-host': "realtor.p.rapidapi.com",
        'x-rapidapi-key': "4ec7cd8216msh9f286dac0bb2dc6p182bfejsn34d7ca9d0a57"
    }
    
    return url, headers, querystring

def make_request(url, headers, querystring):
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

def main():
    area, min_price, max_price, min_bedrooms, min_bathrooms, min_garage = get_search_criteria()
    url, headers, querystring = build_request(area, min_price, max_price, min_bedrooms, min_bathrooms, min_garage)
    response = make_request(url, headers, querystring)
    if response is not None:
        print(json.dumps(response, indent=4))
    else:
        print("Failed to get response from API.")

if __name__ == "__main__":
    main()
