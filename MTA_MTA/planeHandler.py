from omeroweb.webclient.decorators import login_required
import numpy as np


@login_required()
def getStack(iid, conn=None, c=0, t=0):
    imgObj = conn.getObject("Image", iid)
    sizeX = imgObj.getSizeX()
    sizeY = imgObj.getSizeY()
    numZ = imgObj.getSizeZ()

    stack = np.zeros((sizeX, sizeY, numZ))

    for thisZ in range(0, numZ - 1):
        stack[:, :, thisZ] = imgObj.getPrimaryPixels().getPlane(thisZ, int(c), int(t))

    return stack
