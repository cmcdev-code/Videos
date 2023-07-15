
from manim import *
class SquareAndCircle(Scene):
    def construct(self):

        length=5
        squares=[]

        squares.append(Square())

        
        squares[0].set_fill(BLUE,0.1)
        squares[0].width=1
        self.play(Write(squares[0]),run_time=0.6)
        for i in range(1,length+15):
            local_square=Square()
            local_square.width=1
            squares.append(local_square)
            squares[i].set_fill(BLUE,0.1)
            squares[i].set_x(squares[i-1].get_x()+squares[i-1].width)
            squares[i].set_y(squares[i-1].get_y()+squares[i-1].width)
            if(i<=5):
                self.play(Write(squares[i]),run_time=0.5/(i*0.6))
            else:
                self.play(Write(squares[i]),run_time=0.001)
        
        first_group=VGroup(* squares[:length+15])

        self.play(first_group.animate.scale(0.3).set_x(first_group.get_x()-10).set_y(first_group.get_y()-9.4), run_time=5)

       
        length=1  
        squares=[]
        squares.append(Square())

        squares[0].set_fill(BLUE,0.1)
        squares[0].width=1
        self.play(ReplacementTransform(first_group,squares[0]),run_time=0.6)
        for i in range(1,length):
            local_square=Square()
            local_square.width=1
            squares.append(local_square)
            squares[i].set_fill(BLUE,0.1)
            squares[i].set_x(squares[i-1].get_x()+squares[i-1].width)
            squares[i].set_y(squares[i-1].get_y()+squares[i-1].width)
       
            self.play(Create(squares[i]),run_time=0.5)
        self.wait(1)
        self.play(squares[0].animate.set_fill(RED,0.2),run_time=0.6)
        text= Text('1').scale(1)
        text.next_to(squares[0],DOWN)
        self.play(Create(text),run_time=0.6)
        

        for i in range(length):
            self.remove(text) 
          # show the shapes on screen

        
        group__=VGroup(* squares[:1])

        length=2  
        squares=[]
        squares.append(Square())

        squares[0].set_fill(BLUE,0.1)
        squares[0].width=1
        
        for i in range(1,length):
            local_square=Square()
            local_square.width=1
            squares.append(local_square)
            squares[i].set_fill(BLUE,0.1)
            squares[i].set_x(squares[i-1].get_x()+squares[i-1].width)
            squares[i].set_y(squares[i-1].get_y()+squares[i-1].width)
       
        group___=VGroup(* squares[:length])
        self.play(ReplacementTransform(group__,group___))    
        self.wait(1)
        self.play(squares[0].animate.set_fill(RED,0.2),squares[1].animate.set_fill(RED,0.2),run_time=0.6)
        
        text= Text('1').scale(1)
        text.next_to(squares[0],DOWN)
        self.play(Create(text),run_time=0.6)
        
        self.wait(2)
        self.play(squares[0].animate.set_fill(BLUE,0.1),squares[1].animate.set_fill(BLUE,0.1),run_time=0.6)
        self.wait(1)

        self.play(squares[0].animate.set_fill(YELLOW,0.2),squares[1].animate.set_fill(YELLOW,0.2),run_time=0.6)
        

        

        text2=Text('2').scale(1)
        text2.next_to(squares[0],DOWN)
        self.play(ReplacementTransform(text,text2),run_time=0.6)

        self.wait(1.2)
        for i in range(length):
            self.remove(text) 
            self.remove(text2)

        length=3  
        squares=[]
        squares.append(Square())

        squares[0].set_fill(BLUE,0.1)
        squares[0].width=1
       
        for i in range(1,length):
            local_square=Square()
            local_square.width=1
            squares.append(local_square)
            squares[i].set_fill(BLUE,0.1)
            squares[i].set_x(squares[i-1].get_x()+squares[i-1].width)
            squares[i].set_y(squares[i-1].get_y()+squares[i-1].width)
       
        
        group____=VGroup(* squares[:length])

        self.play(ReplacementTransform(group___,group____))
        

        self.play(squares[0].animate.set_fill(RED,0.2),run_time=0.6)
        
        self.wait(1)

        self.play(squares[1].animate.set_fill(RED,0.2),squares[2].animate.set_fill(RED,0.2),run_time=0.6)
    

        text=[]
        text.append(Text('1').scale(1))
        text[0].next_to(squares[0],DOWN)
        self.play(Create(text[0]),run_time=0.6)

        self.wait(2)

        self.play(squares[1].animate.set_fill(BLUE,0.1),squares[2].animate.set_fill(BLUE,0.1),run_time=0.6)
    

        self.wait(1)

        self.play(squares[1].animate.set_fill(YELLOW,0.2),squares[2].animate.set_fill(YELLOW,0.2),run_time=0.6)
        

        text.append(Text('2').scale(1))
        text[1].next_to(squares[0],DOWN)
        self.play(ReplacementTransform(text[0],text[1]),run_time=0.6)

        self.wait(2)

        self.play(squares[0].animate.set_fill(BLUE,0.1),squares[2].animate.set_fill(BLUE,0.1),squares[1].animate.set_fill(BLUE,0.1),run_time=0.6)
       
   

        self.wait(1)

        self.play(squares[0].animate.set_fill(YELLOW,0.2),squares[1].animate.set_fill(YELLOW,0.2),run_time=0.6)
    
        self.wait(1)
        self.play(squares[2].animate.set_fill(RED,0.2),run_time=0.6)



        text.append(Text('3').scale(1))
        text[2].next_to(squares[0],DOWN)
        self.play(ReplacementTransform(text[1],text[2]),run_time=0.6)

        
        for i in range(3):
            self.remove(text[i])

        group_3_blue=VGroup(*squares[:3])

        for i in range(3):
            group_3_blue[i]=group_3_blue[i].set_fill(BLUE,0.1)

