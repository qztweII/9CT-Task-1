a = "s"
seeR = False
seeY = False
finished = False
finding = 1
boardX = 1 #figure these out!
boardY = 1
moveCount = 0
distance = 'PortX' #replace with ultrasonic sensor code
colour = 'PortX' #replace with colour sensor

def find():
    global seeY, seeR, finding, moveCount
    while finding == 1:
        if moveCount >= 3:
            finding =2
            break
        moveCount += 1
        print("forward(boardX / 3)") # ive changed some of the code to print instead of run to test without robot
        for i in range(36):
            print("rotate(5)") #
            if distance == 200: #change == to < later when we use robot
                finding == 9
                break
        print("rotate(180)") #
    while finding == 2:
        rotate(90)
        forward(boardY)
        rotate(90)
        finding = 3
        moveCount = 0
    while finding == 3:
        if moveCount >= 3:
            finding =4
            break
        moveCount += 1
        print("forward(boardX / 3)") # ive changed some of the code to print instead of run to test without robot
        for i in range(36):
            print("rotate(5)") #
            if distance == 200: #change == to < later when we use robot
                finding == 9
                break
        print("rotate(180)") #
    while finding == 4:
        rotate(90)
        forward(boardY / 2)
        rotate(90)
        moveCount = 0
        finding = 5
    while finding == 5:
        forward(boardX / 2)
        for i in range(72): #FINISH
            a


while finished == False:
    find()