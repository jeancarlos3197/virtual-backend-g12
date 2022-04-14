from rest_framework import serializers
from .models import Usuario

class RegistroUsuarioSerializer(serializers.ModelSerializer):

  def save(self):
    # creo una instancia de mi usuario con los campos ya validados
    nuevoUsuario = Usuario(**self.validated_data)
    # encripto la contraseña
    nuevoUsuario.set_password(self.validated_data.get('password'))
    # guardo el usuario en la base de datos
    nuevoUsuario.save()

    return nuevoUsuario

  class Meta:
    model = Usuario
    exclude = ['groups', 'user_permissions']
    # mediante el atributo extra_kwargs indicar que la password seria de solo escritura y ademas que el id sea solo lectura
    # fields = '__all__'
    extra_kwargs = {
      'password': {
        'write_only': True
        },
        'id': {
          'read_only': True
        }
    }