def format_itineraries(itineraries):
    formatted_str = ""
    
    for i, itinerary in enumerate(itineraries, 1):
        # Unpacking the tuple
        traveler_name, origin, destination = itinerary
        
        # Formatting each itinerary
        formatted_str += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    
    return formatted_str.strip()

# Sample input
itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

# Calling the function
result = format_itineraries(itineraries)
print(result)
