from django.http import HttpResponse
from django.shortcuts import render
from omeroweb.webclient.decorators import login_required, render_response
from PIL import Image
import numpy as np
import intensityFunctions as iFun
import segmentationFunctions as seg


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


def justapage(request):
    return render(request, 'MTA_MTA/justapage.html')


@login_required()
@render_response()
def test_template_3columns(request, conn=None, **kwargs):
    request.session['user_id'] = conn.getUserId()
    request.session.modified = True
    return {'template': 'MTA_MTA/test_template_3columns.html'}


@login_required()
def mta(request, imageId=3823317, conn=None, **kwargs):
    # image = conn.getObject("Image", imageId)
    return render(request, 'MTA_MTA/mta.html', {'imageId': imageId})


@login_required()
def getImage(request, imageId=3823317, conn=None, **kwargs):
    theZ = request.z
    return render(request, 'MTA_MTA/getImage.html', {'z': theZ,
                                                     'imageId': imageId})


@login_required()
def testAjax(request, imageId=3823317, z=5, conn=None, group=None, **kwargs):
    # theZ = request.z
    # imageId = request.imageId
    if group is None:
        my_exp_id = conn.getUser().getId()
        group_id = conn.getEventContext().groupId

    projects = conn.getObjects("Project", opts={'owner': my_exp_id,
                                                'group': group_id,
                                                'order_by': 'lower(obj.name)',
                                                'limit': 10, 'offset': 0})

    return render(request, 'MTA_MTA/testAjax.html', {'projects': projects})


@login_required()
def loadTree(request, conn=None, **kwargs):
    my_exp_id = conn.getUser().getId()
    default_group_id = conn.getEventContext().groupId
    # tree = '<ul id="dataTree">'
    # projects = conn.getObjects("Project", opts={'owner': my_exp_id,
      #                                          'group': default_group_id,
      #                                          'order_by': 'lower(obj.name)',
      #                                          'limit': 10, 'offset': 0})
    # for project in projects:
        # tree += '<li id="{}">{}<ul>'.format(project.id, project.name)
        # datasets = project.listChildren()
        # numDs = datasets.__sizeof__()
        # dsCounter = 0
        # for dataset in datasets:
            # tree += '<li id="{}">{}<ul>'.format(dataset.id, dataset.name)
            # dsCounter += 1
            # images = dataset.listChildren()
            # numImages = images.__sizeof__()
            # imageCounter = 0
            # for image in images:
                # tree += '<li id="{}">{}</li>'.format(image.id, image.name)
                # imageCounter += 1
                # if imageCounter == numImages:
                    # tree += '</ul></li>'
            # if dsCounter == numDs:
                # tree += '</ul></li>'
    # tree += '</ul>'
    # blah = 'asdfasdf'

    return render(request, 'MTA_MTA/loadTree.html', {'projects': projects})


@login_required()
def intensityAnalysis(request, conn=None, datasetId=None, **kwargs):

    return render(request, 'MTA_MTA/intensityAnalysis.html', {'datasetId': datasetId})


@login_required()
def segmentImage(request, conn=None, iid=None, z=0, c=0, t=0, minSize=1, **kwargs):
    imgObj = conn.getObject("Image", iid)
    # zctList = [25, 0, 0]
    pixels = imgObj.getPrimaryPixels()
    # if (z is None):
    #    numZ = pixels.getSizeZ()
    #    z = np.floor(numZ/2)
    plane = pixels.getPlane(int(z), int(c), int(t))
    planeOtsu = seg.segOtsu(plane, minSize)
    planeOtsu = planeOtsu * 255
    plane8 = planeOtsu.astype(np.uint8)
    img8 = Image.fromarray(plane8)
    response = HttpResponse(content_type='image/jpeg')
    img8.save(response, 'jpeg')

    return response


@login_required()
def measure(request, iid, c, minSize, conn=None, **kwargs):
    data = iFun.measureFromMask(conn, iid, c, minSize)
    return HttpResponse(data, content_type="application/json")
