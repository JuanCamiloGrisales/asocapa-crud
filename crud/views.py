from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente

# Create your views here.


def index(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}

    return render(request, 'home.html', context)


def create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            nuevo_form = ClienteForm()
            context = {'form': nuevo_form, 'success': True}
            return render(request, 'create.html', context)

    form = ClienteForm()
    context = {'form': form}
    return render(request, 'create.html', context)


def update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        try:
            form = ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                return redirect('index')
        except Exception as e:
            context = {'form': form, 'error': e}
            return render(request, 'create.html', context)
    form = ClienteForm(instance=cliente)
    context = {'form': form}
    return render(request, 'create.html', context)
    


def delete(request, pk):
    try:
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.delete()
    except Cliente.DoesNotExist:
        raise Http404("No se pudo encontrar el cliente especificado.")

    return redirect('index')
