open System

type MappingRule = { Destination : int64; Source : int64; Length : int64 }

type Almanac = { Rules: MappingRule list list; Seeds : int64 list } with
    static member ParseFromString (input : seq<string>) : Almanac =
        let seeds =
            ((Seq.head input).Split(':', StringSplitOptions.TrimEntries)[1]).Split(' ', StringSplitOptions.RemoveEmptyEntries)
            |> Seq.map int64
            |> List.ofSeq
        let rules =
            seq {
                let mutable mappingRules = ResizeArray<MappingRule>()
                for row in Seq.skip 1 input do
                    if (String.IsNullOrWhiteSpace(row)) then
                        if mappingRules.Count > 0 then
                            yield mappingRules |> Seq.toList
                    else if row.Contains(':') then
                        mappingRules.Clear()
                    else
                        match row.Split(' ', StringSplitOptions.RemoveEmptyEntries) |> Array.map int64 with
                        | [| destination; source; length |] ->
                            mappingRules.Add({ Destination = destination; Source = source; Length = length })
                        | _ -> failwith "invalid input"
                if mappingRules.Count > 0 then yield mappingRules |> Seq.toList
            }
            |> List.ofSeq
        { Rules = rules; Seeds = seeds }

    member this.MapSeeds() =
        let applyRule (rules : MappingRule list) seed =
            let rule = rules |> Seq.tryFind (fun r -> r.Source <= seed && r.Source + r.Length >= seed)
            match rule with
            | Some rule -> seed + rule.Destination - rule.Source
            | None -> seed
        let mapSeed seed =
            this.Rules
            |> Seq.scan (fun s t -> applyRule t s) seed
            |> Seq.toList
        this.Seeds |> List.map mapSeed
    
let solvePartA input =
    Almanac.ParseFromString(input).MapSeeds() |> Seq.map (Seq.last) |> Seq.min

let testInput = [
    "seeds: 79 14 55 13"
    ""
    "seed-to-soil map:"
    "50 98 2"
    "52 50 48"
    ""
    "soil-to-fertilizer map:"
    "0 15 37"
    "37 52 2"
    "39 0 15"
    ""
    "fertilizer-to-water map:"
    "49 53 8"
    "0 11 42"
    "42 0 7"
    "57 7 4"
    ""
    "water-to-light map:"
    "88 18 7"
    "18 25 70"
    ""
    "light-to-temperature map:"
    "45 77 23"
    "81 45 19"
    "68 64 13"
    ""
    "temperature-to-humidity map:"
    "0 69 1"
    "1 0 69"
    ""
    "humidity-to-location map:"
    "60 56 37"
    "56 93 4"
]

testInput |> solvePartA |> printfn "Test Case Part One: %d"  // solution: 35
// testInput |> solvePartB |> printfn "Test Case Part Two: %d"  // solution: 30

let input = IO.File.ReadLines("input.txt")
input |> solvePartA |> printfn "Answer to Part One: %d"  // solution: 111,627,841
// input |> solvePartB |> printfn "Answer to Part Two: %d"  // solution: 5,833,065