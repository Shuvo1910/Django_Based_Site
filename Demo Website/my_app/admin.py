from django.contrib import admin
from my_app.models import *


admin.site.register([UserInfoModel, ProductModel])

