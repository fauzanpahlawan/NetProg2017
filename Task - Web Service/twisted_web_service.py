from twisted.web.resource import Resource
from twisted.web import server
from twisted.internet import reactor
from connect_to_database import *
import json


class Home(Resource):
    def render_GET(self, request):
        return "Welcome to e11 company!"


class Employee(Resource):
    def render_GET(self, request):
        return select_all('employee')

    def render_POST(self, request):
        try:
            _id = request.args["id"][0]
            name = request.args["name"][0]
            position = request.args["position"][0]
            addr = request.args["address"][0]
            return insert_into('employee', (_id, name, position, addr))
        except:
            return "The form need id, name, position, and address"

    def getChild(self, _id, request):
        return EmployeeID(int(_id))


class EmployeeID(Resource):
    def __init__(self, _id):
        Resource.__init__(self)
        self._id = _id

    def render_GET(self, request):
        return select_one('employee', self._id)

    def render_PUT(self, request):
        def update_data(keys, data_update, data_current):
            data_update = data_update.split('&')
            for i in data_update:
                if keys in i:
                    return i.split('=')[1].replace('+', ' ')
                else:
                    return data_current[keys]

        data_current = json.loads(select_one('employee', self._id))["data"][0]
        data_update = request.content.getvalue()
        name = update_data('name', data_update, data_current)
        position = update_data('position', data_update, data_current)
        address = update_data('address', data_update, data_current)
        return alter_table('employee', (name, position, address, self._id))

    def render_DELETE(self, request):
        return delete_from('employee', self._id)


root = Resource()
root.putChild('', Home())
root.putChild('employee', Employee())
site = server.Site(root)
reactor.listenTCP(7777, site)
reactor.run()
