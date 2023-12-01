open System

let solvePartA =
    let getFirstDigit = Seq.filter Char.IsDigit >> Seq.head >> string
    let getLastDigit = Seq.filter Char.IsDigit >> Seq.last >> string
    let getCalibrationValue v = (getFirstDigit v + getLastDigit v) |> int
    Seq.map getCalibrationValue >> Seq.sum

let solvePartB =
    let replacements = ["one", '1'; "two", '2'; "three", '3'; "four", '4'; "five", '5'; "six", '6'; "seven", '7'; "eight", '8'; "nine", '9']
    let rec replaceWords (s : string) =
        match s.ToCharArray() |> List.ofArray with
        | [] -> Seq.empty
        | head::tail when Char.IsDigit(head) ->
            seq { yield head; yield! replaceWords (String.Join("", tail)) }
        | head::tail ->
            match Seq.tryFind (fun (k : string, v) -> s.StartsWith(k)) replacements with
            | Some (k, v) -> seq { yield v; yield! replaceWords (s.Substring(k.Length - 1)) }
            | None -> seq { yield head; yield! replaceWords (String.Join("", tail)) }
    Seq.map (fun (s : string) -> (s.ToLower() |> replaceWords |> (fun chars -> String.Join("", chars)))) >> solvePartA

(* test cases *)
// [| "1abc2"; "pqr3stu8vwx"; "a1b2c3d4e5f"; "treb7uchet" |] |> solvePartA |> printfn "%d"  // expected output is 142
// [| "two1nine"; "eightwothree"; "abcone2threexyz"; "xtwone3four"; "4nineeightseven2"; "zoneight234"; "7pqrstsixteen" |] |> solvePartB |> printfn "%d"  // expected output is 281

let input = IO.File.ReadLines("input.txt")
input |> solvePartA |> printfn "Answer to Part One: %d"  // expected output is 55,130
input |> solvePartB |> printfn "Answer to Part Two: %d"  // expected output is 54,985