import json
import datetime

from dateutil.relativedelta import relativedelta
from flask import Flask, request
from business_logic import sql_operator
from business_logic.fmp_api import FMPapi
from business_logic.sql_login import SQLLoginCRUD


class Host:
    def __init__(self):
        self.app = Flask(__name__)
        self.sysdate = datetime.date.today()

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

        @self.app.route('/api/ticker/ticker_metrics')
        def get_ticker_metrics() -> json:
            """
            phpMyAdmin afp_ii.ticker_metrics --> {metrics}
            :return: json with result of ticker metrics
            """
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            try:
                db = sql_operator.SQLOperator(api_key, ticker)
                query = f"SELECT * FROM ticker_metrics WHERE symbol='{ticker}' ORDER BY ticker_id desc LIMIT 1"
                result = db.read(query)[0]

                sql = f"SELECT max(date) FROM balance_sheet WHERE symbol='{ticker}'"
                sql_date = SQLLoginCRUD.read(sql)[0][0]
                sql_date = sql_date + relativedelta(years=1)
                if sql_date < self.sysdate:
                    db.update_ticker_metrics()

                return {
                    'success': True,
                    'status': 200,
                    'results': result
                }
            except Exception as e:
                return {
                    'success': False,
                    'status': 400,
                    'message': f"Error! {e}"}

        @self.app.route('/api/ticker/sec_filings')
        def get_sec_filings() -> json:
            """
            phpMyAdmin afp_ii.sec_filings --> {SEC filings}
            :return: json with result of SEC filings
            """
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            try:
                db = sql_operator.SQLOperator(api_key, ticker)
                result = db.read("SELECT * FROM sec_filings")
                return {
                    'success': True,
                    'status': 200,
                    'results': result
                }
            except Exception as e:
                return {
                    'success': False,
                    'status': 400,
                    'message': f"Error! {e}"}

        @self.app.route('/api/ticker/balance_sheet')
        def get_balance_sheet() -> json:
            """
            phpMyAdmin afp_ii.balance_sheet --> {balance sheets}
            :return: json with result of balance sheets
            """
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            try:
                db = sql_operator.SQLOperator(api_key, ticker)
                result = db.read("SELECT * FROM balance_sheet")
                return {
                    'success': True,
                    'status': 200,
                    'results': result
                }
            except Exception as e:
                return {
                    'success': False,
                    'status': 400,
                    'message': f"Error! {e}"}

        @self.app.route('/api/ticker/cash_flow_statement')
        def get_cash_flow_statement() -> json:
            """
            phpMyAdmin afp_ii.cash_flow_statement --> {cash flow statements}
            :return: json with result of cash flow statements
            """
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            try:
                db = sql_operator.SQLOperator(api_key, ticker)
                result = db.read("SELECT * FROM cash_flow_statement")
                return {
                    'success': True,
                    'status': 200,
                    'results': result
                }
            except Exception as e:
                return {
                    'success': False,
                    'status': 400,
                    'message': f"Error! {e}"}

        @self.app.route('/api/ticker/income_statement')
        def get_income_statement() -> json:
            """
            phpMyAdmin afp_ii.income_statement --> {income statements}
            :return: json with result of income statements
            """
            api_key = request.args.get('api_key')
            ticker = request.args.get('ticker')
            try:
                db = sql_operator.SQLOperator(api_key, ticker)
                result = db.read("SELECT * FROM income_statement")
                return {
                    'success': True,
                    'status': 200,
                    'results': result
                }
            except Exception as e:
                return {
                    'success': False,
                    'status': 400,
                    'message': f"Error! {e}"}

        @self.app.route('/api/news')
        def get_news() -> json:
            """
            FMP api service based news articles.
            :return: json with news articles
            """
            api_key = request.args.get('api_key')
            ticker = 'MSFT'
            try:
                fmp = FMPapi(api_key, ticker)
                result = fmp.get_news_articles()
                return {
                    'success': True,
                    'status': 200,
                    'results': result['content']
                }
            except Exception as e:
                return {
                    'success': False,
                    'status': 400,
                    'message': f"Error! {e}"}

    def run(self) -> None:
        self.app.run(debug=True)
