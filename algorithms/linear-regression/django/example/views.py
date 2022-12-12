from django.shortcuts import render
from .forms import LinearRegressionForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        form = LinearRegressionForm(data=request.POST)
        if form.is_valid():
            new_item = form.save()
            new_item.train()
            y = new_item.predict(request.POST['x'])
            return render(request, 'example/index.html', {'form': form, 'prediction': y.tolist()})
    else:
        form = LinearRegressionForm()

    return render(request, 'example/index.html', {'form': form})
