from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# from skymarket.users.managers import UserRoles, UserManager
# from managers import UserManager, UserRoles
from users.managers import UserManager, UserRoles


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    phone = PhoneNumberField()
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    # Необходимые параметры для корректной работе Django
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()
