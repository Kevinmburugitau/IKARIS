Module Calc
  Public num1 As Double
  Public num2 As Double
  Sub Main()
    num1 = CDbl(Console.ReadLine())
    num2 = CDbl(Console.ReadLine())
    Result()
    Console.ReadLine()
  End Sub
  
  Public Function Addition()
    Addition = num1 + num2
  End Function
  Public Function Subtraction()
    Subtraction = num1 - num2
  End Function
  Public Function Multiplication()
    Multiplication = num1 * num2
  End Function
  Public Function Division()
    If num2 = 0 Then
      Console.WriteLine("math error in Division")
      Division = 0
    Else
      Division = num1/num2
    End If
  End Function
  Public Sub Result()
    Console.WriteLine("num1:{0} num2:{1} Addition:{2} Subtraction:{3} Multiplication:{4} Division:{5}", num1, num2, Addition(), Subtraction(), Multiplication(), Division())
  End Sub
End Module
