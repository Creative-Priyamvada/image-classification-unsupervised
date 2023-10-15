# image-classification-unsupervised


## new environemt

- `python3 -m pip install --user virtualenv` 
- `python3 -m venv env_name` 
- `source env_name/bin/activate`

## install required packages

- `pip install -r requirements.txt`

# Steps

### 1. extract_frames from videos - 

captures 200 frame from each mp4 file in 'videos' folder at fps=1, and saves i 'frames' folder. After 200 frames, moves on to next video in the folder.

`python extract_frames_from_vid.py`

### 2. cropping and convert to grayscale  - 

takes content of frames folder -> crops -> grayscale -> save in 'cropped_frames' folder

`python crop-grayscale.py`
### 3. rename -

renames all input images in cropped_frames' folder to number (eg. 1.jpg, 2.jpg...) for homogeneity.

`python rename.py` 
### 4. fitting  -  

kmeans clusering , after fitting saves fitted model as 'model_*.pkl' which can be loaded later 

`python cluster-fitting.py`


### To classify based on saved model 
`python classify.py` - loads model, identifies which category it belongs to

### Deleteting files/folders no longer required

- delete contents of folder, not the folder itself `python del-file-folder-folder_content.py --content <foldername>`
- delete folder `python del-file-folder-folder_content.py <foldername>`
- delete file `python del-file-folder-folder_content.py <filename>`


Note: videos folder has one test video. It can be removed when training with own videos.




