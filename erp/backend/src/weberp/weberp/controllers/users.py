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

	def add(self):
		"""POST /users: Create a new item."""
		email = request.params['name']
		password = request.params["password"]
		name = request.params["name"]
		status = 2 if "status" not in request.params else request.params["status"]
		address = request.params["address"] if "address" in request.params else None
		phone = request.params["phone"] if "phone" in request.params else None
		teamid = request.params["team"] if "team" in request.params else None
		managerid = request.params["manager"] if "manager" in request.params else None
		salary = request.params["salary"] if "salary" in request.params else None
		notes = request.params["notes"] if "notes" in request.params else None
		
		user = model.User(email, password, name, status, address, phone, salary, teamid, managerid, notes)
		model.meta.Session.add(user)
		model.meta.Session.commit()		
		return render("users/opstatus.mako")
		        
	def show(self):
		#show method
		return 'this works'
		
	def login(self, username, password):	
		c.user = model.User.query().filter(User.email_usr == username).filter(User.password_usr == password).one()
		return render("users/login.mako")
		
	def list(self):
		c.users = model.User.query().all()
		return render("users/index.mako")
	
	def details(self, id):
		c.user = model.User.query().get(id)
		return render("users/login.mako")
	
	def update(self, id):
		user = model.User.query().get(id)
		if user is None:
			abort(404)
		if "password" in request.params:
			user.password_usr = request.params["password"]

		if "name" in request.params:
			user.name_usr = request.params["name"]

		if "status" in request.params:
			user.status_usr = request.params["status"]

		if "address" in request.params:
			user.address_usr = request.params["address"]

		if "phone" in request.params:
			user.phone_usr = request.params["phone"]

		if "teamid" in request.params:
			user.teamid_usr = request.params["teamid"]

		if "managerid" in request.params:
			user.managerid_usr = request.params["managerid"]

		if "salary" in request.params:
			user.salary_usr = request.params["salary"]

		if "notes" in request.params:
			user.notes_usr = request.params["notes"]
		model.meta.Session.commit()
		return render("users/opstatus.mako")
	
	def delete(self, id):
		user = model.User.query().get(id)
		if user is None:
			abort(404)
		model.meta.Session.delete(user)
		model.meta.Session.commit()
		return render("users/opstatus.mako")