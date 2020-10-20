----------------------------------------------------------------------------------------------------------------------
Configuration server file:

Respect order and write after '=' w/o spaces, never leave blank lines or spaces/tabs.
There will be comments (with '#') that will guide you.
----------------------------------------------------------------------------------------------------------------------
Configuration sensor file:

write after '=' w/o spaces, never leave blank lines or spaces/tabs.
the first number is the region/zone the following of '=' are the sensors IDs attached to the region/zone separated by ','
for example 1=3,48,2,987 is region one wich have those sensors.
Sensors IDs could be repeated in different zones to activate different cameras.
----------------------------------------------------------------------------------------------------------------------
Configuration camera file

write after '=' w/o spaces, never leave blank lines or spaces/tabs.
the first number is the region/zone the following of '=' are the camera's ip (with port) attached to the region/zone separated by ','
for example 1=192.168.1.35:4747,1.192.168.1.38:4747,192.168.1.60:4747 is region one wich have those cameras
ips could be repeated in different zones, for example you could do a special zone that has all the cameras or more specific ones.
When a sensor in a zone fire an alarm, cameras in the same zone would be asked to send pictures so have in mind sensors 
should be in the same zone you want pictures from.
----------------------------------------------------------------------------------------------------------------------
You can put your own comments in any config file using '#' at the start and I highly recommend to do so.
for example (in config cameras file):
#zone1 is the west drilling site
1:192.168...,192.168...
#zone2 is the southeast drilling site
2:192.168...,192.168...
#zone3 is the kitchen
3:192.168...,192.168...
#zone4 are all the drilling sites (all ips should be here, except for the kitchen ones)
4:192.168...,192.168...

keep in mind that the number of zones in the sensor config file must be equal to the number of zones in the camera file
if you are not using a zone comment it with '#' or delete it. 
----------------------------------------------------------------------------------------------------------------------
Enjoy!
By: ROI96 2020
----------------------------------------------------------------------------------------------------------------------