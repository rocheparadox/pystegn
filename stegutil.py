

def convert_to_proper_binary(binary_value):
    pre_buffer = 8 - len(binary_value)
    for i in range(pre_buffer):
        binary_value = '0' + binary_value

    return binary_value

def convert_string_to_binary(string):
    binary_values = []
    for char in string:
        binary_value = format(ord(char), 'b')
        binary_value = convert_to_proper_binary(binary_value)
        binary_values.append(binary_value)

    return binary_values

def convert_binary_to_string(binary_values):
    string=''
    for binary in binary_values:
        dec = int(binary, 2)
        string = string + chr(dec)

    return string

def manipulate_lsb(binary, lsb_value):
    binary = binary[:-1] + lsb_value
    return binary

def manipulate_pixel(pixel, lsb_value):
    pixel_binary = format(pixel[2], 'b')
    pixel_binary_start = pixel_binary
    pixel_binary = manipulate_lsb(pixel_binary, lsb_value)
    pixel_result = int(pixel_binary,2)
    #print(pixel,pixel_binary_start,pixel_binary, pixel_result, lsb_value)
    pixel = (pixel[0], pixel[1], pixel_result)
    return pixel

def get_size_of_payload(string):
    return len(string)*8

def get_size_of_image(image):
    return image.size[0] * image.size[1]

def split_binary_string(steg_binary_values):
    binary_list = []
    binary_value = ''
    for i in range(len(steg_binary_values)):
        if(i%8 == 0):
            binary_list.append(binary_value)
            binary_value=''
        binary_value = binary_value + steg_binary_values[i]

    return binary_list[1:]