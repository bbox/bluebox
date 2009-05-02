"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
	"""Create, configure and return the routes Mapper"""
	map = Mapper(directory=config['pylons.paths']['controllers'],
			always_scan=config['debug'])
	map.minimization = False
	
	# The ErrorController route (handles 404/500 error pages); it should
	# likely stay at the top, ensuring it can always be resolved
	map.connect('/error/{action}', controller='error')
	map.connect('/error/{action}/{id}', controller='error')
	
	# CUSTOM ROUTES HERE
	map.resource("/users", "users")
	map.connect("users_login", "/users/login/:username/:password", controller="users", action="login")
	
	map.resource("/teams", "teams")
	map.connect("teams_with_manager", "/teams/with/manager/:id", controller="teams", action="teams_for_manager")
	
	map.resource("/projects", "projects")
	map.connect("projects_for_team", "/projects/for/team/:id", controller="projects", action="filter_by_team")
	
	map.resource("/documents", "documents")
	map.resource("/tasks", "tasks")
	map.resource("/meetings", "meetings")
	map.resource("/messages", "messages")
	#    map.connect('/{controller}/{action}')
	#    map.connect('/{controller}/{action}/{id}')
	
	return map
