# Python code block to create VLAN

import cps
import cps_object

# Create CPS Object
cps_obj = cps_object.CPSObject('dell-base-if-cmn/if/interfaces/interface')

# Populate the attributes for the CPS object
cps_obj.add_attr("base-if-vlan/if/interfaces/interface/id",100)
cps_obj.add_attr('if/interfaces/interface/type','ianaift:l2vlan')

# Associate a CPS operation with the CPS object
cps_update = {'change':cps_obj.get(),'operation': 'create'}

# Add the CPS operation, object pair to a new CPS transaction
transaction = cps.transaction([cps_update])

# Check for failure
if not transaction: 
    raise RuntimeError ("Error creating Vlan")
print "Successfully created"
