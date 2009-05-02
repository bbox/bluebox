import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render
from weberp.lib.helpers import Error
from weberp import model
from weberp.model import User
from weberp.model import Team
log = logging.getLogger(__name__)

class TeamsController(BaseController):

	def __init__(self):
		response.charset = 'utf8'
		response.content_type  = "application/xml"
		
	def index(self):
		"""GET /teams: All items in the collection."""
		# url('teams')
		result = model.Team.query().all()
		if len(result) == 0: #nothing in db
			error = Error()
			error.id = 1
			error.message = "No data in the system"
			c.error = error
			return render("users/error.mako")
		c.teams = result
		return render("teams/index.mako")


	def show(self, id):
		"""GET /teams/id: Show a specific item."""
		# url('teams', id=ID)		
		result = model.Team.query().get(id)
		if result is None:
			error = Error()
			error.id = 2
			error.message = "The team with the id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
		c.teams = [result]
		return render("teams/index.mako")
		
	def create(self):
		"""POST /teams: Create a new item."""
		# url('teams')
		if "name" not in request.params:
			error = Error()
			error.id = 4
			error.message = "Missing required data. At least username/password must be supplied"
			c.error = error
			return render("users/error.mako")
		
		name = request.params["name"]
		manager = request.params["manager_id"] if "manager_id" in request.params else None
		team = Team(name, manager)
		model.meta.Session.add(team)
		model.meta.Session.commit()
		return render("users/opstatus.mako")

	def update(self, id):
		team = model.Team.query().get(id)
		if team is None:
			error = Error()
			error.id = 2
			error.message = "The team with the id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
		if "name" in request.params:
			team.name_tms = request.params["name"]

		if "manager_id" in request.params:
			team.managerid_tms = request.params["manager_id"]
		
		model.meta.Session.commit()
		return render("users/opstatus.mako")


	def delete(self, id):
		team = model.Team.query().get(id)
		if team is None:
			error = Error()
			error.id = 2
			error.message = "The team with the id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
			
		model.meta.Session.delete(team)
		model.meta.Session.commit()
		return render("users/opstatus.mako")
	
	def teams_for_manager(self, id):
		teams = model.Team.query().filter(Team.managerid_tms == id).all()
		if len(teams) == 0:
			error = Error()
			error.id = 5
			error.message = "No teams for manager id %s." % id
			c.error = error
			return render("users/error.mako")
		c.teams = teams
		return render("teams/index.mako")