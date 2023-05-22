using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using Stock_analysis_client;
using System.Text.RegularExpressions;

namespace LoginUnitTest
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TextBoxEmptyTest1()
        {
            Login login = new Login();
            string text = "";
            bool expected;
            if (text == "")
            {
                expected = true;
            }
            else
            {
                expected= false;
            }
            Assert.AreEqual(login.TextBoxIsEmpty(text), expected);
        }
        public void TextBoxEmptyTest2()
        {
            Login login = new Login();
            string text = "valami";
            bool expected;
            if (text == "")
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(login.TextBoxIsEmpty(text), expected);
        }

        public void TextBoxLength1()
        {
            Login login = new Login();
            string text = "valami";
            bool expected;
            if (text.Length > 20)
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(login.TextBoxLenght(text), expected);
        }

        public void TextBoxLength2()
        {
            Login login = new Login();
            string text = "valamitidekellirjakhogytöbblegyenmint20";
            bool expected;
            if (text.Length > 20)
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(login.TextBoxLenght(text), expected);
        }

        public void TextBoxStartsWith1()
        {
            Login login = new Login();
            string text = "valami";
            bool expected;
            if (text.StartsWith("."))
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(login.TextBoxLenght(text), expected);
        }

        public void TextBoxStartsWith2()
        {
            Login login = new Login();
            string text = ".valami";
            bool expected;
            if (text.StartsWith("."))
            {
                expected = true;
            }
            else
            {
                expected = false;
            }
            Assert.AreEqual(login.TextBoxLenght(text), expected);
        }
    }
}
