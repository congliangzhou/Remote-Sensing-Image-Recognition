import os
from PIL import Image

def decomposetiffimage(src, rownum, colnum, dstpath):
    tiffimage = Image.open(src)
    w, h = tiffimage.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, tiffimage.format, tiffimage.mode))
        

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        TIFF = fn[-1]        

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                tiffimage.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + str(TIFF)), TIFF)
                num = num + 1

        print('total Number: %s' % num)
    

src = input('Please input file path：')
dstpath = input('Please input the output file name: ')
if (dstpath == '') or os.path.exists(dstpath):
    row = int(input('Row Number：'))
    col = int(input('Col Number：'))
    if row > 0 and col > 0:
        decomposetiffimage(src, row, col, dstpath)
      

