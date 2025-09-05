import sys
import array

numbers = array.array('i', [99,85,74,52])  

sys.stdout.write( str(numbers) )
sys.stdout.write( "\n" )
sys.stdout.write( str(numbers[1]) )
sys.stdout.write( "\n" )
sys.stdout.write( str(numbers[3]) )