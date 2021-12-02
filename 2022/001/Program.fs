let calorieTotaller (calorieTotals : ResizeArray<int>, currentTotal) element =
    match element with
    | "" -> calorieTotals.Add(currentTotal); calorieTotals, 0
    | _ -> calorieTotals, currentTotal + int element
let calorieTotals =
    System.IO.File.ReadLines("input.txt")
    |> Seq.fold calorieTotaller (ResizeArray<int>(), 0)
    |> fst
    |> Seq.sortDescending
    |> Seq.take 3

printfn "Answer to Part One: %d" <| Seq.max calorieTotals  // should be 71471

printfn "Answer to Part Two: %d" <| Seq.sum calorieTotals  // should be 211189