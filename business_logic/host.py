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
            :return: json of user's api_key
            """
            un = request.args.get('username')
            pw = request.args.get('pwd')
            query = f"SELECT api_key FROM users WHERE username='{un}' AND pwd=md5('{pw}')"
            result = SQLLoginCRUD.read(query)
            return jsonify(result[0])

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
