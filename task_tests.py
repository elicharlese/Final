from task_functions import *

### Test all-cases for the get_selection() function ###
arg1 = the_menu["L"]
result = get_selection(arg1, list_menu)
expected_result = 'You selected option L to > List.'
print(f"--> get_selection({arg1, list_menu}) returned `{result}`\n")
assert result == expected_result