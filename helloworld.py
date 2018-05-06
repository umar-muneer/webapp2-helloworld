import cgi

from google.appengine.api import users
from google.appengine.ext import db
import webapp2

class GreetingModel(db):
    author=db.UserProperty()
    content=db.StringProperty(multiline=True)
    datetime=db.DateTimeProperty(auto_now_add=True)

def guestbook_key(guestbook_name=None):
    return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</pre></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook)
], debug=True)