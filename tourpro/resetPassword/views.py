from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes  # Change this line
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode

UserModel = get_user_model()
User = get_user_model()

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = UserModel.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': 'http://127.0.0.1:8000/',
                        'site_name': 'YourSite',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    send_mail(subject, email, "admin@example.com", [user.email], fail_silently=False)
                messages.success(request, 'An email has been sent to ' + email + ". Please check its inbox to continue reseting password.")
                return redirect('/')
            else:
                messages.error(request, 'No user is associated with this email address')
                return redirect('custom_password_reset')
    else:
        form = PasswordResetForm()
    return render(request, 'password/password_reset_request.html', context={'form': form})


def password_reset_done(request):
    return render(request, "password/password_reset_done.html")

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, 'Your password has been reset.')
                return redirect('password_reset_complete')
            else:
                messages.error(request, 'Passwords do not match.')
                return redirect('password_reset_confirm', uidb64=uidb64, token=token)
        return render(request, "password/password_reset_confirm.html", {'uidb64': uidb64, 'token': token})
    else:
        messages.error(request, 'The reset password link is no longer valid.')
        return redirect('password_reset_request')
def password_reset_complete(request):
    return render(request, "password/password_reset_complete.html")
