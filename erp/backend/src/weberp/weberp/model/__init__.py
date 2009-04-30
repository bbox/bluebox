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
    meta.Session.mapper(User, users_table)
 

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
    sa.Column("teamid_usr", sa.types.Integer, nullable=False),
    sa.Column("managerid_usr", sa.types.Integer, nullable=False),
    sa.Column("notes_usr", sa.types.Text, nullable=False),
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