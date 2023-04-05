import json
from fmp_api import FMPapi


class PayloadAssembler(FMPapi):
    def assemble_metrics(self) -> json:
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
            return merged_metrics
        except:
            raise Exception("assemble_metrics failed to merge jsons in PayloadAssembler")
