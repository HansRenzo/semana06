from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.TextField(null=False)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table = 'categorias'

class Producto(models.Model):
    nombre = models.TextField(null=False)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)

    createdAt= models.DateTimeField(auto_now_add=True, db_column='created_at')

    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    # on_delete > es la accion que tomara al momento de hacer la eliminacion de una categoria y si esta tiene productos
    # CASCADE > elimina la categoria y luego elimina en forma consecutiva a todos los productos de esa categoria
    # PROTECT > evita la eliminacion de la categoria siempre y cuando esta tenga productos y lanzara un error de tipo IntegrityError
    # RESTICT > evita la eliminacion al igual que el PROTECT pero esto emitira un error de tipo RestrictedError
    # SET_NULL > elimina la categoria y a todos sus productos les cambia el valor de la categoria_id a NULL
    # SET_DEFAULT > elimina la categoria y de acuerdo al valor que le colocamos en default lo cambiara a ese valor
    # DO_NOTHING > No realiza ninguna accion, elimina la categoria y no hace ningun cambio en los productos, No se debe utilizar esta opcion ya que genera mala integridad de los datos

    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE, db_column='categoria_id',
                                  related_name='productos')
    class Meta:
        db_table = 'productos'
        ordering =['-nombre', 'precio']
        unique_together = ['nombre', 'precio']