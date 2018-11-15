from PIL import Image
import imagehash
import time

if __name__ == '__main__':

    hash1 = imagehash.average_hash(Image.open('E:\\test\peppers2_512.png'))
    hash2 = imagehash.average_hash(Image.open('E:\\test\incline.png'))

    out_score = hash1 - hash2
    print("本次程序运行的时间为%.10f秒" % time.clock())
    if 0 <= out_score < 5:
        print("汉明距离为%d,哇呜这两幅图片很像" % (out_score))
    elif 5 <= out_score < 10:
        print("汉明距离为%d,这两幅图片很像,但又有一些差别" % (out_score))
    else:
        print("汉明距离为%d,这两幅图片好像差距挺大的" % (out_score))
