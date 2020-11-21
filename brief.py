'''
Display all 'Up' interfaces
'''

with open ('notes/ipv4_int_bri.txt') as f:
    for line in f:
        # interface, address, status, protocol = line.split()
        interface = line[:31].rstrip()
        address = line[31:47].rstrip()
        status = line[47:69].rstrip()
        protocol = line[69:].rstrip()
        if status == 'Up' == protocol:
            # %-30s - left justify up to 30 spaces to the right
            print '%-30s %s' % (interface, address)
