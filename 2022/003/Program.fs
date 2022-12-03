let input = System.IO.File.ReadLines("input.txt")

let getDuplicatedElement (row : string) =
    let compartmentA, compartmentB = Set.ofSeq row[.. row.Length / 2 - 1], Set.ofSeq row[row.Length / 2 ..]
    Set.intersect compartmentA compartmentB |> Seq.exactlyOne

let scoreElement e = int(e) - if System.Char.IsLower(e) then 96 else 38

input
|> Seq.map getDuplicatedElement
|> Seq.map scoreElement
|> Seq.sum
|> printfn "Answer to Part One: %d"  // expected output is 8088

input
|> Seq.map Set.ofSeq
|> Seq.chunkBySize 3
|> Seq.map (Set.intersectMany >> Seq.exactlyOne >> scoreElement)
|> Seq.sum
|> printfn "Answer to Part Two: %d"  // expected output is 2522