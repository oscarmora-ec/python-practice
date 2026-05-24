#this is a momment in Python
#commets start with # just like bash scripts

#print shows text on screen

print("Hello World")

#variable stores values
#no need to declare type like on other languages

name = "Oscar"
age = 36
city = "Lawrence"

#print with variables

print(name)
print(age)
print(city)

#f-string - combnes text and variables in one line
# f before the quote means format string
# {variable} inserts the variable value into the string

print (f"My name is {name}, I am {age} years old and I live in {city}.")
print (f"{city} is a great place")

# list sotres multiple values in one variable
#square brackets define a list
#comma separates each item in the list

activities = ["Shawsheen Park", "Kidville", "Discovery Museum"]

#print the whole list
print(activities)

#print one item by index
#index starts at 0 not 1

print(activities[0])
print(activities[1])
print(activities[2])

print(len(activities)) #len counts how many items are in the list

# dictionary stores key-value pairs
#curly braces denines a dictionary
#colon separes key and value
activity = {
    "name": "Shawsheen Park",
    "type": "outdoor",
    "city": "Andover",
    "ageMin": 2,
    "ageMax": 10
}

# print the whole dictionary
print(activity)

#access one values by key
print(activity["name"])
print(activity["type"])         
print(activity["city"])

#d-string with dictionary values
print (f"{activity['name']} is in {activity['city']}")
print()
print()
print()
print()

#for loop goes through each item in a list or dictionary
#activity is a temporary variable that holds each item
#you choose the same -it can be anything
for activity in activities:
    print(activity)

#loop with index number
for i in range(len(activities)):
    print(f"{i}: {activities[i]}")


print()
print()
print()

#list of dictionaries - like Cosmos DB activities
playspot_activities = [
    {
        "name": "Shawsheen River Park",
        "type": "Outdoor", 
        "city": "Andover",
    }
    ,
    {
        "name": "Kidville Indoor Play",
        "type": "Indoor", 
        "city": "Burlington"
    },  
    {
        "name": "Discovery Museum",
        "type": "Indoor", 
        "city": "Acton"
    }
]

# loop thorugh and print each activity nicely
for activity in playspot_activities:
    print(f"{activity['name']} - {activity['type']} - {activity['city']}")


print()
print() 

#def keyword defines a function - a reusable block of code that performs a specific task
#function name is get_activity_info
#print_acitivity is the function name
#activity is the parameter it accepts
def print_activity(activity):
    print(f"Name: {activity['name']}")
    print(f"Type: {activity['type']}")
    print(f"City: {activity['city']}")
    print("------------------- ")

#call the function for each acivity in the list
for activity in playspot_activities:
    print_activity(activity)