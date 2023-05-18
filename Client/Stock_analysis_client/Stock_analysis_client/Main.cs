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
        private string apiKey;
        public Main(Login login, string apiKey)
        {
            InitializeComponent();
            this.apiKey = apiKey;
            this.login = login;
            sparta.Text = apiKey;
            label1.Text = "fuck you";
        }
        private Login login;
    }
}