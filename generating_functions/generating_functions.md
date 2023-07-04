# What is recursion?
You may have heard of the word recursion from your computer science textbook or mentioned by someone talking about algorithms, but what does recursion actually mean and how can it be applied to solve your problems?

Oftentimes in mathematics and in computer science seemingly hard problems can be broken down into smaller problems that each have simpler and elegant solutions. One example of this is the “climbing stairs problem”.  

    “Suppose we have a staircase of length n and we can either take 1 step or 2 steps. How many distinct ways are we able to reach the top?” 

If we break this down, a staircase with a length of 1 only allows one way to get to the top; by taking **one** step.
Furthermore, if we have a staircase of length 2 then now we have some possibilities. We can climb each step one at a time or climb 2 at the same time, which leaves us with **2** distinct ways to get to the top.

Are you seeing the pattern? If not no worries; here are the next two iterations in our problem:



(Show graphic, 3 steps = 3 ways, 4 steps = 5 ways)

_If we have a staircase of length three then we have a choice we can either take 1 singular step, or we can take 2 steps. If we took the 1 singular step then we have two final steps to climb, as was previously shown this can be done in 2 distinct ways. Now if we took the two steps then we have one final step to climb and this can be done in 1 way. The sum of both of these is the distinct number of ways to climb the staircase therefore there is a total of **3** ways._

So this tells use that if we know the number of ways two climb n-1 and n-2 steps these summed together will give us the number of ways to climb n steps.

If we were to implement this in code it would look like.

```py
def stairs(length):
    if(length==1):
        return 1
    if(length==2):
        return 2
    return stairs(length-1)+stairs(length-2) 
```
Or if i were to implement this as a sequence it would follow this equation


$$b_{n+2}=b_{n+1}+b_n, b_1:=1 b_2:=2$$

Either one of these will **always** produce the correct solution after enough iterations, however if you think about it this is quite a large waste of resources. For example if we wanted to know the number of ways to climb a staircase of length $n$ then using this approach we would have to know the number of ways to climb both staircases of length $n-1$ and $n-2$. Now again if we did not know the number of ways to climb these, we would have to know the number of ways to climb a stair case of $n-2$, $n-3$ and $n-3$,$n-4$ respectively. It should be pretty clear now on why we would want a method that is not so iterative. So this makes us ask the question. 

    "Is there a way to calculate the number of ways to climb a staircase of length n without needing to know the number of ways to calculate number of ways to climb leading up to n?" 

**Well in fact there is!** 
One of the methods to do this is through the use of **generating functions**.

## Now what is a generating function?

Simply put a generating function is way of laying out all the terms of a sequence as the coefficients of a power series.<!--https://en.wikipedia.org/wiki/Generating_function#:~:text=In%20mathematics%2C%20a%20generating%20function,generating%20function%20of%20the%20sequence.-->


 We do this by defining the generating function say $G(x)$ where
 $$G(x)= \sum_{n\geq 0}a_nx^n $$

Now what we will do is get the previous equation we have to "fit" so we can use the function G(x)
We do this by first redefining the equation $$a_{n+2}=a_{n+1}+a_n, a_0:=1 a_1:=2$$

Notice that $a_0 =1 $ and $a_1 = 2$ this will just shift the starting position of the sequence so now the nth  number in this sequence is the $n-1$ number in the other sequence.
Now what we do is multiply both sides by $x^{n+2}$.

$$a_{n+2}  x^{n+2} =a_{n+1} x^{n+2}+a_n  x^{n+2}$$

Now what we will do is sum over both sides. 


$$
\sum_{n \geq 0} a_{n+2}  x^{n+2} =\sum_{n \geq 0}a_{n+1} x^{n+2}+\sum_{n \geq 0}a_n  x^{n+2}
$$

Notice that all of these are almost in the form of how we defined $G(x)$. If we are able to successfully manipulate them then we can apply the replace it with $G(x)$.

Let us first start on the left side of the equation. With $\sum_{n \geq 0} a_{n+2}  x^{n+2} $.

