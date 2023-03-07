#Imports
import PIL
from PIL import Image

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        self.degrees=degrees
        '''
            Arguments:
            degrees: rotation degree.
        '''

    def __call__(self, sample):
        self.sample=sample
        img=Image.open(self.sample)
        img.show()
        im1 = img.rotate(self.degrees, PIL.Image.NEAREST, expand = 1)
        im1.show()
        im1.save('my_package/data/images/rotated.jpg')
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
