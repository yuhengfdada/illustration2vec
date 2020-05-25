import os
import requests
import re
import time
f = 'image_links.txt'
lines = open(f).readlines()
open(f, 'w').writelines(lines[5376:])