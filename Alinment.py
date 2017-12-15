class DNAAlignment:
    def __init__(self, input_dna1, input_dna2):
        self.dna1 = input_dna1
        self.dna2 = input_dna2
        self.score = Alignment()

    def count_score(self):
        self.score = self.get_best_score(self.dna1, self.dna2)

    def __str__(self):
        return str(self.score) + "\n" + "Score: " + str(self.score.count_score())

    def get_best_score(self, dna1, dna2):
        l1, l2 = len(dna1), len(dna2)
        if l1 == 0 and l2 == 0:
            return Alignment()
        elif l2 == 0:
            result = self.get_best_score(dna1[1:], dna2)
            result.add_match(dna1[0], "-")
            return result
        elif l1 == 0:
            result = self.get_best_score(dna1, dna2[1:])
            result.add_match("-", dna2[0])
            return result
        else:
            first = self.get_best_score(dna1[1:], dna2)
            first.add_match(dna1[0], "-")
            second = self.get_best_score(dna1, dna2[1:])
            second.add_match("-", dna2[0])
            both = self.get_best_score(dna1[1:], dna2[1:])
            both.add_match(dna1[0], dna2[0])
            if first.count_score() >= second.count_score() and first.count_score() >= both.count_score():
                return first
            elif second.count_score() >= both.count_score() and second.count_score() >= both.count_score():
                return second
            else:
                return both


class Alignment:
    def __init__(self):
        self.dna1 = ""
        self.dna2 = ""

    def __str__(self):
        return self.dna1 + "\n" + self.dna2

    def __repr__(self):
        return self.dna1 + "\n" + self.dna2

    def count_score(self):
        curr_score = 0
        l1 = len(self.dna1)
        for i in range(l1):
            if self.dna1[i] == self.dna2[i]:
                curr_score += 2
            elif self.dna1[i] == "_" or self.dna2[i] == "_":
                curr_score -= 2
            else:
                curr_score -= 1
        return curr_score

    def add_match(self, first_nucleotide, second_nucleotide):
        self.dna1 = first_nucleotide + self.dna1
        self.dna2 = second_nucleotide + self.dna2


#x = DNAAlignment("GGCC", "TCC")
#x.count_score()
#print(x)
