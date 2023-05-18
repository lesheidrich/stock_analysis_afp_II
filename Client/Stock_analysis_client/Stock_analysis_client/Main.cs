using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Stock_analysis_client
{
    public partial class Main : Form
    {
        public Main(Login login, string username, string pwd,string api_key)
        {
            InitializeComponent();
            this.login = login;
            this.un = username;
            this.pw = pwd;
            this.api = api_key;
        }
        private Login login;
        private string un;
        private string pw;
        private string api;

        private void Main_FormClosing(object sender, FormClosingEventArgs e)
        {
            login.Show();
        }
    }
}
