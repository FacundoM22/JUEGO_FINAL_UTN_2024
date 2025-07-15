class EfectoAlpha:
    def __init__(self, velocidad=3, min_alpha=0, max_alpha=255):
        self.alpha = min_alpha
        self.direction = 1
        self.velocidad = velocidad
        self.min = min_alpha
        self.max = max_alpha

    def update(self):
        self.alpha += self.direction * self.velocidad
        
        if self.alpha >= self.max:
            self.alpha = self.max
            self.direction = -1
        elif self.alpha <= self.min:
            self.alpha = self.min
            self.direction = 1
        
        return self.alpha
    
    def reset(self):
        self.alpha = self.min
        self.direction = 1