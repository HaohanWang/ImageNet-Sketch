__author__ = 'Haohan Wang'

import cv2

import os

import numpy as np


def readSaveImage(readFolder, writeFolder):
    imgs = []
    cn = 0
    for r, d, f in os.walk(readFolder):
        for fn in f:
            if cn > 50:
                break
            try:
                img = cv2.imread(readFolder + fn, cv2.IMREAD_UNCHANGED)
                if np.mean(img)>0:
                    cv2.imwrite(writeFolder + 'sketch_' + str(cn) + '.JPEG', img)
                    cn += 1
                    imgs.append(img)
            except:
                pass

    while cn < 50:
        if cn < 50:
            for i in range(len(imgs)):
                try:
                    img2 = cv2.flip(imgs[i], 1)
                    cv2.imwrite(writeFolder + 'sketch_' + str(cn) + '.JPEG', img2)
                    cn += 1
                except:
                    pass
                if cn > 50:
                    break
        if cn < 50:
            for i in range(len(imgs)):
                try:
                    img2 = cv2.flip(imgs[i], 0)
                    cv2.imwrite(writeFolder + 'sketch_' + str(cn) + '.JPEG', img2)
                    cn += 1
                except:
                    pass
                if cn > 50:
                    break
        if cn < 50:
            for i in range(len(imgs)):
                try:
                    img2 = cv2.flip(imgs[i], -1)
                    cv2.imwrite(writeFolder + 'sketch_' + str(cn) + '.JPEG', img2)
                    cn += 1
                except:
                    pass
                if cn > 50:
                    break
        if cn < 50:
            for i in range(len(imgs)):
                try:
                    img2 = imgs[i]
                    cv2.imwrite(writeFolder + 'sketch_' + str(cn) + '.JPEG', img2)
                    cn += 1
                except:
                    pass
                if cn > 50:
                    break



def run():
    text = [line.strip() for line in open('../data/folder2class.txt')]
    c = 0
    for line in text:
        c += 1
        print '---------------'
        print 'We are working on class', c
        folderName, className = line.split()
        writeFolder = '/media/haohanwang/Info/ImageNet/sketch/' + folderName + '/'
        keyWords = 'sketch of ' + ' '.join(className.split('_'))
        readFolder = 'downloads/' + keyWords + '/'
        readSaveImage(readFolder, writeFolder)

if __name__ == '__main__':
    run()

