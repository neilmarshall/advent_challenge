let solve d =
    let generator (n, t, f, s) =
        let n' = if Map.containsKey n f && Map.containsKey n s then Map.find n s - Map.find n f else 0
        let f' = if Map.containsKey n' s then Map.add n' (Map.find n' s) f else if Map.containsKey n' f then f else Map.add n' t f
        let s' = if Map.containsKey n' f then Map.add n' t s else s
        Some (n', (n', t + 1, f', s'))
    seq {
        yield! d
        let f = d |> Seq.indexed |> Seq.map (fun (a, b) -> b, a + 1) |> Map.ofSeq
        yield! Seq.unfold generator (Seq.last d, Seq.length d + 1, f, Map.empty)
    }

[6; 13; 1; 15; 2; 0] |> solve |> Seq.take 2020 |> Seq.last |> printfn "%d"  // 1194
[6; 13; 1; 15; 2; 0] |> solve |> Seq.take 30000000 |> Seq.last |> printfn "%d"  // 48710