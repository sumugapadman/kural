from flask import Flask, request, Blueprint, render_template
from src.controllers import Thirukural
import random

common_blueprint = Blueprint('common', __name__)

@common_blueprint.route('/')
def index():
    random_kural = random.randint(1,1330)
    kural_info = Thirukural(random_kural)
    kural = kural_info.getKural()
    return render_template('index.html',kural=kural)