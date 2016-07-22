""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

# from flask import Flask, request, redirect, render_template, session, flash
# import re
# import os,binascii
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class PokesModel(Model):
    def __init__(self):
        super(PokesModel, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """

    def add_one_user_m(self, new_user_details):
            print "MMMMMMMMMMMMMM",new_user_details
            print "NNNNNNNNNNNN", new_user_details['f_birth']
            password = new_user_details['f_password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            add_query = "INSERT INTO users (name, alias, email, pw_hash, birth, created_at, updated_at) \
            VALUES (:spec_name, :spec_alias, :spec_email, :spec_pw_hash, :spec_birth, NOW(), NOW())"
            add_data = { 
            'spec_name': new_user_details['f_name'],
            'spec_alias': new_user_details['f_alias'],
            'spec_email': new_user_details['f_email'],
            'spec_pw_hash': hashed_pw,
            'spec_birth': new_user_details['f_birth']
            }
            return self.db.query_db(add_query, add_data)

    def login_m(self, new_user_details):
        query = "SELECT * from users where email = :spec_email LIMIT 1"
        data = {'spec_email': new_user_details['f_login']}
        user = self.db.query_db(query, data)
        if user[0]:
            if self.bcrypt.check_password_hash(user[0]['pw_hash'], new_user_details['f_password']):
                return user[0]
        return False

    def get_all_users_m(self):
        # return self.db.query_db("SELECT * FROM users ORDER BY created_at DESC")
        return self.db.query_db("SELECT users.id, users.name, users.alias, pokes.num_pokes FROM users \
            LEFT JOIN pokes ON users.id = pokes.user_id")


