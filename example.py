#!/usr/bin/python
 
from mask import *
 
screen = SnackScreen()
 
m = Mask( screen, "Demo", 30 )
m.entry( "Entry", "entry1", "value of entry 1" )
m.password( "Password", "passwd1", "value of entry 1" )
m.radios( "Select", "sel1", [ ('Yes','yes', 0), ('No','no', 1) ] )
m.list( "List", "list1", [ ('Yes','yes', 0), ('No','no', 1) ] )
m.checks( "Check", "chk1", [ ('Yes','yes', 0), ('No','no', 1) ] )
m.buttons( yes="Yes", no="No" )
(cmd, results) = m.run()
 
screen.finish()
 
print cmd, results

# will print something like:
# yes {'passwd1': 'value of entry 1', 'entry1': 'Value of the entry', 'list1': 'no', 'sel1': 'no', 'chk1': ['no']}