If we were to write out the terms of $G(x)$ it would look like this
$$a_0x^0+a_1x^1+...+a_nx^n+... $$
<!-- add each term one by one in the animation -->

Now if we were to write out the terms of the left side of the equation it would look like 
$$\sum_{n\geq0}a_{n+2}x^{n+2} = a_2x^2+a_3x^3+...+a_nx^n+...$$

We can see that if we were to subtract the first two terms of the summation for $G(x)$ from itself then we would have the summation $\sum_{n\geq0}a_{n+2}x^{n+2}$.

$$
\sum_{n \geq 0} a_{n+2}  x^{n+2} =G(x) -a_0 - a_1  x
$$ 

Because we defined $a_0=1$ and $a_1=2$ we can substitute them.

$$G(x) -a_0 - a_1  x^1= G(x)- 1 -2x$$


Now we can replace the left side with this 

$$G(x) -1 - 2  x =\sum_{n \geq 0}a_{n+1} x^{n+2}+\sum_{n \geq 0}a_n  x^{n+2}$$

Now we start work on the right side of the equation.

We can bring down one of the x's $\sum_{n\geq0} a_{n+1} x^{n+2}= x\sum_{n\geq0} a_{n+1} x^{n+1}$


Now lets deal with just $\sum_{n \geq 0} a_{n+1}x^{n+1}$
Just like the left side of the equation if we were to write out the terms one by one of this summation it would look like. 
 $$ \sum_{n\geq 0 }a_{n+1}x^{n+1} = a_1x^1 + a_2x^2+...+a_nx^n+...$$

Again as we can see this is almost the same as $a_0x^0 +a_1x^1+...+a_nx^n+...$

All we have to do is subtract the first term $a_0x^0$

$$ \sum_{n\geq 0 }a_{n+1}x^{n+1}= G(x) - a_0x^0$$

Subbing in the value that we defined $a_0$ to be we have. 

$$ \sum_{n\geq 0 }a_{n+1}x^{n+1}= G(x) - 1$$


Now that we know what $ \sum_{n\geq 0 }a_{n+1}x^{n+1} = G(x) -1 $ we can replace it in the first term on the right side. 

$$\sum_{n\geq0} a_{n+1} x^{n+2}= x\sum_{n\geq0} a_{n+1} x^{n+1}$$

$$\sum_{n\geq0} a_{n+1} x^{n+2}= x(G(x)-1)$$


$$G(x) -1 - 2  x =\sum_{n \geq 0}a_{n+1} x^{n+2}+\sum_{n \geq 0}a_n  x^{n+2}$$


$$G(x) -1 - 2  x =x(G(x)-1)+\sum_{n \geq 0}a_n  x^{n+2}$$


Now lets deal with the last term on the right side of the equation $\sum_{n \geq 0}a_n  x^{n+2}$. 

What we will do is bring down $x^2$.

$$\sum_{n \geq 0}a_n  x^{n+2}=x^2\sum_{n \geq 0}a_n  x^{n}$$

This leads to the simple substation. $ \sum_{n \geq 0} a_n  x^n = G(x)$

$$\sum_{n \geq 0}a_n  x^{n+2}=x^2\sum_{n \geq 0}a_n  x^{n}$$
$$\sum_{n \geq 0}a_n  x^{n+2}=x^2G(x)$$

Now we can replace it in our equation. 

$$G(x) -1 - 2  x =x(G(x)-1)+\sum_{n \geq 0}a_n  x^{n+2}$$
$$G(x) -1 - 2  x =x(G(x)-1)+x^2\sum_{n \geq 0}a_n  x^{n}$$
$$G(x) -1 - 2  x =x(G(x)-1)+x^2G(x)$$


Now we want to solve the equation for $G(x)$ in terms of $x$



This can be done with some basic algebra 
$$G(x) -1 - 2  x =x G(x) -x+x^2  G(x)$$

$$G(x)-x G(x) -x^2  G(x)=-x +1 +2  x$$

