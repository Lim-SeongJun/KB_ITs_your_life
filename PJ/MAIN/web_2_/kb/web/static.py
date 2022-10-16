import os
from kb import settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, 'web', 'static')
]

STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static')