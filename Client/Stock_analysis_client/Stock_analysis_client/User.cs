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


        private string password;

        public string Password
        {
            get { return password; }
            set { password = value; }
        }

        private int isAdmin;
        public int IsAdmin
        {
            get { return isAdmin; }
            set { isAdmin = value; }
        }

        private int api_key;

        public int API_Key
        {
            get { return api_key; }
            set { api_key = value; }
        }

    }
}