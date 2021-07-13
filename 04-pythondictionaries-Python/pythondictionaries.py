"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of cities
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of cities)
1
American City
American City
2
Asian City - Country
Asian City - Country"""


def add(locations):
    locations.update({"Asia": {'India':['Bangalore']}})
    locations.update({"Africa":{"Egypt":["Cairo"]}})
    locations["North America"]["USA"].append("Atlanta")
    locations["Asia"].update({'China':['Shanghai']})
    return locations
def sortUSA():	
    locations=add(locations = {'North America': {'USA': ['Mountain View']}})
    a=locations["North America"]["USA"]
    a.sort()
    return a
def alphaAsia():
    str=""
    lis=[]
    locations=add(locations = {'North America': {'USA': ['Mountain View']}})
    b=locations["Asia"]
    for j in b:
        a=locations["Asia"][j]
        for i in a:
            str+=i+" - "+j
            lis.append(str)
            str=""
    return lis

# Note: Check for test cases to understand the output format.
add(locations = {'North America': {'USA': ['Mountain View']}})