from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required

from django.conf import settings
from accounts.forms import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import send_mail

from django.template.loader import get_template



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()



            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))




            else:
                messages.error(request, "unable to log you in at this time!")




    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data.get("email")
            contact_email = request.POST.get('contact_email' , '')
            form_content = request.POST.get('content', '')

            subject = "Thanks for the email"
            from_email = settings.EMAIL_HOST_USER
            to_email = [contact_email]
            message = """welcome"""
            send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=message, fail_silently=True)

            return redirect('contact_thanks')

    return render(request, 'contacts/contact.html', {
        'form': form_class,
    })



