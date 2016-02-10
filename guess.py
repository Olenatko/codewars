class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives <= 0:
            raise Exception("Omae wa mo shindeiru")
        if self.number == n:
            return True
        if self.number != n:
            self.lives -= 1
            return False
guess_res = Guesser(5, 4)
print(guess_res.guess(5))