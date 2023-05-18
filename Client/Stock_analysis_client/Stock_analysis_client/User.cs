using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Stock_analysis_client
{
    public class User
    {
        private int id;

        public int Id
        {
            get { return id; }
            set { id = value; }
        }


        private string username;

        public string Username
        {
            get { return username; }
            set { username = value; }
        }


        private string pwd;

        public string Pwd
        {
            get { return pwd; }
            set { pwd = value; }
        }

        private int isAdmin;
        public int IsAdmin
        {
            get { return isAdmin; }
            set { isAdmin = value; }
        }

        private string api_key;

        public string API_Key
        {
            get { return api_key; }
            set { api_key = value; }
        }

        private int email;

        public int Email
        {
            get { return email; }
            set { email = value; }
        }

        private int full_name;

        public int Full_Name
        {
            get { return full_name; }
            set { full_name = value; }
        }
    }
}
