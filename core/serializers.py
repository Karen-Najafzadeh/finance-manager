from djoser.serializers import UserCreateSerializer as DjoserDefaultUserCreateSerializer
class UserCreateSerializer (DjoserDefaultUserCreateSerializer):
    class Meta (DjoserDefaultUserCreateSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name']