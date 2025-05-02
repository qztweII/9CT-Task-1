a = "s"
seeR = False
seeY = False
finished = False
distance = PortX #replace with ultrasonic sensor code
colour = PortX #replace with colour sensor

def find():
    global seeY, seeR
    while distance > 200:
        turn_left195
        forward10
        turn_right50 #
        wait800 #
        for i in range(12):
            if distance <200:
                break
            turn_right5
            wait800
    while distance > 5:
        forward3 #
    if colour == (75,84):
        seeY = True
        push_to_destination #
        go_back #
    elif colour == (56,68):
        seeR = True
        push_to_destination #
        go_back #
    else:
        go_back #


while finished == False:
    find()