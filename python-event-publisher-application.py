# Python code block for event publisher application

import   cps
import   cps_utils

# Create handle to connect to the event service
handle   =  cps.event_connect()

# Create object
obj   =  cps_utils.CPSObject('base-port/interface',qual='observed', data=   {"ifindex":23})

# Send CPS event
cps.event_send(handle,   obj.get())
