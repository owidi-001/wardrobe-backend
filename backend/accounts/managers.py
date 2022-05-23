from django.contrib.auth.models import (
    BaseUserManager
)

# from customer.models import Customer
# from vendor.models import Vendor


class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Please input your name')

        if not phone:
            raise ValueError('Please input your phone number')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password=None):
        """
        Creates and saves a superuser with the given name, email, phone and password.
        """
        user = self.create_user(
            name,
            email,
            password=password,
            phone=phone,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    # def create_customer(self, name, email, phone, password=None):
    #     """
    #     Creates and saves a customer with the given name, email, phone and password.
    #     """
    #     user = self.create_user(name, email, phone, password)
    #     Customer.objects.create(user=user)
    #     return user

    # def create_vendor(self, name, email, phone, password=None):
    #     """
    #     Creates and saves a vendor with the given name, email, phone and password.
    #     """
    #     user = self.create_user(name, email, phone, password)
    #     Vendor.objects.create(user=user)
    #     return user
