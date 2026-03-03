import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'admin123'

user_qs = User.objects.filter(username=username)
if not user_qs.exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Created superuser '{username}' with password '{password}'")
else:
    user = user_qs.first()
    if not user.is_superuser or not user.is_staff:
        user.is_superuser = True
        user.is_staff = True
    user.set_password(password)
    user.save()
    print(f"Updated superuser '{username}' and set password to '{password}'")
