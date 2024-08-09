import sys

def my_function(x: str, y:str) -> None:
  print( "The sum of x and y is: " + str( x + y ))

  for i in range(0, 10 ):
      print(i )

  if x>10 :
   print("X is greater than 10")

  if y== 20:
    print("Y is equal to 20")

  unused_variable = 100
  random_num = 50

my_function( 5,20)
