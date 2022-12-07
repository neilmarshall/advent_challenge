open System.Collections.Generic

type Element = | Directory of Dictionary<string, Element> | File of int

let rec getElementSize = function
    | Directory d -> d.Values |> Seq.map getElementSize |> Seq.sum
    | File f -> f

let rec getDirectories = function
    | Directory d ->
        seq {
            yield Directory d;
            for e in d.Values do
                yield! getDirectories e
        }
    | File _ -> Seq.empty

let rec parseInstructions (instructions : string list) (rootDirectory : Element) (cwd : Element) (fullPath : string list) =
    match instructions with
    | instruction::tail ->
        if instruction = "$ cd /" then
            parseInstructions tail (rootDirectory : Element) rootDirectory []
        elif instruction = "$ cd .." then
            let folder e t =
                match e with
                | Directory d -> d[t]
                | _ -> failwith  "root directory MUST be of type 'Directory'"
            match fullPath with
            | [] ->
                parseInstructions tail rootDirectory rootDirectory fullPath
            | _::fullPath ->
                let newDirectory =
                    fullPath
                    |> Seq.rev
                    |> Seq.fold folder rootDirectory
                parseInstructions tail rootDirectory newDirectory fullPath
        elif instruction.StartsWith("$ cd ") then
            let newDirectory =
                match cwd with
                | Directory d -> d[instruction[5..]]
                | _ -> failwith "current working directory MUST be of type 'Directory'"
            parseInstructions tail rootDirectory newDirectory (instruction[5..]::fullPath)
        elif instruction = "$ ls" then
            parseInstructions tail (rootDirectory : Element) cwd fullPath
        elif instruction.StartsWith("dir ") then
            match instruction.Split(" ", 2) with
            | [| _; k |] ->
                match cwd with
                | Directory d -> d.Add(k, Directory <| Dictionary<string, Element>())
                | _ -> failwith "current working directory MUST be of type 'Directory'"
                parseInstructions tail rootDirectory cwd fullPath
            | _ -> invalidArg instruction "invalid format for 'dir' instruction"
        else
            match instruction.Split(" ", 2) with
            | [| fileSize; fileName |] ->
                let parseResult, fileSize = System.Int32.TryParse(fileSize)
                if parseResult then
                    match cwd with
                    | Directory d -> d.Add(fileName, File fileSize)
                    | _ -> failwith "current working directory MUST be of type 'Directory'"
                    parseInstructions tail rootDirectory cwd fullPath
                else
                    invalidArg instruction "invalid format for 'file' instruction (could not parse file size)"
            | _ -> invalidArg instruction "invalid format for 'file' instruction"
    | [] -> rootDirectory

let instructions = System.IO.File.ReadLines("input.txt")

let rootDirectory = Directory (Dictionary<string, Element>())

let parsedDirectory = parseInstructions (instructions |> Seq.toList) rootDirectory rootDirectory []

parsedDirectory
|> getDirectories
|> Seq.map getElementSize
|> Seq.filter ((>) 100000)
|> Seq.sum
|> printfn "Answer to Part One: %d"  // expected output is 1,501,149

let unusedSpace= 70_000_000 - getElementSize parsedDirectory
parsedDirectory
|> getDirectories
|> Seq.map getElementSize
|> Seq.filter ((+) unusedSpace >> (<) 30_000_000)
|> Seq.min
|> printfn "Answer to Part Two: %d"  // expected output is 10_096_985
