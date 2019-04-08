from stegimage import stegimage
import sys

image_location = None
payload_location = None

if len(sys.argv) > 1:
    image_location = sys.argv[1]
if len(sys.argv) > 2:
    payload_location = sys.argv[2]


print('done')
stegimage_obj = stegimage()

print("priming image with data....")
encoded_image = stegimage_obj.encode_image(image_location, payload_location)
encoded_image.save('encoded_img01.png')
print("priming successful....")
