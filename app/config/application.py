# IMPORTS #####################################################################
from os import urandom


# CONFIGURATIONS ##############################################################
class AppDevConfig:
	"""
	Application Development Configuration
	"""
	SECRET_KEY: bytes = urandom(32)
	FLASK_ENV: str = "development"
	FLASK_DEBUG: bool = True


class AppProdConfig(AppDevConfig):
	"""
	Application Production Configuration
	"""
	FLASK_ENV: str = "production"
	FLASK_DEBUG: bool = False