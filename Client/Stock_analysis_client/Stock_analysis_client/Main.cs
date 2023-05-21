using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.Serialization;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using RestSharp;

namespace Stock_analysis_client
{
    public partial class Main : Form
    {
        
        public Main(Login login, User user)
        {
            InitializeComponent();
            InitializeNewsDG();
            RefreshNewsDG();
            this.apiKey = user.API_Key;
            this.login = login;
            this.user = user;
            if (apiKey is null)
            {
                apikeylb.Text = "null";
            }
            usernamelb.Text = $"Welcome {user.Username}";
            apikeylb.Text = $"Your API key: {apiKey}";
        }
        private Login login;
        private string apiKey;
        private User user;



        public void InitializeNewsDG()
        {
            newsdg.Columns.Add("content", "content");
        }

        public void RefreshNewsDG()
        {
            RestClient mainClient = new RestClient("http://localhost:5000/api/news");
            RestRequest request = new RestRequest();
            request.AddParameter("api_key", apiKey);


            try
            {
                RestResponse response = mainClient.Get(request);
                if (response.StatusCode != System.Net.HttpStatusCode.OK)
                {
                    MessageBox.Show(response.StatusDescription);
                }
                else
                {
                    Response res = mainClient.Deserialize<Response>(response).Data;
                    if (res.Status != 200)
                    {
                        MessageBox.Show(res.Message);
                    }
                    else
                    {
                        newsdg.Rows.Clear();
                        newsdg.Rows.Add(res.Results);

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

        private void Main_Load(object sender, EventArgs e)
        {

        }

        private void ProfileBox_Click(object sender, EventArgs e)
        {
            new Profile(this, user).Show();
        }

        private void tickerbt_Click(object sender, EventArgs e)
        {
            new TickerInfo(this, apiKey).Show();
        }

    }
}