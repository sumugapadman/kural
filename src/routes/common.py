from flask import Flask, request, Blueprint, render_template

common_blueprint = Blueprint('common', __name__)

@common_blueprint.route('/')
def index():
    return render_template('index.html')