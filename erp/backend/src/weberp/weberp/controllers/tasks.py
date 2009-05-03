import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render
from weberp.lib.helpers import Error
from weberp.lib.helpers import validate_presence_of
from weberp import model
from weberp.model import Task

log = logging.getLogger(__name__)

class TasksController(BaseController):

	def __init__(self):
		response.charset = 'utf8'
		response.content_type  = "application/xml"
		
	def index(self):
		tasks = model.Task.query().all()
		if len(tasks) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.tasks = tasks
		return render("tasks/index.mako")
		    
	def show(self, id):
		task = model.Task.query().get(id)
		if task is None:
			error = Error()
			error.id = 1
			error.message = "Task with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")
		c.tasks = [task]
		return render("tasks/index.mako")
    
	def create(self):
		"""POST /tasks: Create a new item."""
		# url('tasks')
		if "idprj_tsk" not in request.params or "title_tsk" not in request.params or "status_tsk" not in request.params or "added_by_tsk" not in request.params:
			error = Error()
			error.id = 1
			error.message = "Missing required params"
			c.error = error
			return render("users/error.mako")	
		
		task = model.Task(request.params["idprj_tsk"], request.params["title_tsk"], request.params["added_by_tsk"], request.params["status_tsk"])
		task.description_tsk = request.params["description_tsk"] if "description_tsk" in request.params else None
		task.assignedto_tsk = request.params["assignedto_tsk"] if "assignedto_tsk" in request.params else None
		task.timeleft_tsk = request.params["timeleft_tsk"] if "timeleft_tsk" in request.params else None
		task.starton_tsk = request.params["starton_tsk"] if "starton_tsk" in request.params else None
		task.endon_tsk = request.params["endon_tsk"] if "endon_tsk" in request.params else None

		model.meta.Session.add(task)
		model.meta.Session.commit()
		
		return render("users/opstatus.mako")
		
	def update(self, id):
		task = model.Task.query().get(id)
		if task is None:
			error = Error()
			error.id = 1
			error.message = "Task with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")

		if "idprj_tsk" in request.params:
			task.idprj_tsk = request.params["idprj_tsk"]

		if "title_tsk" in request.params:
			task.title_tsk = request.params["title_tsk"]

		if "status_tsk" in request.params:
			task.status_tsk = request.params["status_tsk"]

		if "addedby_tsk" in request.params:
			task.addedby_tsk = request.params["addedby_tsk"]
		
		if "description_tsk" in request.params:
			task.description_tsk = request.params["description_tsk"]
		
		if "assignedto_tsk" in request.params:
			task.assignedto_tsk = request.params["assignedto_tsk"]
		
		if "timeleft_tsk" in request.params:
			task.timeleft_tsk = request.params["timeleft_tsk"]

		if "starton_tsk" in request.params:
			task.starton_tsk = request.params["starton_tsk"]

		if "endon_tsk" in request.params:
			task.endon_tsk = request.params["endon_tsk"]
			
		model.meta.Session.commit()
		return render("users/opstatus.mako")
		
	def delete(self, id):
		task = model.Task.query().get(id)
		if task is None:
			error = Error()
			error.id = 1
			error.message = "Task with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")			
		model.meta.Session.delete(task)
		model.meta.Session.commit()
		return render("users/opstatus.mako")
