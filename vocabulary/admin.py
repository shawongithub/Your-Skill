from django.contrib import admin

# Register your models here.
from . models import Vocabulary, Comment, MyList

admin.site.register(Vocabulary)
admin.site.register(Comment)
admin.site.register(MyList)