!/usr/bin/python

# Simple base ACL CPS config using the generic CPS Python module and utilities
# Create ACL Table
# Create ACL entry to drop all packets received on specific port from specific source MAC

import   cps_utils
import   nas_os_utils

# Yang enum name to number map
e_stg   =  {'INGRESS':   1,   'EGRESS':   2}
e_ftype   =  {'SRC_MAC':   3,   'DST_MAC':   4,   'SRC_IP':   5,   'DST_IP':   6, 'IN_PORT':   9,   'DSCP':   21}
e_atype   =  {'PACKET_ACTION':   3,   'SET_TC':   10}
e_ptype   =  {'DROP':   1}

# Inform CPS utility about the type of each attribute
type_map   =  {
   'base-acl/entry/SRC_MAC_VALUE/addr':   'mac', 
   'base-acl/entry/SRC_MAC_VALUE/mask':   'mac',
}

for   key,val   in   type_map.items():
    cps_utils.cps_attr_types_map.add_type(key,   val)

# Create ACL Table
# Create CPS object and fill leaf attributes
cps_obj   =  cps_utils.CPSObject(module='base-acl/table') cps_obj.add_attr   ('stage',   e_stg['INGRESS']) cps_obj.add_attr   ('priority',   99)

# Populate the leaf-list attribute
cps_obj.add_list   ('allowed-match-fields',   [e_ftype['SRC_MAC'], e_ftype['DST_IP'], e_ftype['DSCP'], e_ftype['IN_PORT']])

# Associate the CPS object with a CPS operation
cps_update   =  ('create',   cps_obj.get())

# Add the CPS object to a new CPS transaction
cps_trans   =  cps_utils.CPSTransaction([cps_update])

# Commit the CPS transaction 
r = cps_trans.commit()
if not   r:
    raise   RuntimeError   ("Error   creating   ACL  Table")

# Retrieve CPS object ID
ret   =  cps_utils.CPSObject   (module='base-acl/table',   obj=r[0]['change'])
tbl_id   =  ret.get_attr_data   ('id')
print   "Successfully   created   ACL  Table   " +  str(tbl_id)

# Create ACL entry
# Drop all packets received on specific port from specific range of MACs
# Create CPS Object and fill leaf attributes
cps_obj   =  cps_utils.CPSObject(module='base-acl/entry')
cps_obj.add_attr   ('table-id',   tbl_id)
cps_obj.add_attr   ('priority',   512)

# Filters     
# Match Filter 1 - Src MAC
cps_obj.add_embed_attr   (['match','0','type'],   e_ftype['SRC_MAC'])

# The two at the end indicates that the type should be deducted from the last two attrs (SRC_MAC_VALUE,addr)
cps_obj.add_embed_attr   (['match','0','SRC_MAC_VALUE','addr'], '50:10:6e:00:00:00',   2)

# Match Filter 2 - Rx Port
cps_obj.add_embed_attr   (['match','1','type'],   e_ftype['IN_PORT'])
cps_obj.add_embed_attr   (['match','1','IN_PORT_VALUE'],   nas_os_utils.if_nametoindex('e101-001-0')) 

# Action - Drop
cps_obj.add_embed_attr   (['action','0','type'],   e_atype['PACKET_ACTION'])
cps_obj.add_embed_attr   (['action','0','PACKET_ACTION_VALUE'],   e_ptype['DROP'])

# Associate the CPS object with a CPS operation 
cps_update = ('create',   cps_obj.get())

# Add the CPS object to a new CPS transaction 
cps_trans = cps_utils.CPSTransaction([cps_update])

# Commit the CPS transaction 
r = cps_trans.commit()
if not   r:
    raise   RuntimeError   ("Error   creating   MAC   ACL  Entry")

# Retrieve CPS object ID
ret   =  cps_utils.CPSObject   (module='base-acl/entry',   obj=r[0]['change'])
mac_eid   =  ret.get_attr_data   ('id')
print   "Successfully   created   MAC   ACL  Entry   " +  str(mac_eid)
