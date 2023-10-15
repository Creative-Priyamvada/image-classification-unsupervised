# Program To Read video
# and Extract Frames
import cv2
import os 
import settings



# Function to extract frames
def FrameCapture(path):
      
    # Path to video file
    vidObj = cv2.VideoCapture(path)
  
    # Used as counter variable
    count = 0
  
    # checks whether frames were extracted
    success = 1
    '''
    while success:
        vidObj.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
        #print('image :',image,type(image),image.shape)
  
        # Saves the frames with frame-count
        op_path=os.path.join('frames',"frame%d.jpg" % count)
        cv2.imwrite(op_path, image)
        print('----------')
        count += 1

    '''
    while success:
        #-----------changes here adding if  statement ------
        
        vidObj.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
        # function extract frames
        success, image = vidObj.read()    
        # Saves the frames with frame-count
        image_name=os.path.basename(path)+"-frame%d.jpg"
        op_path=os.path.join('frames',image_name % count)
        try:
            cv2.imwrite(op_path, image)
            print('writing frame :',op_path)
            count += 1
        except Exception as e:
            #print('Exception occurs : probably end of file, skipping frame') #to see problem we can print e here
            pass

  

# Driver Code
if __name__ == '__main__':
  

    for item in os.listdir("videos"):
        if item.endswith(".mp4"):
            path=os.path.join(settings.WORKING_DIRECTORY,"videos",item)
            print('path :',path)
            # Calling the function
            #FrameCapture("videos/bkg-imc-bei_final_q_226442.mp4")
            FrameCapture(path)
