from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def new_survey(cls, data):
        query = "insert into dojos (name, location, language, comment) values(%(name)s,%(location)s,%(language)s,%(comment)s)"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)
    
    @classmethod
    def get_survey(cls):
        query = "select * from dojos order by id desc limit 1"
        results = connectToMySQL('dojo_survey_schema').query_db(query)

        return cls(results[0])
    
    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) <3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if survey['location'] == "--Select a Location--":
            flash("Must Select a Location")
            is_valid = False
        if survey['language'] == "--Select a Language--":
            flash("Must Select a Language")
            is_valid = False
        if len(survey['comment']) < 5:
            flash("Comments must be at least 5 characters")
            is_valid = False
        return is_valid