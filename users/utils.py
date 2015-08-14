from somelibrary import somefunction


def calculate_stuff():
    """
    Just to demonstrate macros - `somefunction` accepts a dictionary, not a
    list of variables, so we need to convert the following variable
    definitions to a dictionary.

    To record the macro to change these lines to a dictionary definition:

    Put the cursor on the first line
    1.  Press qa      - starts recording in register `a`
    2.  Press ^       - go to the beginning of the current line
    3.  Press i"      - go to insert mode and insert a "
    4.  Press Escape  - exit insert mode
    5.  Press ww      - jump forward the next two "words"
    6.  Press h       - move back one character
    7.  Press i"      - go to insert mode and insert a "
    8.  Press Escape  - exit insert mode
    9.  Press l       - move right one character
    10. Press x       - delete the current character
    11. Press r:      - replace the current character with a :
    12. Press A,      - move the cursor to the end of the line, enter insert
                        mode, and insert a comma
    13. Press Escape  - exit insert mode
    14. Press j       - move down one line
    15. Press q       - stop recording

    Now to run the macro on the next line, type @a (which means, "run the
    macro in register `a`").

    """
    first_var = "somestuff"
    second_var = "someotherstuff"
    third_var = "wooters"
    fourth_var = "this is the best one for sure ;-)"
    fith_var = "What would you do with a klondike bar?"
    sixth_var = "This is the sixth variable"

    somefunction(first_var, second_var, third_var, fourth_var)
