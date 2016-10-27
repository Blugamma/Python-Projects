from graphics import *
from random import randint

textFile = open('data.txt', 'r')
data = textFile.read().split("\n")
emojiList=[]
for word in data:
    emojiList.append(int(word))
print(emojiList)
textFile.close()

window = GraphWin("Visualisation", 1000, 800)
window.setBackground((color_rgb(135,206,250)))
while True:
    for data in emojiList:
        randomX = randint(150, 700)
        randomY = randint(150, 700) 
        loadPic = [Image(Point(randomX,randomY), "happyEmoji.gif"), Image(Point(randomX,randomY), "straightEmoji.gif"), Image(Point(randomX,randomY), "sadEmoji.gif"), Image(Point(randomX,randomY), "superHappy.gif")]
        if data > 40 and data <=50:
            loadPic[2].draw(window)
            passGrade = Text(Point(500,20), "Pass")
            passGrade.setFace('arial')
            passGrade.setSize(20)
            passGrade.setStyle('bold')
            passGrade.draw(window)
        elif data > 50 and data <=60:
            loadPic[1].draw(window)
            thirdGrade = Text(Point(500,20), "2:2")
            thirdGrade.setFace('arial')
            thirdGrade.setSize(20)
            thirdGrade.setStyle('bold')
            thirdGrade.draw(window)  
        elif data > 60 and data <=70:
            loadPic[0].draw(window)
            secondGrade = Text(Point(500,20), "2:1")
            secondGrade.setFace('arial')
            secondGrade.setSize(20)
            secondGrade.setStyle('bold')
            secondGrade.draw(window)
        elif data > 70:
            loadPic[3].draw(window)
            firstGrade = Text(Point(500,20), "1st")
            firstGrade.setFace('arial')
            firstGrade.setSize(20)
            firstGrade.setStyle('bold')
            firstGrade.draw(window)
        print(data)
        grade = Text(Point(500,50), data)
        grade.setFace('arial')
        grade.setSize(20)
        grade.setStyle('bold')
        grade.draw(window) 
        time.sleep(1)
        box = Rectangle(Point(0,0),Point(1000,800))
        box.setFill(color_rgb(135,206,250))
        box.draw(window)


   
