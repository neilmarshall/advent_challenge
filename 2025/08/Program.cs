using System.Numerics;

const int CONNECTIONS = 1000;

var junctionBoxes = File.ReadAllLines("input.txt").Select(ParseJunctionBox).ToArray();

var junctionBoxPairsUnordered =
    from box1 in junctionBoxes
    from box2 in junctionBoxes
    where box1 != box2
    select (box1, box2);

var junctionBoxPairs = junctionBoxPairsUnordered
    .DistinctBy(obj => (Vector3.Min(obj.box1, obj.box2), Vector3.Max(obj.box1, obj.box2)))
    .OrderBy(obj => Vector3.Distance(obj.box1, obj.box2))
    .ToArray();

var circuits = new HashSet<HashSet<Vector3>>();
long solutionPartA = 0;
long solutionPartB = 0;
foreach (var (obj, i) in junctionBoxPairs.Select((o, i) => (o, i)))
{
    var circuit1 = circuits.FirstOrDefault(c => c.Contains(obj.box1));
    var circuit2 = circuits.FirstOrDefault(c => c.Contains(obj.box2));

    // no circuit found containing either junction box
    if (circuit1 is null && circuit2 is null)
    {
        var circuit = new HashSet<Vector3>();
        circuit.Add(obj.box1);
        circuit.Add(obj.box2);
        circuits.Add(circuit);
    }
    // both junction boxes are already in existing circuits - possibly the same one
    else if (circuit1 is not null && circuit2 is not null)
    {
        // junction boxes are in different circuits, so we need to merge those circuits
        if (circuit1 != circuit2)
        {
            circuit1.UnionWith(circuit2);
            circuits.Remove(circuit2);
        }
    }
    // one junction box can be found in an existing circuit, and the other cannot
    else
    {
        if (circuit1 is not null)
        {
            circuit1.Add(obj.box1);
            circuit1.Add(obj.box2);
        }
        else if (circuit2 is not null)
        {
            circuit2.Add(obj.box1);
            circuit2.Add(obj.box2);
        }
    }

    if (i == CONNECTIONS)
    {
        solutionPartA = circuits
            .OrderByDescending(c => c.Count)
            .Take(3)
            .Aggregate(1, (a, c) => a * c.Count);
    }

    if (circuits.Count == 1 && circuits.Single().Count == CONNECTIONS)
    {
        solutionPartB = (long)obj.box1.X * (long)obj.box2.X;
        break;
    }
}

Console.WriteLine($"Solution to Part A: {solutionPartA:N0}");  // should be 84,968
Console.WriteLine($"Solution to Part B: {solutionPartB:N0}");  // should be 8,663,467,782

static Vector3 ParseJunctionBox(string rawInput)
{
    var floats = rawInput.Split(',').Select(float.Parse).ToArray();
    if (floats.Length != 3)
        throw new ArgumentException("Invalid input");
    return new Vector3(floats[0], floats[1], floats[2]);
}
