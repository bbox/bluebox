import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render
from weberp.lib.helpers import Error
from weberp.lib.helpers import validate_presence_of
from weberp import model
from weberp.model import Meeting

from datetime import datetime

log = logging.getLogger(__name__)

class MeetingsController(BaseController):

	def __init__(self):
		response.charset = 'utf8'
		response.content_type  = "application/xml"
		
	def index(self):
		meetings = model.Meeting.query().all()
		if len(meetings) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.meetings = meetings
		return render("meetings/index.mako")
		    
	def show(self, id):
		meeting = model.Meeting.query().get(id)
		if meeting is None:
			error = Error()
			error.id = 1
			error.message = "Meeting with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")
		c.meetings = [meeting]
		return render("meetings/index.mako")

	def create(self):
		"""POST /meetings: Create a new item."""
		# url('meetings')
		required_post = ["subject", "participants", "owner", "start"]
		if not validate_presence_of(required_post, request.params):
			error = Error()
			error.id = 1
			error.message = "Missing required params"
			c.error = error
			return render("users/error.mako")	
			
		meeting = model.Meeting(request.params["subject"], request.params["participants"], request.params["owner"], datetime.strptime(request.params["start"], "%d/%m/%y %H:%M"))
		meeting.location_met = request.params["location"] if "location" in request.params else None
		meeting.notes_met = request.params["notes"] if "notes" in request.params else None
		meeting.end_met = request.params["end_met"] if "end_met" in request.params else None

		model.meta.Session.add(meeting)
		model.meta.Session.commit()
		
		return render("users/opstatus.mako")
		
	def update(self, id):
		meeting = model.Meeting.query().get(id)
		if meeting is None:
			error = Error()
			error.id = 1
			error.message = "Meeting with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")

		if "subject" in request.params:
			meeting.subject_met = request.params["subject"]

		if "location" in request.params:
			meeting.location_met = request.params["location"]

		if "participants" in request.params:
			meeting.participants_met = request.params["participants_met"]

		if "owner" in request.params:
			meeting.owner_met = request.params["owner"]
		
		if "start" in request.params:
			meeting.start_met = datetime.strptime(request.params["start"], "%d/%m/%y %H:%M")
		
		if "end" in request.params:
			meeting.end_met = datetime.strptime(request.params["end"], "%d/%m/%y %H:%M")
		
		if "notes" in request.params:
			meeting.notes_met = request.params["notes"]
			
		model.meta.Session.commit()
		return render("users/opstatus.mako")
		
	def delete(self, id):
		meeting = model.Meeting.query().get(id)
		if meeting is None:
			error = Error()
			error.id = 1
			error.message = "Meeting with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")			
		model.meta.Session.delete(meeting)
		model.meta.Session.commit()
		return render("users/opstatus.mako")
