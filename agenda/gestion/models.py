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

class Tareas(models.Model):
  class CategoriasOpciones(models.TextChoices):
    # Cada opcion le podemos pasar dos paramtros en la cual el primero sera su abreviatura para que se guarde en la bd y el nombre completo
    TODO = 'TODO', 'TO_DO'
    IN_PROGRESS = 'IP', 'IN_PROGRESS'
    DONE = 'DONE', 'DONE'
    CANCELLED = 'CANCELLED', 'CANCELLED'

  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=45, null=False)
  categoria = models.CharField(max_length=45, choices=CategoriasOpciones.choices, default=CategoriasOpciones.TODO)

  # categoria = models.CharField(max_length=45, choices=[
  #   ('TODO', 'TO_DO'),
  #   ('IP', 'IN_PROGRESS'),
  #   ('DONE', 'DONE'),
  #   ('CANCELLED', 'CANCELLED'),
  # ], default='TODO')

  fechaCaducidad = models.DateTimeField(db_column='fecha_caducidad')
  importancia = models.IntegerField(null=False)
  descripcion = models.TextField()

  createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
  updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')
  # en django se puede utilizar las relaciones one-to-one, one-to-many o many-to-many para crear relaciones entre tablas
  etiquetas = models.ManyToManyField(Etiqueta, db_table='tareas_etiquetas', related_name='tareas')

  class Meta:
    db_table = 'tareas'

