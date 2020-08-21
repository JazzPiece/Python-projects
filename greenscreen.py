###
### Author: Jasur.Jiasuer
### Course: CSc 110
### Description: This is a program that that can combine a PPM 
###              format still image with a green, blue, or red 
###              screen, with a background (or fill) image.
def write_file(out_list,out_file,width,height):
    '''This is my write file function that writes 
    my output list into a file
    '''
    info = open(out_file,'w')
    info.write('P3\n')
    info.write(str(width)+' '+str(height)+'\n')
    info.write('255\n')
    for row in out_list:
        for pixel in row:
            info.write(str(pixel[0])+' '+str(pixel[1])+' '+str(pixel[2])+' ')
        info.write('\n')
    info.close()
def new_image_list(channel,channel_difference,gs_file,fi_file,w,h):
    '''This is my new_image_list function, it
    returns a output list after comparing the 
    pixels
    '''
    '''This part of my code gives me the index
    at each pixels
    '''
    out_list = []
    if channel == 'r':
        channel_index = 0
        index_a = 1
        index_b = 2
    elif channel == 'g':
        channel_index = 1
        index_a = 0
        index_b = 2
    elif channel == 'b':
        channel_index = 2
        index_a = 0
        index_b = 1
    gs_list = load_image_pixels(gs_file)
    fi_list = load_image_pixels(fi_file)
    '''This part of my code decides wether the
    pixel should be replace with background
    '''
    for row in range(0,h):
        row_list = []
        for pixel in range(0,w):
            channel_a = float(gs_list[row][pixel][index_a]*channel_difference)
            channel_b = float(gs_list[row][pixel][index_b]*channel_difference)
            gs_value = float(gs_list[row][pixel][channel_index])
            if channel_a < gs_value:
                if channel_b < gs_value:
                    row_list.append(fi_list[row][pixel])
                else:
                    row_list.append(gs_list[row][pixel])
            else:
                row_list.append(gs_list[row][pixel])
        out_list.append(row_list)
    return out_list
def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        rgb_row = line.strip('\n').split()
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels
def main():
    # Get the 5 input values from the user, as described in the PA specification
    '''channel = 'r', 'g' or 'b'
    channel_difference = a float number between 1.0 to 10.0
    gs_file = a string, greenscreen image file name
    fi_file = a string, fill image file name
    out_file = a string, output file name
    '''
    loop_condition = 1
    while loop_condition == 1:
        channel = str(input('Enter color channel\n'))
        if not (channel == 'g' or channel == 'b' or channel == 'r'):
            print('Channel must be r, g, or b. Will exit.')
            break
        channel_difference = float(input('Enter color channel difference\n'))
        if channel_difference <= 1.0 or channel_difference > 10.0:
            print('Invalid channel difference. Will exit.')
            break
        gs_file = input('Enter greenscreen image file name\n')
        fi_file = input('Enter fill image file name\n')
        dimension_gs = get_image_dimensions_string(gs_file)
        dimension_fi = get_image_dimensions_string(fi_file)
        w_h_list = dimension_gs.split()
        width = int(w_h_list[0])
        height = int(w_h_list[1])
        if dimension_gs != dimension_fi:
            print('Images not the same size. Will exit.')
            break
        out_file = input('Enter output file name\n')
        out_list = new_image_list(channel,channel_difference,gs_file,fi_file,width,height)
        write_file(out_list,out_file,width,height)
        print('Output file written. Exiting.')
        break
main()