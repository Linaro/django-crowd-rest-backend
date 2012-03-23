from django.contrib.auth.models import User
from django.db import models

models.BooleanField(default=False,help_text=("Crowd backed user?")).contribute_to_class(User,'is_crowd_user')