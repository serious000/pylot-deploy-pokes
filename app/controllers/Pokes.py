"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import Flask, request, redirect, render_template, session, flash
import re
import os,binascii
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class Pokes(Controller):
    def __init__(self, action):
        super(Pokes, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('PokesModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        # all_course = self.models['Course'].get_all_courses_m()

        # query = "SELECT * FROM courses"
        # all_courses = self.db.query_db(query)
        # print all_course
        return self.load_view('index.html')

    def add(self):
        # print "REQUEST.FORM IS", request.form
        user_details = request.form
        valid=True
        if (len(user_details['f_email']) < 1) or (not EMAIL_REGEX.match(user_details['f_email'])):
            valid=False
            flash("Invalid Email Address!",'error')
        # if (len(user_details['f_name']) < 2) or (not str(user_details['f_name']).isalpha()):
        if (len(user_details['f_name']) < 2):
            valid=False
            flash("Invalid name!",'error')
        # if (len(user_details['f_alias']) < 2) or (not str(user_details['f_alias']).isalpha()):
        if (len(user_details['f_alias']) < 2):
            valid=False
            flash("Invalid alias!",'error')
        if len(user_details['f_password']) < 8: 
            valid=False
            flash("Sorry, your password is less than 8 characters",'error')
        if user_details['f_password'] != user_details['f_pw_confirmation']:
            valid=False
            flash("Passwords must match!",'error')
        if valid==False:
            return redirect('/')
        else:
            self.models['PokesModel'].add_one_user_m(user_details)
            # message = "registered and logged in!"
            # return self.load_view('success.html', s_f_name=user_details['f_alias'], s_msg=message)
            return redirect('/')

    def login(self):
        session.clear()
        user_details = request.form
        login_user = self.models['PokesModel'].login_m(user_details)
        if not login_user:
            flash("Wrong Password!",'error')
            return redirect('/')
        else:
            session['login_id'] = login_user['id']
            # flash("Success!",'success')
            # message = "logged in!"
            # return self.load_view('success.html', s_f_name=login_user['first_name'], s_msg=message)
            # self.load_view('success.html', s_f_name=login_user['first_name'], s_msg=message)
            return redirect('/pokes/success')

    def pokes(self):
        all_users = self.models['PokesModel'].get_all_users_m()
        print "PPPPP", all_users
        return self.load_view('success.html', s_alluser=all_users)
        # return self.load_view('success.html')

    def poke_one_user(self):
        pass

    def logout(self):
        session.clear()
        return redirect('/')

