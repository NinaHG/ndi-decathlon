# IMPORTS #####################################################################
from os import environ
from dotenv import load_dotenv


# Class #######################################################################
class Environment:

	def __init__(self, default_mode: str = "production"):
		load_dotenv()
		self._prod = "production"
		self._dev = "development"
		self._mode = environ.get("FLASK_ENV")

		if self._mode is None:
			if default_mode not in {self._prod, self._dev}:
				raise AttributeError()
			else:
				self._mode = default_mode

	def is_prod_env(self):
		return self._prod == self._mode

	def is_dev_env(self):
		return self._dev == self._mode

	@property
	def mode(self):
		return self._mode

	def config(self, dev_config: object, prod_config: object):
		return dev_config if self.is_dev_env() else prod_config


# Execution environment #######################################################
env = Environment()