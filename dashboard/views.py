from django.shortcuts import render, redirect
from .forms import ModelForm
from .models import MLModel
import numpy as np

# Create your views here.
def index(request):
  if request.method == 'POST':
    form = ModelForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('dashboard-results')
  else:
    form = ModelForm()
    
  form = ModelForm()
  context = {
    'form': form,
  }
  return render(request, 'dashboard/index.html', context)

def results(request):
    prediction_results = MLModel.objects.all()
    total_berhasil = MLModel.objects.filter(keberhasilan="['Ya']").count()
    total_gagal = MLModel.objects.filter(keberhasilan="['Tidak']").count()
    total_data = prediction_results.count()

    if total_data > 0:
        average_matematika = "{:.2f}".format(np.mean([result.matematika for result in prediction_results]))
        average_bahasa_inggris = "{:.2f}".format(np.mean([result.bahasa_inggris for result in prediction_results]))
        average_bahasa_indonesia = "{:.2f}".format(np.mean([result.bahasa_indonesia for result in prediction_results]))
        tingkat_keberhasilan = "{:.2f}".format((total_berhasil / total_data) * 100)
    else:
        average_matematika = 0
        average_bahasa_inggris = 0
        average_bahasa_indonesia = 0
        tingkat_keberhasilan = 0
    
    print(total_data)
    print(average_matematika)
    print(average_bahasa_inggris)
    print(average_bahasa_indonesia)
    print(tingkat_keberhasilan)

    context = {
        'prediction_results': prediction_results,
        'tingkat_keberhasilan': tingkat_keberhasilan,
        'average_matematika': average_matematika,
        'average_bahasa_inggris': average_bahasa_inggris,
        'average_bahasa_indonesia': average_bahasa_indonesia,
        'jumlah_berhasil': total_berhasil,
        'jumlah_gagal': total_gagal,
        'total_data': total_data,
    }
  
    return render(request, 'dashboard/result.html', context)