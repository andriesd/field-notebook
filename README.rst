==============
Field Notebook
==============

Field Notebook is a simple Django app for storing digital field objects and recording notes and metadata about those objects in order to allow for later quick and easy retrieval and automated grouping by attributes of special interest. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add 'notebook' folder file to your new project.

2. In your project's settings.py, type 'notebook' into your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'notebook',
    ]

3. Above INSTALLED_APPS, paste the following lines of code:
	
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
	MEDIA_URL = '/media/'

3. Change the notebook URLconf in your project urls.py too look like this::

	urlpatterns = [
    	url(r'^notebook/', include('notebook.urls')),
    	url(r'^admin/', include(admin.site.urls)),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

4. In your project urls.py, add the following lines of code above the url patterns:
	
	from django.conf import settings
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns

	from django.conf.urls.static import static

5. Run `python manage.py migrate` to create the notebook models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to start entering data into your notebook (you'll need the Admin app enabled).
   See documentation.txt in 'docs' for further details on enabling the Admin 
   as well as instructions on how to launch the development server.

7. Visit http://127.0.0.1:8000/notebook/ to view the entries in your notebook.






