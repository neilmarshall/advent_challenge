(*
Monkey 0:
  Starting items: 50, 70, 89, 75, 66, 66
  Operation: new = old * 5
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 1:
  Starting items: 85
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 6

Monkey 2:
  Starting items: 66, 51, 71, 76, 58, 55, 58, 60
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 79, 52, 55, 51
  Operation: new = old + 6
  Test: divisible by 3
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 4:
  Starting items: 69, 92
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 5:
  Starting items: 71, 76, 73, 98, 67, 79, 99
  Operation: new = old + 8
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 6:
  Starting items: 82, 76, 69, 69, 57
  Operation: new = old + 7
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 7:
  Starting items: 65, 79, 86
  Operation: new = old + 5
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 0
*)
open Microsoft.FSharp.Core.Operators.Checked

type Monkey = { Items : ResizeArray<int64>; Operation : int64 -> int64; Test : int64 -> int; mutable Inspections : int64 }
type ReductionFactor = | Divisor of int64 | Modulo of int64

let monkeys () = [|
    { Items = ResizeArray<int64>(seq {50L; 70L; 89L; 75L; 66L; 66L}); Operation = (*) 5L; Test = (fun n -> if n % 2L = 0L then 2 else 1); Inspections = 0L }
    { Items = ResizeArray<int64>(seq {85L}); Operation = (fun n -> n * n); Test = (fun n -> if n % 7L = 0L then 3 else 6); Inspections = 0L }
    { Items = ResizeArray<int64>(seq {66L; 51L; 71L; 76L; 58L; 55L; 58L; 60L}); Operation = (+) 1L; Test = (fun n -> if n % 13L = 0L then 1 else 3); Inspections = 0L }
    { Items = ResizeArray<int64>(seq {79L; 52L; 55L; 51L}); Operation = (+) 6L; Test = (fun n -> if n % 3L = 0L then 6 else 4); Inspections = 0L }
    { Items = ResizeArray<int64>(seq {69L; 92L}); Operation = (*) 17L; Test = (fun n -> if n % 19L = 0L then 7 else 5); Inspections = 0L }
    { Items = ResizeArray<int64>(seq {71L; 76L; 73L; 98L; 67L; 79L; 99L}); Operation = (+) 8L; Test = (fun n -> if n % 5L = 0L then 0 else 2); Inspections = 0L }
    { Items = ResizeArray<int64>(seq {82L; 76L; 69L; 69L; 57L}); Operation = (+) 7L; Test = (fun n -> if n % 11L = 0L then 7 else 4); Inspections = 0L }
    { Items = ResizeArray<int64>(seq {65L; 79L; 86L}); Operation = (+) 5L; Test = (fun n -> if n % 17L = 0L then 5 else 0); Inspections = 0L }
|]

let stepThroughRounds rounds reductionFactor (monkeys : Monkey[]) =
    let stepThroughRound monkey =
        for worryValue in monkey.Items do
            monkey.Inspections <- monkey.Inspections + 1L
            let worryValue =
                match reductionFactor with
                | Divisor n -> monkey.Operation worryValue / n
                | Modulo n -> monkey.Operation worryValue % n
            monkeys[monkey.Test worryValue].Items.Add(worryValue)
        monkey.Items.Clear()
    for _ in [1..rounds] do
        Array.iter stepThroughRound monkeys 
    monkeys

monkeys()
|> stepThroughRounds 20 (Divisor 3L)
|> Seq.sortByDescending (fun m -> m.Inspections)
|> Seq.take 2
|> Seq.fold (fun s t -> s * t.Inspections) 1L
|> printfn "Answer to Part One: %d"  // expected output is 151,312

monkeys()
|> stepThroughRounds 10_000 (Modulo (2L * 7L * 13L * 3L * 19L * 5L * 11L * 17L))
|> Seq.sortByDescending (fun m -> m.Inspections)
|> Seq.take 2
|> Seq.fold (fun s t -> s * t.Inspections) 1L
|> printfn "Answer to Part Two: %d"  // expected output is 51,382,025,916