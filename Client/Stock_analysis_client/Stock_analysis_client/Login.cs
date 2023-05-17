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

        public void ClearInput()
        {
            Usernametb.Text = "";
            Passwordtb.Text = "";
        }

        private void SignIn()
        {
            RestClient cls = new RestClient("http://localhost:5000/api/users/login");
            RestRequest request = new RestRequest();
            request.AddParameter("username", Usernametb.Text);
            request.AddParameter("pwd", Passwordtb.Text);

            RestResponse res = cls.Get(request);
            MessageBox.Show(res.ToString());

            try
            {
                RestResponse response = cls.Get(request);
                if (response.StatusCode != System.Net.HttpStatusCode.OK)
                {
                    MessageBox.Show(response.StatusDescription);
                }
                else
                {
                    Response res2 = cls.Deserialize<Response>(response).Data;
                    if (res2.Status != 200)
                    {
                        MessageBox.Show(res2.Message);
                    }
                    else
                    {
                        User u = new User()
                        {
                            Username = Usernametb.Text,
                            Password = Passwordtb.Text
                        };

                        var apiKey = res2.Id.ToString();
                        Console.WriteLine(apiKey);
                        MessageBox.Show(apiKey);

                        new Main(this).Show();
                        this.Hide();
                        ClearInput();
                    }
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
