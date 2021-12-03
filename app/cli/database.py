# IMPORTS #####################################################################
from flask.cli import AppGroup
import click
from os import path, mkdir, remove
from yaml import load_all, Loader

from app import app, db


# GROUP NAME ##################################################################
# Create a subgroup for database commands.
group = AppGroup(name="database", help="Database manager commands.")
app.cli.add_command(group)


# CONSTANTS ###################################################################
DATABASE_PATH = app.config.get("SQLALCHEMY_DATABASE_PATH")


# FUNCTIONS ###################################################################
def is_database_exist():
	return path.exists(DATABASE_PATH)


def create_database_directory():
	database_directory = path.dirname(DATABASE_PATH)
	if not path.exists(database_directory):
		mkdir(path.dirname(DATABASE_PATH))


def abort_if_false(ctx, param, value):
	if not value:
		ctx.abort()


def get_tables():
	tables = db.get_tables_for_bind()
	representation = ", ".join(map(lambda t: str(t), tables))
	return len(tables), representation


def ask_question(question: str, default_answer: bool):
	default_positive_answer = (" [Y/n]: ", {"n", "non", "no"})
	default_negative_answer = (" [y/N]: ", {"o", "oui", "y", "yes"})
	answer = default_positive_answer if default_answer else default_negative_answer
	return input(question + answer[0]).lower() not in answer[1]


# COMMANDS ####################################################################
@group.command(name="create", help="Create the database and they tables.")
@click.option("--force", default=False, is_flag=True, help="Force the creation of the database and its tables even if they already exist.")
def create_database(force):
	stop_command_execution = False
	if not is_database_exist():
		create_database_directory()
	elif not force:
		stop_command_execution = ask_question(question="This database already exist. Do you want to continue?", default_answer=False)
	if stop_command_execution:
		print("Aborted!")
	else:
		db.drop_all()
		db.create_all()
		tables = get_tables()
		print(f"Database was created with table{'s' if tables[0] > 1 else ''}: {tables[1]}")


@group.command(name="load", help="Load data sample from à yaml file.")
@click.argument("filepath", type=click.Path(exists=True))
def load_database_sample(filepath):
	with open(file=filepath, mode="r") as file:
		documents = load_all(file.read(), Loader=Loader)
		print("\n---\n".join(map(lambda document: "\n".join(map(lambda elem: elem.__repr__(), document)), documents)))


@group.command(name="remove", help="Remove database.")
@click.option("--force", is_flag=True, expose_value=False, callback=abort_if_false, prompt="Are you sure you want to remove the database?")
def remove_database():
	if is_database_exist():
		remove(DATABASE_PATH)
		print("Database was removed.")
	else:
		print("Database does not exist.")


@group.command(name="drop-tables", help="Delete tables in database.")
@click.option("--force", is_flag=True, expose_value=False, callback=abort_if_false, prompt="Are you sure you want to purge tables?")
def drop_tables():
	if is_database_exist():
		db.drop_all()
		print("Tables was dropped.")
	else:
		print("Database does not exist.")


@group.command(name="drop-dataset", help="Delete dataset in database.")
@click.option("--force", is_flag=True, expose_value=False, callback=abort_if_false, prompt="Are you sure you want to purge dataset?")
def drop_dataset():
	if is_database_exist():
		db.drop_all()
		db.create_all()
		print("Dataset was dropped.")
	else:
		print("Database does not exist.")


@group.command(name="show-tables", help="Show list of database tables.")
def show_tables():
	tables = get_tables()
	print(f"table{'s' if tables[0] > 1 else ''}: {tables[1]}")


@group.command(name="engine", help="Show URL database engine.")
def engine():
	print(db.engine.url)