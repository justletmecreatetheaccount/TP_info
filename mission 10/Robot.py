class Robot:

    def __init__(self, nom):
        # nom du robot
        self.__nom = nom
        self.__history = []

    def __str__(self):
        """
        Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant le nom,
        les coordonnées et l'orientation du robot.
        """
        return str(self.nom()) + "@(" + str(round(self.x())) + "," + \
               str(round(self.y())) + ") angle: " + str(self.angle())

    def add_history(self, command, arg):
        self.__history.append((command, arg))

    def history(self):
        return self.__history

    def unplay(self):
        try:
            self.turtle.color("white")
        except:
            pass

        for action in reversed(self.history()):
            if action[0] == "forward":
                self.move_backward(action[1])
            if action[0] == "backward":
                self.move_forward(action[1])
            if action[0] == "right":
                self.turn_left()
            if action[0] == "left":
                self.turn_right()

        self.__history = []

    def nom(self):
        return self.__nom
