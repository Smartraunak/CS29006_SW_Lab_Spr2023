#Imports
from my_package.model import ImageCaptioningModel
from my_package.data.dataset import Dataset
from my_package.data.download import Download
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.rescale import RescaleImage
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.crop import CropImage
from my_package.data.transforms.rotate import RotateImage
import numpy as np
from PIL import Image
def experiment(annotation_file, captioner, transforms, outputs):
     d= Dataset(annotation_file,transforms)
     down=Download()
     list=d.__getann__(['file_name','captions','url'])
     for i in range(int(len(list)/3)):
        path1="data/imgs/"+str(i)+".jpg"
        print( " Name :-")
        print(list[i])
        print("Captions :- ")
        print(list[i+10][1])
        down(path1,list[i+20])
     path="data/imgs/9.jpg"
     output_size=(0.8,0.5)
     flip=FlipImage()
     flip(path)
     i=ImageCaptioningModel()
     capt=i(path,3)
     for i in range(len(capt)):
        print("caption"+str(i+1)+":-")
        print(capt[i])
     #rescale=RescaleImage(output_size)
     #rescale(path)
     #ImageCaptioningModel()
     blur=BlurImage(2)
     blur(path)
     path2="my_package/data/images/gaussian_blur.jpg"
     i=ImageCaptioningModel()
     capt=i(path2,3)
     for i in range(len(capt)):
        print("caption"+str(i+1)+":-")
        print(capt[i])

     #ImageCaptioningModel()
     #crop=CropImage((100,150))
     #crop(path)
     #ImageCaptioningModel()
     #img(path,3)
     rotate=RotateImage(45)
     rotate(path)
     i=ImageCaptioningModel()
     path3="my_package/data/images/rotated.jpg"
     capt=i(path3,3)
     for i in range(len(capt)):
        print("caption"+str(i+1)+":-")
        print(capt[i])

     #img=ImageCaptioningModel()
     #img(path,3)

    



    #Create the instances of the dataset, download


    #Print image names and their captions from annotation file using dataset object


    #Download images to ./data/imgs/ folder using download object


    #Transform the required image (roll number mod 10) and save it seperately


    #Get the predictions from the captioner for the above saved transformed image  
def main():
    captioner = ImageCaptioningModel()
    experiment('data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], None) # Sample arguments to call experiment()


if __name__ == '__main__':
    main()