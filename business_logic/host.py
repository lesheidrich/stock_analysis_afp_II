import json
from flask import Flask, jsonify, request
from business_logic import sql_operator
from business_logic.sql_login import SQLLoginCRUD


class Host:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/api/users/login')
        def get_login() -> json:
            """
            request args: username, pwd <-- C# client login
            Checks args against users table, returns user's api_key
            :return: json status info
            """
            un = request.args.get('username')
            pw = request.args.get('pwd')
            query = f"SELECT api_key FROM users WHERE username='{un}' AND pwd=md5('{pw}')"
            try:
                result = SQLLoginCRUD.read(query)
                return {
                    'success': True,
                    'status': 200,
                    'api_key': result[0][0]
                }
            except Exception as e:
                return {
                    'success': False,
                    'status': 400,
                    'message': f"Error! {e}"}

        @self.app.route('/api/users/create')
        def create_user() -> json:
            """
            request arg: string of partial mysql insert into command as follows:
                key name: query
                sample value: 'alfonzo', md5('pwd'), 'apikey', '0', 'email', 'full name'
            :return: json status info
            """
            query = request.args.get('query')
            try:
                SQLLoginCRUD.insert(query)
                return {
                    'success': True,
                    'status': 200,
                    'message': f"User has been created successfully with params: {query}"
                }
            except Exception as e:
                return {
                    'success': False,
                    'status': 400,
                    'message': f"Error! {e}"}

        @self.app.route('/api/users/delete')
        def delete_user() -> json:
            """
            request arg: delete user where condition met:
                key name: query
                sample value: username='bela'
            Admin status required!
            :return: json status info
            """
            apikey = request.args.get('api_key')
            query = request.args.get('query')
            sql = f"SELECT is_admin FROM users WHERE api_key='{apikey}'"
            admin = SQLLoginCRUD.read(sql)[0][0]
            if admin > 0:
                try:
                    SQLLoginCRUD.delete_where(query)
                    return {
                        'success': True,
                        'status': 200,
                        'message': f"User has been deleted successfully with params: {query}"
                    }
                except Exception as e:
                    return {
                        'success': False,
                        'status': 400,
                        'message': f"Error! {e}"}
            else:
                return {
                    'success': False,
                    'status': 403,
                    'message': "Access Denied: You do not have permission to access this resource!"
                }

        @self.app.route('/api/users/update')
        def update_user() -> json:
            """
            request arg: update where condition met:
                key name: query
                sample value: SET username='bill' WHERE username='bela'
            Admin status required!
            :return: json status info
            """
            apikey = request.args.get('api_key')
            query = request.args.get('query')
            sql = f"SELECT is_admin FROM users WHERE api_key='{apikey}'"
            admin = SQLLoginCRUD.read(sql)[0][0]
            if admin > 0:
                try:
                    SQLLoginCRUD.update(query)
                    return {
                        'success': True,
                        'status': 200,
                        'message': f"User has been updated successfully where: {query}!"
                    }
                except Exception as e:
                    return {
                        'success': False,
                        'status': 400,
                        'message': f"Error! {e}"}
            else:
                return {
                    'success': False,
                    'status': 403,
                    'message': "Access Denied: You do not have permission to access this resource!"
                }





        @self.app.route('/api/ticker_metrics')
        def get_ticker_metrics() -> json:
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            db = sql_operator.SQLOperator(api_key, ticker)
            result = db.read("select * from ticker_metrics")
            return jsonify(result)

        @self.app.route('/api/sec_filings')
        def get_sec_filings() -> json:
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            db = sql_operator.SQLOperator(api_key, ticker)
            result = db.read("select * from sec_filings")
            return jsonify(result)

        @self.app.route('/api/balance_sheet')
        def get_balance_sheet() -> json:
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            db = sql_operator.SQLOperator(api_key, ticker)
            result = db.read("select * from balance_sheet")
            return jsonify(result)

        @self.app.route('/api/cash_flow_statement')
        def get_cashflow_statement() -> json:
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            db = sql_operator.SQLOperator(api_key, ticker)
            result = db.read("select * from cash_flow_statement")
            return jsonify(result)

        @self.app.route('/api/income_statement')
        def get_income_statement() -> json:
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            db = sql_operator.SQLOperator(api_key, ticker)
            result = db.read("select * from income_statement")
            return jsonify(result)

    def run(self) -> None:
        self.app.run(debug=True)



# @app.route('/data')
# def get_data():
#     api_key = request.args.get('api_key')
#     ticker = request.args.get('ticker')
#     c = sql.Handler(api_key, ticker)
#     query = "select * from sec_filings"
#     print(ticker)
#
#     # res = ['puppyfarts', 'kittentitties']
#     res = c.read(query)
#     # pprint(jsonify(res))
#     return jsonify(res)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
