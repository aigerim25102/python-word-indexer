from fileposition import FilePosition
from occurrencemap import OccurrenceMap

omap = OccurrenceMap()

# Add words manually
omap.add("day", "dir1/f1", FilePosition())
omap.add("day", "dir1/f1", FilePosition())   # duplicate position, set prevents counting twice
p = FilePosition()
p.advance(5)
omap.add("day", "dir1/f1", p)

omap.add("great", "dir1/f2", FilePosition())

print("\n=== Internal repr ===")
print(repr(omap))

print("\n=== Pretty print ===")
print(omap)

print("\n=== Counts ===")
print("Distinct words:", omap.distinctWords())
print("Total occurrences:", omap.totalOccurrences())
print("Total of 'day':", omap.totalOccurrences("day"))
print("Total of 'day' in dir1/f1:", omap.totalOccurrences("day", "dir1/f1"))
