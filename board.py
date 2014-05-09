init_val = "*"

def check_input(player):
    while True:
        hey_you = raw_input(player +"'s move")
        try:
            int(hey_you)
            return int(hey_you)
            break
        except ValueError:
            continue

class board:
    def __init__(self,ul = init_val, um= init_val, ur=init_val, ml= init_val, mm = init_val, mr = init_val,bl = init_val, bm = init_val, br = init_val):
        self.ul = ul
        self.um=um
        self.ur=ur
        self.ml=ml
        self.mm=mm
        self.mr=mr
        self.bl=bl
        self.bm=bm
        self.br=br
    def display(self):
        print str(self.ul) + " " +str(self.um)+" " +str(self.ur)
        print str(self.ml) + " " +str(self.mm)+" " +str(self.mr)
        print str(self.bl) + " " +str(self.bm)+" " +str(self.br)
    def make_move(self, player):
        cell = check_input(player)
        if cell == 1:
            if self.ul == init_val:
                self.ul = player
        if cell ==2:
            if self.um == init_val:
                self.um = player
        if cell ==3:
            if self.ur == init_val:
                self.ur = player
        if cell ==4:
            if self.ml == init_val:
                self.ml = player
        if cell ==5:
            if self.mm == init_val:
                self.mm = player
        if cell ==6:
            if self.mr == init_val:
                self.mr = player
        if cell ==7:
            if self.bl == init_val:
                self.bl = player
        if cell ==8:
            if self.bm == init_val:
                self.bm = player
        if cell ==9:
            if self.br == init_val:
                self.br = player
    def win_test(self):
        def connection_test(self):
            if self.ul==self.um and self.ul==self.ur:
                if self.ul == "x":
                    return "xwins"
                if self.ul == "o":
                    return "owins"
            elif self.ml==self.mm and self.mm==self.mr:
                if self.ml == "x":
                    return "xwins"
                if self.ml == "o":
                    return "owins"
            elif self.bl==self.bm and self.bm==self.br:
                if self.bl == "x":
                    return "xwins"
                if self.bl == "o":
                    return "owins"
            elif self.ul==self.ml and self.ml==self.bl:
                if self.bl == "x":
                    return "xwins"
                if self.bl == "o":
                    return "owins"
            elif self.um==self.mm and self.mm==self.bm:
                if self.bm == "x":
                    return "xwins"
                if self.bm == "o":
                    return "owins"
            elif self.ur==self.mr and self.br==self.mr:
                if self.br == "x":
                    return "xwins"
                if self.br == "o":
                    return "owins"
            elif self.ul==self.mm and self.mm==self.br:
                if self.mm == "x":
                    return "xwins"
                if self.mm == "o":
                    return "owins"
            elif self.bl==self.mm and self.mm==self.ur:
                if self.mm == "x":
                    return "xwins"
                if self.mm == "o":
                    return "owins"
            elif self.bl!=init_val and self.ml!=init_val and self.ul!=init_val and self.bm!=init_val and self.mm!=init_val and self.um!=init_val and self.br!=init_val and self.mr!=init_val and self.ur!=init_val:
                return "tie"
            else:
                return "nowin"
        if connection_test(self) == "xwins":
            self.display()
            while True: raw_input("X WINS")
        if connection_test(self) == "owins":
            self.display()
            while True: raw_input("O WINS")
