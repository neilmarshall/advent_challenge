let countVisibleTrees input =
    let height, width = Array.length input, String.length <| Array.head input

    let forest, mask = Array2D.zeroCreate<int> height width, Array2D.create height width 1

    for i in [0 .. height - 1] do
        for j in [0 .. width - 1] do
            forest[i, j] <- int(string(input[i][j]))

    let masker h w t =
        let isMasked = Array.exists ((<=) t)
        if (h > 0 && h < height - 1) && (w > 0 && w < width - 1) then
            let dimensions = seq {
                forest[..h-1, w]
                forest[h+1.., w]
                forest[h, ..w-1]
                forest[h, w+1..]
            }
            if Seq.forall isMasked dimensions then mask[h, w] <- 0

    let array2DSum arr =
        let mutable sum = 0
        arr |> Array2D.iter (fun t -> sum <- sum + t)
        sum

    forest |> Array2D.iteri masker
    mask |> array2DSum

let getScenicScore input =
    let height, width = Array.length input, String.length <| Array.head input

    let forest, scores = Array2D.zeroCreate<int> height width, Array2D.zeroCreate<int> height width

    for i in [0 .. height - 1] do
        for j in [0 .. width - 1] do
            forest[i, j] <- int(string(input[i][j]))

    let scorer h w t =
        let scoreDimension (dimension : int[]) =
            let reducer (total, cont) n =
                if cont then (total + 1, n < t) else (total, false)
            Array.fold reducer (0, true) dimension |> fst
        if (h > 0 && h < height - 1) && (w > 0 && w < width - 1) then
            let dimensions = seq {
                forest[..h-1, w] |> Array.rev
                forest[h+1.., w]
                forest[h, ..w-1] |> Array.rev
                forest[h, w+1..]
            }
            scores[h, w] <- dimensions |> Seq.map scoreDimension |> Seq.reduce (*)

    let array2DMax arr =
        let mutable max = 0
        arr |> Array2D.iter (fun t -> if t > max then max <- t)
        max

    forest |> Array2D.iteri scorer
    scores |> array2DMax

let input = System.IO.File.ReadLines("input.txt") |> Seq.toArray

input |> countVisibleTrees |> printfn "Answer to Part One: %d"  // expected output is 1,733
input |> getScenicScore |> printfn "Answer to Part Two: %d"  // expected output is 284,648