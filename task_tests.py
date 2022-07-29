from task_functions import *

# Assert statements (0.0/14.0)

"""
get_new_task
delete_item
update_task
get_written_date
"""

assert is_valid_name("abcde")
assert not is_valid_name('a')

assert is_valid_index('1', [{'name' : 'test', 'info' : 'test','proitity':'5','duedate':'test','done':'test'}], start_idx = 1)
assert not is_valid_index('2', [{'name' : 'test', 'info' : 'test','proitity':'5','duedate':'test','done':'test'}], start_idx = 1)

assert is_valid_month('01')
assert not is_valid_month('KVJSBVJBDSK')

assert is_valid_day('27')
assert not is_valid_day('33')


assert is_valid_year('1999')
assert not is_valid_year('19')

assert is_valid_date('01/01/1999')
assert not is_valid_date('01/099')

assert is_valid_priority('1', {
        1: "Lowest",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Highest"
    })
assert not is_valid_priority('8', {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
})

assert is_valid_completion('no')
assert not is_valid_completion('ffof')


assert get_new_task(["foobar", "bla", "2", "01/01/1999", "no"], {
        1: "Lowest",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Highest"
    }) == {
        "name": "foobar",
        "info": "bla",
        "priority": 2,
        "duedate": "01/01/1999",
        "done": "no"
    }

assert get_new_task(["foobar", "bla", "2", "01/01/1999", "yes"], {
        1: "Lowest",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Highest"
    }) == {
        "name": "foobar",
        "info": "bla",
        "priority": 2,
        "duedate": "01/01/1999",
        "done": "yes"
    }

assert delete_item([{'name' : 'test', 'info' : 'test','proitity':5,'duedate':'test','done':'test'}], '1', start_idx=1) == {
    'name' : 'test', 'info' : 'test','proitity':5,'duedate':'test','done':'test'} 

assert delete_item([{'name' : 'test2', 'info' : 'test','proitity':5,'duedate':'test','done':'test'}], '1', start_idx=1) == {
    'name' : 'test2', 'info' : 'test','proitity':5,'duedate':'test','done':'test'} 

assert update_task([{'name' : 'test', 'info' : 'test','proitity':5,'duedate':'test','done':'test'}], '1', {
        1: "Lowest",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Highest"
    }, "name", "test2", start_idx=1) == {'name' : 'test2', 'info' : 'test','proitity':5,'duedate':'test','done':'test'}

assert update_task([{'name' : 'test', 'info' : 'test','proitity':5,'duedate':'test','done':'test'}], '1', {
        1: "Lowest",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Highest"
    }, "info", "test2", start_idx=1) == {'name' : 'test', 'info' : 'test2','proitity':5,'duedate':'test','done':'test'}

assert get_written_date("01/01/1999") == "January 1, 1999"
assert get_written_date("01/01/1998") == "January 1, 1998"

assert load_tasks_from_csv("foobar.csv", [], {
        1: "Lowest",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Highest"
    }) == None

assert load_tasks_from_csv("foobar23.csv", [], {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}) == None






