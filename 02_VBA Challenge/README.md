## Bonus Multiple Year Stock Data
<!-- Sub stockMarket():

'Set Dimensions
Dim total As Double
Dim i As Long
Dim change As Single
Dim j As Integer
Dim start As Long
Dim rowCount As Long
Dim percentChange As Single
Dim ws As Worksheet

For Each ws In Worksheets
'Create the column headers
ws.Range("i1").Value = "Ticker"
ws.Range("j1").Value = "Yearly Change"
ws.Range("k1").Value = "Percentage Change"
ws.Range("l1").Value = "Total Stock Volume"
ws.Range("P1").Value = "Ticker"
ws.Range("Q1").Value = "Value"
ws.Range("O2").Value = "Greatest % Increase"
ws.Range("O3").Value = "Greatest % Decrease"
ws.Range("O4").Value = "Greatest Total Volume"

'Set initial Values
j = 0
total = 0
change = 0
start = 2

'Get the row number of the last row
rowCount = Cells(Rows.Count, "A").End(xlUp).Row

For i = 2 To rowCount
    If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
    
        total = total + ws.Cells(i, 7).Value
        
        If total = 0 Then
            'Print 0 values results for tickers
            ws.Range("i" & 2 + j).Value = ws.Cells(i, 1).Value
            ws.Range("j" & 2 + j).Value = 0
            ws.Range("k" & 2 + j).Value = "%" & 0
            ws.Range("l" & 2 + j).Value = 0
        Else
            'Print non-zero values results
            If ws.Cells(start, 3) = 0 Then
                For find_value = start To i
                    If ws.Cells(find_value, 3).Value <> 0 Then
                        start = find_value
                        Exit For
            End If
            Next find_value
        End If
        
        'Percentage Changes
            change = (ws.Cells(i, 6) - ws.Cells(start, 3))
            percentChange = Round((change / ws.Cells(start, 3) * 100), 2)
            
            'Start next stock ticker
            start = i + 1
            
            'print results
            ws.Range("I" & 2 + j).Value = ws.Cells(i, 1).Value
            ws.Range("j" & 2 + j).Value = Round(change, 2)
            ws.Range("k" & 2 + j).Value = "%" & percentChange
            ws.Range("l" & 2 + j).Value = total
            
            'Change of color yearly change
            Select Case change
                Case Is > 0
                ws.Range("j" & 2 + j).Interior.ColorIndex = 4
                Case Is < 0
                ws.Range("j" & 2 + j).Interior.ColorIndex = 3
                Case Else
                ws.Range("j" & 2 + j).Interior.ColorIndex = 0
            End Select
            End If
            
            'Reset ticker
            total = 0
            change = 0
            j = j + 1
            
            'If ticker is same
            Else
                total = total + ws.Cells(i, 7).Value
            End If
        Next i
    'Max and Min
    ws.Range("q2") = "%" & WorksheetFunction.Max(ws.Range("K2:K" & rowCount)) * 100
    ws.Range("q3") = "%" & WorksheetFunction.Min(ws.Range("K2:K" & rowCount)) * 100
    ws.Range("q4") = WorksheetFunction.Max(ws.Range("L2:L" & rowCount))
    
    'return one less
    increase_number = WorksheetFunction.Match(WorksheetFunction.Max(ws.Range("K2:K" & rowCount)), ws.Range("K2:K" & rowCount), 0)
    decrease_number = WorksheetFunction.Match(WorksheetFunction.Min(ws.Range("K2:K" & rowCount)), ws.Range("K2:K" & rowCount), 0)
    volume_number = WorksheetFunction.Match(WorksheetFunction.Max(ws.Range("L2:L" & rowCount)), ws.Range("L2:L" & rowCount), 0)
    
    'final ticker symbol for total
    ws.Range("P2") = ws.Cells(increase_number + 1, 9)
    ws.Range("P3") = ws.Cells(decrease_number + 1, 9)
    ws.Range("P4") = ws.Cells(volume_number + 1, 9)
    
Next ws

      
    


End Sub



            

            End If
        Next i
    'Max and Min
    Range("q2") = "%" & WorksheetFunction.Max(Range("K2:K" & rowCount)) * 100
    Range("q3") = "%" & WorksheetFunction.Min(Range("K2:K" & rowCount)) * 100
    Range("q4") = WorksheetFunction.Max(Range("L2:L" & rowCount))
    
    'return one less
    increase_number = WorksheetFunction.Match(WorksheetFunction.Max(Range("K2:K" & rowCount)), Range("K2:K" & rowCount), 0)
    decrease_number = WorksheetFunction.Match(WorksheetFunction.Min(Range("K2:K" & rowCount)), Range("K2:K" & rowCount), 0)
    volume_number = WorksheetFunction.Match(WorksheetFunction.Max(Range("L2:L" & rowCount)), Range("L2:L" & rowCount), 0)
    
    'final ticker symbol for total
    Range("P2") = Cells(increase_number + 1, 9)
    Range("P3") = Cells(decrease_number + 1, 9)
    Range("P4") = Cells(volume_number + 1, 9)
        
    


End Sub
 -->