######################## now will break up 
        length=4  
        squares=[]
        squares.append(Square())

        squares[0].set_fill(BLUE,0.1)
        squares[0].width=1
        
        for i in range(1,length):
            local_square=Square()
            local_square.width=1
            squares.append(local_square)
            squares[i].set_fill(BLUE,0.1)
            squares[i].set_x(squares[i-1].get_x()+squares[i-1].width)
            squares[i].set_y(squares[i-1].get_y()+squares[i-1].width)
       
        
        group_____=VGroup(*squares[:length])

        self.play(ReplacementTransform(group____,group_____))

        
        self.play(squares[0].animate.set_fill(RED,0.2),run_time=0.6)

        self.play(squares[0].animate.set_x(squares[0].get_x()-4),squares[1].animate.set_x(squares[1].get_x()-4),squares[2].animate.set_x(squares[2].get_x()-4),squares[3].animate.set_x(squares[3].get_x()-4),run_time=0.9)
        self.play(squares[0].animate.set_y(squares[0].get_y()-1),squares[3].animate.set_y(squares[3].get_y()-1),squares[2].animate.set_y(squares[2].get_y()-1),squares[1].animate.set_y(squares[1].get_y()-1),run_time=0.8)
        
       
        #self.play(squares[])
        text=Text('→').scale(3)


        self.play(Create(text),run_time=0.4)

        
            

        group_12132= group___.copy()

        group_12132.set_x(3)
        group_12132.scale(1)
        group_12132.set_y(-.2)

        self.play(Create(group_12132))

        group_3_copy_copy=group_12132.copy()
        length_2=3
        squares1=[]
        squares1.append(Square())
        squares1[0].width=0.6
        squares1[0].set_x(2)
        squares1[0].set_y(2.1)
        squares1[0].set_fill(RED,0.2)
        
        squares1.append(Square())
        squares1[1].width=0.6
        squares1[1].set_x(squares1[0].get_x()+squares1[0].width)
        squares1[1].set_y(squares1[0].get_y()+squares1[0].width)
        squares1[1].set_fill(RED,0.2)
       
        squares1.append(Square())
        squares1[2].width=0.6
        squares1[2].set_x(squares1[1].get_x()+squares1[1].width)
        squares1[2].set_y(squares1[1].get_y()+squares1[1].width)
        squares1[2].set_fill(RED,0.2)
       

       



        squares2=[]
        squares2.append(Square())
        squares2[0].width=0.6
        squares2[0].set_x(2)
        squares2[0].set_y(-0.2)
        squares2[0].set_fill(RED,0.2)
       
        squares2.append(Square())
        squares2[1].width=0.6
        squares2[1].set_x(squares2[0].get_x()+squares2[0].width)
        squares2[1].set_y(squares2[0].get_y()+squares2[0].width)
        squares2[1].set_fill(YELLOW,0.2)
        
        squares2.append(Square())
        squares2[2].width=0.6
        squares2[2].set_x(squares2[1].get_x()+squares2[1].width)
        squares2[2].set_y(squares2[1].get_y()+squares2[1].width)
        squares2[2].set_fill(YELLOW,0.2)
        


        squares3=[]
        squares3.append(Square())
        squares3[0].width=0.6
        squares3[0].set_x(2)
        squares3[0].set_y(-2.5)
        squares3[0].set_fill(YELLOW,0.2)
       
        squares3.append(Square())
        squares3[1].width=0.6
        squares3[1].set_x(squares3[0].get_x()+squares3[0].width)
        squares3[1].set_y(squares3[0].get_y()+squares3[0].width)
        squares3[1].set_fill(YELLOW,0.2)
        
        squares3.append(Square())
        squares3[2].width=0.6
        squares3[2].set_x(squares3[1].get_x()+squares3[1].width)
        squares3[2].set_y(squares3[1].get_y()+squares3[1].width)
        squares3[2].set_fill(RED,0.2)
               

 
        


        group_3=VGroup(squares1[0],squares1[1],squares1[2],squares2[0],squares2[1],squares2[2],squares3[0],squares3[1],squares3[2])
        group_3_copy= group_3.copy()


        self.play(ReplacementTransform(group_12132,group_3_copy),run_time=0.8)
        self.wait(2.3)
       
        self.play(squares[0].animate.set_fill(YELLOW,0.2),squares[1].animate.set_fill(YELLOW,0.2),run_time=0.3)

     
        squares21=[]

        squares21.append(Square())
        squares21[0].width=0.6
        squares21[0].set_x(2)
        squares21[0].set_y(1.2)
        squares21[0].set_fill(RED,0.2)
        
        squares21.append(Square())
        squares21[1].width=0.6
        squares21[1].set_x(squares21[0].get_x()+squares21[0].width)
        squares21[1].set_y(squares21[0].get_y()+squares21[0].width)
        squares21[1].set_fill(RED,0.2)
        

        squares22=[]

        squares22.append(Square())
        squares22[0].width=0.6
        squares22[0].set_x(2)
        squares22[0].set_y(-1.2)
        squares22[0].set_fill(YELLOW,0.2)
       
        squares22.append(Square())
        squares22[1].width=0.6
        squares22[1].set_x(squares22[0].get_x()+squares22[0].width)
        squares22[1].set_y(squares22[0].get_y()+squares22[0].width)
        squares22[1].set_fill(YELLOW,0.2)
       


        group_2=VGroup(squares21[0],squares21[1],squares22[0],squares22[1])
        self.wait(1)

        group_2_copy=group_2.copy()

        self.play(ReplacementTransform(group_3_copy,group_2_copy))

        self.wait(3)
        group_4=VGroup(squares[0],squares[1],squares[2],squares[3])

       
        group_4[0]=group_4[0].set_fill(BLUE,0.1)
        group_4[1]=group_4[1].set_fill(BLUE,0.1)

        group_4_copy=group_4.copy() 
        
      


        length=5  
        squares=[]
        squares.append(Square())

        squares[0].set_fill(BLUE,0.1)
        squares[0].width=1
        
        for i in range(1,length):
            local_square=Square()
            local_square.width=1
            squares.append(local_square)
            squares[i].set_fill(BLUE,0.1)
            squares[i].set_x(squares[i-1].get_x()+squares[i-1].width)
            squares[i].set_y(squares[i-1].get_y()+squares[i-1].width)
       
            
        
        group_5=VGroup(*squares[:5])

      

        
        group_5=group_5.scale(0.6).set_x(squares[0].get_x()-3).set_y(squares[0].get_y()-.3)
       
     
        self.play(ReplacementTransform(group_4,group_5))       

        self.play(group_5[0].animate.set_fill(RED,0.2))
        self.play(ReplacementTransform(group_2_copy,group_4_copy.set_x(3).scale(0.6).set_y(-0.1)))
        
        self.wait(3)

        

        group_3=group_3.set_x(3).scale(0.6)

        copy_group_3=group_3.copy()

        group_2=group_2.set_x(5).scale(0.6).set_y(group_3.get_y())




        big_group=VGroup(group_3,group_2)

       
        
        self.play(ReplacementTransform(group_4_copy,big_group))

      
        self.wait(3)

       
      
        
        self.play(group_5[0].animate.set_fill(YELLOW,0.2),group_5[1].animate.set_fill(YELLOW,0.2),run_time=0.4)


        group_3_copy_copy.scale(.6)
        self.play(ReplacementTransform(big_group,group_3_copy_copy))
       
        
     

        self.wait(2)
        
        self.play(ReplacementTransform(group_3_copy_copy,copy_group_3))
        self.wait(2)
