import urllib
# import bs4
# import pandas as pd
# import numpy as np 
url = 'http://www.bigdataexaminer.com/'
beautiful = urllib.urlopen(url).read()
print(beautiful)