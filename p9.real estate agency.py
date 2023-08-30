import pandas as pd
import numpy as np
data = {
    'Property_ID': [6574, 7321, 9846, 3758, 7574, 2323, 1048, 9999, 8888, 3691],
    'Location': ['LA', 'Paris', 'LA', 'Las vegas', 'NY', 'Malaysia', 'LA', 'Shinjuku', 'Shinjuku', 'Germany'],
    'No_of_bedroom': [3, 8, 4, 2, 3, 2, 2, 3, 2, 5],
    'Area_in_sqft': [400, 1200, 900, 300, 450, 250, 280, 500, 400, 750],
    'listing_price': [20000, 90000, 25000, 15000, 25000, 20000, 18000, 27000, 17000, 40000]}
property_data = pd.DataFrame(data)
print(f"\nThe data set for the real estate agency :\n {property_data}")
avg_listing_price = property_data.groupby('Location')['listing_price'].mean()
print(f"\nThe average listing price of properties in each location : \n {avg_listing_price}")
Properties_4BHK = property_data[property_data['No_of_bedroom'] > 4]
print(f"\nThe number of properties with more than four bedrooms : \n {Properties_4BHK}")
property_with_large_area = property_data['Area_in_sqft'].max()
print(f"\nThe property with the largest area : {property_with_large_area}")
