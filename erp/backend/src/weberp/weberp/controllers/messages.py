import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render
from weberp.lib.helpers import Error
from weberp.lib.helpers import validate_presence_of
from weberp import model
from weberp.model import Message

log = logging.getLogger(__name__)

class MessagesController(BaseController):

	def __init__(self):
		response.charset = 'utf8'
		response.content_type  = "application/xml"
		
	def index(self):
		messages = model.Message.query().all()
		if len(messages) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.messages = messages			
		return render('messages/index.mako')
	
	def show(self, id):
		message = model.Message.query().get(id)
		if message is None:
			error = Error()
			error.id = 2
			error.message = "Message with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")
		c.messages = [message]
		return render('messages/index.mako')
	
	def create(self):
		required_post = ["to", "from", "subject", "body"]
		
		if not validate_presence_of(required_post, request.params):
			error = Error()
			error.id = 2
			error.message = "Message with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")
		
		message = model.Message(request.params["from"], request.params["to"], request.params["subject"], request.params["body"])
	
		model.meta.Session.add(message)
		model.meta.Session.commit()
		
		return render("users/opstatus.mako")

	def update(self, id):
		message = model.Message.query().get(id)
		if message is None:
			error = Error()
			error.id = 2
			error.message = "Message with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")
		
		if "from" in request.params:
			message.from_msg = request.params["from"]

		if "to" in request.params:
			message.to_msg = request.params["to"]

		if "subject" in request.params:
			message.title_msg = request.params["subject"]

		if "body" in request.params:
			message.body_msg = request.params["body"]	

		model.meta.Session.commit()		
		return render("users/opstatus.mako")
		
	def delete(self, id):
		message = model.Message.query().get(id)
		if message is None:
			error = Error()
			error.id = 2
			error.message = "Message with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")
		
		model.meta.Session.delete(message)
		model.meta.Session.commit()
		
		return render("users/opstatus.mako")
