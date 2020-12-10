open System
open System.IO
open System.Text.RegularExpressions

type Instruction = Mask of string | Operation of int64 * int64

type ProblemState = { MemoryValues : Map<int64, int64>; Mask : string } with
    member this.Total = this.MemoryValues |> Map.toList |> List.map snd |> List.sum

let parse (row : string) : Instruction =
    let maskMatch = Regex("^mask = (?<mask>[01X]+)$").Match(row)
    let operationMatch = Regex("^mem\[(?<location>\d+)\] = (?<seed>\d+)$").Match(row)
    if maskMatch.Success then
        maskMatch.Groups.["mask"].Value |> Mask
    else if operationMatch.Success then
        let location = operationMatch.Groups.["location"].Value |> Int64.Parse
        let seed = operationMatch.Groups.["seed"].Value |> Int64.Parse
        Operation (location, seed)
    else
        invalidArg "row" <| sprintf "Bad input: %s" row

let version1 =
    let maskSeed mask (seed : int64) =
        Seq.zip (Convert.ToString(seed, 2).PadLeft(36, '0')) mask
        |> Seq.map (fun (c0, c1) -> if c1 <> 'X' then string c1 else string c0)
        |> String.concat ""
        |> (fun n -> Convert.ToInt64(n, 2))
    let foldFunction s = function
        | Mask mask -> { s with Mask = mask }
        | Operation (location, seed) -> { s with MemoryValues = Map.add location (maskSeed s.Mask seed) s.MemoryValues }
    Array.map parse >> Array.fold foldFunction { MemoryValues = Map.empty; Mask = String.Empty } >> (fun p -> p.Total)

let version2 =
    let maskSeed mask (seed : int64) =
        Seq.zip (Convert.ToString(seed, 2).PadLeft(36, '0')) mask
        |> Seq.map (fun (c0, c1) -> if c1 <> '0' then string c1 else string c0)
        |> String.concat ""
    let rec getMemoryLocations (mask : string) : seq<int64> =
        if mask.Contains("X") then
            let i = mask.IndexOf('X')
            seq {
                yield! getMemoryLocations <| sprintf "%s%s%s" (mask.Substring(0, i)) "0" (mask.Substring(i + 1))
                yield! getMemoryLocations <| sprintf "%s%s%s" (mask.Substring(0, i)) "1" (mask.Substring(i + 1))
            }
        else
            seq { yield Convert.ToInt64(mask, 2) }
    let foldFunction s = function
        | Mask mask ->
            { s with Mask = mask }
        | Operation (location, value) ->
            let memoryValues = maskSeed s.Mask location |> getMemoryLocations |> Seq.fold (fun s t -> Map.add t value s) s.MemoryValues
            { s with MemoryValues = memoryValues }
    Array.map parse >> Array.fold foldFunction { MemoryValues = Map.empty; Mask = String.Empty } >> (fun p -> p.Total)

File.ReadAllLines("./input/input_14.txt") |> version1 |> printfn "%d"  // 14862056079561
File.ReadAllLines("./input/input_14.txt") |> version2 |> printfn "%d"  // 3296185383161
