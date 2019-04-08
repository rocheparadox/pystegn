from stegimage import stegimage
import sys

encoded_image_location = None
decoded_payload_location = None

if len(sys.argv) > 1:
    encoded_image_location = sys.argv[1]
if len(sys.argv) > 2:
    decoded_payload_location = sys.argv[2]

stegimage_obj = stegimage()
print("Decoding image for data...")
decoded_payload_string = stegimage_obj.decode_image(encoded_image_location, decoded_payload_location)
print('Decoding successful...')
#print(stegimage_obj.decoded_payload_location)
with open(stegimage_obj.decoded_payload_location,'w+') as output_file:
    output_file.write(decoded_payload_string)

print('output file at ' + stegimage_obj.decoded_payload_location)