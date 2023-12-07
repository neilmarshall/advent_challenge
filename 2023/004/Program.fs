open System

type Card = { Number : int; WinningNumbers : Set<int>; CardNumbers : Set<int> } with
    member this.CountMatches() = Set.intersect this.WinningNumbers this.CardNumbers |> Seq.length

    member this.Score() = this.CountMatches() - 1 |> (fun n -> 2.**n) |> int

    static member ParseFromStringSeq =
        let parseCard (s : string) =
            let number = (s.Split(':')[0]).Split(' ', StringSplitOptions.RemoveEmptyEntries)[1] |> int
            let numbers =
                (s.Split(':')[1]).Split('|', StringSplitOptions.TrimEntries)
                |> Array.map (fun s' -> s'.Split(' ', StringSplitOptions.RemoveEmptyEntries) |> Seq.map int |> Set.ofSeq)
            match number, numbers with
            | number, [| winningNumbers; cardNumbers |] ->
                { Number = number; WinningNumbers = winningNumbers; CardNumbers = cardNumbers }
            | _ -> failwith "invalid input"
        Seq.map parseCard

let solvePartA =
    Card.ParseFromStringSeq >> Seq.map (fun c -> c.Score()) >> Seq.sum

let solvePartB input =
    let folder s t =
        { t.Number + 1 .. t.Number + t.CountMatches() }
        |> Seq.replicate (1 + if Map.containsKey t.Number s then Map.find t.Number s else 0)
        |> Seq.collect id
        |> Seq.fold (fun m n -> if Map.containsKey n m then Map.add n (Map.find n m + 1) m else Map.add n 1 m) s
    input
    |> Card.ParseFromStringSeq
    |> Seq.fold folder Map.empty
    |> Map.values
    |> Seq.sum
    |> (+) (Seq.length input)

let testInput = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

testInput |> solvePartA |> printfn "Test Case Part One: %d"  // solution: 13
testInput |> solvePartB |> printfn "Test Case Part Two: %d"  // solution: 30

let input = IO.File.ReadLines("input.txt")
input |> solvePartA |> printfn "Answer to Part One: %d"  // solution: 20,667
input |> solvePartB |> printfn "Answer to Part Two: %d"  // solution: 5,833,065