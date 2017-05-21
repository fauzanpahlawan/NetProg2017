from twisted.web.resource import Resource
from twisted.web import server
from twisted.internet import reactor


class Home(Resource):
    def render_GET(self, request):
        return "This is index page."


class Student(Resource):
    def render_GET(self, request):
        return "Student page."

    def render_POST(self, request):
        name = request.args["name"][0]
        addr = request.args["addr"][0]
        return "You send: " + name + " - " + addr


class Lecture(Resource):
    def render_GET(self, request):
        return "Lecture page."


class Login(Resource):
    def render_GET(self, request):
        return "Login page of student."
# Enlist the resource
# Create resource root
root = Resource()
root.putChild('', Home())
root.putChild('student', Student())
root.putChild('lecture', Lecture())
root.putChild('login', Login())
# Create site component
site = server.Site(root)

# Define reactor
reactor.listenTCP(7777, site)
reactor.run()
