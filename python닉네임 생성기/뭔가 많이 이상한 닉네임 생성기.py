import random

f = open("index.txt", 'r')
s = open("index2.txt", 'r')
file = f.read()

index = file.split('\n')
file = s.read()

index2 = file.split('\n')
ran1max = len(index) - 1 
ran2max = len(index2) - 1
print('뭔가 이상한 닉네임 짓기 프로그램에 오신것을 환영합니다. \n생성을 시작하겠습니다.\n')
while True:
    ran = random.randrange(0,ran1max)
    ran2 = random.randrange(0,ran2max)
    
    print(index[ran], end = ' ')
    print(index2[ran2], end = '')
        
    re = input('\n종료(Yes = Yes)')
    
    if re == 'Y' or re == 'y' or re == 'Yes' or re == 'yes' or re == 'YES' or re == '1':
        print('닉네임 짓기 프로그렘을 종료합니다.')
        break
    
    elif re == '훈민정음':
        print('나랏말싸미 듕귁에 달아 문자와로 서르 사맛디 아니할쎄 \n이런 젼차로 어린 백셩이 니르고져 홀 배 이셔도  \n마참내 제 뜨들 시러펴디 몯 할 노미 하니라 \n내 이랄 위하야 어엿비 너겨 새로 스믈 여듧 짜랄 맹가노니 \n사람마다 해여 수비 니겨 날로 쑤메 뼌한킈 하고져 할따라미니라')

f.close()
