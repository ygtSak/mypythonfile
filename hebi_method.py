class Square:
    sqr_list = []
    
    def __init__(self, l):
        self.length = l
        i = 0
        while i < 4:
            self.sqr_list.append(self.length)
            i+=1
            
        print("Created!")


s1 = Square(25)
print("{}by{}by{}by{}".format(Square.sqr_list[0],
                              Square.sqr_list[1],
                              Square.sqr_list[2],
                              Square.sqr_list[3],))
