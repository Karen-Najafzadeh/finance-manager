from djoser.serializers import UserCreateSerializer as x
class UserCreateSerializer (x):
    class Meta (x.Meta):
        fields = ['id','username','password','email','first_name','last_name']