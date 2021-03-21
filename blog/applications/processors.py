from applications.home.models import Home

# processor para recuperar telefono y correo del registro home

def home_contact(request):
    home = Home.objects.latest('created')

    return {
        'phone': home.phone,
        'email': home.contact_email,
    }
