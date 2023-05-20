namespace Stock_analysis_client
{
    partial class Main
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Main));
            this.apikeylb = new System.Windows.Forms.Label();
            this.ProfileBox = new System.Windows.Forms.PictureBox();
            this.tickerbt = new System.Windows.Forms.Button();
            this.usernamelb = new System.Windows.Forms.Label();
            this.newslb = new System.Windows.Forms.Label();
            this.newsdg = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.ProfileBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.newsdg)).BeginInit();
            this.SuspendLayout();
            // 
            // apikeylb
            // 
            this.apikeylb.AutoSize = true;
            this.apikeylb.BackColor = System.Drawing.Color.Transparent;
            this.apikeylb.Cursor = System.Windows.Forms.Cursors.Default;
            this.apikeylb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.apikeylb.Location = new System.Drawing.Point(383, 66);
            this.apikeylb.Name = "apikeylb";
            this.apikeylb.Size = new System.Drawing.Size(61, 20);
            this.apikeylb.TabIndex = 0;
            this.apikeylb.Text = "ApiKey";
            this.apikeylb.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // ProfileBox
            // 
            this.ProfileBox.BackColor = System.Drawing.SystemColors.Control;
            this.ProfileBox.Image = global::Stock_analysis_client.Properties.Resources.userblue;
            this.ProfileBox.Location = new System.Drawing.Point(718, 23);
            this.ProfileBox.Name = "ProfileBox";
            this.ProfileBox.Size = new System.Drawing.Size(100, 51);
            this.ProfileBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.ProfileBox.TabIndex = 1;
            this.ProfileBox.TabStop = false;
            this.ProfileBox.Click += new System.EventHandler(this.ProfileBox_Click);
            // 
            // tickerbt
            // 
            this.tickerbt.BackColor = System.Drawing.Color.White;
            this.tickerbt.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.tickerbt.Location = new System.Drawing.Point(653, 161);
            this.tickerbt.Name = "tickerbt";
            this.tickerbt.Size = new System.Drawing.Size(165, 41);
            this.tickerbt.TabIndex = 2;
            this.tickerbt.Text = "Search for a ticker";
            this.tickerbt.UseVisualStyleBackColor = false;
            this.tickerbt.Click += new System.EventHandler(this.tickerbt_Click);
            // 
            // usernamelb
            // 
            this.usernamelb.AutoSize = true;
            this.usernamelb.BackColor = System.Drawing.Color.Transparent;
            this.usernamelb.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.usernamelb.Location = new System.Drawing.Point(382, 23);
            this.usernamelb.Name = "usernamelb";
            this.usernamelb.Size = new System.Drawing.Size(89, 25);
            this.usernamelb.TabIndex = 3;
            this.usernamelb.Text = "welcome";
            this.usernamelb.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // newslb
            // 
            this.newslb.AutoSize = true;
            this.newslb.BackColor = System.Drawing.Color.Transparent;
            this.newslb.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.newslb.Location = new System.Drawing.Point(133, 84);
            this.newslb.Name = "newslb";
            this.newslb.Size = new System.Drawing.Size(75, 29);
            this.newslb.TabIndex = 4;
            this.newslb.Text = "News";
            // 
            // newsdg
            // 
            this.newsdg.BackgroundColor = System.Drawing.Color.AliceBlue;
            this.newsdg.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.newsdg.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.newsdg.GridColor = System.Drawing.Color.AliceBlue;
            this.newsdg.Location = new System.Drawing.Point(12, 116);
            this.newsdg.Name = "newsdg";
            this.newsdg.RowHeadersWidth = 51;
            this.newsdg.RowTemplate.Height = 24;
            this.newsdg.Size = new System.Drawing.Size(346, 425);
            this.newsdg.TabIndex = 5;
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.WhiteSmoke;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.ClientSize = new System.Drawing.Size(850, 555);
            this.Controls.Add(this.newsdg);
            this.Controls.Add(this.newslb);
            this.Controls.Add(this.usernamelb);
            this.Controls.Add(this.tickerbt);
            this.Controls.Add(this.ProfileBox);
            this.Controls.Add(this.apikeylb);
            this.DoubleBuffered = true;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Main";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Main";
            this.Load += new System.EventHandler(this.Main_Load);
            ((System.ComponentModel.ISupportInitialize)(this.ProfileBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.newsdg)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label apikeylb;
        private System.Windows.Forms.PictureBox ProfileBox;
        private System.Windows.Forms.Button tickerbt;
        private System.Windows.Forms.Label usernamelb;
        private System.Windows.Forms.Label newslb;
        private System.Windows.Forms.DataGridView newsdg;
    }
}