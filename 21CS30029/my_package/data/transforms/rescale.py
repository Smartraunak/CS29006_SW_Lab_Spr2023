#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        self.output_size=output_size
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''


    def __call__(self, image):
        self.image=image
        img=Image.open(image)
        img.show()
        re_img=img.resize((round(img.size[0]*self.output_size[0])),(round(img.size[1]*self.output_size[1])))
        re_img.show()
        re_img.save('my_package/data/images/rescale.jpg')

        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''