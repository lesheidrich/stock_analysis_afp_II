using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using RestSharp;

namespace Stock_analysis_client
{
    public partial class Login : Form
    {
        HttpClient client = new HttpClient();

        private static Login instance;
        public static Login GetInstance()
        {
            if (instance == null)
            {
                instance = new Login();
            }
            return instance;
        }

        private Login()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Loginbt_Click(object sender, EventArgs e)
        {
            RestClient cls = new RestClient("http://localhost:5000/api/users/login");
            RestRequest request = new RestRequest();
            request.AddParameter("username", Usernametb.Text);
            request.AddParameter("pwd", Passwordtb.Text);

            RestResponse res = cls.Get(request);
            MessageBox.Show(res.ToString());

        }

        private void SingUpbt_Click(object sender, EventArgs e)
        {
           new Register().Show();
            Hide();
        }

        private void Usernametb_TextChanged(object sender, EventArgs e)
        {

        }

        private void Passwordtb_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
