#!/usr/bin/python3
import sys
import os

sys.stdout.flush()
os.execl(sys.executable, 'python', __file__, *sys.argv[1:])