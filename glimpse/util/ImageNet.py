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
import Image
import gimage

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
                    
    '''
    crop each image from imagenet to be 256x256 based on the images shortest side.
    '''            
    def normalizeCorpus(self,dir):
        
        for img in os.listdir(dir):
            print img
            # find the shortest side of the image then scale by that side
            tmp = Image.open(os.path.join(dir,img))
            width,height = tmp.size
            #normalized = gimage.ScaleAndCropImage(tmp, (256,256))
            #normalized.save(os.path.join(dir,img),"JPEG")
            #scale the shortest side to 256 pixels then crop out an even 256 x 256 image
            
            if width <= height:
                # figure out the height percent that we need to scale by to get 256 scaling ratio
                hScale = 256/float(width)
                newHeight = int(float(height)*float(hScale))
                tmp = tmp.resize((256,newHeight),Image.ANTIALIAS)
                w,h = tmp.size
                top = (h-256)/2
                bottom = (h+256)/2
                tmp = tmp.crop((0,top,w,bottom))
                
            elif height <= width:
                
                wScale = float(256)/float(height)
                newWidth = int(float(width)*float(wScale))
                tmp = tmp.resize((newWidth,256),Image.ANTIALIAS)
                w,h = tmp.size
                left = (w-256)/2
                right = (w+256)/2
                tmp = tmp.crop((left,0,right,h))
            #first check if shortest size is greater than 256 pixels
            tmp.save(os.path.join(dir,img),"JPEG")
            