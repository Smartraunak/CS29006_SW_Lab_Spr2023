from PIL import Image
import requests
from io import BytesIO

class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    def __call__(self, path, url):
        self.url=url
        self.path=path
        r = requests.get(url)
        i = Image.open(BytesIO(r.content))
        i.show()
        i.save(path)
        '''
            Arguments:
            path: download path with the file name
            url: required image URL
        '''
