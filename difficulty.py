def difficulty_level(level):
    test_num_range = ()
    if level == 1:
        test_num_range = (0, 10)
    elif level == 2:
        test_num_range = (0, 25)
    elif level == 3:
        test_num_range = (0, 100)
    return test_num_range
