from django.db import models

from interview.core.behaviors import IsActiveModel, TimestampedProfileModel, IsStaffModel, IsSuperUserModel, IsAdminModel
    

class UserRoleTypeModel(IsStaffModel, IsSuperUserModel, IsAdminModel, models.Model):
    role_name = models.CharField(max_length=225)
    enabled = models.BooleanField()
    tags = models.ManyToManyField(OrderTag, related_name='orders')

    class Meta:
        abstract = True

class UserRoles(IsStaffModel, IsSuperUserModel, IsAdminModel, TimestampedProfileModel, models.Model):
    types = models.ForeignKey(
        UserRoleTypeModel,
        on_delete=models.CASCADE,
        related_name='userroles'
    )
    class Meta:
        verbose_name_plural = 'User Roles'
    
    def __str__(self) -> str:
        return self.name

class UserProfile(UserProfileModel, TimestampedProfileModel, IsActiveModel, models.Model):
    user_roles = models.ForeignKey(
        UserRoles,
        on_delete=models.CASCADE,
        related_name='userroles'
    )
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField()
    metadata = models.JSONField()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_full_name(cls, type_id: int):
        obj =  cls.objects.filter(type_id=type_id)
        return "{} {}".format(obj.first_name, obj.last_name)

    @classmethod
    def get_user_name(cls, type_id: int):
        return cls.objects.filter(type_id=type_id)
        return "{}".format(obj.user_name)
