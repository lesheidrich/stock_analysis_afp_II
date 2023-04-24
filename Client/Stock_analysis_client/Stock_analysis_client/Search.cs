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

    List<SearchHistoryItem> searchHistory = new List<SearchHistoryItem>();

    private void btnSearch_Click(object sender, EventArgs e)
    {
        // Get the search query from the TextBox control
        string searchQuery = txtSearch.Text;

        // Perform the search using an external data source or API
        MessageBox.Show("You searched for: " + searchQuery);

        // Add the search query and time to the search history
        SearchHistoryItem searchItem = new SearchHistoryItem
        {
            SearchQuery = searchQuery,
            SearchTime = DateTime.Now
        };
        searchHistory.Add(searchItem);

        // Clear the search query from the TextBox control
        txtSearch.Clear();
    }

    private void btnViewHistory_Click(object sender, EventArgs e)
    {
        // Create a new Form to display the search history
        SearchHistoryForm historyForm = new SearchHistoryForm();

        // Bind the search history list
        historyForm.dgvHistory.DataSource = searchHistory;

        // Show the Form as a dialog
        historyForm.ShowDialog();
    }
}