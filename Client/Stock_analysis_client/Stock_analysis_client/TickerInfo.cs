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
    public partial class TickerInfo : Form
    {
        public TickerInfo(Main main, string apikey)
        {
            InitializeComponent();
            this.main = main;
            this.apiKey = apikey;
        }

        private string apiKey;
        private Main main;
    }
}
