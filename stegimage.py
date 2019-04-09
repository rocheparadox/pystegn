from PIL import Image
import stegutil

class stegimage:

    def __init__(self):
        self.__image_location = 'image.png'
        self.__payload_location = 'payload.txt'
        self.__encoded_image_location = 'encoded_img01.png'
        self.decoded_payload_location = 'decoded_payload'

        self.STOPBUFFER = 'FFFFFFFFEEEEEEEFFFFFFEEEEEEEE'

    def is_image_enough_for_payload(self):
        is_image_enough = False
        if self.__image_size > self.__payload_size:
            is_image_enough = True

        return is_image_enough


    def encode_image(self, image_location=None, payload_location=None):

        if image_location != None:
            self.__image_location = image_location
        if payload_location != None:
            self.__payload_location = payload_location

        image = Image.open(self.__image_location)
        string = open(self.__payload_location, 'r').read()

        payload = string + self.STOPBUFFER
        #print(payload)
        payload_binary_values = stegutil.convert_string_to_binary(payload)
        #print(payload_binary_values)
        payload_binary_values = ''.join(payload_binary_values)
        #print(payload_binary_values)

        self.__image_size = stegutil.get_size_of_image(image)
        self.__payload_size = stegutil.get_size_of_payload(payload)
        #print(self.__image_size, self.__payload_size)

        if not self.is_image_enough_for_payload():
            print('Image ain\'t large enough for the data')
            exit()
        pixels = list(image.getdata())
        for x in range(self.__payload_size):
            pixels[x] = stegutil.manipulate_pixel(pixels[x], payload_binary_values[x])

        image.close()
        steg_image = Image.new(image.mode, image.size)
        steg_image.putdata(pixels)
        #steg_image.save('encoded_img01.jpg')
        return steg_image

    def decode_image(self,encoded_image_location=None, decoded_payload_location=None):

        if encoded_image_location != None:
            self.__encoded_image_location = encoded_image_location
        if decoded_payload_location != None:
            self.__payload_location = decoded_payload_location

        image = Image.open(self.__encoded_image_location)

        steg_pixels = list(image.getdata())
        steg_binary_values = ''
        for steg_pixel in steg_pixels:
            lsb = format((steg_pixel[2]), 'b')[-1]
            steg_binary_values = steg_binary_values + lsb

        #print(steg_binary_values)

        binary_list = stegutil.split_binary_string(steg_binary_values)

        #print(binary_list)
        final_string = stegutil.convert_binary_to_string(binary_list)

        # print(final_string)
        stop_buffer_index = final_string.find(self.STOPBUFFER)

        #print(final_string[:stop_buffer_index])
        return final_string[:stop_buffer_index]


