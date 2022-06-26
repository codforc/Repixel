import sys, random, argparse
from PIL import Image

parser = argparse.ArgumentParser(usage='main.py [-h] -p IMAGE_PATH -r *R /G +B (* / + -)')
parser.add_argument('--path', '-p', required=True, help=argparse.SUPPRESS)
parser.add_argument('--rgb', '-r', nargs=(3), type=str, required=True, help=argparse.SUPPRESS)
args = parser.parse_args()

img_path = args.path
t_rgb = {'r': args.rgb[0], 'g': args.rgb[1], 'b': args.rgb[2]}

img = Image.open(img_path)
pix = img.load()

#width
for x in range(img.size[0]):
    #height
    for y in range(img.size[1]):
        rgb = pix[x,y]

        #need optimization. please fork and feedback :D
        c = 0
        __t_rgb = []
        for v in t_rgb.values():
            if '-' in v:
                __t_rgb.append(rgb[c] - int(v.replace('-','')))
            elif '+' in v:
                __t_rgb.append(rgb[c] + int(v.replace('+','')))
            elif '*' in v:
                __t_rgb.append(rgb[c] * int(v.replace('*','')))
            elif '/' in v:
                __t_rgb.append(int(rgb[c] / int(v.replace('/',''))))
            c+=1    

        pix[x,y] = tuple(__t_rgb)

# you can change compress level, saving, anything.
new_path = str(random.randint(0, 1000000)) + '__' + img.filename
img.save(new_path, format=img.format, compress_level=9)
img.show()
img.close()

print('finish. image saved in current directory.')

#favorite 
    # -50 -25 -100 -
    # +50 +25 +120 +
    #*2 -50 -120