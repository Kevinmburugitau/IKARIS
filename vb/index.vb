'Module Program
 ' Sub Main()
  '  Dim name As String = "Richard"
   ' Dim age As Integer = 19
    'Dim height As Double = 6.5
    'Console.WriteLine("blah")
    'Console.ReadLine()
    'Console.WriteLine("{0}", name)
  'End Sub
'End Module

Public Class Rectangle
  Private Length As Double
  Private Width As Double
  
  Public Sub Measurements()
    Length = CDbl(Console.ReadLine())
    Width = CDbl(Console.ReadLine())
  End Sub
  Public Function GetArea()
    GetArea = Length * Width
  End Function
  Public Function GetPerimeter()
    GetPerimeter = 2 * (Length + Width)
  End Function
  Public Sub OutPut()
    Console.WriteLine("Length:{0} Width:{1} Area:{2} Perimeter:{3}", Length,Width,GetArea(),GetPerimeter())
  End Sub
  Shared Sub Main()
    Dim r As New Rectangle()
    r.Measurements()
    r.OutPut()
    Console.ReadLine()
  End Sub
End Class
