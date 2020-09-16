from datetime import datetime
from django.db.models import Q
from analysis.models import SiteNote
from django.contrib.auth.models import User

def get_enable_site_note():
    return SiteNote.objects.filter(enable='1').order_by('idx')
    #return SiteNote.objects.filter(enable='1').order_by('idx')#.order_by('-idx', 'name')

def select_users(type):
    if type == 0:
        return User.objects.filter(is_superuser=0)#
    elif type == 1:#admin
        return User.objects.filter(is_superuser=1)
    else:
        return User.objects.all()