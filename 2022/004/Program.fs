let input = System.IO.File.ReadLines("input.txt")

let isDuplicate includeOverlap row =
    let parseRow (row : string) =
        let extractLimits (e : string) =
            match e.Split('-', 2) with
            | [|n1; n2|] -> int(n1), int(n2)
            | _ -> failwith "bad input"
        match row.Split(',', 2) with
        | [|first; second|] -> extractLimits first, extractLimits second
        | _ -> failwith "bad input"
    let (m1, m2), (n1, n2) = parseRow row
    if includeOverlap then
        (m1 <= n1 && m2 >= n1) || (n1 <= m2 && n2 >= m1)
    else
        (m1 <= n1 && m2 >= n2) || (n1 <= m1 && n2 >= m2)

input |> Seq.filter (isDuplicate false) |> Seq.length |> printfn "Answer to Part One: %d"  // expected output is 464

input |> Seq.filter (isDuplicate true) |> Seq.length |> printfn "Answer to Part Two: %d"  // expected output is 770