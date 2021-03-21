from django.db import models

class EntryManager(models.Manager):

    def entry_cover(self):
        return self.filter(
            public=True,
            cover=True,
        ).order_by('-created').first()

    def home_entries(self):
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]

    def recent_entries(self):
        return self.filter(
            public=True
        ).order_by('-created')[:6]

    def search_entry(self, kword, category):
         if len(category) > 0 :
            return self.filter(
                category__short_name=category,
                title__icontains=kword,
                public=True
            ).order_by('-created')[:6]
        