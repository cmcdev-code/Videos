from manim import *

class GeneratingFunction(Scene):
    def construct(self):

        txt=Text("What is recursion?",slant=ITALIC).scale(2)

        self.play(FadeIn(txt))

        self.wait(2)

        self.remove(txt)
        
        txt=Text("Recursion occurs when the definition of a concept or process"+"\n"+ "depends on a simpler version of itself.".center(len("    Recursion occurs when the definition of a concept or process"))).scale(.6)


        self.play(FadeIn(txt))

        self.wait(2)

        self.remove(txt)

        txt=Text("Suppose we had a staircase of length n and we"+"\n"+"can either travel 1 or 2 steps at a time.").scale(0.8)
        self.play(FadeIn(txt))

        self.wait(2)

        self.remove(txt)
        txt=Text("How many distinct ways can we reach the top?").scale(0.8)
        self.play(FadeIn(txt))

        self.wait(2)

        self.remove(txt)

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

        self.play(first_group.animate.scale(0.3).set_x(first_group.get_x()-9.1).set_y(first_group.get_y()-9.4), run_time=5)

       
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
        self.wait(1)

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

        self.remove(copy_group_3,text,group_5)
        # Define the generating function equation
        rr = MathTex("b_{n+2}=b_{n+1}+b_n, b_1:=1 b_2:=2")
        
        self.play(Create(rr))

        rr_1=MathTex("a_{n+2}=a_{n+1}+a_n, a_0:=1 a_1:=2")


        self.wait(3)


        self.play(Transform(rr,rr_1))



        generating_function=MathTex("G(x)= \\sum_{n\\geq 0}a_nx^n")

        self.play(Transform(rr,generating_function),run_time=1.0)

        self.wait(2)

        self.play(Transform(rr,rr_1))

        self.wait(3)

        rr_1_x=MathTex("a_{n+2}  x^{n+2} =a_{n+1} x^{n+2}+a_n  x^{n+2}")

        self.play(Transform(rr,rr_1_x))
        self.wait(3)

        rr_s=MathTex("\\sum_{n \\geq 0} a_{n+2}  x^{n+2} =\\sum_{n \\geq 0}a_{n+1} x^{n+2}+\\sum_{n \\geq 0}a_n  x^{n+2}")
        self.play(Transform(rr,rr_s))

        self.wait(3)

        rr_left=MathTex("\\sum_{n \\geq 0} a_{n+2}  x^{n+2}")
        self.play(Transform(rr,rr_left))
        
        self.wait(3)

        rr_l_s=MathTex("G(x)=a_0x^0+a_1x^1+...+a_nx^n+...")

        self.play(Transform(rr,rr_l_s))

        self.wait(3)

        rr___1=MathTex("\\sum_{n\\geq0}a_{n+2}x^{n+2} = a_2x^2+a_3x^3+...+a_nx^n+...")
        self.play(Transform(rr,rr___1))

        self.wait(2)

        rr_1_2=MathTex("\\sum_{n \\geq 0} a_{n+2}  x^{n+2} =G(x) -a_0 - a_1  x")
        self.play(Transform(rr,rr_1_2))
        
        self.wait(2)
        rr_1_2_2=MathTex("G(x) -a_0 - a_1  x^1= G(x)- 1 -2x")

        self.play(Transform(rr,rr_1_2_2))
        self.wait(2)

        rr_21=MathTex("G(x) -1 - 2  x =\\sum_{n \\geq 0}a_{n+1} x^{n+2}+\\sum_{n \\geq 0}a_n  x^{n+2}")

        self.play(Transform(rr,rr_21))
        self.wait(2)

        rr_21=MathTex("\\sum_{n\\geq0} a_{n+1} x^{n+2}= x\\sum_{n\\geq0} a_{n+1} x^{n+1}")

        self.play(Transform(rr,rr_21))

        self.wait(2)
        rr_21=MathTex("\\sum_{n \\geq 0} a_{n+1}x^{n+1}")

        
        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("\\sum_{n\\geq 0 }a_{n+1}x^{n+1} = a_1x^1 + a_2x^2+...+a_nx^n+...")

        
        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("a_0x^0 +a_1x^1+...+a_nx^n+...")

        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex(" \\sum_{n\\geq 0 }a_{n+1}x^{n+1}= G(x) - a_0x^0")

        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("\\sum_{n\\geq 0 }a_{n+1}x^{n+1}= G(x) - 1")
        self.play(Transform(rr,rr_21))

        self.wait(2)
        
        rr_21=MathTex("\\sum_{n\\geq0} a_{n+1} x^{n+2}= x\\sum_{n\\geq0} a_{n+1} x^{n+1}")
        self.play(Transform(rr,rr_21))

        self.wait(2)
        
        rr_21=MathTex("\\sum_{n\\geq0} a_{n+1} x^{n+2}= x(G(x)-1)")
        self.play(Transform(rr,rr_21))

        self.wait(2)
        
        rr_21=MathTex("G(x) -1 - 2  x =\\sum_{n \\geq 0}a_{n+1} x^{n+2}+\\sum_{n \\geq 0}a_n  x^{n+2}")

        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("G(x) -1 - 2  x =x(G(x)-1)+\\sum_{n \\geq 0}a_n  x^{n+2}")        

        self.play(Transform(rr,rr_21))

        self.wait(2)
        
        rr_21=MathTex("\\sum_{n \\geq 0}a_n  x^{n+2}=x^2\\sum_{n \\geq 0}a_n  x^{n}")

        self.play(Transform(rr,rr_21))

        self.wait(2)
        
        rr_21=MathTex("\\sum_{n \\geq 0} a_n  x^n = G(x)")

        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("\\sum_{n \\geq 0}a_n  x^{n+2}=x^2\\sum_{n \\geq 0}a_n  x^{n}")
        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("\\sum_{n \\geq 0}a_n  x^{n+2}=x^2G(x)")

        self.play(Transform(rr,rr_21))

        self.wait(2)


        rr_21=MathTex("G(x) -1 - 2  x =x(G(x)-1)+\\sum_{n \\geq 0}a_n  x^{n+2}")

        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("G(x) -1 - 2  x =x(G(x)-1)+x^2\\sum_{n \\geq 0}a_n  x^{n}")

        
        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("G(x) -1 - 2  x =x(G(x)-1)+x^2G(x)")
        self.play(Transform(rr,rr_21))

        self.wait(2)
        rr_21=MathTex("G(x) -1 - 2  x =x G(x) -x+x^2  G(x)")
        self.play(Transform(rr,rr_21))

        self.wait(2)
        rr_21=MathTex("G(x)-x G(x) -x^2  G(x)=-x +1 +2  x")

        self.play(Transform(rr,rr_21))

        self.wait(2)        


        rr_21=MathTex("G(x)-xG(x) -x^2G(x)=1 +x")

        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("G(x)(1-x -x^2)=1 +x")

        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("G(x)=\\frac{1 +x}{1-x -x^2}") 
        self.play(Transform(rr,rr_21))

        self.wait(2)
        
        rr_21=MathTex("G(x)=\\frac{1}{1-x -x^2} +\\frac{x}{1-x -x^2}")
        self.play(Transform(rr,rr_21))

        self.wait(2)

  
        rr_21=MathTex("G(x)=\\frac{1}{1-x -x^2} +\\frac{x}{1-x -x^2}")
        self.play(Transform(rr,rr_21))

        self.wait(2)


        rr_21=MathTex("\\frac{1}{1-x -x^2} = \\frac{1}{(x+\\frac{1+\\sqrt{5}}{2})(-x +\\frac{-1+\\sqrt{5}}{2} )}").scale(0.6)
        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("\\frac{1}{(x+\\frac{1+\\sqrt{5}}{2})(-x +\\frac{-1+\\sqrt{5}}{2} )}= \\frac{A}{x+\\frac{1+\\sqrt{5}}{2}}+ \\frac{B}{-x +\\frac{-1+\\sqrt{5}}{2}}").scale(0.6)
        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("1 = A(-x +\\frac{-1 + \\sqrt{5}}{2}) + B(x+ \\frac{1 + \\sqrt{5}}{2})")
        self.play(Transform(rr,rr_21))

        self.wait(2)


        rr_21=MathTex("1 = A(-\\frac{-1 + \\sqrt{5}}{2} +\\frac{-1 + \\sqrt{5}}{2}) + B(\\frac{-1 + \\sqrt{5}}{2}+ \\frac{1 + \\sqrt{5}}{2})").scale(0.6)
        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex(" 1 = A\\cdot0 + B(\\frac{-1 + \\sqrt{5}}{2}+ \\frac{1 + \\sqrt{5}}{2})")

        self.play(Transform(rr,rr_21))

        self.wait(2)
        rr_21=MathTex(" 1 = B(\\frac{-1 + \\sqrt{5}}{2}+ \\frac{1 + \\sqrt{5}}{2})")

        self.play(Transform(rr,rr_21))

        self.wait(2)

        rr_21=MathTex("1 = B\\sqrt{5} ")
        self.play(Transform(rr,rr_21))

        self.wait(2)
       
        rr_21=MathTex("B= \\frac{1}{\\sqrt{5}}")
        self.play(Transform(rr,rr_21))

        self.wait(2)
        rr_21=MathTex(" 1 = A(-x +\\frac{-1 + \\sqrt{5}}{2}) + \\frac{1}{\\sqrt{5}}(x+ \\frac{1 + \\sqrt{5}}{2})")
        self.play(Transform(rr,rr_21))

        self.wait(2)  

        rr_21=MathTex("1 = A(-\\frac{1 + \\sqrt{5}}{2} +\\frac{-1 + \\sqrt{5}}{2}) + \\frac{1}{\\sqrt{5}}(-\\frac{1 + \\sqrt{5}}{2}+ \\frac{1 + \\sqrt{5}}{2})").scale(0.6)
        self.play(Transform(rr,rr_21))

        self.wait(2)  
        rr_21=MathTex("1 = A(-\\frac{1 + \\sqrt{5}}{2} +\\frac{-1 + \\sqrt{5}}{2}) + \\frac{1}{\\sqrt{5}}\\cdot 0")
        self.play(Transform(rr,rr_21))

        self.wait(2)  
        rr_21=MathTex("1 = A(\\frac{1 + \\sqrt{5}}{2} +\\frac{-1 + \\sqrt{5}}{2})")
        self.play(Transform(rr,rr_21))

        self.wait(2)  
        rr_21=MathTex("1= A \\sqrt{5}")
        
        self.play(Transform(rr,rr_21))

        self.wait(2)
        rr_21=MathTex("A= \\frac{1}{\\sqrt{5}}")

        self.play(Transform(rr,rr_21))
        
        self.wait(2)
        rr_21=MathTex("\\frac{1}{(x+\\frac{1+\\sqrt{5}}{2})(-x +\\frac{-1+\\sqrt{5}}{2} )}=  \\frac{1}{\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{1}{\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})}").scale(0.6)
        self.play(Transform(rr,rr_21))
        
        self.wait(2)
        rr_21=MathTex("G(x)= \\frac{1}{(x+\\frac{1+\\sqrt{5}}{2})(-x +\\frac{-1+\\sqrt{5}}{2} )} +\\frac{x}{1-x -x^2}")


        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("G(x)= \\frac{1}{\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{1}{\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})} +\\frac{x}{1-x -x^2}")

        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("\\frac{x}{1-x -x^2}")

        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("\\frac{x}{(x+\\frac{1+\\sqrt{5}}{2})(-x +\\frac{-1+\\sqrt{5}}{2} )}= \\frac{A}{x+\\frac{1+\\sqrt{5}}{2}}+ \\frac{B}{-x +\\frac{-1+\\sqrt{5}}{2}}").scale(0.6)

        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("x= A(-x+\\frac{-1+\\sqrt{5}}{2}) +B(x+\\frac{1+\\sqrt{5}}{2})")

        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("\\frac{-1+\\sqrt{5}}{2}= A(-\\frac{-1+\\sqrt{5}}{2}+\\frac{-1+\\sqrt{5}}{2}) +B(\\frac{-1+\\sqrt{5}}{2}+\\frac{1+\\sqrt{5}}{2})").scale(0.5)

        
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("\\frac{-1+\\sqrt{5}}{2}= A\\cdot0 +B(\\frac{-1+\\sqrt{5}}{2}+\\frac{1+\\sqrt{5}}{2})")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("\\frac{-1+\\sqrt{5}}{2}=B(\\frac{-1+\\sqrt{5}}{2}+\\frac{1+\\sqrt{5}}{2})")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("\\frac{-1+\\sqrt{5}}{2}=B\\sqrt{5}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("B=\\frac{-1+\\sqrt{5}}{2\\sqrt{5}}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("-\\frac{1+\\sqrt{5}}{2}= A(\\frac{1+\\sqrt{5}}{2}+\\frac{-1+\\sqrt{5}}{2}) +\\frac{-1+\\sqrt{5}}{2\\sqrt{5}}(-\\frac{1+\\sqrt{5}}{2}+\\frac{1+\\sqrt{5}}{2})").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("-\\frac{1+\\sqrt{5}}{2}= A(\\frac{1+\\sqrt{5}}{2}+\\frac{-1+\\sqrt{5}}{2}) +\\frac{-1+\\sqrt{5}}{2\\sqrt{5}}\\cdot0").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("\\frac{-1-\\sqrt{5}}{2}= A(\\frac{1+\\sqrt{5}}{2}+\\frac{-1+\\sqrt{5}}{2})")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("-\\frac{-1-\\sqrt{5}}{2}= A \\sqrt{5}")
                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("A=\\frac{-1-\\sqrt{5}}{2\\sqrt{5}}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("\\frac{x}{(x+\\frac{1+\\sqrt{5}}{2})(-x +\\frac{-1+\\sqrt{5}}{2} )}= \\frac{-1-\\sqrt{5}}{2\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{-1+\\sqrt{5}}{2\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})}").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("G(x)= \\frac{1}{\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{1}{\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})} +\\frac{x}{1-x -x^2}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("G(x)= \\frac{1}{\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{1}{\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})} +\\frac{-1-\\sqrt{5}}{2\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{-1+\\sqrt{5}}{2\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})}").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("G(x)= \\frac{1}{\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{1}{\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})} + \\frac{-1-\\sqrt{5}}{2\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{-1+\\sqrt{5}}{2\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})}").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("G(x)= \\frac{2}{2\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{2}{2\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})} + \\frac{-1-\\sqrt{5}}{2\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{-1+\\sqrt{5}}{2\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})}").scale(0.6)
                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("G(x)= \\frac{1-\\sqrt{5}}{2\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{1+\\sqrt{5}}{2\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)



        rr_21=MathTex("C \\frac{1}{1-a}= C\\sum_{n\\geq 0}a^n")
                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


  
        rr_21=MathTex("G(x)= \\frac{1-\\sqrt{5}}{2\\sqrt{5}(x+\\frac{1+\\sqrt{5}}{2})}+ \\frac{1+\\sqrt{5}}{2\\sqrt{5}(-x +\\frac{-1+\\sqrt{5}}{2})}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("G(x)= \\frac{1-\\sqrt{5}}{2\\sqrt{5}(\\frac{x}{\\frac{1+\\sqrt{5}}{2}}+1)\\cdot \\frac{1+\\sqrt{5}}{2}}+ \\frac{1+\\sqrt{5}}{2\\sqrt{5}(\\frac{-x}{\\frac{-1+\\sqrt{5}}{2}} +1)\\cdot \\frac{-1+\\sqrt{5}}{2}}").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("G(x)= \\frac{1-\\sqrt{5}}{\\sqrt{5}(1+\\sqrt{5})(1- \\frac{-2x}{1+\\sqrt{5}})}+ \\frac{1+\\sqrt{5}}{\\sqrt{5}(-1+\\sqrt{5})(1 - \\frac{2x}{-1+\\sqrt{5}})}")
                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("G(x)= \\frac{1-\\sqrt{5}}{\\sqrt{5}(1+\\sqrt{5})} \\sum_{n \\geq 0} (\\frac{-2}{1+\\sqrt{5}})^nx^n+ \\frac{1+\\sqrt{5}}{\\sqrt{5}(-1+\\sqrt{5})}\\sum_{n \\geq 0} (\\frac{2}{-1+\\sqrt{5}})^n x^n").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("G(x)= \\sum_{n \\geq 0} (\\frac{1-\\sqrt{5}}{\\sqrt{5}(1+\\sqrt{5})}(\\frac{-2}{1+\\sqrt{5}})^n+ \\frac{1+\\sqrt{5}}{\\sqrt{5}(-1+\\sqrt{5})} (\\frac{2}{-1+\\sqrt{5}})^n) x^n").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("\\sum_{n \\geq 0}a_nx^n= \\sum_{n \\geq 0}( \\frac{1-\\sqrt{5}}{\\sqrt{5}(1+\\sqrt{5})}(\\frac{-2}{1+\\sqrt{5}})^n+ \\frac{1+\\sqrt{5}}{\\sqrt{5}(-1+\\sqrt{5})} (\\frac{2}{-1+\\sqrt{5}})^n) x^n").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("a_n= \\frac{1-\\sqrt{5}}{\\sqrt{5}(1+\\sqrt{5})}(\\frac{-2}{1+\\sqrt{5}})^n+ \\frac{1+\\sqrt{5}}{\\sqrt{5}(-1+\\sqrt{5})} (\\frac{2}{-1+\\sqrt{5}})^n")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("b_n=a_{n-1}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)


        rr_21=MathTex("b_n= \\frac{1-\\sqrt{5}}{\\sqrt{5}(1+\\sqrt{5})}(\\frac{-2}{1+\\sqrt{5}})^{n-1}+ \\frac{1+\\sqrt{5}}{\\sqrt{5}(-1+\\sqrt{5})} (\\frac{2}{-1+\\sqrt{5}})^{n-1}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("b_n= \\frac{1-\\sqrt{5}}{\\sqrt{5}(1+\\sqrt{5})}(\\frac{-2}{1+\\sqrt{5}})^{n}\\cdot \\frac{1+\\sqrt{5}}{2}+ \\frac{1+\\sqrt{5}}{\\sqrt{5}(-1+\\sqrt{5})} (\\frac{2}{-1+\\sqrt{5}})^{n}\\cdot \\frac{-1+\\sqrt{5}}{2}").scale(0.6)

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("b_n= \\frac{1-\\sqrt{5}}{-2\\sqrt{5}}(\\frac{-2}{1+\\sqrt{5}})^{n}+ \\frac{1+\\sqrt{5}}{2\\sqrt{5}} (\\frac{2}{-1+\\sqrt{5}})^{n}")

                
        self.play(Transform(rr,rr_21))
        
        self.wait(2)

        rr_21=MathTex("b_n= \\frac{1-\\sqrt{5}}{-2\\sqrt{5}}(\\frac{1-\\sqrt{5}}{2})^{n}+ \\frac{1+\\sqrt{5}}{2\\sqrt{5}} (\\frac{1+\\sqrt{5}}{2})^{n}")
        self.wait(3)



    




