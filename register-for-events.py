# Python code block to register for events

import   cps

# Create handle to connect to event service
handle   =  cps.event_connect()

# Regidter key with event service
cps.event_register(handle,   cps.key_from_name('observed','base-port/interface'))
while   True:
    obj  =  cps.event_wait(handle)
    print   obj
