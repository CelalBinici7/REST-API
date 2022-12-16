#!/bin/bash
str="<This will cause an error>"
from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Games(Resource):
    def get(self):
        data = pd.read_csv('game.csv')
        data = data[data['genre']== 'Shooter']
        data = data.to_dict('records')
        return {'data' : data }, 200

    def post(self):
        id = request.args['id']
        title = request.args['title']
        short_description = request.args['short_description']
        game_url = request.args['game_url']
        genre = request.args['genre']
        platform = request.args['platform']
        publisher = request.args['publisher']
        developer = request.args['developer']
        release_date = request.args['release_date']
        freetogame_profile_url = request.args['freetogame_profile_url']
        

        data = pd.read_csv('game.csv')

        new_data = pd.DataFrame({
            'id'      			: [id],
            'title'   			: [title],
            'short_description'         : [short_description],
            'game_url'      		: [game_url],
            'genre'      		: [genre],
            'platform'      		: [platform],
            'publisher'      		: [publisher],
            'developer'      		: [developer],
            'release_date'      	: [release_date],
            'freetogame_profile_url'    : [freetogame_profile_url]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('game.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 200

    def delete(self):
        name = request.args['genre']
        data = pd.read_csv('game.csv')
        data = data[data['genre'] != genre]

        data.to_csv('game.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200

class title(Resource):
    def get(self):
        data = pd.read_csv('game.csv',usecols=['title'])
        data = data.to_dict('records')
        return {'data' : data }, 200
 

class genre(Resource):
    def get(self):
        data = pd.read_csv('game.csv',usecols=[5])
        data = data.to_dict('records')
        	
        return {'data' : data}, 200
        
        
class platform(Resource):
    def get(self):
        data = pd.read_csv('game.csv',usecols=[1,6])
        data = data.to_dict('records')
        
        return {'data' : data }, 200        


   
class genre2(Resource):
    def get(self,genre):
        data = pd.read_csv('game.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['genre'] == genre :
                return {'data' : entry}, 200
        return {'message' : 'No entry found with this name !'}, 404
 

# Add URL endpoints
api.add_resource(title, '/title')
api.add_resource(platform, '/platform')
api.add_resource(genre, '/genre')
api.add_resource(Games, '/Games')

api.add_resource(genre2, '/<string:genre>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
    app.run()

