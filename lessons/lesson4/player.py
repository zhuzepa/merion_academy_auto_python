class Player:
    def __init__(self, nick):
        self.nickname = nick
        self.xp = 0

    def upgrade(self, xp_to_add=1):
        old_val = self.xp
        new_val = old_val + xp_to_add
        self.xp = new_val
        # self.xp += xp_to_add

    def get_info(self):
        expirience = str(self.xp)
        string = self.nickname + "(" + expirience + "xp)"
        return string
        # return self.nickname + "("+ str(self.xp) +"xp)"
