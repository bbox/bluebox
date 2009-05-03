"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from weberp.model import meta

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine
    
    sm = orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)
    meta.Session = orm.scoped_session(sm)

    # Here we use the "contextual session": http://www.sqlalchemy.org/docs/05/session.html#contextual-thread-local-sessions
    meta.Session.mapper(User, users_table, properties = {"team": orm.relation(Team, backref="users", primaryjoin=users_table.c.teamid_usr==teams_table.c.id_tms)})
    meta.Session.mapper(Team, teams_table, properties = {"manager": orm.relation(User, primaryjoin=teams_table.c.managerid_tms==users_table.c.id_usr)})
    meta.Session.mapper(Project, projects_table)
    meta.Session.mapper(Document, documents_table, properties = {"project": orm.relation(Project, backref="documents", primaryjoin=documents_table.c.idprj_doc==projects_table.c.id_prj)})
    meta.Session.mapper(Task, tasks_table, properties = {"project": orm.relation(Project, backref="tasks", primaryjoin=tasks_table.c.idprj_tsk==projects_table.c.id_prj), "assignee": orm.relation(User, primaryjoin=tasks_table.c.assignedto_tsk==users_table.c.id_usr)})
    meta.Session.mapper(Meeting, meetings_table)
    meta.Session.mapper(Message, messages_table, properties = {"expeditor": orm.relation(User, primaryjoin=messages_table.c.from_msg==users_table.c.id_usr), "destinatar": orm.relation(User, primaryjoin=messages_table.c.to_msg==users_table.c.id_usr)})
## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)

users_table = sa.Table("users_usr", meta.metadata,
    sa.Column("id_usr", sa.types.Integer, primary_key=True),
    sa.Column("name_usr", sa.types.Unicode(200), nullable=False),
    sa.Column("address_usr", sa.types.UnicodeText, nullable=False),
    sa.Column("email_usr", sa.types.Unicode(200), nullable=False),
    sa.Column("password_usr", sa.types.Unicode(200), nullable=False),
    sa.Column("status_usr", sa.types.Integer, nullable=False),
    sa.Column("address_usr", sa.types.Text, nullable=True),
    sa.Column("phone_usr", sa.types.Unicode(30), nullable=True),
    sa.Column("salary_usr", sa.types.Integer, nullable=True),
    sa.Column("teamid_usr", sa.types.Integer, sa.ForeignKey("teams_tms.id_tms"), nullable=False),
    sa.Column("managerid_usr", sa.types.Integer, nullable=False),
    sa.Column("notes_usr", sa.types.Text, nullable=False),
)

teams_table = sa.Table("teams_tms", meta.metadata,
    sa.Column("id_tms", sa.types.Integer, primary_key=True),
    sa.Column("name_tms", sa.types.Unicode(200), nullable=False),
	sa.Column("managerid_tms", sa.types.Integer, sa.ForeignKey("users_usr.id_usr"), nullable=False),

)

projects_table = sa.Table("projects_prj", meta.metadata,
	sa.Column("id_prj", sa.types.Integer, primary_key=True),
	sa.Column("name_prj", sa.types.Unicode(200), nullable=False),
	sa.Column("status_prj", sa.types.Integer, nullable=False),
	sa.Column("added_by_prj", sa.types.Integer, nullable=False),
	sa.Column("owned_by_prj", sa.types.Integer, nullable=True),
	sa.Column("startdate_prj", sa.types.DateTime, nullable=True),
	sa.Column("enddate_prj", sa.types.DateTime, nullable=True),	
	sa.Column("cost_prj", sa.types.Float, nullable=True),
)

documents_table = sa.Table("documents_doc", meta.metadata,
	sa.Column("id_doc", sa.types.Integer, primary_key=True),
	sa.Column("idprj_doc", sa.types.Integer, sa.ForeignKey("projects_prj.id_prj"), nullable=False),
	sa.Column("name_doc", sa.types.Unicode(200), nullable=False),
	sa.Column("file_doc", sa.types.Unicode(200), nullable=True),
)

