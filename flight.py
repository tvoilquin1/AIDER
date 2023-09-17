import requests
import json

def get_cheapest_flights(start_date, end_date, start_city, end_city):
    # API endpoint
    url = "http://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/US/USD/en-US/{}/{}/{}/?apiKey=YOUR_API_KEY".format(start_city, end_city, start_date, end_date)

    # Making our request
    response = requests.get(url)

    # Converting the response to JSON
    data = response.json()

    # Getting the quotes
    quotes = data['Quotes']

    # Sorting the quotes by price
    sorted_quotes = sorted(quotes, key=lambda k: k['MinPrice'])

    # Getting the top 5 quotes
    top_5_quotes = sorted_quotes[:5]

    # Printing the top 5 quotes
    for quote in top_5_quotes:
        print("Airline: {}, Flight Number: {}, Departure Time: {}, Arrival Time: {}, Price: {}".format(quote['OutboundLeg']['CarrierIds'][0], quote['QuoteId'], quote['OutboundLeg']['DepartureDate'], quote['InboundLeg']['DepartureDate'], quote['MinPrice']))
