from flask_restful import Resource, Api
from flask_ngrok import run_with_ngrok
import sentiment_review_process as AI
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
run_with_ngrok(app)

class String_Compute(Resource):
    def get(self, review):
        return jsonify({"Score" : AI.main(review.replace("%20", " "))})

api.add_resource(String_Compute, '/<string:review>')

if __name__ == '__main__':
    app.run()