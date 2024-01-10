Sure, here's an example with all the code snippets integrated, including the `apps.py` code:

1. **models.py:**
   ```python
   # yourapp/models.py
   from django.db import models
   from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
   from django.dispatch import receiver

   class YourModel(models.Model):
       name = models.CharField(max_length=255)

   @receiver(pre_save, sender=YourModel)
   def your_model_pre_save(sender, instance, **kwargs):
       print(f"Before saving {instance}")

   @receiver(post_save, sender=YourModel)
   def your_model_post_save(sender, instance, created, **kwargs):
       print(f"After saving {instance}, Created: {created}")

   @receiver(pre_delete, sender=YourModel)
   def your_model_pre_delete(sender, instance, **kwargs):
       print(f"Before deleting {instance}")

   @receiver(post_delete, sender=YourModel)
   def your_model_post_delete(sender, instance, **kwargs):
       print(f"After deleting {instance}")
   ```

2. **apps.py:**
   ```python
   # yourapp/apps.py
   from django.apps import AppConfig

   class YourAppConfig(AppConfig):
       default_auto_field = 'django.db.models.BigAutoField'
       name = 'yourapp'

       def ready(self):
           import yourapp.signals
   ```

3. **__init__.py:**
   Create an empty `__init__.py` file in your app directory to make it a Python package.

With this structure, Django will automatically discover and use the `ready` method in your `YourAppConfig` class when the app is loaded. This will connect the signals for your `YourModel` model.

Make sure to replace "yourapp" with the actual name of your app.

Remember to run `makemigrations` and `migrate` after making changes to your models or signals to apply the changes to the database.
