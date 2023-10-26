Sure, here's an example of how to create a Django application with a file upload feature using core HTML forms instead of Django's built-in form system. This code provides both the front-end HTML and the back-end Django views:

**1. Create a new Django project and app**:

```bash
django-admin startproject file_upload_project
cd file_upload_project
python manage.py startapp file_upload
```

**2. Define the Model** (models.py):

```python
# file_upload/models.py
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
```

**3. Create a View to Display the Upload Form** (views.py):

```python
# file_upload/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        uploaded_file_instance = UploadedFile(file=uploaded_file)
        uploaded_file_instance.save()
        return HttpResponseRedirect('/file_list/')
    return render(request, 'file_upload/upload.html')
```

**4. Create a View to List Uploaded Files** (views.py):

```python
# file_upload/views.py
from django.shortcuts import render
from .models import UploadedFile

def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'file_upload/file_list.html', {'files': files})
```

**5. Create Templates**:

- Create the templates for rendering the upload form and displaying the list of uploaded files.

- `file_upload/templates/file_upload/upload.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Upload File</title>
</head>
<body>
    <h2>Upload File</h2>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <label for="file">Select a file:</label>
        <input type="file" name="file" id="file" required>
        <br>
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```

- `file_upload/templates/file_upload/file_list.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Uploaded Files</title>
</head>
<body>
    <h2>Uploaded Files</h2>
    <ul>
        {% for file in files %}
            <li><a href="{{ file.file.url }}" target="_blank">{{ file.file.name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

**6. Create URL Patterns** (urls.py):

Define URL patterns in your app's `urls.py` and project's `urls.py`:

- `file_upload/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('file_list/', views.file_list, name='file_list'),
]
```

- `file_upload_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file_upload/', include('file_upload.urls')),
]
```

**7. Configure Media Settings** (settings.py):

In your project's `settings.py`, make sure you have the following settings to handle media files for file uploads:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

**8. Run Migrations**:

Run migrations to create the database table for the `UploadedFile` model:

```bash
python manage.py makemigrations
python manage.py migrate
```

**9. Create the Media Directory**:

Create the `media` directory in your project's root directory to store uploaded files:

```bash
mkdir media
```

**10. Run the Development Server**:

Start the development server:

```bash
python manage.py runserver
```

Now, you can access the `/file_upload/upload/` URL to upload files and view the list of uploaded files at `/file_upload/file_list/`. This code provides a basic example of how to create a Django file upload application with core HTML forms.
