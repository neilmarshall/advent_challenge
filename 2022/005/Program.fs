open System.Text.RegularExpressions

let parseRows reverseOrder rows =
    let (|StackLayout|StackCount|MoveInstruction|Blank|) (s : string) =
        if System.String.IsNullOrWhiteSpace(s) then Blank
        else if Regex.IsMatch(s, "\[\w\]") then StackLayout
        else if s.StartsWith("move") then MoveInstruction
        else StackCount

    let rec parseStackLayout row =
        match row with
        | "" -> Seq.empty
        | s when System.String.IsNullOrWhiteSpace(s[..3]) -> seq { yield None; yield! parseStackLayout s[4..] }
        | s when Regex.IsMatch(s, "^ ?\[\w\]") -> seq { yield Some s[1]; yield! parseStackLayout s[4..] }
        | _ -> failwith "invalid input"

    let optionStacks = ResizeArray<ResizeArray<char option>>()
    let stacks = ResizeArray<ResizeArray<char>>()

    let parseRow row =
        match row with
        | StackLayout ->
            let stackLayout = parseStackLayout row
            if optionStacks.Count = 0 then for _ in stackLayout do optionStacks.Add(ResizeArray<char option>())
            stackLayout |> Seq.iteri (fun i t -> optionStacks[i].Add(t))
        | StackCount ->
            let optionExtractor = Seq.filter Option.isSome >> Seq.map Option.get
            optionStacks |> Seq.iteri (fun i t -> t.Reverse(); stacks.Add(ResizeArray<char>(t |> optionExtractor)))
        | Blank -> ()
        | MoveInstruction ->
            let groups = Regex.Match(row, "move (?<count>\d+) from (?<source>\d+) to (?<destination>\d+)").Groups
            let count, source, destination = int(groups["count"].Value), int(groups["source"].Value) - 1, int(groups["destination"].Value) - 1
            let source, destination = stacks[source], stacks[destination]
            if reverseOrder then
                for i in [count.. -1 ..1] do
                    destination.Add(source[source.Count - i])
                for i in [count.. -1 ..1] do
                    source.RemoveAt(source.Count - i)
            else
                for _ in [1 .. count] do
                    destination.Add(source[source.Count - 1])
                    source.RemoveAt(source.Count - 1)
    rows |> Seq.iter parseRow

    stacks

let input = System.IO.File.ReadLines("input.txt")
input |> parseRows false |> Seq.map (Seq.last >> string) |> String.concat "" |> printfn "Answer to Part One: %s"  // expected output is BSDMQFLSP
input |> parseRows true |> Seq.map (Seq.last >> string) |> String.concat "" |> printfn "Answer to Part Two: %s"  // expected output is PGSQBFLDP