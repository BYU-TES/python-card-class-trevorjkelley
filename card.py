#definition for a card class

class Card:
    def __init__(self, new_suit, new_rank):
        self.suit = new_suit
        self.rank = new_rank
        self.value = 0
        match new_rank:
            case "Two":
                self.value = 2
            case "Three":
                self.value = 3
            case "Four":
                self.value = 4
            case "Five":
                self.value = 5
            case "Six":
                self.value = 6
            case "Seven":
                self.value = 7
            case "Eight":
                self.value = 8
            case "Nine":
                self.value = 9
            case "Ten":
                self.value = 10
            case "Jack":
                self.value = 10
            case "Queen":
                self.value = 10
            case "King":
                self.value = 10
            case "Ace":
                self.value = 11
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def get_value(self):
        return self.value
    def __str__(self):
        result = f"{self.rank} of {self.suit}"
        return result
    def change_ace(self):
        if self.suit == "Ace" and self.value == 11:
            self.value = 1 
            return True
        else:
            return False
        
    