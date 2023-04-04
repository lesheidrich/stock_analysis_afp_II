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
    public partial class Search : Form1
    {
        public TextBox SearchResultsTextBox { get; set; }
        public string SearchContent { get; set; }
        public Search()
        {
            InitializeComponent();

            this.SearchResultsTextBox = new System.Windows.Forms.TextBox();
            this.SearchContent = new System.Windows.Forms.Content

            this.SearchResultsTextBox.Text = this.SearchContent;
        }
        private void InitializeComponent()
        {
            throw new NotImplementedException();
        }
    }
}
