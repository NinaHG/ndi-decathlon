# IMPORTS #####################################################################
from flask_security.models.fsqla_v2 import FsUserMixin, FsRoleMixin
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app import db


# MODEL #######################################################################
class User(db.Model, FsUserMixin):
	__tablename__ = "user"
	# user personal information
	id = Column(Integer(), primary_key=True, autoincrement=True)
	email = Column(String(255), unique=True, nullable=False)
	password = Column(String(255), nullable=False)
	first_name = Column(String(255), nullable=False)
	last_name = Column(String(255), nullable=False)

	# relation with roles
	roles = relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))


class Role(db.Model, FsRoleMixin):
	__tablename__ = "role"
	# role information
	id = Column(Integer(), primary_key=True, autoincrement=True)
	name = Column(String(80), unique=True)
	description = Column(String(255))


class RolesUsers(db.Model):
	__tablename__ = "roles_users"
	id = Column(Integer(), primary_key=True, autoincrement=True)
	user_id = Column('user_id', Integer(), ForeignKey('user.id'))
	role_id = Column('role_id', Integer(), ForeignKey('role.id'))