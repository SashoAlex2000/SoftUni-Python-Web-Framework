from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.common.utils import get_user_liked_photos
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


# Create your views here.

# cannot be used for now,
# def get_post_photo_form(request, form, success_url, template_path):
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request,
#                   template_path,
#                   context
#                   )
#

@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():

            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()

            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
    }

    return render(request,
                  'photos/photo-add-page.html',
                  context
                  )


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    user_liked_photos = PhotoLike.objects.filter(
        photo_id=pk,
        user_id=request.user.pk)

    current_likes_count = photo.photolike_set.count()
    print(photo.tagged_pets.all())

    context = {

        'photo': photo,
        'has_user_liked': user_liked_photos,
        'current_likes_count': current_likes_count,
        'is_owner': request.user == photo.user,

    }

    return render(request,
                  'photos/photo-details-page.html',
                  context
                  )


def edit_photo(request, pk):

    current_photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PhotoEditForm(instance=current_photo)
    else:
        form = PhotoEditForm(request.POST, instance=current_photo)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'current_photo': current_photo,
    }

    return render(request,
                  'photos/photo-edit-page.html',
                  context
                  )


def delete_photo(request, pk):

    current_photo = Photo.objects.filter(pk=pk).get()
    current_photo.tagged_pets.clear()
    PhotoLike.objects.filter(photo_id=current_photo.pk).delete()
    PhotoComment.objects.filter(photo_id=current_photo.pk).delete()
    current_photo.delete()

    return redirect('index')
