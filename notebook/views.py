from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Object, Creator, Place

def index(request):
    return render(request, 'notebook/index.html')

def object_guide(request):
    object_list = Object.objects.all()
    template = loader.get_template('notebook/object_guide.html')
    context = RequestContext(request, {
        'object_list': object_list,
    })
    return HttpResponse(template.render(context))

def creator_guide(request):
    creator_list = Creator.objects.all()
    template = loader.get_template('notebook/creator_guide.html')
    context = RequestContext(request, {
        'creator_list': creator_list,
    })
    return HttpResponse(template.render(context))

def object_guide_by_creator(request, object_creator__creator_name):
    creator = Creator.objects.get(creator_name=object_creator__creator_name)
    objects = Object.objects.filter(object_creator__creator_name=object_creator__creator_name)
    template = loader.get_template('notebook/object_guide_by_creator.html')
    #context = {'monuments': monuments}
    context = RequestContext(request, {
        'creator': creator,
        'objects': objects,
    })
    return HttpResponse(template.render(context)) 

def place_guide(request):
    place_list = Place.objects.all()
    template = loader.get_template('notebook/place_guide.html')
    context = RequestContext(request, {
        'place_list': place_list,
    })
    return HttpResponse(template.render(context))

def object_guide_by_place(request, place_created__place_name):
    place = Place.objects.get(place_name=place_created__place_name)
    objects = Object.objects.filter(place_created__place_name=place_created__place_name)
    template = loader.get_template('notebook/object_guide_by_place.html')
    #context = {'monuments': monuments}
    context = RequestContext(request, {
        'place': place,
        'objects': objects,
    })
    return HttpResponse(template.render(context)) 

def object_detail(request, slug):
    object_data = Object.objects.get(slug=slug)
    context = {'object_data': object_data}
    return render(request, 'notebook/object_detail.html', context)