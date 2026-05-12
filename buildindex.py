
from fileposition import FilePosition
from occurrencemap import OccurrenceMap
from filescanning import recDirIterator

import codecs

def buildAndPrint( topdir : str ) -> None :
  

   occ = OccurrenceMap( )

   try :
      for fname, word, position in recDirIterator( topdir ) :
         occ. add( word, fname, position )

   except Exception as ex:
      print( "there was an exception: " + str( ex ))

   print( occ ) 

   if True: 
      file = open( "output_for_" + topdir + ".txt", "w", encoding = "utf8" )
      file. write( str( occ ) + "\n" )
      file. write( "number of distinct words  " + str( occ. distinctWords( )) + "\n" )
      file. write( "number of occurrences     " + str( occ. totalOccurrences( )) + "\n" )
      file. write( "\n" )
      file. close( ) 

buildAndPrint( "test_dir" )

