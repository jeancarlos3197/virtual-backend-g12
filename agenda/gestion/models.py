from django.db import models

class Etiqueta(models.Model):
  # https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
  # https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
  id = models.AutoField(primary_key=True, unique=True, null=False)
  nombre = models.CharField(max_length=20, unique=True, null=False)

  # Columans de auditoria, ayudaran en el seguimiento de la creacion de registros
  createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
  updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

  # todas las configuraciones propieas de la tabla sera mediante la definicion de sus atributos en la clase Meta

  class Meta:
    # cambiar el nombre de la tabla en la bd (a diferencia del nombre de la Clase)
    db_table = 'etiquetas'
    # modificar el ordenamiento natural (por el id) e imponiendo el propio que sea ASC del nombre solamente funcionara cuando se haga el ORM
    ordering = ['-nombre']