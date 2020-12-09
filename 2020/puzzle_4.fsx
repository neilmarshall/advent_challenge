open System
open System.IO
open System.Text.RegularExpressions

let data = File.ReadAllLines("./input/input_4.txt") |> List.ofArray

let parse data =
    let rec parse data acc =
        match data with
        | [] -> acc
        | _ ->
            match List.tryFindIndex ((=) String.Empty) data with
            | Some i ->
                let row = data |> List.take i |> String.concat " "
                parse (List.skip (i + 1) data) (row::acc)
            | None -> (data |> String.concat " ")::acc
    parse data []

let basicValidator (s : string) =
    let parts = s.Split(' ') |> Array.map (fun p -> p.Substring(0, 3)) |> Set.ofArray
    ["byr"; "ecl"; "eyr"; "hcl"; "hgt"; "iyr"; "pid"]
    |> List.forall (fun p -> Set.contains p parts)

let rangeValidator minValue maxValue regex (groupKey : string) s =
    let m = Regex(regex).Match(s)
    match m.Success with
    | true -> let value = Int32.Parse(m.Groups.[groupKey].Value) in value >= minValue && value <= maxValue
    | _ -> false

type Unit = | CM | IN
let (|HGT|_|) minYear maxYear unit s =
    let (|HGTCM|_|) s = if rangeValidator minYear maxYear "^hgt:(?<value>\d{2,3})cm$" "value" s then Some HGTCM else None
    let (|HGTIN|_|) s = if rangeValidator minYear maxYear "^hgt:(?<value>\d{2,3})in$" "value" s then Some HGTIN else None
    match unit, s with
    | CM, HGTCM -> Some HGT
    | IN, HGTIN -> Some HGT
    | _ -> None
let (|BYR|_|) minYear maxYear s = if rangeValidator minYear maxYear "^byr:(?<year>\d{4})$" "year" s then Some BYR else None
let (|IYR|_|) minYear maxYear s = if rangeValidator minYear maxYear "^iyr:(?<year>\d{4})$" "year" s then Some IYR else None
let (|EYR|_|) minYear maxYear s = if rangeValidator minYear maxYear "^eyr:(?<year>\d{4})$" "year" s then Some EYR else None
let (|HCL|_|) s = if Regex("^hcl:#[0-9-a-z]{6}$").Match(s).Success then Some HCL else None
let (|ECL|_|) s = if Regex("^ecl:(amb|blu|brn|gry|grn|hzl|oth)$").Match(s).Success then Some ECL else None
let (|PID|_|) s = if Regex("^pid:\d{9}$").Match(s).Success then Some PID else None
let (|CID|_|) s = if Regex("^cid:\w+$").Match(s).Success then Some CID else None

let advancedValidator s =
    if basicValidator s
        then
            let validator = function
                | BYR 1920 2002 | IYR 2010 2020 | EYR 2020 2030 | HGT  150 193 CM | HGT  59 76 IN | HCL | ECL | PID | CID -> true
                | _ -> false
            s.Split(' ') |> Array.forall validator
        else false

let data' = parse data
data' |> List.filter basicValidator |> List.length |> printfn "%d"  // should be 247
data' |> List.filter advancedValidator |> List.length |> printfn "%d"  // should be 145
