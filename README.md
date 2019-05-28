# ImageNet-Sketch

![ImageNet-Sketch](imagenet_sketch.jpg "ImageNet Sketch")

## Description

ImageNet-Sketch data set consists of 50000 images, 50 images for each of the 1000 ImageNet classes. 
We construct the data set with Google Image queries "sketch of \_\_", where \_\_ is the standard class name. 
We only search within the "black and white" color scheme.
We initially query 100 images for every class, and then manually clean the pulled images by deleting the irrelevant images and images that are for similar but different classes. 
For some classes, there are less than 50 images after manually cleaning, 
and then we augment the data set by flipping and rotating the images. 

This github repo consists of the scripts we used to conduct query and clean images. 

## [Download the Data](https://drive.google.com/open?id=1Mj0i5HBthqH1p_yeXzsg22gZduvgoNeA) 
 - zip file is 7.8 GB
 - extracted files will be 8.4 GB

## Reference

The data set is introduced together with the following paper, so if you find this data set helpful, please consider cite: 
    
    Haohan Wang, Songwei Ge, Eric P. Xing, and Zachary C. Lipton. "Learning Robust Global Representations by Penalizing Local Predictive Power"
