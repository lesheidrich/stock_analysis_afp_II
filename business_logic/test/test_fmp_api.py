import unittest
from business_logic.fmp_api import FMPapi


class FMPapiTest(unittest.TestCase):
    def setUp(self):
        self.api_key = '07f36a5b1c35e69f0046d0e6a3ab12d6'
        # self.api_key = '2b1c52c776217c377aa030db56150115'
        self.ticker = 'MSFT'
        self.fmp_api = FMPapi(self.api_key, self.ticker)

    def test_get_key_metrics_ttm(self):
        result = self.fmp_api.get_key_metrics_ttm()
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)
        self.assertIn('revenuePerShareTTM', result)

    def test_get_financial_ratios_ttm(self):
        result = self.fmp_api.get_financial_ratios_ttm()
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)
        self.assertIn('dividendYielTTM', result)

    def test_get_news_articles(self):
        result = self.fmp_api.get_news_articles()
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)
        self.assertIn('content', result)

    def test_get_company_profile(self):
        result = self.fmp_api.get_company_profile()
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)
        self.assertIn('symbol', result)

    def test_get_fmp_rating(self):
        result = self.fmp_api.get_fmp_rating()
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)
        self.assertIn('symbol', result)

    def test_get_enterprise_value(self):
        result = self.fmp_api.get_enterprise_value()
        self.assertIsInstance(result, list)
        self.assertIsNotNone(result)
        self.assertIn('symbol', result[0])

    def test_get_sec_filings(self):
        result = self.fmp_api.get_sec_filings()
        self.assertIsInstance(result, list)
        self.assertIsNotNone(result)
        self.assertIn('symbol', result[0])
