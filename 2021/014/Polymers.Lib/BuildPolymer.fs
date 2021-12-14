module Polymers.Lib

open System.Collections.Generic

let buildPolymer (template : string) (insertionRules : Dictionary<string, string>) (steps : int) =
    let rec extendPolymer steps (state : Map<string, int64>) =
        let additiveUpdate v = function | Some n -> Some (n + v) | None -> Some v
        if steps = 0 then
            state
            |> Map.toSeq
            |> Seq.groupBy (fst >> Seq.head)
            |> Seq.map (fun (k, v) -> k, Seq.map snd v |> Seq.sum)
            |> Seq.fold (fun m (k, v) -> Map.change k (additiveUpdate v) m) (Map.ofList [Seq.last template, 1L])
            |> Map.toSeq
        else
            let folder (m : Map<string, int64>) (k : string) (v : int64) =
                m
                |> Map.change (string(k[0]) + insertionRules[k]) (additiveUpdate v)
                |> Map.change (insertionRules[k] + string(k[1])) (additiveUpdate v)
            state
            |> Map.fold folder Map.empty
            |> extendPolymer (steps - 1)
    let polymer =
        template
        |> Seq.windowed 2
        |> Seq.map (Seq.map string >> String.concat "")
        |> Seq.countBy id
        |> Seq.map (fun (k, v) -> k, int64 v)
        |> Map.ofSeq
        |> extendPolymer steps
    (polymer |> Seq.maxBy snd |> snd) - (polymer |> Seq.minBy snd |> snd)