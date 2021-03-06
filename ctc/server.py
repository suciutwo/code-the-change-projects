"""The server, which handles all routing logic."""
import os

import webapp2

from ctc import handlers


IS_DEV = (
    'SERVER_SOFTWARE' in os.environ and
    os.environ['SERVER_SOFTWARE'].startswith('Development'))


def named_route(path, handler):
    """Returns a webapp2 route with a name populated.

    Args:
        path: the string path to handle.
        handler: a class that will be used as the handler and as the name.

    Returns:
        The corresponding webapp2 handler.
    """
    return webapp2.Route(path, handler=handler, name=handler)


APP = webapp2.WSGIApplication([
    named_route(r'/', handlers.MainPage),
    named_route(r'/projects', handlers.ListProjects),
    named_route(r'/project/<project_id:\d+>', handlers.DisplayProject),
    named_route(r'/project/<project_id:\d+>/edit', handlers.EditProject),
    named_route(r'/project/<project_id:\d+>/join', handlers.JoinProject),
    named_route(r'/project/<project_id:\d+>/leave', handlers.LeaveProject),
    named_route(r'/project/new', handlers.NewProject),
    named_route(r'/dashboard', handlers.DisplayDashboard),
    named_route(r'/user/<user_id:\d+>', handlers.DisplayUser),
    named_route(r'/user/<user_id:\d+>/edit', handlers.EditUser)
], debug=IS_DEV)
