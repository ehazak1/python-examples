'''
Like Logo.
'''
import turtle


=============================== RESTART: Shell ===============================
>>> 
>>> def star():
	angle = 60
	for i in range(360/angle):
		box()
		right(angle)

		
>>> star()

Traceback (most recent call last):
  File "<pyshell#701>", line 1, in <module>
    star()
  File "<pyshell#700>", line 4, in star
    box()
NameError: global name 'box' is not defined
>>> from turtle import *
>>> def el():
	forward(100)
	right(90)

	
>>> def box():
	el()
	el()
	el()
	el()

	
>>> def star():
	angle = 60
	for i in range(360/angle):
		box()
		right(angle)

		
>>> star()
>>> 
>>> def star(angle):
	for i in range(360/angle):
		box()
		right(angle)

		
>>> star(50)
>>> 
>>> clearscreen()
>>> begin_fill()
>>> color('red')
>>> fillcolor('purple')
>>> star(60)
>>> end_fill()
