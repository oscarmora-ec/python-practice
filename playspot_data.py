#playSpot Cosmos DB reader
#this script connects to our real Cosmos DB
#and reads activities just like our azure function does

#import the Cosmos DB library we just intalled
#import string

import os

from azure.cosmos import CosmosClient



# connection string from environment variable
# never hardcode secrets in code
COSMOS_CONNECTION = os.environ.get("COSMOS_CONNECTION")

#database and container names - same as in our Azure Function
DATABASE_NAME = "playspot-database"
CONTAINER_NAME = "activities"

# create a client using the connection string
client = CosmosClient.from_connection_string(COSMOS_CONNECTION)

#get reference to the database
database = client.get_database_client(DATABASE_NAME)

#get reference to the container
container = database.get_container_client(CONTAINER_NAME)

#query all activities - same query we wrote in Cosmos DB portal
query = "SELECT * FROM activities"

#excecute the query and get results
items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True  
))

#print how many activities we found
print(f"found {len(items)} activities")
print("----")

# loop through and print each activity
for item in items:
    print(f"Name: {item['name']}")
    print(f"Type: {item['type']}")
    print(f"City: {item['city']}")
    print("----")

