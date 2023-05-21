using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Runtime.Serialization;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows.Forms;
using RestSharp;

namespace Stock_analysis_client
{
    public partial class Login : Form
    {
        RestClient loginClient = new RestClient("http://localhost:5000/api/users/login");
        public Login()
        {
            InitializeComponent();
        }

        public void ClearContents()
        {
            Usernametb.Clear();
            Passwordtb.Clear();
            Usernametb.Focus();
        }


        private static Login instance;
        public static Login GetInstance()
        {
            if (instance == null)
            {
                instance = new Login();
            }
            return instance;
        }

        private void Loginbt_Click(object sender, EventArgs e)
        {
            SignIn();
        }

        private void SignIn()
        {
            RestRequest request = new RestRequest();
            request.AddParameter("username", Usernametb.Text);
            request.AddParameter("pwd", Passwordtb.Text);


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
                    if (res.Status != 200)
                    {
                        MessageBox.Show(res.Message);   
                    }
                    else
                    {
                        User user = new User()
                        {
                            Username = Usernametb.Text,
                            Password = Passwordtb.Text,
                            API_Key = res.API_Key,
                            //Email = res.Users[0].Email,
                            //Id = res.Id,
                            //Email = res.Users[1].Email,
                            //IsAdmin = res.Users[1].IsAdmin,
                            //User_Name = res.Users[1].User_Name,

                        };
                        new Main(this, user).Show();
                        this.Hide();
                        ClearContents();
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

        private void label1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            if (Passwordtb.PasswordChar == '*')
            {
                Passwordtb.PasswordChar = '\0';
            }
            else
            {
                Passwordtb.PasswordChar = '*';
            }
        }
    }
}
