from django.db import models
from django.contrib.auth import get_user_model
USER = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name="name is category:", max_length=200)
    brand = models.CharField(verbose_name="brand:", max_length=70)
    NOUT_TYPE = (
        (1, 'Laptoop'),
        (2, 'Noutbook'),
        (3, 'MackBoock'),
    )
    nout_type1 = models.IntegerField(verbose_name='Nout-Type', choices=NOUT_TYPE)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)






