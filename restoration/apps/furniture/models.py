from django.db import models
from django.core.exceptions import ValidationError


class Legs(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    size = models.IntegerField(null=False, blank=False, verbose_name="size (in cm)")
    created_ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Legs"

    def __str__(self):
        return self.name


class Feet(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    width = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    radius = models.IntegerField(null=True, blank=True)
    created_ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feet"

    def __str__(self):
        return self.name

    def validate(self):
        if self.radius and (self.length or self.width):
            raise ValidationError(
                'A foot with a radius can not have length or width.')
        if self.length and not self.width:
            raise ValidationError(
                'A foot with a length must also have a width.')
        if self.width and not self.length:
            raise ValidationError(
                'A foot with a width must also have a length.')

    def clean(self):
        self.validate()

    def save(self, *args, **kwargs):
        self.validate()
        super().save(*args, **kwargs)


class Tables(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False, blank=False)
    legs = models.ForeignKey(Legs, on_delete=models.CASCADE, verbose_name="leg_id")
    leg_count = models.IntegerField(null=True, blank=True)
    feet = models.ForeignKey(Feet, on_delete=models.CASCADE, verbose_name="feet_id")
    feet_count = models.IntegerField(null=True, blank=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Table"

    def __str__(self):
        return self.name

    def validate(self):
        if self.leg_count != self.feet_count:
            raise ValidationError(
                'Leg Count & Feet Count should be equal in a Table.')

    def clean(self):
        self.validate()

    def save(self, *args, **kwargs):
        self.validate()
        super().save(*args, **kwargs)
