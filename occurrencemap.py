from fileposition import FilePosition
from typing import Dict, Set, Optional
import os


class OccurrenceMap:
    occs: Dict[str, Dict[str, Set[FilePosition]]]

    def __init__(self):
        self.occs = dict()

    def add(self, word: str, fname: str, pos: FilePosition) -> None:
        w = word.lower()
        if w not in self.occs:
            self.occs[w] = {}
        if fname not in self.occs[w]:
            self.occs[w][fname] = set()
        self.occs[w][fname].add(pos.clone())

    def distinctWords(self) -> int:
        return len(self.occs)

    def totalOccurrences(self, word: Optional[str] = None,
                         fname: Optional[str] = None) -> int:
        if word is None:
            return sum(len(posset)
                       for filemap in self.occs.values()
                       for posset in filemap.values())
        if word not in self.occs:
            return 0
        if fname is None:
            return sum(len(posset) for posset in self.occs[word].values())
        return len(self.occs[word].get(fname, set()))

    def __repr__(self) -> str:
        return str(self.occs)

    def __str__(self) -> str:
        lines = []
        for word in sorted(self.occs.keys()):
            total = sum(len(posset) for posset in self.occs[word].values())
             
            lines.append(f"\"{word}\" has {total} occurrences(s):")
            for fpath in sorted(self.occs[word].keys(),
                                key=lambda p: p.replace(os.sep, '/')):
                printable = fpath.replace(os.sep, '/')
                lines.append(f"   in file {printable}")
                for pos in sorted(self.occs[word][fpath]):
                    lines.append(f"      at line {pos.line}, column {pos.column}")
        return "\n".join(lines)
