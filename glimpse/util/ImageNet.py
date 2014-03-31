"""
Created on Mar 30, 2014

@author: georgedittmar@gmail.com

The ImageNet module consists of a series of utility classes and methods to help work with the image net 
dataset. Utility classes will consist of the ability to take an image net URL list file and download 
the images from the web to the local host machine and cropping functions to help create training sets that 
will work with glimpse.

"""
import urllib
import os
import os.path

class ImageNet():
    def __init__(self):
        pass
    """
    Downloads a set of urls from the image net database and saves them to the given location on disk.
    """
    def downloadImages(self,saveDir,classTag,urls):
        with open(urls) as urlFile:
            for line in urlFile:
                # grab each url and save to disk
                filename = line.split("/")[-1]
                urlReq = urllib.urlopen(line)
                
                #we must check that the url actually returns us a 200 status code before we can try to download.
                if urlReq.getcode() == 200 and urlReq.info().maintype == "image":
                    urllib.urlretrieve(line, os.path.join(saveDir,filename))
                
        