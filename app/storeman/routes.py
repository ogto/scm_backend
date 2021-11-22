"""
Storeman routes table
soonho.bahng@stafact.net
2021.09.13
"""

from flask_restx import Api
from app.storeman import blueprint

from app.storeman.controller.user_controller import api as user_ns
from app.storeman.controller.group_controller import api as group_ns
from app.storeman.controller.store_controller import api as store_ns
from app.storeman.controller.menu_controller import api as menu_ns
from app.storeman.controller.auth_controller import api as auth_ns
from app.storeman.controller.category_controller import api as cat_ns
from app.storeman.controller.prd_controller import api as prd_ns
from app.storeman.controller.hd_api_controller import api as hd_ns

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus (restx) web service'
          )
api.add_namespace(user_ns)
api.add_namespace(group_ns)
api.add_namespace(store_ns)
api.add_namespace(menu_ns)
api.add_namespace(auth_ns)
api.add_namespace(cat_ns)
api.add_namespace(prd_ns)
api.add_namespace(hd_ns)