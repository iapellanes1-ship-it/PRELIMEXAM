import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User

admin = User.objects.get(username='admin')
admin.set_password('admin123')
admin.save()
print("Password for admin user set to 'admin123'")
