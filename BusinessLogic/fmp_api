import json
import requests


class FMPapi:
    def __init__(self, api_key: str, ticker: str):
        self.base_url = 'https://financialmodelingprep.com/api/v3'
        self.payload = {'apikey': api_key}
        self.ticker = ticker.upper()

    def error_respone(self, name: str, response_code: int) -> json:
        """
        :param name: string: exact function name where error occured
        :param response_code: request response code
        :return: creates json for error message used in all api functions
        """
        return {
            "error code": 1,
            "response type": "api error",
            "status code": response_code,
            "details": f"{name} function encountered an error"
        }

    def get_key_metrics_ttm(self) -> json:
        """
        Using TTM: Trailing Twelve Month for following metrics:
        https://financialmodelingprep.com/api/v3/key-metrics-ttm/AAPL?limit=40&apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :return: json of key metrics for past 12 months
        """
        url = f'{self.base_url}/key-metrics-ttm/{self.ticker}'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()[0]
        else:
            return self.error_respone("get_key_metrics_ttm", response.status_code)

    def get_financial_ratios_ttm(self) -> json:
        """
        https://financialmodelingprep.com/api/v3/ratios-ttm/AAPL?apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :return: json of TTM metrics
        """
        url = f'{self.base_url}/ratios-ttm/{self.ticker}'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()[0]
        else:
            return self.error_respone("get_financial_ratios_ttm", response.status_code)

    def get_news_articles(self) -> json:
        """
        https://financialmodelingprep.com/api/v3/fmp/articles?page=0&size=5&apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :return: json FMP news articles
        """
        url = f'{self.base_url}/fmp/articles'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()
        else:
            return self.error_respone("get_news_articles", response.status_code)

    def get_company_profile(self) -> json:
        """
        https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :return: json company profile
        """
        url = f'{self.base_url}/profile/{self.ticker}'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()[0]
        else:
            return self.error_respone("get_company_profile", response.status_code)

    def get_fmp_rating(self) -> json:
        """
        https://financialmodelingprep.com/api/v3/rating/AAPL?apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        FORMULA: https://site.financialmodelingprep.com/developer/docs/recommendations-formula/
        :return: json FMP rating
        """
        url = f'{self.base_url}/rating/{self.ticker}'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()[0]
        else:
            return self.error_respone("get_fmp_rating", response.status_code)

    def get_enterprise_value(self, limit=120) -> [json]:
        """
        https://financialmodelingprep.com/api/v3/enterprise-values/AAPL?limit=120&apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :param limit: char limit for result json, default=120
        :return: annual enterprise values
        """
        url = f'{self.base_url}/enterprise-values/{self.ticker}?limit={limit}'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()
        else:
            return self.error_respone("get_enterprise_value", response.status_code)

    def get_sec_filings(self) -> [json]:
        """
        https://financialmodelingprep.com/api/v3/sec_filings/AAPL?page=0&apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :return: json SEC filings
        """
        url = f'{self.base_url}/sec_filings/{self.ticker}?page=0'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()
        else:
            return self.error_respone("get_sec_filings", response.status_code)

    def get_income_statement(self, limit=120) -> [json]:
        """
        https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :param limit: char limit for result json, default=120
        :return: 5 years of income statements
        """
        url = f'{self.base_url}/income-statement/{self.ticker}?limit={limit}'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()
        else:
            return self.error_respone("get_income_statement", response.status_code)

    def get_cash_flow_statement(self, limit=120) -> [json]:
        """
        https://financialmodelingprep.com/api/v3/cash-flow-statement/AAPL?limit=120&apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :param limit: char limit for result json, default=120
        :return: 5 years of cash flow statements
        """
        url = f'{self.base_url}/cash-flow-statement/{self.ticker}?limit={limit}'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()
        else:
            return self.error_respone("get_cash_flow_statement", response.status_code)

    def get_balance_sheet_statement(self, limit=120) -> [json]:
        """
        https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?limit=120&apikey=07f36a5b1c35e69f0046d0e6a3ab12d6
        :param limit: char limit for result json, default=120
        :return: last years of balance sheets up to char limit
        """
        url = f'{self.base_url}/balance-sheet-statement/{self.ticker}?limit={limit}'
        response = requests.get(url, params=self.payload)

        if response.status_code == 200:
            return response.json()
        else:
            return self.error_respone("get_balance_sheet_statement", response.status_code)
