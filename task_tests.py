from task_functions import *
from task_system import *

# Assert statements (0.0/14.0)

### Test all-cases for the print_main_menu(menu) function ###
arg1 = the_menu
result = print_main_menu(arg1)
expected_result = None
print(f"--> print_main_menu({arg1}) returned `{result}`\n")
assert result == expected_result

### Test all-cases for the get_selection(action, suboptions, to_upper=True, go_back=False) function ###
# Test action = 'L'
arg1 = 'L'
arg2 = list_menu
result = get_selection(arg1, arg2)
expected_result = 'List'
print(f"--> get_selection({arg1, arg2}) returned `{result}`\n")
assert result == expected_result
# Test action = 'A'
arg1 = 'A'
arg2 = list_menu
result = get_selection(arg1, arg2)
expected_result = 'A'
print(f"--> get_selection({arg1, arg2}) returned `{result}`\n")
assert result == expected_result
# Test action = 'C'
arg1 = 'C'
arg2 = list_menu
result = get_selection(arg1, arg2)
expected_result = 'C'
print(f"--> get_selection({arg1, arg2}) returned `{result}`\n")
assert result == expected_result


# ### Test all-cases for the print_task(task, priority_map, name_only=False) function ###
# # Test name_only = False
# arg1 = task
# arg2 = priority_map
# result = print_task(arg1, arg2)
# expected_result = None
# print(f"--> print_task({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the get_written_date(date_input) function ###
# arg1 = date_input
# result = get_written_date(arg1)
# expected_result = None
# print(f"--> get_written_date({arg1}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the print_tasks(task_list, priority_map, name_only=False, show_idx=False, start_idx=0, completed="all") function ###
# arg1 = task_list
# arg2 = priority_map
# result = print_tasks(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> print_tasks({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the get_new_task(task_list, priority_map, name_only=False, show_idx=False, start_idx=0, completed="all") function ###
# arg1 = task_list
# arg2 = priority_map
# result = get_new_task(arg1, arg2)
# expected_result = None
# print(f"--> get_new_task({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the is_valid_name(name) function ###
# # Test with a valid name
# arg1 = 'Test'
# result = is_valid_name(arg1)
# expected_result = type()
# print(f"--> is_valid_name({arg1}) returned `{result}`\n")
# assert result == expected_result
# # Test with an invalid name
# arg1 = ''
# result = is_valid_name(arg1)
# expected_result = type()
# print(f"--> is_valid_name({arg1}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the is_valid_priority(priority) function ###
# # Test with a valid priority
# arg1 = 1
# result = is_valid_priority(arg1)
# expected_result = True
# print(f"--> is_valid_priority({arg1}) returned `{result}`\n")
# assert result == expected_result
# # Test with an invalid priority
# arg1 = 7
# result = is_valid_priority(arg1)
# expected_result = True
# print(f"--> is_valid_priority({arg1}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the is_valid_date(date) function ###
# # Test with a valid date
# arg1 = '2020-01-01'
# result = is_valid_date(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_date({arg1}) returned `{result}`\n")
# assert result == expected_result
# # Test with an invalid date
# arg1 = 'JAN 01 2020'
# result = is_valid_date(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_date({arg1}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the is_valid_completion(completion) function ###
# # Test with a valid completion
# arg1 = 'done'
# result = is_valid_completion(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_completion({arg1}) returned `{result}`\n")
# assert result == expected_result
# # Test with an invalid
# arg1 = 'invalid'
# result = is_valid_completion(arg1)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_completion({arg1}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the is_valid_index(idx, in_list, start_idx = 0) function ###
# arg1 = idx
# arg2 = in_list
# result = is_valid_index(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> is_valid_index({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0) function ###
# # Test if info_list contains empty string
# arg1 = info_list
# arg2 = idx
# arg3 = priority_map
# arg4 = field_key
# arg5 = field_info
# result = update_task(arg1, arg2, arg3, arg4, arg5)
# expected_result = 'You selected option L to > List.'
# print(f"--> update_task({arg1, arg2, arg3, arg4, arg5}) returned `{result}`\n")
# assert result == expected_result
# # Test if idx is invalid
# arg1 = info_list
# arg2 = idx
# arg3 = priority_map
# arg4 = field_key
# arg5 = field_info
# result = update_task(arg1, arg2, arg3, arg4, arg5)
# expected_result = 'You selected option L to > List.'
# print(f"--> update_task({arg1, arg2, arg3, arg4, arg5}) returned `{result}`\n")
# assert result == expected_result
# # Test if field_key is invalid
# arg1 = info_list
# arg2 = idx
# arg3 = priority_map
# arg4 = field_key
# arg5 = field_info
# result = update_task(arg1, arg2, arg3, arg4, arg5)
# expected_result = 'You selected option L to > List.'
# print(f"--> update_task({arg1, arg2, arg3, arg4, arg5}) returned `{result}`\n")
# assert result == expected_result
# # Test if validation passes for info_list[idx]
# arg1 = info_list
# arg2 = idx
# arg3 = priority_map
# arg4 = field_key
# arg5 = field_info
# result = update_task(arg1, arg2, arg3, arg4, arg5)
# expected_result = 'You selected option L to > List.'
# print(f"--> update_task({arg1, arg2, arg3, arg4, arg5}) returned `{result}`\n")
# assert result == expected_result
# # Test if validation fails return field_key
# arg1 = info_list
# arg2 = idx
# arg3 = priority_map
# arg4 = field_key
# arg5 = field_info
# result = update_task(arg1, arg2, arg3, arg4, arg5)
# expected_result = 'You selected option L to > List.'
# print(f"--> update_task({arg1, arg2, arg3, arg4, arg5}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the delete_item(in_list, idx, start_idx = 0) function ###
# # Test if input_list is empty
# arg1 = in_list
# arg2 = idx
# result = delete_item(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> delete_item({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result
# # Test if idx id not type string
# arg1 = in_list
# arg2 = idx
# result = delete_item(arg1, arg2)
# expected_result = None
# print(f"--> delete_item({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result
# # Test if start_idx is not type int
# arg1 = in_list
# arg2 = idx
# result = delete_item(arg1, arg2)
# expected_result = None
# print(f"--> delete_item({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result
# # Test is_valid_index(idx, in_list, start_idx = 0) returns False
# arg1 = in_list
# arg2 = idx
# result = delete_item(arg1, arg2)
# expected_result = -1
# print(f"--> delete_item({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result
# # Test if success which returns the element removed from the input list
# arg1 = in_list
# arg2 = idx
# result = delete_item(arg1, arg2)
# expected_result = 'You selected option L to > List.'
# print(f"--> delete_item({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the load_tasks_from_csv(filename, in_list, priority_map) function ###
# # Test last 4 characters of filename are not .csv
# arg1 = filename
# arg2 = in_list
# arg3 = priority_map
# result = load_tasks_from_csv(arg1, arg2, arg3)
# expected_result = -1
# print(f"--> load_tasks_from_csv({arg1, arg2, arg3}) returned `{result}`\n")
# assert result == expected_result
# # Test if `filename` is not a string
# arg1 = filename
# arg2 = in_list
# arg3 = priority_map
# result = load_tasks_from_csv(arg1, arg2, arg3)
# expected_result = -1
# print(f"--> load_tasks_from_csv({arg1, arg2, arg3}) returned `{result}`\n")
# assert result == expected_result
# # Test if the entire file is read from `in list`
# arg1 = filename
# arg2 = in_list
# arg3 = priority_map
# result = load_tasks_from_csv(arg1, arg2, arg3)
# expected_result = -1
# print(f"--> load_tasks_from_csv({arg1, arg2, arg3}) returned `{result}`\n")
# assert result == expected_result

# ### Test all-cases for the save_tasks_to_csv(tasks_list, filename) function ###
# # Test if the last 4 characters of the filename are not .csv
# arg1 = tasks_list
# arg2 = filename
# result = save_tasks_to_csv(arg1, arg2)
# expected_result = -1
# print(f"--> save_tasks_to_csv({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result
# # Test if able to successfully write to the `filename`
# arg1 = tasks_list
# arg2 = filename
# result = save_tasks_to_csv(arg1, arg2)
# expected_result = None
# print(f"--> save_tasks_to_csv({arg1, arg2}) returned `{result}`\n")
# assert result == expected_result