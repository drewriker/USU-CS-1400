import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    def changeMouth(self):
        self.__smile = False if True else True
        self.draw_face()

    def changeEmotion(self):
        self.__happy = False if True else True
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = False if True else True
        self.draw_face()

    def __drawMouth(self):
        turtle.pu()
        turtle.pensize(5)

        if self.isSmile():
            turtle.goto(-35, -40)
            turtle.setheading(315)
            turtle.pd()
            turtle.circle(50, 90)
        else:
            turtle.goto(35, -40)
            turtle.setheading(140)
            turtle.pd()
            turtle.circle(50, 90)

    def __drawHead(self):
        turtle.reset()
        turtle.pu()
        turtle.goto(0, -100)

        if self.__happy:
            turtle.fillcolor("yellow")
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
        else:
            turtle.fillcolor("red")
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()

    def __drawEyes(self):
        turtle.pu()

        if self.__darkEyes:
            turtle.goto(-35, 30)
            turtle.fillcolor("black")
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()

            turtle.pu()
            turtle.goto(35, 30)
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()
        else:
            turtle.goto(-35, 30)
            turtle.fillcolor("blue")
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()

            turtle.pu()
            turtle.goto(35, 30)
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()


def main():
    face = Face()
    face.draw_face()
    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
