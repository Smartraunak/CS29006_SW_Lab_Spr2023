#Imports
from PIL import Image, ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius=radius
        
  

    def __call__(self, image):
        self.image=image
        OriImage=Image.open(self.image)
        OriImage.show()

        gaussImage=OriImage.filter(ImageFilter.GaussianBlur(self.radius))
        gaussImage.show()
        gaussImage.save('my_package/data/images/gaussian_blur.jpg')
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

