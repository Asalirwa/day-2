def fizzbuzz(x,y):
  if not (isinstance(x,list) and isinstance(y,list)):
    return "invalid input"
  newlist = x+y
  mylist =len(newlist)
  if(mylist % 5==0 and mylist % 3==0):
    return "fizzbuzz"

  if( mylist % 5==0):
    return "buzz"
  if (mylist % 3==0):
    return "fizz"

  return len(newlist) 


