def linear(some_list):
    if any(isinstance(i, list) for i in some_list):
        i = 0
        while i != len(some_list):
            if isinstance(some_list[i], list):
                new_list = linear(some_list[i])
                del some_list[i]
                for j in new_list:
                    some_list.insert(i, j)
                    i += 1
            else:
                i += 1
    return some_list








