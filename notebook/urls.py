from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'[guide]/objects/$', views.object_guide, name='object_guide'),
    url(r'[guide]/creators/$', views.creator_guide, name='creator_guide'),
    url(r'[guide]/places/$', views.place_guide, name='place_guide'),
    url(r'[guide]/objects/object_detail/(?P<slug>[a-z_]+)/$', views.object_detail, name='object_detail'),
    url(r'[guide]/creators/(?P<object_creator__creator_name>[A-Z\sa-z_]+)/$', views.object_guide_by_creator, name='object_guide_by_creator'),
    url(r'[guide]/places/(?P<place_created__place_name>[A-Z\sa-z_]*)/$', views.object_guide_by_place, name='object_guide_by_place')
]
