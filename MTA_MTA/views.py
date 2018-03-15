from django.http import HttpResponse
from omeroweb.webclient.decorators import login_required
from django.shortcuts import render


def index(request):
    """
    Just a place-holder while we get started
    """
    return HttpResponse("Welcome to your app home-page! adsfasdfasdf")


@login_required()
def stack_preview(request, imageId, conn=None, **kwargs):
    """ Shows a subset of Z-planes for an image """
    image = conn.getObject("Image", imageId)
    image_name = image.getName()
    size_z = image.getSizeZ()
    z_indexes = [0, int(size_z*0.25), int(size_z*0.5), int(size_z*0.75),
                 size_z-1]
    return render(request, 'MTA_MTA/stack_preview.html',
                  {'imageId': imageId, 'image_name': image_name,
                   'z_indexes': z_indexes})


def test_template(request):
    return render(request, 'MTA_MTA/test_template.html')
