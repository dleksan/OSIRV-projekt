img=cv2.imread('cropan_v21.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
weights=[[128,64,4,2,1,32,16,8,0,0,16,8],
         [32,16,8,128,64,4,2,1,0,0,0,4],
         [4,2,1,32,16,8,0,0,0,0,0,2],
         [8,128,64,4,2,1,0,0,0,0,0,1],
         [1,32,16,8,0,0,0,0,0,0,0,0],
         [64,4,2,1,0,0,0,0,0,0,0,0],
         [16,8,0,0,0,0,0,0,0,0,128,64],
         [2,1,0,0,0,0,0,0,0,0,32,16],
         [0,0,0,0,0,0,0,0,0,0,4,2],
         [0,0,0,0,0,0,0,0,0,0,0,128],
         [0,0,0,0,0,0,128,64,0,0,0,32],
         [128,64,32,0,0,0,32,16,8,128,64,4]]

#255 bijela #0 crna
logicMatrix=np.empty(shape=(12,12), dtype='object')

height=box[0,1]-box[1,1]
width=box[2,0]-box[1,0]

#print("width and height")
#print(height)
#print(width)

startPointX=box[1,1]+int(width/14+width/16)
startPointY=box[0,0]+int(height/14+height/28)

#print("Start point coordinates")
#print("x:",startPointX)

#print("y:",startPointY)


endPointX=box[0,1]-int(width/14+width/28)
endPointY=box[2,0]-int(width/14+width/28)

#print("End point coordinates")
#print("x:",endPointX)
#print("y:",endPointY)

stepX=int((endPointX-startPointX)/12)+1

stepY=int((endPointY-startPointY)/12)+1
#print("Steps")
#print("x:",stepX)
#print("y:",stepY)

i=0;
j=0;
for x in range(startPointX,endPointX+stepX,stepX):
  for y in range(startPointY,endPointY+stepY,stepY):  
      i=int((x-startPointX)/stepX)
      j=int((y-startPointY)/stepY) 
      #print(i,j)    
      if gray[x,y]<128:
          logicMatrix[i,j]=1
      else:
          logicMatrix[i,j]=0
      
#print(gray)


for x in range(startPointX,endPointX+stepX,stepX):
  for y in range(startPointY,endPointY+stepY,stepY):  
      if gray[x,y]<128:
          gray[x,y]=255
      else:
          gray[x,y]=0


print("Slika sa označenim poljima:")
cv2_imshow(gray)
print("Matrica s vrijednostima polja (0 za bijelo polje, 1 za crno polje)")
print(logicMatrix)






print("Dekodirana poruka:")
firstSymbol=weights[3][0]*logicMatrix[3][0]+weights[4][0]*logicMatrix[4][0]+weights[6][10]*logicMatrix[6][10]+weights[6][11]*logicMatrix[6][11]+weights[7][10]*logicMatrix[7][10]+weights[7][11]*logicMatrix[7][11]+weights[8][10]*logicMatrix[8][10]+weights[8][11]*logicMatrix[8][11]
if (firstSymbol <= 128):
    firstSymbol=firstSymbol-1
    print(chr(firstSymbol))
else:
  print(firstSymbol-130)

secondSymbol=weights[0][0]*logicMatrix[0][0]+weights[0][1]*logicMatrix[0][1]+weights[1][0]*logicMatrix[1][0]+weights[1][1]*logicMatrix[1][1]+weights[1][2]*logicMatrix[1][2]+weights[2][0]*logicMatrix[2][0]+weights[2][1]*logicMatrix[2][1]+weights[2][2]*logicMatrix[2][2]
if (secondSymbol <= 128):
    secondSymbol=secondSymbol-1
    print(chr(secondSymbol))
else:
  print(secondSymbol-130)

thirdSymbol=weights[0][2]*logicMatrix[0][2]+weights[0][3]*logicMatrix[0][3]+weights[0][4]*logicMatrix[0][4]+weights[10][6]*logicMatrix[10][6]+weights[10][7]*logicMatrix[10][7]+weights[11][6]*logicMatrix[11][6]+weights[11][7]*logicMatrix[11][7]+weights[11][8]*logicMatrix[11][8]
if (thirdSymbol <= 128):
    thirdSymbol=thirdSymbol-1
    print(chr(thirdSymbol))
else:
    print(thirdSymbol-130)

fourthSymbol=weights[0][5]*logicMatrix[0][5]+weights[0][6]*logicMatrix[0][6]+weights[0][7]*logicMatrix[0][7]+weights[1][5]*logicMatrix[1][5]+weights[1][6]*logicMatrix[1][6]+weights[1][7]*logicMatrix[1][7]+weights[11][9]*logicMatrix[11][9]+weights[11][10]*logicMatrix[11][10]
if (fourthSymbol <= 128):
    fourthSymbol=fourthSymbol-1
    print(chr(fourthSymbol))
else:
    print(fourthSymbol-130)


fifthSymbol=weights[1][3]*logicMatrix[1][3]+weights[1][4]*logicMatrix[1][4]+weights[2][3]*logicMatrix[2][3]+weights[2][4]*logicMatrix[2][4]+weights[2][5]*logicMatrix[2][5]+weights[3][3]*logicMatrix[3][3]+weights[3][4]*logicMatrix[3][4]+weights[3][5]*logicMatrix[3][5]
if (fifthSymbol <= 128):
    fifthSymbol=fifthSymbol-1
    print(chr(fifthSymbol))
else:
    print(fifthSymbol-130)

sixthSymbol=weights[3][1]*logicMatrix[3][1]+weights[3][2]*logicMatrix[3][2]+weights[4][1]*logicMatrix[4][1]+weights[4][2]*logicMatrix[4][2]+weights[4][3]*logicMatrix[4][3]+weights[5][1]*logicMatrix[5][1]+weights[5][2]*logicMatrix[5][2]+weights[5][3]*logicMatrix[5][3]
if (sixthSymbol <= 128):
    sixthSymbol=sixthSymbol-1
    print(chr(sixthSymbol))
else:
    print(sixthSymbol-130)

seventhSymbol=weights[5][0]*logicMatrix[5][0]+weights[6][0]*logicMatrix[6][0]+weights[6][1]*logicMatrix[6][1]+weights[7][0]*logicMatrix[7][0]+weights[7][1]*logicMatrix[7][1]+weights[9][11]*logicMatrix[9][11]+weights[10][11]*logicMatrix[10][11]+weights[11][11]*logicMatrix[11][11]
if (seventhSymbol <= 128):
    seventhSymbol=seventhSymbol-1
    print(chr(seventhSymbol))
else:
    print(seventhSymbol-130)



eightSymbol=weights[0][10]*logicMatrix[0][10]+weights[0][11]*logicMatrix[0][11]+weights[1][11]*logicMatrix[1][11]+weights[2][11]*logicMatrix[2][11]+weights[3][11]*logicMatrix[3][11]+weights[11][0]*logicMatrix[11][0]+weights[11][1]*logicMatrix[11][1]+weights[11][2]*logicMatrix[11][2]
if (eightSymbol <= 128):
    eightSymbol=eightSymbol-1
    print(chr(eightSymbol))
else:
    print(eightSymbol-130)
