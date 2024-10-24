

class InputController:
    def __init__(self, left=None, right=None, up=None, down=None):
        self.left = left
        self.right = right
        self.down = down
        self.up = up

    def input_connected(self):
        if self.left or self.right or self.up or self.down:
            return True
        else:
            return False