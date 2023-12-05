open System

type Color = |Blue|Red|Green
type Reveal = int * Color
type Turn = Reveal list
type Game = int * Turn list

let Bag = Map.ofList [ Red, 12; Green, 13; Blue, 14 ]

let validateReveal ((count, color) : Reveal) : bool =
    Bag[color] >= count

let parseReveal (reveal : string) =
    match reveal.Trim().Split(' ') with
    | [| count; color |] ->
        match System.Int32.TryParse(count) with
        | true, count ->
            let color =
                match color with
                | "blue" -> Blue
                | "red" -> Red
                | "green" -> Green
                | _ -> failwith "Invalid input"
            (count, color) |> Reveal
        | false, _ -> failwith "Invalid input"
    |__ -> failwith "Invalid input"

let validateTurn (turn : string) =
    turn.Split(',') |> Array.map parseReveal |> Array.forall validateReveal

let validateGame (game : string) =
    game.Substring(game.IndexOf(':') + 2).Split(';') |> Array.forall validateTurn

let parseGame (game : string) : Game =
    let idx = System.Int32.Parse((game.Split(':')[0]).Split(' ')[1])
    let turns =
        game.Substring(game.IndexOf(':') + 2).Split(';')
        |> Array.map (fun turn -> turn.Split(',') |> Array.map parseReveal |> Array.toList)
        |> Array.toList
    idx, turns

let getValidGames : seq<string> -> Game list =
    Seq.filter validateGame >> Seq.map parseGame >> Seq.toList

let getPower ((_, turns): Game) =
    let minimumCubes = Map.ofList [ Blue, 0; Red, 0; Green, 0 ]
    let folder (minimumCubes : Map<Color, int>) ((count, color): Reveal) =
        if minimumCubes[color] < count
            then Map.add color count minimumCubes
            else minimumCubes
    turns
    |> Seq.collect (fun (reveals : Reveal list) -> reveals)
    |> Seq.fold folder minimumCubes
    |> Map.values
    |> Seq.reduce (*)

let getPowers : seq<string> -> int =
    Seq.map parseGame >> Seq.map getPower >> Seq.sum

let testInput = [|
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
|]
let input = IO.File.ReadLines("input.txt")
testInput |> getValidGames |> List.sumBy (fun (idx, _) -> idx) |> printfn "Test Case Part One: %d"
input |> getValidGames |> List.sumBy (fun (idx, _) -> idx) |> printfn "Answer to Part One: %d"  // answer - 2,006
testInput |> getPowers |> printfn "Test Case Part Two: %d"
input |> getPowers |> printfn "Answer to Part Two: %d"  // answer - 84,911