let groups = [for g in System.IO.File.ReadAllText("./input/input_6.txt").Split("\n\n") -> g.Trim().Split("\n")]

let solve f =
    Seq.map (Array.map Set.ofSeq)
    >> Seq.map (Array.reduce f >> Seq.length)
    >> Seq.sum

solve Set.union groups |> printfn "%d"  // 6703
solve Set.intersect groups |> printfn "%d"  // 3430
