module AlignmentLib

let AlignBasic (input : int[]) : int =
    {1..(Array.length input)} |> Seq.map (fun n -> input |> Array.map (fun e -> abs(e - n)) |> Seq.sum) |> Seq.min

let AlignAdvanced (input : int[]) : int =
    let T n = n * (n + 1) / 2
    {1..(Array.length input)} |> Seq.map (fun n -> input |> Array.map (fun e -> T(abs(e - n))) |> Seq.sum) |> Seq.min