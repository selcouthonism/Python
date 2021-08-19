import json
import math

office_lat = math.radians(53.339428)
office_long = math.radians(-6.257664)
requested_range = 100
customer_dict = {}

# This method calculates range between two positions.
# Method takes latitude and longitude parameters in degree.
def calculateRange(customer_lat, customer_long):

    customer_lat = math.radians(float(customer_lat))
    customer_long = math.radians(float(customer_long))
    
    
    angle = math.acos(math.sin(office_lat) * math.sin(customer_lat)
        + math.cos(office_lat) * math.cos(customer_lat) * math.cos(abs(office_long - customer_long)));
    
    # convert back to degrees
    angle = math.degrees(angle);
    
    # each degree on a great circle of Earth is 60 nautical miles. 1 NM = 1.85200 KM
    range = 60 * 1.85200 * angle;		
    
    return int(range)

def open_file_and_find_customer(path):
    with open(path + os.path.sep + "customer.txt", "r") as f:
        for line in f.readlines():
            customer = json.loads(line)
            if calculateRange(customer["latitude"], customer["longitude"]) < requested_range:
                customer_dict[customer["user_id"]] = customer["name"]
                
 
 def sort_and_write_to_file():
     with open("invited_customers.txt", "w+") as f:
        for (customer_id, customer_name) sorted(customer_dict):
            f.write(customer_id + " " + customer_name)

open_file_and_find_customer()
sort_and_write_to_file()

# some JSON:
customer_info = '{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}'

# parse
customer = json.loads(customer_info)
print(calculateRange(customer["latitude"], customer["longitude"]))

#read args from terminal
#https://stackoverflow.com/questions/70797/how-to-prompt-for-user-input-and-read-command-line-arguments
