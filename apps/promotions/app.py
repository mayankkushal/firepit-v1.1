from oscar.apps.promotions.app import PromotionsApplication as BasePromotionsApplication
from django.conf.urls import url
from firepit.views import Index

class PromotionsApplication(BasePromotionsApplication):

	def get_urls(self):
		urls = super(PromotionsApplication, self).get_urls()
		urls[2] = url(r'^$', Index.as_view(), name='home')
		return self.post_process_urls(urls)

application = PromotionsApplication()