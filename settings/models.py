from django.db import models
from parler.models import TranslatableModel, TranslatedFields

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
    )

    def __unicode__(self):
        return self.text_title_hero


class TopNav(TranslatableModel):
    class Meta:
        verbose_name_plural = 'Top Nav'
    
    translations = TranslatedFields (
        use_settings = models.BooleanField(default=False),
        site_logo = models.ImageField(null=True, blank=True),
        home = models.TextField(null=True, blank=True),
        rooms_and_suites = models.TextField(null=True, blank=True),
        facilities = models.TextField(null=True, blank=True),
        contact_us = models.TextField(null=True, blank=True),
        book_now = models.TextField(null=True, blank=True),
    )

    def __unicode__(self):
        return self.home