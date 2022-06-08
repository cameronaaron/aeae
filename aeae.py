if __name__ == '__main__':
  exit()

langdict = {'æ':0, 'ä':1, 'â':2, 'å':3, 'ă':4, 'ạ':5, 'ą':6, 'a':7,'€':8, 'ę':9, 'ê':10, 'ĕ':11, 'ė':12, 'ë':13, '¬':14, 'e':15}


#decode from 4 bit codepage

def dccp(str):
  b = []                # make an empty list
  for i in str:         # every char in the function string
    a = hex(ord(i))     # get the hex value of the char
    b.append(a[2])      # split it and add to the list
    b.append(a[3])
  c =  []               # make another empty list
  for i in b:           # put 
    c.append(int(i),16)
    

#encode to 4 bit codepage

def encp(str):
  b = 0
  for i in str:
    a = langdict[i]
    
  
  

def parse(str):
  i = str
  l = []
  
  
#?

def tostring(str):
  l = []
  for i in str:
    l.append(i)

