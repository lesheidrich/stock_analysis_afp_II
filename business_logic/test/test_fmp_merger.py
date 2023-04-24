import unittest
from business_logic.fmp_merger import FMPMerger


class FMPapiTest(unittest.TestCase):
    def setUp(self):
        self.api_key = '07f36a5b1c35e69f0046d0e6a3ab12d6'
        # self.api_key = '2b1c52c776217c377aa030db56150115'
        self.ticker = 'MSFT'
        self.fmp_api = FMPMerger(self.api_key, self.ticker)

    def test_fmp_merger(self):
        result = self.fmp_api.get_key_metrics_ttm()
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)
        self.assertIn('revenuePerShareTTM', result)