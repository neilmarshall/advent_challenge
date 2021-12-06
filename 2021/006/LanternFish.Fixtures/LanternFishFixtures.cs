using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LanternFish.Fixtures;

[TestClass]
public class LanternFishFixtures
{
    [TestMethod]
    public void TestCountFish()
    {
        var initialState = new[] { 3, 4, 3, 1, 2 };
        Assert.AreEqual(26, LanternFishLib.CountFish(initialState, 18));
        Assert.AreEqual(5934, LanternFishLib.CountFish(initialState, 80));
        Assert.AreEqual(26984457539, LanternFishLib.CountFish(initialState, 256));
    }
}