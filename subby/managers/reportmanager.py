from django.db import models




class ReportManager(models.Manager):
	use_in_migrations = True
	
	def create_report(self, issue, description, user, sublet):
		report = self.model()
		
		report.set_issue(issue)
		report.set_description(description)
		report.set_user(user)
		report.set_sublet(sublet)
		report.save()
		
		return report