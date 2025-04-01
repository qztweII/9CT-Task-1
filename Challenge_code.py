a = "s"
seeR = False
seeY = False
distance = PortX #replace with ultrasonic sensor code
colour = PortX #replace with colour sensor
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def find():
    global seeY, seeR
    move in a pattern i havent decided yet or random
def found():
    global seeY, seeR
    if distance < 20:
        while distance != 5:
            go_forward
        if distance == (4, 6) and colour == (71, 80):
            seeY = True
        elif distance == (4, 6) and colour == (46, 55):
            seeR = True
        else:
            record_other()
def():
def():
def():
def():
def():

while a != 5:
    while no_red and no_yellow:
        find()
        found()
    pushred()
    pushyellow()
