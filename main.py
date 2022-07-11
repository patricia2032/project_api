import json									# IMPORT

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

# Create Flask application Instance			# CREATE INSTANCE
app = Flask(__name__)
api = Api(app)


class GUID(Resource):						# CLASS

	def get(self):							# GET
		return {}


class extractingInfo_get(Resource):				#Dinamic
	def get(self, id):

		print(id)
		return {}


class extractingInfo_patch(Resource):				#Dinamic
	def patch(self, id):

		print(id)
		return {}




# URL
api.add_resource(GUID, '/guid/9094E4C980C74043A4B586B420E69DDF')


# Run the Flask server (.run)						# RUN SERVER
if __name__ == "__main__":
	app.run(debug=True)