# Python code block to remove multiple MAC table entries

import   cps_utils

# Define VLANs
vlan_list   =[1,2,3,4,5]

# Create CPS object
obj   =  cps_utils.CPSObject('base-mac/flush')

# Add VLAN list to CPS object
count   =  0
el   =  ["input/filter","0","vlan"]
for   vlan   in   vlan_list:
    obj.add_embed_attr(el,   vlan)
    count = count + 1
el[1]   =  str(count)

# Association operation to object
tr_obj   =  ('rpc',   obj.get())
transaction   =  cps_utils.CPSTransaction([tr_obj])

# Verify the return value
ret   =  transaction.commit()
if not   ret:
    raise   RuntimeError("Error   Flushing   entries   from   MAC   Table")
