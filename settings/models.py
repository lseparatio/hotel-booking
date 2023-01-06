from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import FileExtensionValidator
from colorfield.fields import ColorField

class IndexPage(TranslatableModel):
    class Meta:
        verbose_name_plural = 'Index Page'

    translations = TranslatedFields (
        use_settings = models.BooleanField(default=False),
        site_hero = models.ImageField(null=True, blank=True),
        text_title_hero = models.TextField(null=True, blank=True),
        text_small_hero = models.TextField(null=True, blank=True),
        title_2 = models.TextField(null=True, blank=True),
        small_2 = models.TextField(null=True, blank=True),
        book_now = models.TextField(null=True, blank=True),
        first_Of_4_title = models.TextField(null=True, blank=True),
        first_Of_4_subtitle = models.TextField(null=True, blank=True),
        second_Of_4_title = models.TextField(null=True, blank=True),
        second_Of_4_subtitle = models.TextField(null=True, blank=True),
        third_Of_4_title = models.TextField(null=True, blank=True),
        third_Of_4_subtitle = models.TextField(null=True, blank=True),
        fourth_Of_4_title = models.TextField(null=True, blank=True),
        fourth_Of_4_subtitle = models.TextField(null=True, blank=True),
        video = models.FileField(blank=True,null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])]),
        presentation_title = models.TextField(null=True, blank=True),
        image_small1  = models.ImageField(null=True, blank=True),
        image_small2  = models.ImageField(null=True, blank=True),
        image_small3  = models.ImageField(null=True, blank=True),
        image_small4  = models.ImageField(null=True, blank=True),
        image_small5  = models.ImageField(null=True, blank=True),
        image_big  = models.ImageField(null=True, blank=True),
        presentation_description = models.TextField(null=True, blank=True),
        tick_1 = models.TextField(null=True, blank=True),
        tick_2 = models.TextField(null=True, blank=True),
        tick_3 = models.TextField(null=True, blank=True),
    )

    def __unicode__(self):
        return self.text_title_hero


class TopNav(TranslatableModel):
    class Meta:
        verbose_name_plural = 'Top Nav'
    
    translations = TranslatedFields (
        use_settings = models.BooleanField(default=False),
        site_logo = models.ImageField(null=True, blank=True),
        nav_color = ColorField(format="hexa"),
        home = models.TextField(null=True, blank=True),
        rooms_and_suites = models.TextField(null=True, blank=True),
        facilities = models.TextField(null=True, blank=True),
        contact_us = models.TextField(null=True, blank=True),
        book_now = models.TextField(null=True, blank=True),

    )

    def __unicode__(self):
        return self.home