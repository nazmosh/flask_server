# flask_server

Basic implementation of a counting server that takes a JSON as part of a POST request, and updates its internal counter with the POST payload's "count" JSON element. 

## Methods
- *get_count()* - Retrieves the value of the internal counter and returns it along with the current time:
`{
   count: 1
   time: 'Mon Feb 10, 2020'
   }`
- *update_count()* - Takes as input the new value of the counter:
`{ count : 10 } ` and updates the internal counter to that value, then returns the current value of the counter similarly to `get_count()`
