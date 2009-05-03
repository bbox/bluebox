import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from weberp.lib.base import BaseController, render
from weberp import model
from weberp.lib.helpers import Error
from weberp.model import Document
import os
log = logging.getLogger(__name__)

class DocumentsController(BaseController):
	
	def __init__(self):
		response.charset = 'utf8'
		response.content_type  = "application/xml"
		self.document_store = "/uploads/documents"
		
	def index(self):
		result = model.Document.query().all()
		if len(result) == 0:
			error = Error()
			error.id = 1
			error.message = "No data in the system"
			c.error = error
			return render("users/error.mako")
		c.documents = result
		return render('documents/index.mako')
	
	def show(self, id):
		result = model.Document.query().get(id)
		if result is None:
			error = Error()
			error.id = 2
			error.message = "The document with id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
		c.documents = [result]
		return render('documents/index.mako')
		
	def create(self):
		if "name_doc" not in request.params or "idprj_doc" not in request.params:
			error = Error()
			error.id = 4
			error.message = "Missing required data."
			c.error = error
			return render("users/error.mako")
		
		name = request.params["name_doc"]
		project_id = request.params["idprj_doc"]
		permanent_store = "%s/%s/" % (self.document_store, project_id)	
#		myfile = request.POST['document']
#		filename = myfile.filename.lstrip(os.sep)
#		permanent_file = open(os.path.join(permanent_store, filename),'w')
			
#		shutil.copyfileobj(myfile.file, permanent_file)
#		myfile.file.close()
#		permanent_file.close()
		
		doc = model.Document( project_id, name)
		model.meta.Session.add(doc)
		model.meta.Session.commit()
		return render("users/opstatus.mako")
	
	def upload(self, id):
		permanent_store = "%s/%s/" % (self.document_store, id)	
		myfile = request.POST['document']
		filename = myfile.filename.lstrip(os.sep)
		permanent_file = open(os.path.join(self.document_store, filename),'w')
			
		shutil.copyfileobj(myfile.file, permanent_file)
		myfile.file.close()
		permanent_file.close()
		
		doc = model.Document(name, filename, project_id)
		model.meta.Session.add(doc)
		model.meta.Session.commit()
		return render("users/opstatus.mako")
		
	def update(self, id):
		document = model.Document.query().get(id)
		if document is None:
			error = Error()
			error.id = 2
			error.message = "The document with id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
		permanent_store = "%s/%s/" % (self.document_store, document.idprj_doc)
		old_file_location = "%s/%s/%s" % (self.document_store, document.idprj_doc, document.file_doc)
		
		if "name_doc" in request.params:
			document.name_doc = request.params["name"]
		
		if "idprj_doc" in request.params:
			document.idprj_doc = request.params["project_id"]
			
		if "file_doc" in request.params:
			#overwrite old file
			os.remove(old_file_location)
			myfile = request.POST['file_doc']
			filename = myfile.filename.lstrip(os.sep)
			permanent_file = open(os.path.join(permanent_store, filename),'w')
			
			shutil.copyfileobj(myfile.file, permanent_file)
			myfile.file.close()
			permanent_file.close()
			document.file_doc = filename
			
		model.meta.Session.commit()
		return render("users/opstatus.mako")
		
	def delete(self, id):
		document = model.Document.query().get(id)
		if document is None:
			error = Error()
			error.id = 2
			error.message = "The document with id %s does not exist" % id
			c.error = error
			return render("users/error.mako")
		model.meta.Session.delete(document)
		model.meta.Session.commit()
		return render("users/opstatus.mako")