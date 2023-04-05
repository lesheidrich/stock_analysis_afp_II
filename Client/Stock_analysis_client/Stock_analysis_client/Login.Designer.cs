namespace Stock_analysis_client
{
    partial class Login
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
            this.SignInlbl = new System.Windows.Forms.Label();
            this.Usernamelbl = new System.Windows.Forms.Label();
            this.Passwordlbl = new System.Windows.Forms.Label();
            this.Usernametb = new System.Windows.Forms.TextBox();
            this.Passwordtb = new System.Windows.Forms.TextBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.Loginlbl = new System.Windows.Forms.Label();
            this.Loginbt = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // SignInlbl
            // 
            this.SignInlbl.AutoSize = true;
            this.SignInlbl.Font = new System.Drawing.Font("Arial Narrow", 30F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.SignInlbl.Location = new System.Drawing.Point(341, 50);
            this.SignInlbl.Name = "SignInlbl";
            this.SignInlbl.Size = new System.Drawing.Size(121, 46);
            this.SignInlbl.TabIndex = 0;
            this.SignInlbl.Text = "Sign In";
            this.SignInlbl.Click += new System.EventHandler(this.label1_Click);
            // 
            // Usernamelbl
            // 
            this.Usernamelbl.AutoSize = true;
            this.Usernamelbl.BackColor = System.Drawing.Color.Transparent;
            this.Usernamelbl.Font = new System.Drawing.Font("Arial", 15F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.Usernamelbl.Location = new System.Drawing.Point(60, 111);
            this.Usernamelbl.Name = "Usernamelbl";
            this.Usernamelbl.Size = new System.Drawing.Size(108, 24);
            this.Usernamelbl.TabIndex = 1;
            this.Usernamelbl.Text = "Username:";
            // 
            // Passwordlbl
            // 
            this.Passwordlbl.AutoSize = true;
            this.Passwordlbl.BackColor = System.Drawing.Color.Transparent;
            this.Passwordlbl.Font = new System.Drawing.Font("Arial", 15F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.Passwordlbl.Location = new System.Drawing.Point(60, 227);
            this.Passwordlbl.Name = "Passwordlbl";
            this.Passwordlbl.Size = new System.Drawing.Size(103, 24);
            this.Passwordlbl.TabIndex = 2;
            this.Passwordlbl.Text = "Password:";
            // 
            // Usernametb
            // 
            this.Usernametb.BackColor = System.Drawing.SystemColors.Highlight;
            this.Usernametb.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.Usernametb.Location = new System.Drawing.Point(63, 147);
            this.Usernametb.Name = "Usernametb";
            this.Usernametb.Size = new System.Drawing.Size(100, 26);
            this.Usernametb.TabIndex = 3;
            // 
            // Passwordtb
            // 
            this.Passwordtb.BackColor = System.Drawing.SystemColors.Highlight;
            this.Passwordtb.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.Passwordtb.Location = new System.Drawing.Point(63, 272);
            this.Passwordtb.Name = "Passwordtb";
            this.Passwordtb.Size = new System.Drawing.Size(100, 26);
            this.Passwordtb.TabIndex = 4;
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox1.BackgroundImage = global::Stock_analysis_client.Properties.Resources.GoldenStock;
            this.pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pictureBox1.Location = new System.Drawing.Point(437, 111);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(288, 216);
            this.pictureBox1.TabIndex = 5;
            this.pictureBox1.TabStop = false;
            // 
            // Loginlbl
            // 
            this.Loginlbl.AutoSize = true;
            this.Loginlbl.Font = new System.Drawing.Font("Arial Narrow", 26.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.Loginlbl.Location = new System.Drawing.Point(300, 357);
            this.Loginlbl.Name = "Loginlbl";
            this.Loginlbl.Size = new System.Drawing.Size(88, 42);
            this.Loginlbl.TabIndex = 6;
            this.Loginlbl.Text = "Login";
            // 
            // Loginbt
            // 
            this.Loginbt.BackColor = System.Drawing.SystemColors.Highlight;
            this.Loginbt.Location = new System.Drawing.Point(406, 357);
            this.Loginbt.Name = "Loginbt";
            this.Loginbt.Size = new System.Drawing.Size(75, 40);
            this.Loginbt.TabIndex = 7;
            this.Loginbt.UseVisualStyleBackColor = false;
            this.Loginbt.Click += new System.EventHandler(this.Loginbt_Click);
            // 
            // Login
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::Stock_analysis_client.Properties.Resources.BG;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Loginbt);
            this.Controls.Add(this.Loginlbl);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.Passwordtb);
            this.Controls.Add(this.Usernametb);
            this.Controls.Add(this.Passwordlbl);
            this.Controls.Add(this.Usernamelbl);
            this.Controls.Add(this.SignInlbl);
            this.Name = "Login";
            this.Text = "Login";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label SignInlbl;
        private System.Windows.Forms.Label Usernamelbl;
        private System.Windows.Forms.Label Passwordlbl;
        private System.Windows.Forms.TextBox Usernametb;
        private System.Windows.Forms.TextBox Passwordtb;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label Loginlbl;
        private System.Windows.Forms.Button Loginbt;
    }
}