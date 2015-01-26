from django.db import models


class TestProject(models.Model):
    popularity = models.FloatField(null=False, default=0)


class TestFundraiser(models.Model):
    pass


class TestTask(models.Model):
    pass
    