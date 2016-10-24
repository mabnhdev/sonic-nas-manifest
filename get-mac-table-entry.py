# Python code block to get MAC table entry

import   cps_utils 
import   cps

# Register attribute type
cps_utils.add_attr_type("base-mac/query/mac-address",   "mac")

# Define MAC saddress request type
d  =     {"mac-address":   "00:0a:0b:cc:0d:0e","request-type":"2"}

# Associate get operation with CPS object
obj   =  cps_utils.CPSObject('base-mac/query', data=   d)

# Create object filter list
filter_list   =  [] 

# Add the filter object
filter_list.append(obj.get()) 

# Create list for response
l =  []

# Verify objects returned
if cps.get(filter_list,l):
    if l:
        for   ret_obj   in   l:
            cps_utils.print_obj(ret_obj) 
    else:
        print   "No   objects   found"         
else:
    print   "No   objects   found" 
    raise   RuntimeError   ("Error   Getting   MAC   Table   Entries")
