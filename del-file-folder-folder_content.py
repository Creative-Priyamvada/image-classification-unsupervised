import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("--filename", help="enter a filename, foldername to delete",
                    type=str)
parser.add_argument("--content", help="enter a foldername/ to del content of that folder but not folder itself",
                    type=str)
args = parser.parse_args()

'''
--filename accept a filename or folder name and detetes it
--content accepts folder name and deleted only its content

example:
 python del-file-folder-folder_content.py --filename path/to/remove.py
 python del-file-folder-folder_content.py --filename path/to/remove                 # here remove is a folder
 python del-file-folder-folder_content.py --content path/to/remove                 # here remove is a folder

'''


if args.filename:
    path=os.path.join('/Users/priyamvada./Documents/us-image-classification-18nov2021',args.filename)
    print("filename to be deleted", args.filename)
    if os.path.isdir(args.filename)==True:
        print('-----removing folder ------',args.filename)
        #os.rmdir(path)
    elif os.path.isfile(args.filename)==True:
        print('-----removing file------',args.filename)
        #os.remove(args.filename)
    
else:
    print("enter a filename or something")


#folder = '/path/to/folder'
def delete_folder_content(folder):
    print('----deleting content of folder name --',folder)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

if os.path.isdir(args.content)==True:
    delete_folder_content(args.content)
