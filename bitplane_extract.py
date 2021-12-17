##'''Stegsolve i python. v.1.0'''
#!/usr/bin/env python3

from PIL import Image

img = Image.open("frimerke.png")

def get_planes(img_data,bit_pos):
	img_pixels = list(img_data)
	out_pixels = list()
	for i in range(len(img_pixels)):
		bit_plane_value = bin(img_pixels[i])[2:].zfill(8)[7-bit_pos]
		out_pixels.append(255*int(bit_plane_value))	
		out_pixels.append(0)
	return out_pixels

for channel in range(3):
	for bit_pos in range(8):
		out_pixels = get_planes(img.getchannel(channel).getdata(),bit_pos)
		out_img = Image.new("1", img.size)
		out_img.putdata(out_pixels)
		out_img.save(f"{channel}-{bit_pos}.png")
		#out_img.show()