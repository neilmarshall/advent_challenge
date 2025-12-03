open System
open System.IO

type Direction = L | R 
type Instruction = { Direction : Direction; Magnitude : int }
type ProgramState =  { CurrentPosition : int; OriginHitCount : int }

let parseRow (row : string) =
    let direction =
        match row.[0] with
        | 'L' -> L
        | 'R' -> R
        | _ -> failwith "invalid direction"
    { Direction = direction; Magnitude = row.[1..] |> Int32.Parse }

let input = File.ReadAllLines("input.txt") |> Array.map parseRow

let reducer (s : ProgramState) (t : Instruction) =
    let currentPosition =
        match t.Direction with
        | L -> (s.CurrentPosition - t.Magnitude) % 100
        | R -> (s.CurrentPosition + t.Magnitude) % 100
    if currentPosition = 0
        then { s with CurrentPosition = currentPosition; OriginHitCount = s.OriginHitCount + 1 }
        else { s with CurrentPosition = currentPosition }

let finalState = Array.fold reducer { CurrentPosition = 50; OriginHitCount = 0 } input

printfn "Solution to Part A: %d" <| finalState.OriginHitCount
