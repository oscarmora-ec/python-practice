import os
from azure.cosmos import CosmosClient

#connection string from environment variable
COSMOS_CONNECTION = os.environ.get("COSMOS_CONNECTION")
DATABASE_NAME = "playspot-database"
CONTAINER_NAME = "activities"

#connect to Cosmos DB
client = CosmosClient.from_connection_string(COSMOS_CONNECTION)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# get all activities from database
def get_all_activities():
    query = "SELECT * FROM activities"
    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    return items

# filter by type - Indoor or Outdoor
def filter_by_type(activities, activity_type):
    return [a for a in activities if a["type"] == activity_type]

# filter by state - MA or NH
def filter_by_state(activities, state):
    return [a for a in activities if a["state"] == state]

# filter by age - finds activities suitable for a specific age
def filter_by_age(activities, age):
    return [a for a in activities if a["ageMin"] <= age <= a["ageMax"]]

# print activities nicely
def print_activities(activities):
    print(f"Found {len(activities)} activities")
    print("---")
    for a in activities:
        print(f"{a['name']} - {a['type']} - {a['city']}, {a['state']}")
    print("---")


#get all activities from database
all_activities = get_all_activities()

print ("--1--")

#test 1 - show all activities
print("ALL ACTIVITIES")
print_activities(all_activities)    

print ("--2--")

#test 2 - filter by Indoor only
print ("INDOOR ONLY:")
indoor = filter_by_type(all_activities, "Indoor")
print_activities(indoor)

print ("--3--")

#test 3 - filter by Massachiseets only
print("MASSACHUSETTS ONLY:")
ma_activities = filter_by_state(all_activities, "MA")
print_activities(ma_activities)

print ("--4--")

#test 4 - filter by age 5
print("SUITABLE FOR AGE 5:")
AGE_5 = filter_by_age(all_activities, 5)
print_activities(AGE_5)

print ("--5--")

#TEST 5 - combine filter - indoor in MA for age 5
print("INDOOR + MA +AGE 5:")
combined = filter_by_type(all_activities, "Indoor")
combined = filter_by_state(combined, "MA")
combined = filter_by_age(combined, 5)
print_activities(combined)
