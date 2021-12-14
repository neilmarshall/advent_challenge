using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Collections.Generic;
using System.Linq;
using static Polymers.Lib;

namespace Polymers.Fixtures;

[TestClass]
public class BuildPolymerFixtures
{
    [TestMethod]
    public void SampleTests()
    {
        var template = "NNCB";

        var insertionRules = new Dictionary<string, string>
        {
            { "CH", "B" },
            { "HH", "N" },
            { "CB", "H" },
            { "NH", "C" },
            { "HB", "C" },
            { "HC", "B" },
            { "HN", "C" },
            { "NN", "C" },
            { "BH", "H" },
            { "NC", "B" },
            { "NB", "B" },
            { "BN", "B" },
            { "BB", "N" },
            { "BC", "B" },
            { "CC", "N" },
            { "CN", "C" }
        };

        Assert.AreEqual(1588, buildPolymer(template, insertionRules, 10));

        Assert.AreEqual(2188189693529, buildPolymer(template, insertionRules, 40));
    }

    [TestMethod]
    public void InputTests()
    {
        var input = System.IO.File.ReadAllLines("input.txt");

        var template = input.First();

        var insertionRules = input
            .Skip(2)
            .ToDictionary(
                s => s.Split(" -> ").First(),
                s => s.Split(" -> ").Skip(1).First()
            );

        Assert.AreEqual(2010, buildPolymer(template, insertionRules, 10));

        Assert.AreEqual(2437698971143, buildPolymer(template, insertionRules, 40));
    }
}