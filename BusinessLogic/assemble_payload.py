import json
from fmp_api import FMPApi


class PayloadAssembler(FMPApi):
    def assemble_metrics(self) -> json:
        """
        :return: json merged key metrics and financial ratios
        """
        try:
            merged_metrics_dict = self.get_key_metrics_ttm()
            merged_metrics_dict.update(self.get_financial_ratios_ttm())
            return merged_metrics_dict
        except:
            raise Exception("assemble_metrics failed to merge jsons in PayloadAssembler")
