let rec processInstructions locations history instructions =
    let processInstruction locations history instruction =
        let rec updateLocation (hx, hy) (tx, ty) =
            if tx = hx - 2 then tx + 1, if ty < hy then ty + 1 elif ty > hy then ty - 1 else ty
            elif tx = hx + 2 then tx - 1, if ty < hy then ty + 1 elif ty > hy then ty - 1 else ty
            elif ty = hy - 2 then (if tx < hx then tx + 1 elif tx > hx then tx - 1 else tx), ty + 1
            elif ty = hy + 2 then (if tx < hx then tx + 1 elif tx > hx then tx - 1 else tx), ty - 1
            else tx, ty
        let updatedHeadLocation =
            let hx, hy = locations |> List.head
            match instruction with
            | "R" -> hx + 1, hy
            | "L" -> hx - 1, hy
            | "U" -> hx, hy + 1
            | "D" -> hx, hy - 1
            | _ -> failwith "Could not parse instruction"
        let locations' = List.scan updateLocation updatedHeadLocation (List.tail locations)
        let history' = List.zip locations' history |> List.map (fun (l, h) -> Set.add l h)
        locations', history'
    match instructions with
    | head::tail ->
        let locations', history' = processInstruction locations history head
        processInstructions locations' history' tail
    | _ -> history

let solve steps =
    let instructionParser (instruction : string) =
        match instruction.Split(" ", 2) with
        | [| direction; n |] -> List.replicate (int(n)) direction
        | _ -> invalidArg instruction "Could not parse instruction"
    List.map instructionParser
    >> List.concat
    >> processInstructions (List.replicate steps (0, 0)) (List.replicate steps Set.empty)
    >> Seq.last
    >> Seq.length

let instructions = System.IO.File.ReadLines("input.txt") |> Seq.toList
instructions |> solve 2 |> printfn "Answer to Part One: %d"  // expected output is 6,377
instructions |> solve 10 |> printfn "Answer to Part Two: %d"  // expected output is 2,455