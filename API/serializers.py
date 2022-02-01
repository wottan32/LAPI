from rest_framework import serializers
#from rest_framework.validators import UniqueValidator

from .models import Usuario

'''
class UsuarioSerializer(serializers.Serializer):
    ID = serializers.UUIDField(
        #primary_key=True,
        default=uuid.uuid4,
        #editable=False,
        format='hex')
    Nombre = serializers.CharField(max_length=200, required=True, allow_blank=False)
    Apellido = serializers.CharField(max_length=200, required=True, allow_blank=False)
    Email = serializers.EmailField(label='No se permite duplicidad de mails',
                                   help_text='No se permite duplicidad de mails', max_length=200, required=True,
                                   allow_blank=False)
    FechaNac = serializers.DateField(label='YYYY-MM-DD', format='iso-8601', help_text='YYYY-MM-DD')
'''


class UsuarioSerializer(serializers.ModelSerializer):
    #ID = serializers.UUIDField()
    #Nombre = serializers.CharField(max_length=200, required=True)
    #Apellido = serializers.CharField(max_length=200, required=True)
    #Email = serializers.EmailField(
    #    required=True,
    #    validators=[
    #        UniqueValidator(queryset=Usuario.objects.all())
    #    ]
    #)
    #FechaNac = serializers.DateField(required=True)

    class Meta:
        model = Usuario
        fields = ['Nombre', 'Apellido', 'Email', 'FechaNac']
        # extra_kwargs = {'Nombre': {'required': True}}
        # extra_kwargs = {'Apellido': {'required': True}}
        # extra_kwargs = {'Email': {'required': True}}
        # extra_kwargs = {'FechaNac': {'required': True}}

    def create(self, validate_data):
        return Usuario.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.Nombre = validated_data.get('Nombre', instance.Nombre)
        instance.Apellido = validated_data.get('Apellido', instance.Apellido)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.FechaNac = validated_data.get('FechaNac', instance.FechaNac)
        instance.save()
        return instance
