from django.db import models

from interview.core.behaviors import IsActiveModel, UserProfileModel, TimestampedProfileModel, IsStaffModel, IsSuperUserModel, IsAdminModel
    
class UserRoles(IsStaffModel, IsSuperUserModel, IsAdminModel, TimestampedProfileModel, models.Model):

    class Meta:
        verbose_name_plural = 'User Roles'
    
    def __str__(self) -> str:
        return self.name

class UserProfile(UserProfileModel, TimestampedProfileModel, IsActiveModel, models.Model):
    type = models.ForeignKey(
        UserRoles,
        on_delete=models.CASCADE,
        related_name='userroles'
    )
    metadata = models.JSONField()
    

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

    @classmethod
    def is_authenticated(cls, type_id: int):

        obj = cls.objects.filter(type_id=type_id)
        return obj.is_authenticated