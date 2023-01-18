def get_time_of_execute_function(func):
    def wrapper(list, *items):
        import timeit
        function_code = f'''{func(list, *items)}'''
        return timeit.timeit(stmt=function_code, number=10000)
    return wrapper


@get_time_of_execute_function
def add_items_to_list_var1(list, *items):
    list.clear()
    for item in items:
        list.append(item)
    return list

@get_time_of_execute_function
def add_items_to_list_var2(list, *items):
    list = [x for x in items]
    return list


def generate_sequence_of_numbers():
    import random
    return tuple(random.randint(1, 1000000) for _ in range(100000))


res1_time_value = add_items_to_list_var1(list(generate_sequence_of_numbers()), generate_sequence_of_numbers())
res2_time_value = add_items_to_list_var2(list(generate_sequence_of_numbers()), generate_sequence_of_numbers())
