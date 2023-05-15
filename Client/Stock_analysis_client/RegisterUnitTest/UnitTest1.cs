using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using Stock_analysis_client;

namespace RegisterUnitTest
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void Button()
        {
            Register register = new Register();
            string a = "alma";
            string b = "alma";
            bool expected;
            if (a == b)
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            register.PwEqual(a, b);
            Assert.AreEqual(register.PwEqual(a, b), expected);
        }
    }
}
