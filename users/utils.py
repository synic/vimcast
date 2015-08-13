from somelibrary import somefunction

def calculate_stuff():
    """
    Just to demonstrate macros - `somefunction` accepts a dictionary, not a
    list of variables, so we need to convert the following variable
    definitions to a dictionary.
    """
    first_var = "somestuff"
    second_var = "someotherstuff"
    third_var = "wooters"
    fourth_var = "this is the best one for sure ;-)"
    fith_var = "What would you do with a klondike bar?"
    sixth_var = "This is the sixth variable"

    somefunction(first_var, second_var, third_var, fourth_var)
