"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password

def validate_presence_of(lookfor, haystack):
	for item in lookfor:
		if item not in haystack:
			return False
	return True

class Error(object):
	def __init__(self, id=None, message=None):
		self.id = id
		self.message = message