tasks_table = sa.Table("tasks_tsk", meta.metadata,
	sa.Column("id_tsk", sa.types.Integer, primary_key=True),
	sa.Column("idprj_tsk", sa.types.Integer, sa.ForeignKey("projects_prj.id_prj"), nullable=False),
	sa.Column("title_tsk", sa.types.Unicode(200), nullable=False),
	sa.Column("description_tsk", sa.types.Text, nullable=True),
	sa.Column("added_by_tsk", sa.types.Integer, sa.ForeignKey("users_usr.id_usr"), nullable=False),
	sa.Column("assignedto_tsk", sa.types.Integer, sa.ForeignKey("users_usr.id_usr"), nullable=True),
	sa.Column("timeleft_tsk", sa.types.Integer, nullable=True),
	sa.Column("status_tsk", sa.types.Integer, nullable=False),	
	sa.Column("starton_tsk", sa.types.DateTime, nullable=True),
	sa.Column("endon_tsk", sa.types.DateTime, nullable=True),	
)

meetings_table = sa.Table("meetings_met", meta.metadata,
	sa.Column("id_met", sa.types.Integer, primary_key=True),
	sa.Column("subject_met", sa.types.Unicode(255), nullable=False),
	sa.Column("participants_met", sa.types.Unicode(255), nullable=False),
	sa.Column("location_met", sa.types.Unicode(255), nullable=True),
	sa.Column("owner_met", sa.types.Integer, nullable=False),
	sa.Column("notes_met", sa.types.Text, nullable=True),
	sa.Column("start_met", sa.types.DateTime, nullable=False),
	sa.Column("end_met", sa.types.DateTime, nullable=True),
)

messages_table = sa.Table("messages_msg", meta.metadata,
	sa.Column("id_msg", sa.types.Integer, primary_key=True),
	sa.Column("from_msg", sa.types.Integer, sa.ForeignKey("users_usr.id_usr"), nullable=False),
	sa.Column("to_msg", sa.types.Integer, sa.ForeignKey("users_usr.id_usr"), nullable=False),
	sa.Column("title_msg", sa.types.Unicode(255), nullable=False),
	sa.Column("body_msg", sa.types.Text, nullable=False),
)
## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function

class User(object):
	def __init__(self, email_usr, password_usr, name_usr=None, status_usr=0, address_usr=None, phone_usr=None, salary_usr=None, teamid_usr=None, managerid_usr=None, notes_usr=None):
		self.email_usr = email_usr
		self.password_usr = password_usr
		self.status_usr = 0
		self.name_usr = name_usr
		self.address_usr = address_usr
		self.phone_usr = phone_usr
		self.salary_usr = salary_usr
		self.teamid_usr = teamid_usr
		self.managerid_usr = managerid_usr
		self.notes_usr = notes_usr
		
	def __repr__(self):
		return "<User('%d', '%s', '%s')>" % ((self.id_usr or -1), self.email_usr, self.name_usr)
	

class Team(object):
	def __init__(self, name, manager=None):
		self.name_tms = name
		self.managerid_tms = manager
	
	def __repr__(self):
		return "<team><id>%s</id><name>%s</name><manager>%s</manager></team>" % (self.id_tms or -1, self.name_tms, self.manager_tms or 0)
	

class Project(object):
	def __init__(self, name, status, added_by, owner=None, start=None, end=None, cost=None):
		self.name_prj = name
		self.status_prj = status
		self.added_by_prj = added_by
		self.owned_by_prj = owner
		self.startdate_prj = start
		self.enddate_prj = end
		self.cost_prj = cost
	
	def __repr__(self):
		return "project"

class Task(object):
	def __init__(self, project_id, title, added_by, status=0):
		self.idprj_tsk = project_id
		self.title_tsk = title
		self.added_by_tsk = added_by
		self.status_tsk = status
		
	def __repr__(self):
		return "task"
		
class Document(object):
	def __init__(self, project_id, name, file=None):
		self.idprj_doc = project_id
		self.name_doc = name
		self.file_doc = file
	
	def __repr__(self):
		return "document"
	

class Meeting(object):
	def __init__(self, subject, participants, owner, start, location=None, notes=None, end=None):
		self.subject_met = subject
		self.participants_met = participants
		self.owner_met = owner
		self.location_met = location
		self.notes_met = notes
		self.start_met = start
		self.end_met = end
		
	def __repr__(self):
		return "meeting"	
	
class Message(object):
	def __init__(self, from_usr, to_usr, title, body):
		self.from_msg = from_usr
		self.to_msg = to_usr
		self.title_msg = title
		self.body_msg = body
	
	def __repr__(self):
		return "message"