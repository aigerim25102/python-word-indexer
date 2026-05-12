from fileposition import FilePosition
from typing import Tuple, Generator, TextIO

import os
import syntax
import copy
import codecs

def recDirIterator(topdir: str) -> Generator[Tuple[str, str, FilePosition], None, None]:
      
   if not os.path.exists(topdir):
      raise FileNotFoundError(f"Top directory does not exist: {topdir}")
   if not os.path.isdir(topdir):
      raise NotADirectoryError(f"Not a directory: {topdir}")
   for root, dirs, files in os.walk(topdir):
    dirs.sort()
    files.sort()
    for fname in files:
        fullpath = os.path.join(root, fname)   # do not change slashes
        with codecs.open(fullpath, mode="r", encoding="utf-8") as f:
            for (word, pos) in fileIterator(f):
                yield (fullpath, word, pos)





def fileIterator(f):
    pos = FilePosition()
    for raw_line in f:
        line = raw_line.rstrip("\n")
        i = 0
        while i < len(line):
            ch = line[i]
            if syntax.inWord(ch):
                start = i
                while i < len(line) and syntax.inWord(line[i]):
                    i += 1
                word = line[start:i]
                p = pos.clone()
                p.column = start + 1  # 1-based
                yield (word, p)
            else:
                i += 1
        pos.nextLine()
