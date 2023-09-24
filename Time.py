class Time():
    def __init__(self, FPS):
        super().__init__()
        self.time = 0
        self.frames = 0
        self.fps = FPS
    
    def updateTime(self):
        if self.frames != self.fps:
            self.frames += 1
            return False
        self.time += 1
        self.frames = 0
        return True

    def getTime(self):
        changed = self.updateTime()
        if changed:
            return self.time
        return -1