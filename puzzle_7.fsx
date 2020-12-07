open System
open System.IO
open System.Text.RegularExpressions

type NestedBag = | Bag of string | NestedBag of (string * ((int * NestedBag) list))
type BagMap = | BagMap of Map<string, NestedBag>

let parseData d =
    let parse s =
        let m = Regex("^(?<key>\w+ \w+) bags contain( no other bags|(?<values> \d+ (\w+ \w+) bags?,?)*)\.$").Match(s)
        if m.Success then
            let getCount (s : string) = s.Split(' ') |> Seq.head |> Int32.Parse
            let getColour (s : string) = s.Split(' ') |> Seq.skip 1 |> Seq.take 2 |> String.concat " "
            let values = [for c in m.Groups.["values"].Captures -> let v = c.Value.Replace(',', ' ').Trim() in getCount v, getColour v]
            m.Groups.["key"].Value, values
        else
            failwith <| sprintf "could not parse instruction: %s" s
    let rec buildColourTree (m : Map<string, (int * string) list>) (s : string, l : (int * string) list) =
        match l with
        | [] -> Bag s
        | _ -> NestedBag(s, l |> List.map (fun (i, s) -> i, buildColourTree m (s, (Map.find s m))))
    let m = d |> Array.map parse |> Map.ofArray
    m |> Map.map (fun k t -> buildColourTree m (k, t)) |> BagMap

let countBags (BagMap bagMap) bag =
    let rec canHoldColour (BagMap bagMap) baseBag bag =
        match Map.find baseBag bagMap with
        | Bag _ -> false
        | NestedBag (_, l) ->
            if l |> List.exists (fun (_, ct) -> match ct with | NestedBag (s, _) | Bag s -> s = bag)
                then true
                else l |> List.exists (fun (_, ct) -> match ct with | NestedBag (s, _) -> canHoldColour (BagMap bagMap) s bag | _ -> false)
    bagMap |> Map.filter (fun k _ -> canHoldColour (BagMap bagMap) k bag) |> Map.count

let countNestedBags (BagMap bagMap) =
    let rec countNestedBags acc bag =
        match Map.find bag bagMap with
        | Bag _ -> acc
        | NestedBag (_, l) -> acc + (l |> List.map (fun (i, ct) -> i * match ct with | NestedBag (s, _) -> (countNestedBags 1 s) | _ -> 1) |> List.sum)
    countNestedBags 0

let data = File.ReadAllLines("./input_7.txt") |> parseData
countBags data "shiny gold" |> printfn "%d"  // 378
countNestedBags data "shiny gold" |> printfn "%d"  // 27526
