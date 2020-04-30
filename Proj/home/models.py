from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
#Home page model

    templates = "home/home_page.html" #displays "Hello World" on the home page
    max_count = 1 #Limits the number of homepages to 1. Meaning a homepage can not have a child page

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    content_panels = Page.content_panels + [
    	FieldPanel("banner_title")
    ]# editable field in the wagtails admin panel

    class Meta:
    	verbose_name = "Home Page" #When you add a child page to home page, it will say "New Home Page" at the top
    	verbose_name_plural = "Home Pages"

