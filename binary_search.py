def binarySearch(li,search_element):
  beg=0
  end=len(li)-1
  while(beg<=end):
    mid=(beg+end)//2
    if(search_element==li[mid]):
      return mid
    elif(search_element<li[mid]):
      end=mid-1
    elif(search_element>li[mid]):
      beg=mid+1
  else:
    return -1
li=[10,20,30,40,50,60]
search_element=int(input('Enter element to find:'))
res=binarySearch(li,search_element)
if(res!=-1):
  print((f'{search_element} is present at index {res}.'))
else:
  print(f'{search_element} is not present in list.')
  