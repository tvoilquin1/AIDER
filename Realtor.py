import getpass
import requests
import json

def get_search_criteria():
    area = input("Enter the area (city, zip, county): ")
    min_price = input("Enter the minimum price: ")
    max_price = input("Enter the maximum price: ")
    min_bedrooms = input("Enter the minimum number of bedrooms: ")
    min_bathrooms = input("Enter the minimum number of bathrooms: ")
    
    return area, min_price, max_price, min_bedrooms, min_bathrooms

def build_request(area, min_price, max_price, min_bedrooms, min_bathrooms):
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
        "baths_min":min_bathrooms
    }
    headers = {
        'x-rapidapi-host': "realtor.p.rapidapi.com",
        'x-rapidapi-key': "4ec7cd8216msh9f286dac0bb2dc6p182bfejsn34d7ca9d0a57"
    }
    
    return url, headers, querystring

def make_request(url, headers, querystring):
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = json.loads(response.text)
        properties = data.get('properties', [])
        if properties:
            urls = [property.get('rdc_web_url') for property in properties]
            return urls
        else:
            return None
    else:
        return None

def main():
    area, min_price, max_price, min_bedrooms, min_bathrooms = get_search_criteria()
    url, headers, querystring = build_request(area, min_price, max_price, min_bedrooms, min_bathrooms)
    urls = make_request(url, headers, querystring)
    if urls is not None:
        for url in urls:
            print(url)
    else:
        print("Failed to get response from API.")

if __name__ == "__main__":
    main()
def validate_input(area, min_price, max_price, min_bedrooms, min_bathrooms):
    if not area or not min_price or not max_price or not min_bedrooms or not min_bathrooms:
        print("All fields are required.")
        return False
    if not min_price.isdigit() or not max_price.isdigit() or not min_bedrooms.isdigit() or not min_bathrooms.isdigit():
        print("Price, bedrooms, and bathrooms fields must be numbers.")
        return False
    if int(min_price) > int(max_price):
        print("Minimum price cannot be greater than maximum price.")
        return False
    if int(min_bedrooms) < 0 or int(min_bathrooms) < 0:
        print("Bedrooms and bathrooms fields cannot be negative.")
        return False
    return True
