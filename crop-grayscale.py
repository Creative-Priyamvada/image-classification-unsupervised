# cropping.py



# Importing Image class from PIL module
from PIL import Image
import os
import settings

 
def crop(image,count,output_folder,left, top, right, bottom):
    
    # Opens a image in RGB mode
    #im = Image.open(r"/Users/priyamvada./Documents/us-image-classification-18nov2021/frames/frame3.jpg")
    im=Image.open(image,'r').convert('L')
    
    # Size of the image in pixels (size of original image)
    width, height = im.size
    print('width :',width,'height :',height,type(im))

    # Setting the points for cropped image
    #left = 0  
    #top = 170
    #right = 1150 #width
    #bottom =700 #height

    im1 = im.crop((left, top, right, bottom))
    print('left, top, right, bottom : ',left, top, right, bottom)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Saves the frames with frame-count
    output_folder=os.path.join(working_directory,output_folder_name)
    op_path=os.path.join(output_folder,"frame%d.jpg" % count)

    im1.save(op_path)

    
    
#------------define dimensions for cropping---------    

# Setting the points for cropped image
#left = 0  
#top = 170
#right = 1150 #width
#bottom =700 #height
#---------------------------------------------------
    
working_directory=settings.WORKING_DIRECTORY#'/Users/priyamvada./Documents/us-image-classification-18nov2021/image-classification-unsupervised'
input_images_folder='frames'
output_folder_name='cropped_frames'
count=0



for item in os.listdir(os.path.join(working_directory,input_images_folder)):  
    if item.endswith('.jpg'):  
        crop(os.path.join(working_directory,input_images_folder,item),count,output_folder_name,left=int(settings.LEFT), top=int(settings.TOP), right=int(settings.RIGHT), bottom=int(settings.BOTTOM))
        print('---------------------------------------------')
    count=count+1
