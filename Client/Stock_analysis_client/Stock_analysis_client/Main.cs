﻿using System;
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
        public Main(Login login)
        {
            InitializeComponent();
            this.login = login;
        }
        private Login login;
    }
}
