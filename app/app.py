# IMPORTS #####################################################################
from flask import Flask

from .config import AppDevConfig, AppProdConfig
from .env import env


# APPLICATION #################################################################
# Application creation.
app = Flask(__package__)
# Application configuration.
app.config.from_object(env.config(dev_config=AppDevConfig, prod_config=AppProdConfig))


# CONTEXT PROCESSORS ##########################################################
@app.context_processor
def inject_app_name():
	return dict(app_name=__package__)