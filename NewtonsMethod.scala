package week1

object NewtonsMethod extends App {

//  def sqrtiter(guess:Double, x:Double):Double ={
//
//    if(isGoodEnough(guess,x))guess
//    else sqrtiter(improve(guess,x),x)
//  }
//
//  def isGoodEnough(d: Double, d1: Double):Boolean={
//    Math.abs(d*d - d1)/d1 < 0.001
//  }
//
//  def improve(d: Double, d1: Double):Double ={
//
//    (d + d1/d)/2
//  }
//
//  def sqrt(x:Double)=sqrtiter(1.0,x)
//
//  println(sqrt(2))
//  println(sqrt(1e-6))

  // sum of factorials between a and b
  def fact(i: Int):Int = {
    if (i==0) 1 else i * fact(i-1)
  }

  def sumfact(a:Int, b: Int):Int = {
    if (a > b) 0 else fact(a) + sumfact(a + 1, b)
  }
  //currying

  def product(f:Int=> Int)(a:Int, b:Int):Int = {
    if (a>b) 1 else f(a)*product(f)(a+1,b)
  }

  // so this function can be used to calculate factorial

  def factnew(x:Int):Int = product(x=>x)(1,x)

  println(factnew(5))

  println(product(x=>x)(2,4))

  println(sumfact(2,4))


}
