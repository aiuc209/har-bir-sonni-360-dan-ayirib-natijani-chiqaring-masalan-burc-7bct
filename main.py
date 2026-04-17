class Athlete:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def info(self):
        avg = self.average_score()
        print(f"{self.name}: {self.scores} -> O'rtacha: {avg:.1f}")


if __name__ == "__main__":
    s = Athlete("Rustam")
    for n in [8.5, 9.0, 7.8, 9.2, 8.7]:
        s.add_score(n)
    s.info()