$$G(x)-xG(x) -x^2G(x)=1 +x$$

$$G(x)(1-x -x^2)=1 +x$$

$$G(x)=\frac{1 +x}{1-x -x^2}$$

$$G(x)=\frac{1}{1-x -x^2} +\frac{x}{1-x -x^2}$$


	
Now we have two different fractions that are added together, but what we want is to have them in terms of a summation. Particularly of the form $c\sum_{n\geq0}d^nx^n$ Where $c,d \in \mathbb{R}$ This can be done by using partial fraction decomposition.

We will take the first term on the right side of the equation 
$$\frac{1}{1-x -x^2}$$ 

Now what we will do is factor the denominator. And then set it equal to each of its factors divided by two real number $A$ and $B$ then we want to solve for the values of $A$ and $B$ that make this equality true.

$$\frac{1}{1-x -x^2} = \frac{1}{(x+\frac{1+\sqrt{5}}{2})(-x +\frac{-1+\sqrt{5}}{2} )}$$ 

$$\frac{1}{(x+\frac{1+\sqrt{5}}{2})(-x +\frac{-1+\sqrt{5}}{2} )}= \frac{A}{x+\frac{1+\sqrt{5}}{2}}+ \frac{B}{-x +\frac{-1+\sqrt{5}}{2}}$$


$$ 1 = A(-x +\frac{-1 + \sqrt{5}}{2}) + B(x+ \frac{1 + \sqrt{5}}{2}) $$

Now we could multiply the $A$ and $B$ in however in this case if we smartly choose the value of $x$ we can get one of them to multiplied by $0$ and then we just have a linear equation with one unknown. 

$$x = \frac{-1 + \sqrt{5}}{2} $$


$$ 1 = A(-\frac{-1 + \sqrt{5}}{2} +\frac{-1 + \sqrt{5}}{2}) + B(x+ \frac{1 + \sqrt{5}}{2}) $$
$$ 1 = A\cdot0 + B(x+ \frac{1 + \sqrt{5}}{2}) $$

$$ 1 = B(\frac{-1 + \sqrt{5}}{2}+ \frac{1 + \sqrt{5}}{2}) $$
$$ 1 = B\sqrt{5} $$
$$B= \frac{1}{\sqrt{5}}$$

Now that we solved for $B$ we can substitute it back into the equation. 
$$ 1 = A(-x +\frac{-1 + \sqrt{5}}{2}) + \frac{1}{\sqrt{5}}(x+ \frac{1 + \sqrt{5}}{2}) $$

Again if we choose $x$ smartly it will cancel the other expression and we will just have to solve a linear equation with one unknown.
$$x = -\frac{1 + \sqrt{5}}{2} $$

$$ 1 = A(-\frac{1 + \sqrt{5}}{2} +\frac{-1 + \sqrt{5}}{2}) + \frac{1}{\sqrt{5}}(-\frac{1 + \sqrt{5}}{2}+ \frac{1 + \sqrt{5}}{2}) $$

$$ 1 = A(-\frac{1 + \sqrt{5}}{2} +\frac{-1 + \sqrt{5}}{2}) + \frac{1}{\sqrt{5}}\cdot 0 $$

$$ 1 = A(\frac{1 + \sqrt{5}}{2} +\frac{-1 + \sqrt{5}}{2})$$
$$1= A \sqrt{5}$$
$$A= \frac{1}{\sqrt{5}}$$


So now we know

$$\frac{1}{(x+\frac{1+\sqrt{5}}{2})(-x +\frac{-1+\sqrt{5}}{2} )}=  \frac{1}{\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{1}{\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})}$$


Then we can replace it the equation. 

$$G(x)= \frac{1}{(x+\frac{1+\sqrt{5}}{2})(-x +\frac{-1+\sqrt{5}}{2} )} +\frac{x}{1-x -x^2}$$


$$G(x)= \frac{1}{\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{1}{\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})} +\frac{x}{1-x -x^2}$$

Now we will do the same process with 
$$\frac{x}{1-x -x^2}$$




