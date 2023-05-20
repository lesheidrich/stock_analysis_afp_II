using RestSharp;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using RestSharp;

namespace Stock_analysis_client
{
    public partial class Profile : Form
    {
        public Profile(Main main, User u)
        {
            InitializeComponent();
            this.main = main;
            userNameGetLbl.Text = u.Username;
            EMailGetLbl.Text = u.Email;
            passwordGetLbl.Text = u.Password;
            ApiKeyGetLbl.Text = u.API_Key;
            myNameIsLbl.Text = u.User_Name;
        }

        private Main main;


        private void SignOutBtn_Click(object sender, EventArgs e)
        {
            Login.GetInstance().Show();
            Hide();
        }

        private void Register_FormClosing(object sender, FormClosingEventArgs e)
        {
            Login.GetInstance().Show();
        }

    }
}
