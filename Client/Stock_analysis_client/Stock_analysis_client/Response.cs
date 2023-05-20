using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Stock_analysis_client
{
    public class Response
    {
        private bool success;

        public bool Success
        {
            get { return success; }
            set { success = value; }
        }


        private int status;

        public int Status
        {
            get { return status; }
            set { status = value; }
        }


        private string message;

        public string Message
        {
            get { return message; }
            set { message = value; }
        }

        private string api_key;

        public string API_Key
        {
            get { return api_key; }
            set { api_key = value; }
        }

        private string results;

        public string Results
        {
            get { return results; }
            set { results = value; }
        }

        private List<User> users;

        public List<User> Users
        {
            get { return users; }
            set { users = value; }
        }

        private int id;

        public int Id
        {
            get { return id; }
            set { id = value; }
        }

        private int isAdmin;

        public int IsAdmin
        {
            get { return isAdmin; }
            set { isAdmin = value; }
        }


    }
}
