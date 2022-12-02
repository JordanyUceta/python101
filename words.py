x = "jordy" 
y = x.upper()


def print_upper_words(lists, must_start_with):
    """
    function takes the list and returns it with every word uppercased
    """
    
    for y in must_start_with:
        for x in lists: 
            if x[0] == y:
                print(x.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],["h", "y"])
