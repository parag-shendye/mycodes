package week1

object NewtonsMethod extends App {

def sqrtiter(guess:Double, x:Double):Double ={

   if(isGoodEnough(guess,x))guess
   else sqrtiter(improve(guess,x),x)
 }

 def isGoodEnough(d: Double, d1: Double):Boolean={
    Math.abs(d*d - d1)/d1 < 0.001
  }

  def improve(d: Double, d1: Double):Double ={

    (d + d1/d)/2
  }

  def sqrt(x:Double)=sqrtiter(1.0,x)

  println(sqrt(2))
  println(sqrt(1e-6))

