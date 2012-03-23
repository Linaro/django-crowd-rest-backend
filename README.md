Django authentification backend using Crowd REST API
====================================================

This is a very rough implementation of a django backend
using Crowd's REST API.

It is inspired by the various forks of django-crowd-backend.
Those implementations were always using SOUP.
This one simple because it's just using REST API supported by Crowd. 
See [Atlassian](https://developer.atlassian.com/display/CROWDDEV/Crowd+REST+APIs)

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

Problems ?
==========

Just send me a message. Let's see if I can help.

License
=======

Use this code as you want. Consider it free. Say thank you. Don't blame me if it doesn't work for you.