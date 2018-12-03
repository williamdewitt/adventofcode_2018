import cozmo
from collections import Counter

text_file = open("day02_input.txt", "r")
input = text_file.read().split('\n')
match = list('abcdefghijklmnopqrstuvwxyz')

def cozmo_program(robot: cozmo.robot.Robot):
    count2exact = 0
    count3exact = 0

    for box in input:
        counter = Counter(box)
        d = {c : counter.get(c,0) for c in match}

        for value in d.values():
            if value == 2:
                count2exact +=1
                break

        for value in d.values():
            if value == 3:
                count3exact +=1
                break

    print(count2exact * count3exact)

     # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    # find face
    face = None
    face = robot.world.wait_for_observed_face(timeout=30)
    robot.turn_towards_face(face).wait_for_completed()

    # Cosmo says the answer
    robot.say_text("Your puzzle answer is {}".format(str(count2exact * count3exact))).wait_for_completed()

cozmo.run_program(cozmo_program)
