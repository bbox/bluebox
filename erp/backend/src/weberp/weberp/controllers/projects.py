import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render
from weberp.lib.helpers import Error
from weberp import model
from weberp.model import User
from weberp.model import Team
from weberp.model import Project

log = logging.getLogger(__name__)

class ProjectsController(BaseController):

	def __init__(self):
		response.charset = 'utf8'
		response.content_type  = "application/xml"
		
	def index(self):
		result = model.Project.query().all()
		if len(result) == 0: #nothing in db
			error = Error()
			error.id = 1
			error.message = "No data in the system"
			c.error = error
			return render("users/error.mako")		
		c.projects = result
		return render('projects/index.mako')

	def show(self, id):
		result = model.Project.query().get(id)
		if result is None: #nothing in db
			error = Error()
			error.id = 2
			error.message = "The project with the id %s does not exist" % id
			c.error = error
			return render("users/error.mako")		
		c.projects = [result]
		return render('projects/index.mako')
		
	def create(self):
		if len(request.POST) == 0 or "name_prj" not in request.params or "status_prj" not in request.params or  "added_by_prj" not in request.params:
			error = Error()
			error.id = 4
			error.message = "Missing required data."
			c.error = error
			return render("users/error.mako")
		
		name = request.params["name_prj"]
		status = request.params["status_prj"]
		added_by = request.params["added_by_prj"]
		owner = request.params["owned_by_prj"] if "owned_by_prj" in request.params else None
		start = request.params["startdate_prj"] if "startdate_prj" in request.params else None
		end = request.params["enddate_prj"] if "enddate_prj" in request.params else None
		cost = request.params["cost"] if "cost" in request.params else None
		
		project = Project(name, status, added_by, owner, start, end, cost)
		model.meta.Session.add(project)
		model.meta.Session.commit()
		return render("users/opstatus.mako")
		
	def update(self, id):
		pass
		
	def delete(self, id):
		project = model.Project.query().get(id)
		if project is None:
			error = Error()
			error.id = 2
			error.message = "The project with the id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
			
		model.meta.Session.delete(project)
		model.meta.Session.commit()
		return render("users/opstatus.mako")
	
	def filter_by_team(self, id):
		result = model.Project.query().filter(Project.owned_by_prj == id).all()
		if len(result) == 0: #nothing in db
			error = Error()
			error.id = 1
			error.message = "Team with id %s has no projects" % id
			c.error = error
			return render("users/error.mako")
		c.projects = result
		return render("projects/index.mako")