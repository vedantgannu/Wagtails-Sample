from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
#from wagtail.admin.edit_handlers import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
#Home page model

    template = "home/home_page.html" #displays "Hello World" on the home page
    max_count = 1 #Limits the number of homepages to 1. Meaning a homepage can not have a child page

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    #need to do python manage.py makemigrations to add a banner_subtitle to the database

    banner_image = models.ForeignKey(
    	"wagtailimages.Image",
    	null =True,
    	blank=False,
    	on_delete=models.SET_NULL,
    	related_name="+"
    )

    #cta is a call to action = link to another page. Can be to a URL or another Wagtails Page
    banner_cta = models.ForeignKey(
    	"wagtailcore.Page",
    	null =True,
    	blank=True,
    	on_delete=models.SET_NULL,
    	related_name="+"
    )

    content_panels = Page.content_panels + [
    	FieldPanel("banner_title"),
    	FieldPanel("banner_subtitle"),
    	ImageChooserPanel("banner_image"),
    	PageChooserPanel("banner_cta")


    ]# FieldPanel is editable field in the wagtails admin panel
   		#We are making editable banner subtitle field and another field for image selection
   		#We also need to import ImageChooserPanel and PageChooserPanel

    class Meta:
    	verbose_name = "Home Page" #When you add a child page to home page, it will say "New Home Page" at the top
    	verbose_name_plural = "Home Pages"

