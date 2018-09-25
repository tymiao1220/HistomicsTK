from girder.api import access
from girder.api.v1.item import Item as ItemResource
from girder.api.describe import autoDescribeRoute, Description


class ImageBrowseResource(ItemResource):
    """Extends the "item" resource to iterate through images im a folder."""

    def __init__(self, apiRoot):
        # Don't call the parent (Item) constructor, to avoid redefining routes,
        # but do call the grandparent (Resource) constructor
        super(ItemResource, self).__init__()

        self.resourceName = 'item'
        apiRoot.item.route('GET', (':itemId', 'next_image'), self.getNextImage)
        apiRoot.item.route('GET', (':itemId', 'previous_image'), self.getPreviousImage)

    @access.public
    @autoDescribeRoute(
        Description('Get the next image in the same folder as the given item.')
        .param('id', 'The current item ID', paramType='path')
        .errorResponse()
        .errorResponse('This is the last image', code=404)
        .errorResponse('Image ID not found', code=404)
    )
    def getNextImage(self):
        pass

    @access.public
    @autoDescribeRoute(
        Description('Get the previous image in the same folder as the given item.')
        .param('id', 'The current item ID', paramType='path')
        .errorResponse()
        .errorResponse('This is the first image', code=404)
        .errorResponse('Image ID not found', code=404)
    )
    def getPreviousImage(self):
        pass
