from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from .urls import *
from django.core.files.storage import FileSystemStorage

def index(request):
    a = []
    if request.GET:
        var = request.GET.get("search")
        tanlab_ol = Yangilik.objects.all()
        region_id = request.GET.get("region_id")


        if int(region_id) != 0:
            tanlab_ol = tanlab_ol.filter(tumanlar_id_id=region_id)

        for i in tanlab_ol:
            if str(var).lower() in str(i.name).lower():

                a.append(i)

    viloyatlar = Viloyat.objects.all()
    tumanlar = Tuman.objects.all()
    ctx = {
        'viloyatlar': viloyatlar,
        'tumanlar': tumanlar,
        'a': a,
        "askiy": askiy,

        # 'tanlab_ol0': tanlab_ol
    }

    return render(request, 'index.html', ctx)


def registratsiya(request):
    agroUser = AgroUser.objects.all()
    agro_user = AgroUser()
    if request.POST.get('auser'):
        username = request.POST.get("auser")
        password = request.POST.get("pass")

        user = AgroUser().authenticate(username, password)
        print("A", username)
        global askiy
        askiy = username.capitalize()
        print("B", askiy)

        l1, l2 = [], []
        for i in agroUser:
            l1.append(i.username)
            l2.append(i.password)


        if user[0] in l1 and user[1] in l2:

            return redirect(index)



        else:
            messages.error(request, 'USERNAME OR PASSWORD INCORRECT')
            return redirect(registratsiya)
    # registratsiya uchun
    elif request.POST.get("username"):
        # agro_user.user_firma = request.POST.get("user_firma")
        agro_user.username = request.POST.get("username")
        agro_user.email = request.POST.get("email")
        agro_user.password = request.POST.get("password")
        agro_user.number = request.POST.get("number")
        agro_user.save()
        return render(request, 'registratsiya.html')
    else:
        return render(request, 'registratsiya.html')


# def login(request):


def razdel(request):
    yangilik = Yangilik.objects.all()
    ctx = {
        "askiy": askiy,
        'yangilik': yangilik,

    }
    return render(request, 'razdel.html',ctx)


def page(request, prod_id):
    product = Yangilik.objects.get(pk=prod_id)
    ctx = {
        'pro': product,
        "askiy": askiy,
    }
    return render(request, 'page.html', ctx)


def advert(request):
    a = []
    if request.GET:
        var = request.GET.get("search")
        tanlab_ol = Yangilik.objects.all()
        region_id = request.GET.get("region_id")
        print(tanlab_ol)
        print(var, region_id)
        if int(region_id) != 0:
            tanlab_ol = tanlab_ol.filter(tumanlar_id_id=region_id)
        print(tanlab_ol)
        for i in tanlab_ol:
            if str(var).lower() in str(i.name).lower():
                print(i.name)
                a.append(i)
        print(a)
    viloyatlar = Viloyat.objects.all()
    tumanlar = Tuman.objects.all()
    ctx = {
        'viloyatlar': viloyatlar,
        'tumanlar': tumanlar,
        'a': a,

        # 'tanlab_ol0': tanlab_ol
    }

    return render(request, 'advert.html', ctx)


def add(request,):
    yangilik = Yangilik.objects.all()
    model = AgroUser.objects.get(pk=1)
    form = AgroUserForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
    print(form.errors)

    ctx = {
        "form": form,
        "askiy": askiy,
        'yangilik': yangilik,
    }

    return render(request, "add.html", ctx)



def customers(request):
    ctx = {
        "askiy": askiy
    }
    return render(request, 'customers.html',ctx)


def salers(request):
    ctx = {
        "askiy": askiy
    }
    return render(request, 'salers.html',ctx)


def form(request):
    viloyatlar = Viloyat.objects.all()

    if request.POST and request.FILES:

        form = YangiliklarForm(request.POST, request.FILES)
        # print(form.errors)
        rasmlar = request.FILES.getlist("rasmlar", [])
        images = []
        for rasm in rasmlar:
            fs = FileSystemStorage()
            filename = fs.save(rasm.name, rasm)
            uploaded_file_url = fs.url(filename)
            images.append(uploaded_file_url)
        kelishilgan = False
        if request.POST.get("kelishilgan") == 'on':
            kelishilgan = True
        if form.is_valid():
            form.save(images=images, kelishilgan=kelishilgan)
        print(images)
    ctx = {
        "viloyatlar": viloyatlar
    }
    return render(request, "form.html", ctx)


def payment(request):
    ctx = {
        "askiy": askiy
    }
    return render(request, 'payment.html',ctx)


def test(request):
    return render(request, 'test.html')