from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom User Manager
    """

    def create_user(self, email, password=None, **kwargs):
        """
        Create a normal user.
        """
        if not email:
            raise ValueError('Email required.')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Create a super user.
        """
        user = self.create_user(email, password, **kwargs)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
