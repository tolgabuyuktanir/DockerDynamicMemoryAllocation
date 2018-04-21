#
#docker build -t pytest .
#docker run pytest python ./randomNumberSort.py param1 param2
#

import random
import sys

def random_sort(n):
    return sorted([random.random() for i in range(n)])
 
 
if __name__ == "__main__":
	i=0
	if(len(sys.argv)!=3):
		print("Usage:\n python3 randomNumberSort.py repetitions arrayLenght\n\nEx:\n python randomNumberSort.py 10 100")
		
	else:
		while(i<int(sys.argv[1])):
			random_sort(int(sys.argv[2]))
			i+=1
			print(str(i)+".random array is sorting...")
		

