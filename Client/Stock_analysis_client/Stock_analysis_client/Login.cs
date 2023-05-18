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
        string thisisspartaaa;
        //HttpClient client = new HttpClient();
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



        //public async void spartaaaa()
        //{
        //    var client = new HttpClient();

        //    var queryString = new Dictionary<string, string>()
        //    {
        //        { "username", "jenna" },
        //        { "pwd", "pwd" }
        //    };

        //    var requestUrl = new UriBuilder("http://localhost:5000/api/users/login");
        //    requestUrl.Query = new FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

        //    var response = await client.GetAsync(requestUrl.ToString());
        //    response.EnsureSuccessStatusCode();

        //    var jsonResponse = await response.Content.ReadAsStringAsync();

        //    using (var document = JsonDocument.Parse(jsonResponse))
        //    {
        //        var root = document.RootElement;
        //        var apiKey = root.GetProperty("api_key").GetString();

        //        thisisspartaaa =  apiKey;
        //    }
        //}




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
            //RestClient cls = new RestClient("http://localhost:5000/api/users/login");
            RestRequest request = new RestRequest();
            request.AddParameter("username", Usernametb.Text);
            request.AddParameter("pwd", Passwordtb.Text);

            //RestResponse res = loginClient.Get(request);
            //MessageBox.Show(res.ToString());

            try
            {
                RestResponse response = loginClient.Get(request);
                if (response.StatusCode != System.Net.HttpStatusCode.OK)
                {
                    MessageBox.Show(response.StatusDescription);
                    thisisspartaaa = "1";
                }
                else
                {
                    Response res2 = loginClient.Deserialize<Response>(response).Data;
                    if (res2.Status != 200)
                    {
                        thisisspartaaa = "2";
                    }
                    else
                    {
                        //User u = new User()
                        //{
                        //    Username = Usernametb.Text,
                        //    Password = Passwordtb.Text
                        //};

                        //var apiKey = res2.Id.ToString();
                        //Console.WriteLine(apiKey);
                        //MessageBox.Show(apiKey);
                        thisisspartaaa = "3";

                        new Main(this, thisisspartaaa).Show();
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
