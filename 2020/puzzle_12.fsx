type Instruction = | North of int | South of int | East of int | West of int | Left of int | Right of int | Forward of int

type Position = { X : int; Y : int } with
    member this.ManhattanDistance = System.Math.Abs this.X + System.Math.Abs this.Y

let parseInstruction (s : string) =
    let instruction, value = Seq.head s, Seq.skip 1 s |> Seq.map string |> String.concat "" |> System.Int32.Parse
    match instruction with
    | 'N' -> North value
    | 'S' -> South value
    | 'E' -> East value
    | 'W' -> West value
    | 'L' -> Left value
    | 'R' -> Right value
    | 'F' -> Forward value
    | _ -> failwith "bad input"

let rec updatePosition (position, currentInstruction) newInstruction =
    let changeDirection currentInstruction newInstruction n =
        let updateInstruction i = function
            | Left _ ->
                match i with
                | North value -> West value
                | South value -> East value
                | East value -> North value
                | West value -> South value
                | _ -> failwith "bad input"
            | Right _ ->
                match i with
                | North value -> East value
                | South value -> West value
                | East value -> South value
                | West value -> North value
                | _ -> failwith "bad input"
            | _ -> failwith "bad input"
        {1..n} |> Seq.fold (fun s _ -> updateInstruction s newInstruction) currentInstruction
    match newInstruction with
    | North value -> { position with Y = position.Y + value }, currentInstruction
    | South value -> { position with Y = position.Y - value }, currentInstruction
    | East value -> { position with X = position.X + value }, currentInstruction
    | West value -> { position with X = position.X - value }, currentInstruction
    | Left value as p -> position, changeDirection currentInstruction newInstruction (value / 90)
    | Right value as p -> position, changeDirection currentInstruction newInstruction (value / 90)
    | Forward value ->
        match currentInstruction with
        | North _ -> North value
        | South _ -> South value
        | East _ -> East value
        | West _ -> West value
        | _ -> failwith "bad input"
        |> updatePosition (position, currentInstruction)

let updateWaypoint (waypoint, position) instruction =
    let rotateWaypoint w p n =
        let updateWaypoint w = function
            | Left _ -> { w with X = -w.Y; Y = w.X }
            | Right _ -> { w with X = w.Y; Y = -w.X }
            | _ -> failwith "bad input"
        {1..n} |> Seq.fold (fun s _ -> updateWaypoint s p) w
    match instruction with
    | North value -> { waypoint with Y = waypoint.Y + value }, position
    | South value -> { waypoint with Y = waypoint.Y - value }, position
    | East value -> { waypoint with X = waypoint.X + value }, position
    | West value -> { waypoint with X = waypoint.X - value }, position
    | Left value as p -> rotateWaypoint waypoint p (value / 90), position
    | Right value as p -> rotateWaypoint waypoint p (value / 90), position
    | Forward value -> waypoint, { position with X = position.X + value * waypoint.X; Y = position.Y + value * waypoint.Y }

let data = System.IO.File.ReadAllLines("./input/input_12.txt") |> Array.map parseInstruction
data |> Array.fold updatePosition ({ X = 0; Y = 0 }, East 0) |> (fun (p, _) -> p.ManhattanDistance) |> printfn "%A"  // 820
data |> Array.fold updateWaypoint ({ X = 10; Y = 1 }, { X = 0; Y = 0 }) |> (fun (_, p) -> p.ManhattanDistance) |> printfn "%A"  // 66614
