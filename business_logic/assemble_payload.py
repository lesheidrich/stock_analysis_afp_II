import json
from fmp_api import FMPapi


class ForSQL(FMPapi):
    def merge_metrics(self) -> json:
        """
       :return: json merged key metrics and financial ratios
       """
        try:
            metrics_list = [
                self.get_key_metrics_ttm(),
                self.get_financial_ratios_ttm(),
                self.get_company_profile(),
                self.get_fmp_rating(),
                self.get_enterprise_value()[0]]
            merged_metrics = {}

            for package in metrics_list:
                for k, v in package.items():
                    if k not in merged_metrics:
                        merged_metrics[k] = v
            merged_metrics['ticker_range'] = merged_metrics.pop('range')

            return merged_metrics
        except Exception as e:
            raise Exception(f"ERROR: {e}\nAssemble_metrics failed to merge jsons in PayloadAssembler!")
