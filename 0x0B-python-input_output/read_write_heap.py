#!/usr/bin/python3
"""script that finds a string in the heap of a running process, and replaces it

Usage: sudo ./read_write_heap.py pid search_string replace_string"""
import sys


def exitmsg():
    """ Function for Print Information """
    sys.stdout.write("Usage: read_write_heap.py")
    sys.stdout.write(" pid search_string replace_string\n")
    sys.exit(1)

# Run conditions
if len(sys.argv) != 4:
    exitmsg()
pid = int(sys.argv[1])
if pid <= 0:
    exitmsg()
search_string = str(sys.argv[2])
if search_string == "":
    exitmsg()
replace_string = str(sys.argv[3])

# Open maps and mem files in /proc folder
maps = "/proc/{}/maps".format(pid)
mem = "/proc/{}/mem".format(pid)

# Open maps file
try:
    maps_file = open(maps, 'r')
except IOError as e:
    print("[ERROR] Can't open file {}:".format(maps_filename))
    sys.exit(1)

for line in maps_file:
    sline = line.split(' ')

    if sline[-1][:-1] != "[heap]":
        continue
    print("[*] Found [heap]:")

    addr = sline[0]
    perm = sline[1]
    pathname = sline[-1][:-1]

    # Permission Check
    if perm[0] != 'r' or perm[1] != 'w':
        print("[*] {} No r/w permissions".format(pathname))
        maps_file.close()
        sys.exit(0)

    # Start and End of Heap
    addr = addr.split("-")
    if len(addr) != 2:
        print("[*] Wrong addr format")
        maps_file.close()
        sys.exit(1)

    addr_start = int(addr[0], 16)
    addr_end = int(addr[1], 16)

    # Open Mem as bytes type
    try:
        mem_file = open(mem, 'rb+')
    except IOError as e:
        print("[ERROR] Can not open file {}:".format(mem_filename))
        maps_file.close()
        sys.exit(1)
    # Seek address in Heap
    mem_file.seek(addr_start)
    heap = mem_file.read(addr_end - addr_start)

    # Search String
    try:
        i = heap.index(bytes(search_string, "ASCII"))
    except Exception:
        print("Can't find '{}'".format(search_string))
        maps_file.close()
        mem_file.close()
        sys.exit(0)
    print("[*] Found '{}' at {:x}".format(search_string, i))

    # Replace String
    mem_file.seek(addr_start + i)
    mem_file.write(bytes(replace_string + "\0", "ASCII"))
    print("[*] Replace Success")
    maps_file.close()
    mem_file.close()
    # Found heap so now exit
    break
