Django authentification backend using Crowd REST API
====================================================

This is a very rough implementation of a django backend
using Crowd's REST API.

It is inspired by the various forks of django-crowd-backend.
Those implementations were always using SOUP.
This one is just using REST API supported by Crowd. 
See [Atlassian](https://developer.atlassian.com/display/CROWDDEV/Crowd+REST+APIs).

Current implementation
======================

- Connect to Crowd server
- Authenticate given user by password
- Sync Django user instance with attributes from Crowd user
- Setup Djnago user staff/superuser flags based on associated Crowd groups of user

Features
========

- HTTPS certificate validation when connecting to secure Crowd url

Missing
=======

- No handling of SSO cookie

Dependencies
============

- just 'urllib2' with a little tweak from [VerifiedHTTPS](https://github.com/josephturnerjr/urllib2.VerifiedHTTPS)
  to allow validation of https certificate.

How to use it
=============

- Edit settings.py to add 'crowdrest' app to your list of apps

- Adapt configuration settings for crowdrest in settings.py by adding
	
	# whether you want to sync django users from Crowd attributes
	AUTH_CROWD_ALWAYS_UPDATE_USER = True 
    
	# Django user will get staff flag when Crowd user is in given Crowd group
	AUTH_CROWD_STAFF_GROUP = 'staff' 
    
	# Django user will get superuser flag when Crowd user is in given Crowd group
	AUTH_CROWD_SUPERUSER_GROUP = 'superuser' 
    
	# crowdrest will use this username and password to connect to Crowd server
	AUTH_CROWD_APPLICATION_USER = 'django'
	AUTH_CROWD_APPLICATION_PASSWORD = 'django'
    
	# URL to Crowd REST API
	AUTH_CROWD_SERVER_REST_URI = 'http://127.0.0.1:8095/crowd/rest/usermanagement/latest'
    
	# Use given certificate file to validate https connection to Crowd server
	AUTH_CROWD_SERVER_TRUSTED_ROOT_CERTS_FILE = None
  
Problems ?
==========

Just send me a message. Let's see if I can help.

License
=======

Use this code as you want. Consider it free. Say thank you. Don't blame me if it doesn't work for you.