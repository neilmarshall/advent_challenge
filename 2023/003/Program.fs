open System

type Word =
    { Row : int; Column : int; Length : int; Grid : string[] }
    member this.IsSymbolAdjacent() =
        let isSymbol (c : char) = not (Char.IsDigit(c)) && c <> '.'
        let mutable isSymbolAdjacent = false
        if this.Row > 0 then
            if {this.Column .. this.Column + this.Length - 1} |> Seq.exists (fun c -> this.Grid[this.Row - 1][c] |> isSymbol) then
                isSymbolAdjacent <- true
            if this.Column > 0 then
                if this.Grid[this.Row - 1][this.Column - 1] |> isSymbol then
                    isSymbolAdjacent <- true
            if this.Column + this.Length < this.Grid[this.Row].Length - 1 then
                if this.Grid[this.Row - 1][this.Column + this.Length] |> isSymbol then
                    isSymbolAdjacent <- true
        if this.Row < this.Grid.Length - 1 then
            if {this.Column .. this.Column + this.Length - 1} |> Seq.exists (fun c -> this.Grid[this.Row + 1][c] |> isSymbol) then
                isSymbolAdjacent <- true
            if this.Column > 0 then
                if this.Grid[this.Row + 1][this.Column - 1] |> isSymbol then
                    isSymbolAdjacent <- true
            if this.Column + this.Length < this.Grid[this.Row].Length - 1 then
                if this.Grid[this.Row + 1][this.Column + this.Length] |> isSymbol then
                    isSymbolAdjacent <- true
        if this.Column > 0 then
            if this.Grid[this.Row][this.Column - 1] |> isSymbol then
                isSymbolAdjacent <- true
        if this.Column + this.Length < this.Grid[this.Row].Length - 1 then
            if this.Grid[this.Row][this.Column + this.Length] |> isSymbol then
                isSymbolAdjacent <- true
        isSymbolAdjacent

    member this.WordValue() =
        this.Grid[this.Row][this.Column .. this.Column + this.Length - 1] |> int

    member this.AdjacentGears() : seq<(int * int) * Word> =
        let adjacentGears = ResizeArray<int * int>()
        if this.Row > 0 then
            {this.Column .. this.Column + this.Length - 1}
            |> Seq.iter (fun c -> if this.Grid[this.Row - 1][c] = '*' then adjacentGears.Add(this.Row - 1, c))
            if this.Column > 0 then
                if this.Grid[this.Row - 1][this.Column - 1] = '*' then adjacentGears.Add(this.Row - 1, this.Column - 1)
            if this.Column + this.Length < this.Grid[this.Row].Length - 1 then
                if this.Grid[this.Row - 1][this.Column + this.Length] = '*' then adjacentGears.Add(this.Row - 1, this.Column + this.Length)
        if this.Row < this.Grid.Length - 1 then
            {this.Column .. this.Column + this.Length - 1}
            |> Seq.iter (fun c -> if this.Grid[this.Row + 1][c] = '*' then adjacentGears.Add(this.Row + 1, c))
            if this.Column > 0 then
                if this.Grid[this.Row + 1][this.Column - 1] = '*' then adjacentGears.Add(this.Row + 1, this.Column - 1)
            if this.Column + this.Length < this.Grid[this.Row].Length - 1 then
                if this.Grid[this.Row + 1][this.Column + this.Length] = '*' then adjacentGears.Add(this.Row + 1, this.Column + this.Length)
        if this.Column > 0 then
            if this.Grid[this.Row][this.Column - 1] = '*' then adjacentGears.Add(this.Row, this.Column - 1)
        if this.Column + this.Length < this.Grid[this.Row].Length - 1 then
            if this.Grid[this.Row][this.Column + this.Length] = '*' then adjacentGears.Add(this.Row, this.Column + this.Length)
        seq { for adjacentGear in adjacentGears do yield adjacentGear, this }

let parseInput (input : string[]) : seq<Word> =
    let words = ResizeArray<Word>()
    let parseRow r (s : string) =
        let mutable c = 0
        s |> Seq.iteri (fun c' e ->
            if Char.IsDigit(e) then
                if c' = 0 || not (Char.IsDigit(s[c' - 1])) then c <- c'
                if c' = s.Length - 1 || not (Char.IsDigit(s[c' + 1])) then
                    words.Add({ Row = r; Column = c; Length = c' - c + 1; Grid = input }))
    input |> Seq.iteri parseRow
    words

let testInput = [|
    "467..114.."
    "...*......"
    "..35..633."
    "......#..."
    "617*......"
    ".....+.58."
    "..592....."
    "......755."
    "...$.*...."
    ".664.598.."
|]

testInput 
|> parseInput
|> Seq.filter (fun w -> w.IsSymbolAdjacent())
|> Seq.sumBy (fun w -> w.WordValue())
|> printfn "Test Case Part One: %d"  // solution: 4,361

testInput
|> parseInput
|> Seq.map (fun w -> w.AdjacentGears())
|> Seq.collect id
|> Seq.groupBy (fun ((x, _)) -> x)
|> Seq.filter (fun (_, g) -> Seq.length g = 2)
|> Seq.map (fun (_, g) -> g |> Seq.map (fun (_, w) -> w.Grid[w.Row][w.Column .. w.Column + w.Length - 1] |> int) |> Seq.reduce (*))
|> Seq.sum
|> printfn "Test Case Part Two: %d"  // solution: 467,835

let input = IO.File.ReadLines("input.txt") |> Array.ofSeq
input
|> parseInput
|> Seq.filter (fun w -> w.IsSymbolAdjacent())
|> Seq.sumBy (fun w -> w.WordValue())
|> printfn "Answer to Part One: %d"  // solution: 539,713

input
|> parseInput
|> Seq.map (fun w -> w.AdjacentGears())
|> Seq.collect id
|> Seq.groupBy (fun ((x, _)) -> x)
|> Seq.filter (fun (_, g) -> Seq.length g = 2)
|> Seq.map (fun (_, g) -> g |> Seq.map (fun (_, w) -> w.Grid[w.Row][w.Column .. w.Column + w.Length - 1] |> int) |> Seq.reduce (*))
|> Seq.sum
|> printfn "Answer to Part Two: %d"  // solution: 84,159,075