#!/usr/bin/env python3

from PIL import Image

img = Image.open("filename")

def get_planes(img_data,bit_pos):
	img_pixels = list(img_data)
	out_pixels = list()
	for i in range(len(img_pixels)):
		bit_plane_value = bin(img_pixels[i])[2:].zfill(8)[7-bit_pos]
		## Returns either 0 or 1. 
		## Append 0 or 255 (black or white):
		out_pixels.append(255*int(bit_plane_value))	
	return out_pixels

if __name__ == '__main__':

	for channel in range(3):
		for bit_pos in range(8):
			out_pixels = get_planes(img.getchannel(channel).getdata(),bit_pos)
			## Black and white single channel ("1"):
			out_img = Image.new("1", img.size)
			out_img.putdata(out_pixels)
			out_img.save(f"{'RGB'[channel]}-{bit_pos}.png")
			## uncomment if you want to open each picture as it's saved:
			#out_img.show()
		
