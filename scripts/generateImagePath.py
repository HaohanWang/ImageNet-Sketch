__author__ = 'Haohan Wang'

import os
import numpy as np

def run():
    text = [line.strip() for line in open('../data/folder2class.txt')]
    result = []
    for i in range(len(text)):
        line = text[i]
        folderName, className = line.split()
        writeFolder = '/media/haohanwang/Info/ImageNet/sketch/' + folderName + '/'
        for r, d, f in os.walk(writeFolder):
            for fn in f:
                result.append((folderName + '/' + fn, i ))

    np.random.shuffle(result)

    f = open('sketchPath.txt', 'w')
    for (a, b) in result:
        f.writelines(a + ' ' + str(b) + '\n')
    f.close()

if __name__ == '__main__':
    run()