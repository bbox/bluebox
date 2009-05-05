import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render
from weberp.lib.helpers import Error
from weberp import model
from weberp.model import User
log = logging.getLogger(__name__)

class UsersController(BaseController):

	def __init__(self):
		response.charset = 'utf8'
		response.content_type  = "application/xml"
		
	def create(self):
		"""POST /users: Create a new item."""
		if "email_usr" not in request.params or "password_usr" not in request.params:
			error = Error()
			error.id = 4
			error.message = "Missing required data. At least username/password must be supplied"
			c.error = error
			return render("users/error.mako")
		
		email = request.params['email_usr']
		result = model.User.query().filter(User.email_usr == email).all()
		if len(result) > 0:
			error = Error()
			error.id = 5
			error.message = "Username already in use"
			c.error = error
			return render("users/error.mako")
		
		password = request.params["password_usr"]
		name = request.params["name_usr"]
		status = 2 if "status_usr" not in request.params else request.params["status_usr"]
		address = request.params["address_usr"] if "address_usr" in request.params else None
		phone = request.params["phone_usr"] if "phone_usr" in request.params else None
		teamid = request.params["teamid_usr"] if "teamid_usr" in request.params else None
		managerid = request.params["managerid_usr"] if "managerid_usr" in request.params else None
		salary = request.params["salary_usr"] if "salary_usr" in request.params else None
		notes = request.params["notes_usr"] if "notes_usr" in request.params else None
		
		user = model.User(email, password, name, status, address, phone, salary, teamid, managerid, notes)
		model.meta.Session.add(user)
		model.meta.Session.commit()		
		return render("users/opstatus.mako")
		
	def login(self, username, password):	
		result = model.User.query().filter(User.email_usr == username).filter(User.password_usr == password).all()
		if result is None or len(result) == 0:
			error = Error()
			error.id = 3
			error.message = "Bad username or password"
			c.error = error
			return render("users/error.mako")
		c.user = result[0]
		return render("users/login.mako")
		
	def index(self):
		c.users = model.User.query().all()
		if c.users is None or len(c.users) == 0:
			error = Error()
			error.id = 1
			error.message = "No users in the system"
			c.error = error
			return render("users/error.mako")
		return render("users/index.mako")
	
	def show(self, id):
		result = model.User.query().get(id)
		if result is None:
			error = Error()
			error.id = 2
			error.message = "The user with the id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
		c.user = result
		return render("users/login.mako")
	
	def update(self, id):
		user = model.User.query().get(id)
		if user is None:
			error = Error()
			error.id = 2
			error.message = "The user with the id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
			
		if "password_usr" in request.params:
			user.password_usr = request.params["password_usr"]

		if "name_usr" in request.params:
			user.name_usr = request.params["name_usr"]

		if "status_usr" in request.params:
			user.status_usr = request.params["status_usr"]

		if "address_usr" in request.params:
			user.address_usr = request.params["address_usr"]

		if "phone_usr" in request.params:
			user.phone_usr = request.params["phone_usr"]

		if "teamid_usr" in request.params:
			user.teamid_usr = request.params["teamid_usr"]

		if "managerid_usr" in request.params:
			user.managerid_usr = request.params["managerid_usr"]

		if "salary_usr" in request.params:
			user.salary_usr = request.params["salary_usr"]

		if "notes_usr" in request.params:
			user.notes_usr = request.params["notes_usr"]
			
		model.meta.Session.commit()
		return render("users/opstatus.mako")
	
	def delete(self, id):
		user = model.User.query().get(id)
		if user is None:
			error = Error()
			error.id = 2
			error.message = "The user with the id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
			
		model.meta.Session.delete(user)
		model.meta.Session.commit()
		return render("users/opstatus.mako")