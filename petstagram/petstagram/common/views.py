from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse

from petstagram.common.forms import PhotoCommentForm, SearchPhotosForm
from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_user_liked_photos, get_photo_url
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo

import pyperclip


# Create your views here.


def index(request):
    search_form = SearchPhotosForm(request.GET)
    search_pattern = None

    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    search_form.is_valid()
    photos = Photo.objects.all()
    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)

    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }

    return render(request,
                  'common/home-page.html',
                  context,
                  )


# def get_user_liked_photos(photo_id):
#     return PhotoLike.objects.filter(photo_id=photo_id)


def like_photo(request, photo_id):
    # photo_like = PhotoLike(
    #     photo_id=photo_id
    # )
    # photo_like.save()

    user_liked_photos = get_user_liked_photos(photo_id)

    if user_liked_photos:
        user_liked_photos.delete()
    else:

        PhotoLike.objects.create(  # we create a "zapis" of type PhotoLike in the DB to which we refer
            photo_id=photo_id,
        )

    # redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    redirect_path = get_photo_url(request, photo_id)

    return redirect(redirect_path)


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id,
    })
    # photo_details_url = resolve_url('details photo ')
    # pyperclip.copy(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    print(photo)
    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        print(comment)
        comment.photo_id = photo_id
        print(comment.photo)
        comment.save()

    return redirect('index')

