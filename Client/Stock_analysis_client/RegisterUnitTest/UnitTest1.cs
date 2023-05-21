using Microsoft.VisualStudio.TestTools.UnitTesting;
using Stock_analysis_client;
using System;
using System.Text.RegularExpressions;

namespace RegisterUnitTest
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void PWTest1()
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

        [TestMethod]
        public void PWTest2()
        {
            Register register = new Register();
            string a = "alma";
            string b = "körte";
            bool expected;
            if (a == b)
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(register.PwEqual(a, b), expected);
        }

        

        [TestMethod]
        public void EmailTest1()
        {
            Regex validateEmailRegex = new Regex("^\\S+@\\S+\\.\\S+$");

            Register register = new Register();
            string email = "valami@valami.com";
            bool expected;
            if (validateEmailRegex.IsMatch(email))
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(register.ValidateEmail(email), expected);
        }

        [TestMethod]
        public void EmailTest2()
        {
            Regex validateEmailRegex = new Regex("^\\S+@\\S+\\.\\S+$");

            Register register = new Register();
            string email = "valamivalamicom";
            bool expected;
            if (validateEmailRegex.IsMatch(email))
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(register.ValidateEmail(email), expected);
        }

        [TestMethod]
        public void TestBoxEmptyTest1()
        {
            Register register = new Register();
            string textbox = "";
            bool expected;
            if (textbox == "")
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(register.TextboxIsEmpty(textbox), expected);

        }

        [TestMethod]
        public void TestBoxEmptyTest2()
        {
            Register register = new Register();
            string textbox = "asd";
            bool expected;
            if (textbox == "")
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(register.TextboxIsEmpty(textbox), expected);

        }
    }
}
