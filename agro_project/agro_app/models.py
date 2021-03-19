from django.db import models
from django.contrib.postgres.fields import ArrayField


class AgroUser(models.Model):
    # user_type = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    number = models.BigIntegerField()
    is_agree = models.BooleanField(null=True)

    def authenticate(self, username, password):
        self.username = username
        self.password = password
        return [self.username, self.password]

    def __str__(self):
        return self.username


class Viloyat(models.Model):

    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Tuman(models.Model):
    vil_id = models.ForeignKey(Viloyat,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Yangilik(models.Model):
    viloyat_id = models.ForeignKey(Viloyat, on_delete=models.SET_NULL, null=True)
    malumoti_qisqacha = models.TextField(null=False)
    toifa = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=100, null=False)
    reklama_turi = models.SmallIntegerField(null=True)
    biznes = models.BooleanField(null=False, default=True)
    holat = models.SmallIntegerField(null=False)
    chiqarilgan_yili = models.IntegerField(null=False)
    summa_narxi = models.BigIntegerField()
    pul_turi = models.SmallIntegerField(null=False)
    kelishilgan = models.BooleanField(null=True)
    rasmlar = ArrayField(models.ImageField(upload_to="images/", null=False), blank=True, default=[])

    def __str__(self):
        return self.name


# class Tovarlar(models.Model):
#     tafsif = models.CharField(max_length=100, null=False)
#     name_shahar = models.CharField(max_length=100, null=False)
#     elon_nomi = models.CharField(max_length=100, null=False)
#     narxi = models.BigIntegerField(null=False)
#     aqw = models.CharField(max_length=100, null=False)
#     kelishilgan = models.BooleanField(null=True)
#     reklama_turi = models.SmallIntegerField(null=True)
#     holat = models.SmallIntegerField(null=False)
#     toifa = models.SmallIntegerField(null=True)
#     biznes = models.BooleanField(null=False)
#     rasmlar = ArrayField(models.ImageField(upload_to="images/", null=False), blank=True)
#     chiqarilgan_yili = models.IntegerField(null=False)