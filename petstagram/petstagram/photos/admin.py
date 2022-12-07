from django.contrib import admin

from petstagram.photos.models import Photo


# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'photo', 'description', 'pets')

    def pets(self, current_photo_obj):
        tagged_pets = [p.name for p in current_photo_obj.tagged_pets.all()]

        if tagged_pets:
            return ', '.join(tagged_pets)
        else:
            return 'No pets!'

