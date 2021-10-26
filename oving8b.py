qarray = ["hva er hovedstaden i Norge? \n (a) Oslo \n (b) Bergen", "Jupiter har ... måner \n (a) 79 \n (b) 89"]
svararray = []


class Question:
    def __init__(self, svararray, qarray):
        self.x1 = svararray[0]
        self.x2 = svararray[1]
        self.y1 = qarray[0]
        self.y2 = qarray[1]

    def __str__(self):
        if self.x2 == "a" and self.y2 == qarray[1] and self.x1 == "a" and self.y1 == qarray[0]:
            return 'riktig på begge spørsmål'
        if self.x2 == "a" and self.y2 == qarray[1] or self.x1 == "a" and self.y1 == qarray[0]:
            return 'riktig på et spørsmål'
        else:
            return 'feil på begge'


for i in range(len(qarray)):
    print(qarray[i])
    svar = input("svar:")
    svararray.append(svar)

resultat = Question(svararray, qarray)

print(resultat.__str__())
