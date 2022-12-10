let parseInstructions (instructions : seq<string>) =
    seq {
        let mutable step, registerValue = 1, 1
        yield step, registerValue
        for instruction in instructions do
            step <- step + 1
            yield step, registerValue
            match instruction.Split(" ", 2) with
            | [| "addx"; n |] ->
                step <- step + 1
                registerValue <- registerValue + int(n)
                yield step, registerValue
            | _ -> ()
    }

let instructions = System.IO.File.ReadLines("input.txt") |> Seq.toList

instructions
|> parseInstructions
|> Seq.filter (fun (step, _) -> step % 40 = 20)
|> Seq.sumBy (fun (step, registerValue) -> step * registerValue)
|> printfn "Answer to Part One: %d"  // expected output is 14,720

printfn "Answer to Part Two:"  // should print 'FZBPBFZF' to the console
instructions
|> parseInstructions
|> Seq.iter (
    fun (step, registerValue) ->
        let position = (step - 1) % 40
        if position >= registerValue - 1 && position <= registerValue + 1
            then printf "#"
            else printf "."
        if step % 40 = 0 then printf "\n"
)