module PartA =
    let (|Rock|Paper|Scissors|) = function
        | 'A' | 'X' -> Rock
        | 'B' | 'Y' -> Paper
        | 'C' | 'Z' -> Scissors
        | _ -> failwith "unrecognized input"

    let (|Win|Loss|Draw|) (opponent, strategy) =
        match opponent with
        | Rock -> match strategy with | Rock -> Draw | Paper -> Win | Scissors  -> Loss
        | Paper -> match strategy with | Rock -> Loss | Paper -> Draw | Scissors  -> Win
        | Scissors -> match strategy with | Rock -> Win | Paper -> Loss | Scissors  -> Draw

    let scoreRound (round : string) =
        if round.Length <> 3 then failwith "invalid input - must contain three characters"
        let opponent, strategy = round.[0], round.[2]
        let strategyScoreComponent =
            match strategy with
            | Rock -> 1
            | Paper -> 2
            | Scissors -> 3
        let resultScoreComponent =
            match opponent, strategy with
            | Win -> 6
            | Draw -> 3
            | Loss -> 0
        strategyScoreComponent + resultScoreComponent

module PartB =
    let (|Win|Loss|Draw|) = function
        | 'X' -> Loss
        | 'Y' -> Draw
        | 'Z' -> Win
        | _ -> failwith "unrecognized input"

    let (|Rock|Paper|Scissors|) (opponent, targetOutcome) =
        match opponent with
        | 'A' -> match targetOutcome with | Win -> Paper | Loss -> Scissors | Draw  -> Rock
        | 'B' -> match targetOutcome with | Win -> Scissors | Loss -> Rock | Draw  -> Paper
        | 'C' -> match targetOutcome with | Win -> Rock | Loss -> Paper | Draw  -> Scissors
        | _ -> failwith "unrecognized input"

    let scoreRound (round : string) =
        if round.Length <> 3 then failwith "invalid input - must contain three characters"
        let opponent, targetOutcome = round.[0], round.[2]
        let resultScoreComponent =
            match opponent with
            | Win -> 6
            | Draw -> 3
            | Loss -> 0
        let strategyScoreComponent =
            match opponent, targetOutcome with
            | Rock -> 1
            | Paper ->  2
            | Scissors -> 3
        strategyScoreComponent + resultScoreComponent

let strategyGuide = System.IO.File.ReadLines("input.txt")

Seq.fold (fun total round -> total + PartA.scoreRound round) 0 strategyGuide |> printfn "Answer to Part One: %d"  // 10624 is the expected output

Seq.fold (fun total round -> total + PartB.scoreRound round) 0 strategyGuide |> printfn "Answer to Part Two: %d"  // 10624 is the expected output