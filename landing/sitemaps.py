# landing/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class LandingSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return [
            'index',
            'faqs',
            'about-us',
            'legal',
            'refer_and_earn',
            'contact-us',
        ]

    def location(self, item):
        return reverse(item)
