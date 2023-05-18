using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Runtime.Serialization;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using RestSharp;

namespace Stock_analysis_client
{
    public partial class Login : Form
    {
        //HttpClient client = new HttpClient();
        RestClient loginClient = new RestClient("http://localhost:5000/api/users/login");

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

        public void ClearContents()
        {
            Usernametb.Clear();
            Passwordtb.Clear();
            Usernametb.Focus();
        }

        private void SignIn()
        {
            RestRequest request = new RestRequest();
            request.AddParameter("username", Usernametb.Text);
            request.AddParameter("pwd", Passwordtb.Text);

            //RestResponse res = cls.Get(request);
            //MessageBox.Show(res.ToString());

            try
            {
                RestResponse response = loginClient.Get(request);
                if (response.StatusCode != System.Net.HttpStatusCode.OK)
                {
                    MessageBox.Show(response.StatusDescription);
                }
                else
                {
                    Response res = loginClient.Deserialize<Response>(response).Data;
                    if (res.Success != 200)
                    {
                        MessageBox.Show(res.Message);
                    }
                    else
                    {
                        Main mainView = new Main(this, Usernametb.Text, Passwordtb.Text, res.API_Key);
                        mainView.Show();
                      
                        this.Hide();
                    }
                    ClearContents();
                }
            }
            catch (DeserializationException)
            {
                MessageBox.Show("Deserialization error", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (Exception)
            {
                MessageBox.Show("Unknown error", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void Loginbt_Click(object sender, EventArgs e)
        {
            SignIn();
        }
        private void EnterPressed(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                SignIn();
            }
        }

        private void SingUpbt_Click(object sender, EventArgs e)
        {
           new Register().Show();
            Hide();
        }

    }
}
