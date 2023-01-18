def get_time_of_execute_function(func):
    def wrapper():
        import timeit
        function_code = "func()"
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


