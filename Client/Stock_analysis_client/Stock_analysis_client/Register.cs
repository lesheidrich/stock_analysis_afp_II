﻿using System;
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
        }

        public bool TextboxIsEmpty(string text)
        {
            if (text == "")
            {
                return true;
            }
            return false;
        }

        public bool ValidateEmail(string email)
        {
            Regex validateEmailRegex = new Regex("^\\S+@\\S+\\.\\S+$");
            if (validateEmailRegex.IsMatch(email))
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        
        

        public bool PwEqual(string a, string b)
        {
            if (a == b)
            {
                return true;
            }
            return false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if ((TextboxIsEmpty(UsernameTb.Text) || TextboxIsEmpty(EmailTb.Text) ||
                TextboxIsEmpty(PasswordTb.Text) || TextboxIsEmpty(PasswordAgainTb.Text)
                || TextboxIsEmpty(ApiKeyTB.Text)))
            {
                MessageBox.Show("Minegyik mezőt ki kell tölteni", "Kitöltés hiba",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else if (!PwEqual(PasswordTb.Text, PasswordAgainTb.Text))
            {
                MessageBox.Show("A két jelszó nem egyezik", "Jelszó hiba",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
                PasswordTb.Text = "";
                PasswordAgainTb.Text = "";
            }
            else if (!ValidateEmail(EmailTb.Text))
            {
                MessageBox.Show("Az E-mail cím hibás formátumú", "E-mail hiba",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
                EmailTb.Text = "";
            }
            else
            {


                RestClient cls = new RestClient("http://localhost:5000/api/users/create");
                RestRequest request = new RestRequest();

                request.AddQueryParameter("name", UsernameTb.Text);
                request.AddQueryParameter("pwd", PasswordTb.Text);
                request.AddQueryParameter("api_key", ApiKeyTB.Text);
                request.AddQueryParameter("is_admin", 0);
                request.AddQueryParameter("email", EmailTb.Text);
                request.AddQueryParameter("full_name", "My name is " + UsernameTb.Text);

                RestResponse res = cls.Post(request);

                MessageBox.Show("Sikeres regisztráció!", "Sikeres regisztráció", MessageBoxButtons.OK, MessageBoxIcon.Information);

                MessageBox.Show(res.ToString());
                try
                {
                    RestResponse response = cls.Post(request);
                    if (response.StatusCode != System.Net.HttpStatusCode.OK)
                    {
                        MessageBox.Show(response.StatusDescription);
                    }
                    else
                    {

                        Response res2 = cls.Deserialize<Response>(response).Data;
                        if (res2.Success)
                        {
                            MessageBox.Show("Sikeres regisztráció!", "Sikeres regisztráció",
                            MessageBoxButtons.OK, MessageBoxIcon.Information);
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


                Login.GetInstance().Show();
                Hide();
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
