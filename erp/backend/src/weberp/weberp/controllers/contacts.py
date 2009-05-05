import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render
from weberp import model
from weberp.lib.helpers import Error
from weberp.model import Contact
log = logging.getLogger(__name__)
from sqlalchemy import or_

class ContactsController(BaseController):

	def __init__(self):
		response.charset = 'utf8'
		response.content_type  = "application/xml"

	def index(self):
		result = model.Contact.query().all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.contacts = result			
		return render('/contacts/index.mako')

	def clienti(self):
		result = model.Contact.query().filter(Contact.tip_con == 0).all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.contacts = result			
		return render('/contacts/index.mako')

	def furnizori(self):
		result = model.Contact.query().filter(Contact.tip_con == 1).all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.contacts = result			
		return render('/contacts/index.mako')

	def parteneri(self):
		result = model.Contact.query().filter(Contact.tip_con == 2).all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.contacts = result			
		return render('/contacts/index.mako')				
	def index_for_user(self, id):
		result = model.Contact.query().filter(or_(Contact.addedby_con == id, Contact.visible_con == 0)).all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.contacts = result			
		return render('/contacts/index.mako')

	def clienti_for_user(self, id):
		result = model.Contact.query().filter(or_(Contact.addedby_con == id, Contact.visible_con == 0)).filter(Contact.tip_con == 0).all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.contacts = result			
		return render('/contacts/index.mako')
		
	def furnizori_for_user(self, id):
		result = model.Contact.query().filter(or_(Contact.addedby_con == id, Contact.visible_con == 0)).filter(Contact.tip_con == 1).all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.contacts = result			
		return render('/contacts/index.mako')
		
	def parteneri_for_user(self, id):
		result = model.Contact.query().filter(or_(Contact.addedby_con == id, Contact.visible_con == 0)).filter(Contact.tip_con == 2).all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system."
			c.error = error
			return render("users/error.mako")
		c.contacts = result			
		return render('/contacts/index.mako')								

	def show(self, id):
		result = model.Contact.query().get(id)
		if result == None:
			error = Error()
			error.id = 1
			error.message = "Contact with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")
		c.contacts = [result]
		return render('/contacts/index.mako')

	def create(self):
		
		if "denumire_con" not in request.params or "persoana_con" not in request.params or "addedby_con" not in request.params:
			error = Error()
			error.id = 1
			error.message = "Missing required params"
			c.error = error
			return render("users/error.mako")			
		denumire = request.params["denumire_con"]
		persoana_con = request.params["persoana_con"]
		addedby_con = request.params["addedby_con"]
		email = request.params["email_con"] if "email_con" in request.params else None
		phone = request.params["phone_con"] if "phone_con" in request.params else None
		adresa = request.params["adresa_con"] if "adresa_con" in request.params else None
		tip = request.params["tip_con"] if "tip_con" in request.params else 0
		visible = request.params["visible_con"] if "visible_con" in request.params else 0
		
		contact = Contact(denumire, persoana_con, addedby_con, email, phone, adresa, tip, visible)
		
		model.meta.Session.add(contact)
		model.meta.Session.commit()
		return render("users/opstatus.mako")
		
	def update(self, id):
		contact = model.Contact.query().get(id)
		if contact == None:
			error = Error()
			error.id = 1
			error.message = "Contact with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")		

		if "denumire_con" in request.params:
			contact.denumire_con = request.params["denumire_con"]
		
		if "persoana_con" in request.params:
			contact.persoana_con = request.params["persoana_con"]

		if "email_con" in request.params:
			contact.email_con = request.params["email_con"]

		if "phone_con" in request.params:
			contact.phone_con = request.params["phone_con"]

		if "adresa_con" in request.params:
			contact.adresa_con = request.params["adresa_con"]

		if "tip_con" in request.params:
			contact.tip_con = request.params["tip_con"]

		if "addedby_con" in request.params:
			contact.addedby_con = request.params["addedby_con"]

		if "visible_con" in request.params:
			contact.visible_con = request.params["visible_con"]

		model.meta.Session.commit()
		return render("users/opstatus.mako")
		
	def delete(self, id):
		contact = model.Contact.query().get(id)
		if contact == None:
			error = Error()
			error.id = 1
			error.message = "Contact with id %s does not exist." % id
			c.error = error
			return render("users/error.mako")		
		model.meta.Session.delete(contact)
		model.meta.Session.commit()
		return render("users/opstatus.mako")	