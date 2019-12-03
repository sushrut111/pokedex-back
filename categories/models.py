from django.db import models

# Create your models here.
class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    deleted = models.BooleanField(default=False)

class PokemonMap(models.Model):
    cid = models.AutoField(primary_key=True)
    pokeid = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='pokemon'
    )
    current_rank = models.IntegerField()
    old_rank = models.IntegerField()
    deleted = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['pokeid','category'], name= 'pokecategory'),
            ]