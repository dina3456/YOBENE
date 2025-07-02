from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, blank=True)
    established_year = models.PositiveIntegerField(null=True, blank=True)

    def str(self):
        return self.name

class WashingMachine(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    capacity_kg = models.DecimalField(max_digits=4, decimal_places=1)
    energy_class = models.CharField(max_length=4, choices=[
        ('A+', 'A+'),
        ('A++', 'A++'),
        ('A+++', 'A+++'),
        ('B', 'B'),
        ('C', 'C'),
    ], default='A++')
    spin_speed = models.IntegerField(help_text="Оберти на хвилину", default=1200)
    has_dryer = models.BooleanField(default=False)
    color = models.CharField(max_length=50, default="White")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def str(self):
        return f"{self.brand.name} {self.model_name}"
