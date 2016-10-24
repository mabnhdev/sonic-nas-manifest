# Python code block to publish events

import   cps
import   cps_utils

# Create handle to connect to event service
handle   =  cps.event_connect()

# Create CPS object
obj   =  cps_utils.CPSObject('base-port/interface',qual='observed', data=   {"ifindex":23})

# Publish the event
cps.event_send(handle,   obj.get()) 
