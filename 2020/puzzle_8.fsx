type Command = | Acc of int | Jmp of int | Nop of int
type Status = | Terminated | Unterminated

let parseInstruction (instruction : string) =
    let command, value =
        match instruction.Split(' ') with
        | [|command; value|] -> command, value |> System.Int32.Parse
        | _ -> invalidArg instruction "bad input"
    match command with
    | "acc" -> Acc value
    | "jmp" -> Jmp value
    | "nop" -> Nop value
    | _ -> invalidArg command "bad input"

let executeInstructions instructions =
    let rec executeInstructions' (v, a) c =
        match Map.tryFind c instructions with
        | Some instruction ->
            if Set.contains (c, instruction) v then
                Unterminated, a
            else
                match instruction with
                | Acc i -> executeInstructions' (Set.add (c, instruction) v, a + i) (c + 1)
                | Jmp i -> executeInstructions' (Set.add (c, instruction) v, a) (c + i)
                | Nop _ -> executeInstructions' (Set.add (c, instruction) v, a) (c + 1)
        | None -> Terminated, a
    executeInstructions' (Set.empty, 0) 0

let swapInstructions instructions =
    let rec swapInstructions instructions c =
        let swapInstruction instructions c =
            let instruction =
                match (Map.find c instructions) with
                | Acc i -> Acc i
                | Jmp i -> Nop i
                | Nop i -> Jmp i
            Map.add c instruction instructions
        match executeInstructions (swapInstruction instructions c) with
        | Terminated, a -> a
        | Unterminated, _ -> swapInstructions instructions (c + 1)
    swapInstructions instructions 0

let instructions =
    System.IO.File.ReadAllLines("./input/input_8.txt")
    |> Array.map parseInstruction
    |> Array.indexed
    |> Map.ofArray

let (_, a) = executeInstructions instructions in printfn "%A" a  // 1548
swapInstructions instructions |> printfn "%A"  // 1375
