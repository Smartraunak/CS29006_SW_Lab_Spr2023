#Imports
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        self.flip_type=flip_type
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

    def __call__(self, image):
        self.image=image
        img=Image.open(self.image)
        img.show()
        if self.flip_type == 'horizontal':
            imgflip=img.transpose(Image.FLIP_LEFT_RIGHT)
        if self.flip_type == 'vertical':
            imgflip=img.transpose(Image.FLIP_TOP_BOTTOM)
        imgflip.show()
        imgflip.save("my_package/data/images/flipped.jpg")
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
