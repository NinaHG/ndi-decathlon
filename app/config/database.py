# IMPORTS #####################################################################
from typing import Optional
from os import getcwd


# CONFIGURATIONS ##############################################################
class DatabaseConfig:
	SQLALCHEMY_TRACK_MODIFICATIONS = True


class SQLiteConfig(DatabaseConfig):
	"""
	SQLite Configuration

	:schema: driver:///path/database.db
	:example: sqlite:///home/scott/myapp/database/default.db
	"""
	SQLALCHEMY_DATABASE_DRIVER: str = "sqlite"
	SQLALCHEMY_DATABASE_PATH: str = f"{getcwd()}/database/default.db"
	SQLALCHEMY_DATABASE_URI: str = f"{SQLALCHEMY_DATABASE_DRIVER}:///{SQLALCHEMY_DATABASE_PATH}"
	SQLALCHEMY_ENGINE_OPTIONS: dict = {
		"pool_pre_ping": True
	}

	def __init__(self, path: str, options: Optional[dict] = None):
		self.SQLALCHEMY_DATABASE_PATH = path
		self.SQLALCHEMY_DATABASE_URI = f"{self.SQLALCHEMY_DATABASE_DRIVER}:///{path}"
		if options: self.SQLALCHEMY_ENGINE_OPTIONS = options



class PostgreSQLConfig(DatabaseConfig):
	"""
	PostgreSQL Configuration

	schema: dialect+driver://username:password@host:port/database
	example: postgresql://scott:tiger@localhost:5432/my_database
	"""
	pass