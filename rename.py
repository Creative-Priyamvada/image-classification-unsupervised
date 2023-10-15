import os
import settings


#rename 
count=0
working_directory=settings.WORKING_DIRECTORY#'/Users/priyamvada./Documents/us-image-classification-18nov2021/image-classification-unsupervised'


input_images_folder=os.path.join(working_directory,'cropped_frames')
for item in os.listdir(input_images_folder):
    count=count+1
    c=str(count)+'.jpg'
    try:
        os.rename(os.path.join(input_images_folder,item), os.path.join(input_images_folder,c))
    except Exception as e:
        print('count :',c,e)
