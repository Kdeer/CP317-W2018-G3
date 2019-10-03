from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Override of the default Django user manager to support
# our admin scheme as well as email as primary identifier
class UserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, email, password, username=None, **additional):
    if not email:
      raise ValueError('Email must be set to create a user')

    email = self.normalize_email(email)
    user = self.model(email = email, **additional)
    user.is_staff = False
    user.set_username(username)
    user.set_password(password)
    user.save(using = self._db)
    return user

  def create_user(self, email, password = None, username=None, **additional):
    additional.setdefault('is_superuser', False)
    return self._create_user(email, password, username, **additional)

  def create_admin(self, email, password, **additional):
    additional.setdefault('is_admin', True)

    if additional.get('is_admin') is not True:
      raise ValueError('Administrators must have is_admin = True')

    return self._create_user(email, password, **additional)

  def create_superuser(self, email, password, **additional):
    additional.setdefault('is_superuser', True)

    if additional.get('is_superuser') is not True:
      raise ValueError('Superusers must have is_superuser = True')

    return self._create_user(email, password, **additional)
