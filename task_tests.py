from task_functions import *

### Test all-cases for the print_main_menu(menu) function ###
# arg1 = menu
# result = print_main_menu(arg1)
# expected_result = ''
# print(f"--> print_main_menu({arg1}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the get_selection(action, suboptions, to_upper=True, go_back=False) function ###
# arg1 = action
# arg2 = suboptions
# result = get_selection(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> get_selection({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the print_task(task, priority_map, name_only=False) function ###
# arg1 = task
# arg2 = priority_map
# result = print_task(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> print_task({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the get_written_date(date_input) function ###
# arg1 = date_input
# result = get_written_date(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> get_written_date({arg1}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the print_tasks(task_list, priority_map, name_only=False, show_idx=False, start_idx=0, completed="all") function ###
# arg1 = task_list
# arg2 = priority_map
# result = print_tasks(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> print_tasks({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the get_new_task(task_list, priority_map, name_only=False, show_idx=False, start_idx=0, completed="all") function ###
# arg1 = task_list
# arg2 = priority_map
# result = get_new_task(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> get_new_task({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the is_valid_name(name) function ###
# arg1 = name
# result = is_valid_name(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_name({arg1}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the is_valid_priority(priority) function ###
# arg1 = priority
# result = is_valid_priority(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_priority({arg1}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the is_valid_date(date) function ###
# arg1 = date
# result = is_valid_date(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_date({arg1}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the is_valid_completion(completion) function ###
# arg1 = completion
# result = is_valid_completion(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_completion({arg1}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the is_valid_index(idx, in_list, start_idx = 0) function ###
# arg1 = idx
# arg2 = in_list
# result = is_valid_index(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_index({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0) function ###
# arg1 = info_list
# arg2 = idx
# arg3 = priority_map
# arg4 = field_key
# arg5 = field_info
# result = update_task(arg1, arg2, arg3, arg4, arg5)
# expected_result = 'You selected option L to > List.'
# print(f"--> update_task({arg1, arg2, arg3, arg4, arg5}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the delete_item(in_list, idx, start_idx = 0) function ###
# arg1 = in_list
# arg2 = idx
# result = delete_item(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> delete_item({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the load_tasks_from_csv(filename, in_list, priority_map) function ###
# arg1 = filename
# arg2 = in_list
# arg3 = priority_map
# result = load_tasks_from_csv(arg1, arg2, arg3)
# expected_result = 'You selected option L to > List.'
# print(f"--> load_tasks_from_csv({arg1, arg2, arg3}) returned `{result}`\n")
# assert result == expected_result

### Test all-cases for the save_tasks_to_csv(tasks_list, filename) function ###
# arg1 = tasks_list
# arg2 = filename
# result = save_tasks_to_csv(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> save_tasks_to_csv({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result