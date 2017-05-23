import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import RequestContext
from users.forms import UserForm
from users.models import User

def register(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():  
            time = request.POST.get('time', '')
            nama = request.POST.get('nama', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            pekerjaan = request.POST.get('pekerjaan', '')
            institusi = request.POST.get('institusi', '')
        user_obj = User(time=time, nama=nama, email=email, phone=phone, pekerjaan=pekerjaan, institusi=institusi)
        user_obj.save()
 	email_subject = 'Registrasi KLAS'
	email_body = "Hallo, %s, terimaksih telah mendaftar. Jangan lupa ikuti event Cangkru'an." %(nama)
	send_mail(email_subject,email_body,'cangkrukan.klas@gmail.com',[email])
	return render(request, 'users/register.html', {'user_obj': user_obj,'is_registered':True })
 
    else:
        form = UserForm()  
 
        return render(request, 'users/register.html', {'form': form})
 
#@permission_required('is_superuser')
@login_required(login_url="login")
def showdata(request):
    all_users = User.objects.all()
    return render(request, 'users/showdata.html', {'all_users': all_users, })

def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dataregistrasi.csv"'

    writer = csv.writer(response)
    writer.writerow(['','DAFTAR PESERTA YANG TELAH REGISTRASI',''])
    writer.writerow(['time', 'nama', 'email', 'phone', 'pekerjaan', 'institusi'])

    users = User.objects.all().values_list('time', 'nama', 'email', 'phone', 'pekerjaan', 'institusi')
    for user in users:
        writer.writerow(user)

    return response

def page_not_found(request):
	return render(request,'users/404.html')
def delete(request):
	all_users=User.objects.all().delete()
	return render(request, 'users/showdata.html', {'all_users':all_users,})
