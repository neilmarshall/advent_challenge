module LanternFishLib

let CountFish (initialState : int[]) (days : int) : int64 =
    let rec f (d : int) (s : Map<int, int64>) : int64 =
        if d = 0 then
            s |> Map.values |> Seq.sum
        else
            let newFish = match Map.tryFind 0 s with | Some n -> n | None -> 0L
            seq {
                for k in 0..8 do
                    let v = match Map.tryFind k s with | Some k -> k | None -> 0L
                    yield if k = 0 then (6, v) else (k - 1, v)
            }
            |> Map.ofSeq
            |> Map.change 6 (function | Some n -> Some (n + newFish) | None -> Some newFish)
            |> Map.add 8 newFish
            |> f (d - 1)
    initialState
    |> Array.countBy id
    |> Array.map (fun (a, b) -> (a, int64(b)))
    |> Map.ofArray
    |> f days 