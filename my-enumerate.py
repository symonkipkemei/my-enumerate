

courses = ["biology","chemistry","maths","physics","cre","geography"]

#create a function that takes up an iterable

def my_enumerate(iterable,start_point = 0) -> list:
    """Add index to an iterable element

    Args:
        iterable (list,tuple,string): anything that can be iterated over.
        start_point (int): the starting index where the iterable items are counted from, the default start point is 0


    Returns:
        list: A list with the index and each item on iterable paired together in a tuple
    """
    
    # store the tuples (combined index and item ) in a list
    items = []
    #retract starting point by 1,so that the first item on loop is assigned the appropiate value
    start_point = start_point -1

    for item in iterable:
        start_point += 1
        #store start point and item in pairs
        item_tuple = (start_point,item)
        items.append(item_tuple)

    return items

#unpacking the tuples
for index, item in my_enumerate(courses, 1):
    print(index, item)

    