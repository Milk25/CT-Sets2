our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}



def unique_destinations_in_flight():
    unique_flights = our_routes.intersection(competitor_routes)
    print(unique_flights)


unique_destinations_in_flight()



def compare_destinations():
    compare = our_routes.union(competitor_routes)
    print(compare)

compare_destinations()





def difference_in_flights():
    difference = our_routes.symmetric_difference(competitor_routes)
    different = set(difference)
    if different == difference:
        print("Destinations which are different:", difference)
    else:
        print("Destinations are the same!")


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
difference_in_flights()







# def compare_flight_routes(our_routes, competitor_routes):
#     same_flights = our_routes.intersection(competitor_routes)

#     unique_flights = our_routes.difference(competitor_routes)

#     neither_flights_the_same = our_routes.symmetric_difference(competitor_routes)

#     return same_flights, unique_flights, neither_flights_the_same

# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
# same_flights, unique_flights, neither_flights_the_same = compare_flight_routes(our_routes, competitor_routes)

# print("Common flights:", same_flights)
# print("Unique destinations:", unique_flights)
# print("Destinations that neither airline shares:", neither_flights_the_same)