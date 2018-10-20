import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("beige")

    side = turtle.Turtle()
    #side.setposition(0,200)
    side.width(3)
    side.color("blue")
    side.fillcolor("red")
    side.speed(9)
    side.shape("arrow")
    
    side.right(60)
    
    def trian():
        side.begin_fill()
        c= 0
        while c<3:
            side.right(120)
            side.forward(60)
            c+=1
        side.end_fill()
    
    def trian3():
        c3 = 0
        while c3 <3:
            side.right(120)
            side.forward(120)
            trian()
            c3 += 1
    
    c3d = 0
    while c3d < 3:
        side.forward(120)
        trian3()
        c3d+=1     
    
    def trianTotal():
            side.right(120)
            side.forward(120)
            c3h = 0
            while c3h < 3:
                side.forward(120)
                trian3()
                c3h+=1
        
    ct = 0
    while ct <= 2:
        trianTotal()
    ct += 1
      
            
        # side.right(120)
        # side.forward(40)

        # c3h = 0
        # while c3h < 3:
        #     side.forward(40)
        #     trian3()
        #     c3h+=1
            
        
    
    # angle = 0
    # while angle<360:
    #     c=0
    #     while c<8:
    #         side.forward(150)
    #         side.right(45)
    #         c+=1
    #     side.right(5)
    #     angle+=5
    # # c=0
    # while c<8:
    #     side.circle(50)
    #     side.forward(150)
    #     side.right(45)
    #     c+=1
    # side.right(135*0.5)
    # side.forward(150)
    
    # trian = turtle.Turtle()
    # trian.width(3)
    # trian.right(135*.5)
    # trian.forward(150)
    # trian.left(135*.5)
    # trian.color("red")
    # trian.shape("triangle")
    # t=0
    # while t<3:
    #     trian.forward(80)
    #     trian.right(120)
    #     t += 1
    window.exitonclick()

draw()