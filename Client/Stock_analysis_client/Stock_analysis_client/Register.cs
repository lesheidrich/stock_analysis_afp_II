using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Text.RegularExpressions;

namespace Stock_analysis_client
{
    public partial class Register : Form
    {
        public Register()
        {
            InitializeComponent();
            label1.Text = " ";
            label2.Text = " ";
            label3.Text = " ";
            label4.Text = " ";
        }

        Regex validateEmailRegex = new Regex("^\\S+@\\S+\\.\\S+$");
        

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox3.Text != textBox4.Text)
            {
                MessageBox.Show("A két jelszó nem egyezik", "Jelszó hiba",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox3.Text = "";
                textBox4.Text = "";
            }
            else if (!validateEmailRegex.IsMatch(textBox2.Text))
            {
                MessageBox.Show("Az E-mail cím hibás formátumú", "E-mail hiba",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox2.Text = "";
            }
            else
            {
                MessageBox.Show("Sikeres regisztráció!", "Sikeres regisztráció",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
                label1.Text = "Regisztrálva";
                label2.Text = textBox1.Text;
                label3.Text = textBox2.Text;
                label4.Text = textBox3.Text;
            }

        }


    }
}
