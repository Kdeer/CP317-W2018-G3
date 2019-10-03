from django.db import models
from django.conf import settings
from subby.models.sublet import Sublet
from subby.managers.reportmanager import ReportManager

import datetime, pytz



class Report(models.Model):
	FALSE_INFO = 0
	SPAM_POST = 1
	SPAM_EMAIL = 2
	OTHERS = 3
	ISSUES = ((FALSE_INFO, 'Information not matched'),
		(SPAM_POST, 'Spam Postings'),
		(SPAM_EMAIL, 'User send spam emails'),
		(OTHERS, 'Other issues'),
		)
	issue = models.IntegerField(choices=ISSUES, default=FALSE_INFO)
	description = models.TextField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	sublet = models.ForeignKey(Sublet, related_name='report', on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	objects = ReportManager()

	def get_report_id(self):
		return self.id

	def get_created_at(self):
		return self.created_at

	def get_updated_at(self):
		return self.updated_at

	def get_issue(self):
		return self.issue

	def get_user_id(self):
		return self.user.id

	def get_description(self):
		return self.description

	def set_report_id(self, new_report_id):
		self.id = new_report_id
		return

	def set_created_at(self, new_created_at):
		self.created_at = new_created_at
		return

	def set_updated_at(self, new_updated_at):
		self.updated_at = new_updated_at
		return

	def set_issue(self, new_issue):
		self.issue = new_issue
		return

	def set_description(self, new_description):
		self.description = new_description
		return

	def set_user(self, new_user):
		self.user = new_user
		return

	def set_sublet(self, new_sublet):
		self.sublet = new_sublet
		return

