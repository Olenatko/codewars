def my_parse_int(string):

    try:
        return int(string)
    except ValueError:
        return 'Nan'

print(my_parse_int("8 d"))
