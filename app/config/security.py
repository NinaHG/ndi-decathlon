# IMPORTS #####################################################################


# CONFIGURATIONS ##############################################################
class SecurityDevConfig:
	"""
	Security Development Configuration
	"""
	SECURITY_PASSWORD_SALT = "146585145368132386173505678016728509634"
	SECURITY_TRACKABLE = True
	SECURITY_TWO_FACTOR = False
	SECURITY_UNIFIED_SIGNIN = False

	# default admin user
	SECURITY_DEFAULT_ADMIN_FIRST_NAME = "Admin"
	SECURITY_DEFAULT_ADMIN_LAST_NAME = ""
	SECURITY_DEFAULT_ADMIN_EMAIL = "default.admin@gmail.com"
	SECURITY_DEFAULT_ADMIN_PASSWORD = "123456789"

	# default admin role
	SECURITY_ADMIN_ROLE = "admin"

	# register
	SECURITY_REGISTER_URL = "/register"
	SECURITY_REGISTER_USER_TEMPLATE = "page/security/register.html"
	SECURITY_POST_REGISTER_VIEW = "/"

	# confirmation after registering
	SECURITY_CONFIRMABLE = False

	# login
	SECURITY_LOGIN_URL = "/login"
	SECURITY_LOGIN_USER_TEMPLATE = "page/security/login.html"
	# SECURITY_POST_LOGIN_VIEW = "/"

	# logout
	SECURITY_LOGOUT_URL = "/logout"
	SECURITY_LOGOUT_METHODS = ["GET", "POST"]
	SECURITY_POST_LOGOUT_VIEW = SECURITY_LOGIN_URL


class SecurityProdConfig(SecurityDevConfig):
	"""
	Security Production Configuration
	"""
	pass