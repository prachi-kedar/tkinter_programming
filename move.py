import shutil
import os
import time
  
t = time.time()
    
source_dir = '/home/webwerks/Desktop/testing/train'
target_dir = '/home/webwerks/Desktop/testing/temp'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(target_dir, file_name))
print("Done int:",time.time()-t )





