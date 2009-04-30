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
    map.connect("add_user", "/users/new", controller="users", action="add")
    map.connect("update_user", "/users/update/:id", controller="users", action="update")
    map.connect("delete_user", "/users/delete/:id", controller="users", action="delete")

    map.connect("list_users", "/users/", controller="users", action="list")
    map.connect("user_details", "/users/:id", controller="users", action="details")
    map.connect("users_login", "/users/login/:username/:password", controller="users", action="login")
    
#    map.connect('/{controller}/{action}')
#    map.connect('/{controller}/{action}/{id}')
#    map.connect("/users/login", controller='users')

    return map
