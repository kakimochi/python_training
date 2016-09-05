#coding: UTF-8

for num in range(0, 64):
	print "FOOTPRINT_NV" + '{:03d}'.format(num) + " = " + "REGISTER_0x" + '{:02X}'.format(num + 0x80)
