import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render

from weberp import model
from weberp.model import User
log = logging.getLogger(__name__)

class UsersController(BaseController):

#    def index(self):
#        # Return a rendered template
#        #return render('/users.mako')
#        # or, return a response
#        return 'Hello World'
        
	def show(self):
		#show method
		return 'this works'
		
	def login(self, username, password):
		#login method
#		if "email" not in request.params and "password" not in request.params:
#			return "<error>2</error>\r\n<errorMsg>Username/password not sent via POST</errorMsg>"
		
#		username = request.params["email"]
#		password = request.params["password"]
		retVal = "%s_%s" %(username, password)
		
		c.user = model.User.query().filter(User.email_usr == username).all()
		return render("users/login.mako")