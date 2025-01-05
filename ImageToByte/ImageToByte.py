from PIL import Image
import numpy as np 

img = Image.open('five.png')
data = list(img.getdata())
#        print(data)  
data_array = np.array(data)
#        print(f'The dimensions of data currently are: {data_array.shape}') 

#The image chosen by us is yeilding a 784 x 4 matix. And by looking into the data, it seems, that the last values are correct for us.
#So creating a new list:
list1 = [item[3] for item in data]
print(list1)  
#Now use this list in the model to find the number.


'''
And just for fun you can goto CHECK.cpp for checking XD

'''