my_exp_id = conn.getUser().getId()
default_group_id = conn.getEventContext().groupId
tree = '<ul id="dataTree">'
for project in conn.getObjects("Project", opts={'owner': my_exp_id,
                                                'group': default_group_id,
                                                'order_by': 'lower(obj.name)',
                                                'limit': 200, 'offset': 0}):
    tree += '<li id="{}">{}</li><ul>'.format(project.id, project.name)

    datasetList = project.listChildren()
    numDs = datasetList.size()
    dsCounter = 0
    for dataset in datasetList:
        tree += '<li id="{}">{}</li><ul>'.format(dataset.id, dataset.name)
        dsCounter += 1
        imagesList = dataset.listChildren()
        numImages = imagesList.size()
        imageCounter = 0
        for image in imagesList:
            tree += '<li id="{}">{}</li>'.format(image.id, image.name)
            imageCounter += 1
            if imageCounter == numImages:
                tree += '</ul>'

            if dsCounter == numDs:
                tree += '</ul>'

return tree