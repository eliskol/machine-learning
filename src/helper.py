def put_last_entry_first(list):
    output_list = []
    output_list.append(list[-1])
    for i in range(0, len(list) - 1):
        output_list.append(list[i])
    return output_list
