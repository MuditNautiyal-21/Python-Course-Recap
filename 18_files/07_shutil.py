'''
shutil module:

shutil module is very similar to os module but the only difference is that shutil module is a bit powerful!
'''

import shutil

# shutil.rmtree("dir") # didn't run this since it was required to showcase, but this will erase the entire directory tree. One has to be very careful!

shutil.copy("file.txt", "john.txt") # This copied the content of the file file.txt and pasted in john.txt. It will create the file in which it has to paste (if not already present)

# Move a file:

shutil.move("john.txt", "dir")