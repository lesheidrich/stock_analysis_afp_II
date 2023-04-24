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
using RestSharp;
using System.Collections;
using System.Xml.Linq;
using Stock_analysis_client.Properties;


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
            if (PasswordTb.Text != PasswordAgainTb.Text)
            {
                MessageBox.Show("A két jelszó nem egyezik", "Jelszó hiba",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
                PasswordTb.Text = "";
                PasswordAgainTb.Text = "";
            }
            else if (!validateEmailRegex.IsMatch(EmailTb.Text))
            {
                MessageBox.Show("Az E-mail cím hibás formátumú", "E-mail hiba",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
                EmailTb.Text = "";
            }
            else
            {
                /*********** INSERT **************/

                var queryString = new System.Collections.Generic.Dictionary<string, string>()
                   {
                       { "query", "'alfonzo', md5('pwd'), 'apikey', '0', 'email', 'full name'" },
                   };



                RestClient cls = new RestClient("http://localhost:5000/api/users/create");
                RestRequest request = new RestRequest();
                //request.AddObject("query", queryString);
                //PasswordTb.Text, 2134214, 0, EmailTb.Text, "My name is" + UsernameTb.Text
                request.AddParameter("query", "'UsernameTb.Text', md5('PasswordTb.Text'), '2134214', '0', 'EmailTb.Text', 'UsernameTb.Text'");
                //request.AddObject("query", queryString);
                
                //Miután az api register része kész
                
                //request.AddParameter("username", UsernameTb.Text);
                //request.AddParameter("pwd", PasswordTb.Text);
                //request.AddParameter("api_key", 2134214);
                //request.AddParameter("is_admin", 0);
                //request.AddParameter("email", EmailTb.Text);
                //request.AddParameter("full_name", "My name is " + UsernameTb.Text);

                //'alfonzo', md5('pwd'), 'apikey', '0', 'email', 'full name'
                RestResponse res = cls.Get(request);
                MessageBox.Show(res.ToString());


                



                MessageBox.Show("Sikeres regisztráció!", "Sikeres regisztráció",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
                label1.Text = "Regisztrálva";
                label2.Text = UsernameTb.Text;
                label3.Text = EmailTb.Text;
                label4.Text = PasswordTb.Text;
            }

        }

        private void Register_FormClosing(object sender, FormClosingEventArgs e)
        {
            Login.GetInstance().Show();
        }

        private void backBtn_Click(object sender, EventArgs e)
        {
            Login.GetInstance().Show();
            Hide();
        }
    }
}
