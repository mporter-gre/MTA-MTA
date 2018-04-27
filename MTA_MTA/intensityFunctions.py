from skimage.measure import label, regionprops
import segmentationFunctions as seg
import numpy as np
import json


def measureFromMask(conn, iid, c, minSize):
    stack = getStack(iid, conn, c)
    stackSeg = seg.segOtsu(stack, minSize)
    stackSegLbl = label(stackSeg)
    data = []
    for region in regionprops(stackSegLbl, stack):
        item = {"area": region.area, "meanInt": region.mean_intensity}
        data.append(item)
    data_json = json.dumps(data)
    return data_json


def getStack(iid, conn, c=0, t=0):
    imgObj = conn.getObject("Image", iid)
    sizeX = imgObj.getSizeX()
    sizeY = imgObj.getSizeY()
    numZ = imgObj.getSizeZ()
    stack = np.zeros((sizeX, sizeY, numZ))
    for thisZ in range(0, numZ - 1):
        stack[:, :, thisZ] = imgObj.getPrimaryPixels().getPlane(thisZ, int(c), int(t))
    return stack
