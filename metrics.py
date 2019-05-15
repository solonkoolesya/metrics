#!/usr/bin/env python
import psutil
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-cpu', action='store_true', help='print cpu metrics')
parser.add_argument('-mem', action='store_true', help='print memory metrics')


cpu = psutil.cpu_times()
mem = psutil.virtual_memory()
swap_mem = psutil.swap_memory()

if  parser.parse_args().cpu == True:
    print  ("system.cpu.idle", cpu.idle)
    print  ("system.cpu.user", cpu.user)
    print  ("system.cpu.guest", cpu.guest)
    print  ("system.cpu.iowait", cpu.iowait)
    print  ("system.cpu.stolen", cpu.steal)
    print  ("system.cpu.system", cpu.system)

if  parser.parse_args().mem == True:
    print ("virtual total",  mem.total)
    print ("virtual used",  mem.used)
    print ("virtual free",  mem.free)
    print ("virtual shared",  mem.shared)
    print ("swap total",  swap_mem.total)
    print ("swap used",  swap_mem.used)
    print ("swap free",  swap_mem.free)

