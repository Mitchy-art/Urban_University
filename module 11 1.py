import os
import sys
from PIL import Image, ImageOps, ImageFilter
from PIL import ExifTags

im = Image.open("Снимок экрана 2024-09-06 230513.png") 
print(im.format, im.size, im.mode)

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)

size = (100, 150)
with Image.open("Снимок экрана 2024-09-06 230513.png") as im:
    ImageOps.contain(im, size).save("imageops_contain.webp")
    ImageOps.cover(im, size).save("imageops_cover.webp")
    ImageOps.fit(im, size).save("imageops_fit.webp")
    ImageOps.pad(im, size, color="#f00").save("imageops_pad.webp")

    im.thumbnail(size)
    im.save("image_thumbnail.webp")


im_rotate = im.rotate(45, expand=True, resample=Image.BICUBIC)
out = im.filter(ImageFilter.DETAIL)
out = im.point(lambda i: i * 20)

im = Image.open('Снимок экрана 2024-09-06 230513.png')
exif = im.getexif()
gps_ifd = exif.get_ifd(ExifTags.IFD.GPSInfo)
print(gps_ifd)
im.show()