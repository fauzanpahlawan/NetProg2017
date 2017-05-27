from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints


class StaffPage(Resource):
    def __init__(self, staff_name):
        Resource.__init__(self)
        self.staff_name = staff_name

    def render_GET(self, request):
        return "This is staff " + self.staff_name + " page."


class Staff(Resource):
    def getChild(self, name, request):
        return StaffPage(str(name))

root = Staff()
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()