$$\frac{x}{(x+\frac{1+\sqrt{5}}{2})(-x +\frac{-1+\sqrt{5}}{2} )}= \frac{A}{x+\frac{1+\sqrt{5}}{2}}+ \frac{B}{-x +\frac{-1+\sqrt{5}}{2}}
$$

$$x= A(-x+\frac{-1+\sqrt{5}}{2}) +B(x+\frac{1+\sqrt{5}}{2})$$

$$ x = \frac{-1+\sqrt{5}}{2}$$

$$\frac{-1+\sqrt{5}}{2}= A(-\frac{-1+\sqrt{5}}{2}+\frac{-1+\sqrt{5}}{2}) +B(\frac{-1+\sqrt{5}}{2}+\frac{1+\sqrt{5}}{2})$$

$$\frac{-1+\sqrt{5}}{2}= A\cdot0 +B(\frac{-1+\sqrt{5}}{2}+\frac{1+\sqrt{5}}{2})$$

$$\frac{-1+\sqrt{5}}{2}=B(\frac{-1+\sqrt{5}}{2}+\frac{1+\sqrt{5}}{2})$$

$$\frac{-1+\sqrt{5}}{2}=B\sqrt{5}$$
$$B=\frac{-1+\sqrt{5}}{2\sqrt{5}}$$
$$ x = -\frac{1+\sqrt{5}}{2}$$

$$-\frac{1+\sqrt{5}}{2}= A(--\frac{1+\sqrt{5}}{2}+\frac{-1+\sqrt{5}}{2}) +\frac{-1+\sqrt{5}}{2\sqrt{5}}(-\frac{1+\sqrt{5}}{2}+\frac{1+\sqrt{5}}{2})$$

$$-\frac{1+\sqrt{5}}{2}= A(--\frac{1+\sqrt{5}}{2}+\frac{-1+\sqrt{5}}{2}) +\frac{-1+\sqrt{5}}{2\sqrt{5}}\cdot0$$

$$\frac{-1-\sqrt{5}}{2}= A(\frac{1+\sqrt{5}}{2}+\frac{-1+\sqrt{5}}{2})$$
$$-\frac{-1-\sqrt{5}}{2}= A \sqrt{5}$$
$$A=\frac{-1-\sqrt{5}}{2\sqrt{5}}$$

So now we know

$$\frac{x}{(x+\frac{1+\sqrt{5}}{2})(-x +\frac{-1+\sqrt{5}}{2} )}= \frac{-1-\sqrt{5}}{2\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{-1+\sqrt{5}}{2\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})}$$

So again we can replace it in our equation.

$$G(x)= \frac{1}{\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{1}{\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})} +\frac{x}{1-x -x^2}$$

$$G(x)= \frac{1}{\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{1}{\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})} +\frac{-1-\sqrt{5}}{2\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{-1+\sqrt{5}}{2\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})}$$


We can simplify this so we have only two quotients. 

$$G(x)= \frac{1}{\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{1}{\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})} + \frac{-1-\sqrt{5}}{2\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{-1+\sqrt{5}}{2\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})}$$


$$G(x)= \frac{2}{2\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{2}{2\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})} + \frac{-1-\sqrt{5}}{2\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{-1+\sqrt{5}}{2\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})}$$


$$G(x)= \frac{1-\sqrt{5}}{2\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{1+\sqrt{5}}{2\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})} $$

What we want to do now is have both of the quotients on the right hand side in the form of 
$$ C \frac{1}{1-a} ,  C\in \mathbb{R}$$

 
So we can write is as a geometric series 
$$ C \frac{1}{1-a}= C\sum_{n\geq 0}a^n$$

We can do this with both sides of the equation by factoring out from the bottom. 

$\frac{1+\sqrt{5}}{2}$ and $\frac{-1+\sqrt{5}}{2}$ 



