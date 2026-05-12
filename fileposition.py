
class FilePosition : 
   line : int
   column : int

   def __init__( self ) :
       self. line = 1
       self. column = 1

   def advance( self, i : int ) :
      self. column += i

   def nextLine( self ) :
      self. line += 1
      self. column = 1

   def clone( self ) : 
      copy = FilePosition( )
      copy. line = self. line
      copy. column = self. column
      return copy

   def __repr__( self ) -> str : 
      return "( {}, {} )". format( self. line, self. column )

   def __str__( self ) -> str :
      return "line " + str( self. line ) + ", column " + str( self. column )

   def __hash__( self ) -> int :
      return (self.line << 20) ^ self.column

   def __eq__( self, other ) -> bool :
      if not isinstance(other, FilePosition):
          return False
      return self.line==other.line and self.column==other.column
 
   def __lt__( self, other ) -> bool :
      if self.line != other.line:
         return self.line < other.line
      return self.column < other.column

