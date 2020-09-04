# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
实现统计一篇英文文章内每个单词的出现频率，并返回出现频率最高的前10个单词及其出现次数 
"""

import os
import re
from collections import Counter
from optparse import OptionParser

def word_count(filename, num=10):
    with open(filename, "r") as fd:
        all = Counter()
        for line in fd.readlines():
            count = Counter(re.split(r"[^a-zA-Z0-9-]+", line))
            print(count)
            all.update(count)
        
        all[''] =0
        
        return all.most_common(num)
            
        
if __name__ == "__main__":
    usage = """
    %prog file_name
    """

    parser = OptionParser(usage=usage)
    parser.add_option("--file", dest="filename", help="file to count the words")

    (options, args) = parser.parse_args()
    
    
    if not options.filename or not os.path.exists(options.filename):
        parser.print_help()
        exit(1)
    
    count = word_count(filename=options.filename)
    for k, v in count:
        print(k, v)