$$G(x)= \frac{1-\sqrt{5}}{2\sqrt{5}(x+\frac{1+\sqrt{5}}{2})}+ \frac{1+\sqrt{5}}{2\sqrt{5}(-x +\frac{-1+\sqrt{5}}{2})} $$
$$G(x)= \frac{1-\sqrt{5}}{2\sqrt{5}(\frac{x}{\frac{1+\sqrt{5}}{2}}+1)\cdot \frac{1+\sqrt{5}}{2}}+ \frac{1+\sqrt{5}}{2\sqrt{5}(\frac{-x}{\frac{-1+\sqrt{5}}{2}} +1)\cdot \frac{-1+\sqrt{5}}{2}} $$







$$G(x)= \frac{1-\sqrt{5}}{\sqrt{5}(1+\sqrt{5})(1- \frac{-2x}{1+\sqrt{5}})}+ \frac{1+\sqrt{5}}{\sqrt{5}(-1+\sqrt{5})(1 - \frac{2x}{-1+\sqrt{5}})} $$

Now we have it in the form so we can write it as the sum two geometric series.

$$G(x)= \frac{1-\sqrt{5}}{\sqrt{5}(1+\sqrt{5})} \sum_{n \geq 0} (\frac{-2}{1+\sqrt{5}})^nx^n+ \frac{1+\sqrt{5}}{\sqrt{5}(-1+\sqrt{5})}\sum_{n \geq 0} (\frac{2}{-1+\sqrt{5}})^n x^n $$


$$G(x)= \sum_{n \geq 0} (\frac{1-\sqrt{5}}{\sqrt{5}(1+\sqrt{5})}(\frac{-2}{1+\sqrt{5}})^n+ \frac{1+\sqrt{5}}{\sqrt{5}(-1+\sqrt{5})} (\frac{2}{-1+\sqrt{5}})^n) x^n $$

$$\sum_{n \geq 0}a_nx^n= \sum_{n \geq 0}( \frac{1-\sqrt{5}}{\sqrt{5}(1+\sqrt{5})}(\frac{-2}{1+\sqrt{5}})^n+ \frac{1+\sqrt{5}}{\sqrt{5}(-1+\sqrt{5})} (\frac{2}{-1+\sqrt{5}})^n) x^n $$

Now for this to be true for every term in the power series all the coefficients have to also be equal.  

$$a_n= \frac{1-\sqrt{5}}{\sqrt{5}(1+\sqrt{5})}(\frac{-2}{1+\sqrt{5}})^n+ \frac{1+\sqrt{5}}{\sqrt{5}(-1+\sqrt{5})} (\frac{2}{-1+\sqrt{5}})^n $$

However we shifted the starting point of the series back one so we will undo that shift.
$$b_n=a_{n-1}$$


$$b_n= \frac{1-\sqrt{5}}{\sqrt{5}(1+\sqrt{5})}(\frac{-2}{1+\sqrt{5}})^{n-1}+ \frac{1+\sqrt{5}}{\sqrt{5}(-1+\sqrt{5})} (\frac{2}{-1+\sqrt{5}})^{n-1} $$


$$b_n= \frac{1-\sqrt{5}}{\sqrt{5}(1+\sqrt{5})}(\frac{-2}{1+\sqrt{5}})^{n}\cdot \frac{1+\sqrt{5}}{2}+ \frac{1+\sqrt{5}}{\sqrt{5}(-1+\sqrt{5})} (\frac{2}{-1+\sqrt{5}})^{n}\cdot \frac{-1+\sqrt{5}}{2} $$

$$b_n= \frac{1-\sqrt{5}}{-2\sqrt{5}}(\frac{-2}{1+\sqrt{5}})^{n}+ \frac{1+\sqrt{5}}{2\sqrt{5}} (\frac{2}{-1+\sqrt{5}})^{n}$$

$$b_n= \frac{1-\sqrt{5}}{-2\sqrt{5}}(\frac{1-\sqrt{5}}{2})^{n}+ \frac{1+\sqrt{5}}{2\sqrt{5}} (\frac{1+\sqrt{5}}{2})^{n}$$

And here is the closed form solution for the problem
