from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

# Create your models here.

class MLModel(models.Model):
  name = models.CharField(max_length=100, null=True)
  matematika = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)],null=True)
  bahasa_inggris = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)],null=True)
  bahasa_indonesia = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)],null=True)
  keberhasilan = models.CharField(max_length=100, blank=True, null=True)
  date = models.DateField(auto_now_add=True)
  
  def save(self, *args, **kwargs):
    ml_model = joblib.load('ml_model/un_to_it_model.joblib')
    self.keberhasilan = ml_model.predict([[ self.matematika, self.bahasa_inggris, self.bahasa_indonesia ]])
    return super().save(*args, *kwargs)
  
  class Meta:
    ordering = ['-date']
  
  def __str__(self):
    return self.name
  