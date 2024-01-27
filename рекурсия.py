def recursive_sum(n_list):
    total_sum = 0
    for item in n_list:
        if isinstance(item, list):
            total_sum += recursive_sum(item)
        else:
            total_sum += item
    return total_sum
my_list = [1, [2, [3, 4], 5], 6, [7, 8]]
recursive_sum(my_list)
