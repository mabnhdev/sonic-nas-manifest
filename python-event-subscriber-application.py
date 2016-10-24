# Python block code for event subscriber application

import cps
import cps_utils

# Create handle to connect with event service
handle = cps.event_connect()

while True:   
  ev = cps.event_wait(handle)

  if ev[‘key’] == ...:
    ...      elif ev['key'] == ...:
    ...
