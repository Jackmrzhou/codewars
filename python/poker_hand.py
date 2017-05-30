class PokerHand(object):

	RESULT = ["Loss", "Tie", "Win"]

	def __init__(self, hand):
		self.hand = hand.split(' ')
		for index, item in enumerate(self.hand):
			if 'T' in item:
				self.hand[index] = (10, item[1])
			elif 'J' in item:
				self.hand[index] = (11, item[1])
			elif 'Q' in item:
				self.hand[index] = (12, item[1])
			elif 'K' in item:
				self.hand[index] = (13, item[1])
			elif 'A' in item:
				self.hand[index] = (14, item[1])
			else:
				self.hand[index] = (int(item[0]), item[1])
		self.priority = self.match_priority()

	def is_same_color(self):
		color = self.hand[1][1]
		for i in self.hand:
			if i[1] != color:
				return False
		else:
			return True

	def is_straight(self):
		if [i[0] for i in self.hand] == [14,5,4,3,2]:
			for index, item in enumerate(self.hand):
				if item[0] == 14:
					self.hand[index][0] = 1
			return True
		elif [i[0]for i in self.hand] == [x for x in range(self.hand[0][0],self.hand[0][0]-5,-1)]:
			return True
		else:
			return False

	def count_same_card(self):
		result = {}
		for card in self.hand:
			if card[0] not in result:
				result[card[0]] = 1
			else:
				result[card[0]] += 1
		return result

	def is_two_pairs(self,count_cards):
		count = 0;
		for k,v in count_cards.items():
			if v==2:
				count += 1
		return count == 2

	def match_priority(self):
		self.hand = sorted(self.hand, key = lambda x:x[0],reverse=True)
		count_cards = self.count_same_card()
		if self.is_same_color():
			if self.is_straight():
				if self.hand[0][0] == 14:
					return [10,10]
				else:
					return [9,max(self.hand, key=lambda x:x[0])[0]]
			else:
				return [6]+[i[0] for i in self.hand]
		elif self.is_straight():
			return [5, max(self.hand, key=lambda x:x[0])[0]]
		elif max(count_cards.items(), key=lambda x:x[1])[1] == 4:
			return [8]+[i[0] for i in self.hand]
		elif max(count_cards.items(), key=lambda x:x[1])[1] == 3 and len(count_cards) == 2:
			return [7] + [i[0] for i in self.hand]
		elif max(count_cards.items(), key=lambda x:x[1])[1] == 3 and len(count_cards) > 2:
			return [4] + [i[0] for i in self.hand]
		elif self.is_two_pairs(count_cards):
			return [3] + [i[0]for i in self.hand]
		elif max(count_cards.items(), key=lambda x:x[1])[1] == 2:
			return [2] + [i[0] for i in self.hand]
		else:
			return [1] + [i[0] for i in self.hand]

	def compare_with(self, other):
		if self.priority> other.priority:
			return self.RESULT[2]
		elif self.priority < other.priority:
			return self.RESULT[0]
		elif self.priority == other.priority:
			return self.RESULT[1]
Test1 = PokerHand("JC 6H JS JD JH")
Test2 = PokerHand("JC 7H JS JD JH")

print(Test1.priority)
print(Test2.priority)
#other people' solution
from collections import Counter

RESULT      = ["Loss", "Tie", "Win"]
HEX_CARDS   = "23456789ABCDE"
CARD_TO_HEX = str.maketrans("TJQKA", "ABCDE")
MAIN_RANK   = [lambda colC, valC, isS:  5 in colC.values() and isS,                    # Straight Flush
               lambda colC, valC, isS:  4 in valC.values(),                            # Square
               lambda colC, valC, isS:  3 in valC.values() and 2 in valC.values(),     # Full house
               lambda colC, valC, isS:  5 in colC.values(),                            # Flush
               lambda colC, valC, isS:  isS,                                           # Straight
               lambda colC, valC, isS:  3 in valC.values(),                            # Three of a kind
               lambda colC, valC, isS:  2 in valC.values() and len(valC.keys()) == 3,  # 2 pairs
               lambda colC, valC, isS:  2 in valC.values() and len(valC.keys()) == 4,  # 1 pair,
               lambda colC, valC, isS:  True]                                          # 1 card


class PokerHand(object):

    def __init__(self, hand):
        hand         = hand.translate(CARD_TO_HEX)
        valCount     = Counter( hand[n] for n in range(0, len(hand), 3) )
        colorCount   = Counter( hand[n] for n in range(1, len(hand), 3) )
        
        minCardIdx   = int(min(valCount.keys()), 16) - 2
        isStraight   = valCount.keys() == set(HEX_CARDS[minCardIdx:minCardIdx+5])
        hashSameRank = int(''.join(sorted(valCount.keys(), key = lambda k: (valCount[k], k), reverse = True)), 16)
        
        for i,func in enumerate(MAIN_RANK):
            if func(colorCount, valCount, isStraight):
                self.handValue = (len(MAIN_RANK) - i) * 16**5 + hashSameRank
                break
                
        
    def compare_with(self, other):
        return RESULT[ (self.handValue >= other.handValue) + (self.handValue > other.handValue) ]