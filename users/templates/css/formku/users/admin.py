# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import Http404
# Register your models here.
admin.site.register(User)
admin.register(User)

class RestrictStaffToAdminMiddleware(object):
	def process_request(self, request):
		if request.path.startswith(reverse('admin:index')):
			if request.user.is_authenticated():
				if not request.user.is_staff:
					raise Http404
			else:
				raise Http404
