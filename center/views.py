from django.template import loader

from django.http import HttpResponse

from center.models import Center


def all_groups(request):
    centers = Center.objects.all()
    template = loader.get_template('all_groups.html')
    context = {
        'centers': centers
    }

    return HttpResponse(template.render(context, request))


def about(request):
    return HttpResponse('<h2>About Site</h2>')


def contact(request):
    context = {}
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render(context, request))
