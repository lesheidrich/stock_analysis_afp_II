"""
Class is for client
only meant to be guide
TODO: delete after complete on client side
"""


class StockScreeningTable:
    def __init__(self, result):
        self.result = result

    def book_value_per_share(self):
        if self.result['bookValuePerShareTTM'] > 5:
            return ['Book value per share', self.result['bookValuePerShareTTM'], 'ok']
        else:
            return ['Book value per share', self.result['bookValuePerShareTTM'], 0]

    def capex_to_depreciation(self):
        if self.result['capexToDepreciationTTM'] < 1:
            return ['Capex to depreciation', self.result['capexToDepreciationTTM'], 'ok']
        else:
            return ['Capex to depreciation', self.result['capexToDepreciationTTM'], 0]

    def capex_to_operating_cash_flow(self):
        if self.result['capexToOperatingCashFlowTTM'] < 1:
            return ['Capex to operating cash flow', self.result['capexToOperatingCashFlowTTM'], 'ok']
        else:
            return ['Capex to operating cash flow', self.result['capexToOperatingCashFlowTTM'], 0]

    def capex_to_revenue(self):
        if self.result['capexToRevenueTTM'] < 0.05:
            return ['Capex to revenue', self.result['capexToRevenueTTM'], 'ok']
        else:
            return ['Capex to revenue', self.result['capexToRevenueTTM'], 0]

    def cash_per_share(self):
        if self.result['cashPerShareTTM'] > 1:
            return ['Cash per share', self.result['cashPerShareTTM'], 'ok']
        else:
            return ['Cash per share', self.result['cashPerShareTTM'], 0]

    def current_ratio(self):
        if self.result['currentRatioTTM'] > 1:
            return ['Current ratio', self.result['currentRatioTTM'], 'ok']
        else:
            return ['Current ratio', self.result['currentRatioTTM'], 0]

    def days_of_inventory_on_hand(self):
        if self.result['daysOfInventoryOnHandTTM'] < 60:
            return ['Days of inventory on hand', self.result['daysOfInventoryOnHandTTM'], 'ok']
        else:
            return ['Days of inventory on hand', self.result['daysOfInventoryOnHandTTM'], 0]

    def days_payables_outstanding(self):
        if self.result['daysPayablesOutstandingTTM'] < 60:
            return ['Days payables outstanding', self.result['daysPayablesOutstandingTTM'], 'ok']
        else:
            return ['Days payables outstanding', self.result['daysPayablesOutstandingTTM'], 0]

    def days_sales_outstanding(self):
        if self.result['daysSalesOutstandingTTM'] < 60:
            return ['Days sales outstanding', self.result['daysSalesOutstandingTTM'], 'ok']
        else:
            return ['Days sales outstanding', self.result['daysSalesOutstandingTTM'], 0]

    def debt_to_assets(self):
        if self.result['debtToAssetsTTM'] < 0.5:
            return ['Debt to assets', self.result['debtToAssetsTTM'], 'ok']
        else:
            return ['Debt to assets', self.result['debtToAssetsTTM'], 0]

    def debt_to_equity(self):
        if self.result['debtToEquityTTM'] < 1:
            return ['Debt to equity', self.result['debtToEquityTTM'], 'ok']
        else:
            return ['Debt to equity', self.result['debtToEquityTTM'], 0]

    def debt_to_market_cap(self):
        if self.result['debtToMarketCapTTM'] < 0.2:
            return ['Debt to market cap', self.result['debtToMarketCapTTM'], 'ok']
        else:
            return ['Debt to market cap', self.result['debtToMarketCapTTM'], 0]

    def dividend_yield_percentage(self):
        if 2 <= self.result['dividendYieldPercentageTTM'] <= 4:
            return ['Dividend yield percentage', self.result['dividendYieldPercentageTTM'], 'ok']
        else:
            return ['Dividend yield percentage', self.result['dividendYieldPercentageTTM'], 0]

    def dividend_yield(self):
        if 2 <= self.result['dividendYieldTTM'] <= 4:
            return ['Dividend yield', self.result['dividendYieldTTM'], 'ok']
        else:
            return ['Dividend yield', self.result['dividendYieldTTM'], 0]

    def earnings_yield(self):
        if self.result['earningsYieldTTM'] > 7:
            return ['Earnings yield', self.result['earningsYieldTTM'], 'ok']
        else:
            return ['Earnings yield', self.result['earningsYieldTTM'], 0]

    def enterprise_value_over_ebitda(self):
        if self.result['enterpriseValueOverEBITDATTM'] < 12:
            return ['Enterprise value over EBITDA', self.result['enterpriseValueOverEBITDATTM'], 'ok']
        else:
            return ['Enterprise value over EBITDA', self.result['enterpriseValueOverEBITDATTM'], 0]

    def ev_to_free_cash_flow(self):
        if self.result['evToFreeCashFlowTTM'] < 15:
            return ['EV to free cash flow', self.result['evToFreeCashFlowTTM'], 'ok']
        else:
            return ['EV to free cash flow', self.result['evToFreeCashFlowTTM'], 0]

    def ev_to_operating_cash_flow(self):
        if self.result['evToOperatingCashFlowTTM'] < 15:
            return ['EV to operating cash flow', self.result['evToOperatingCashFlowTTM'], 'ok']
        else:
            return ['EV to operating cash flow', self.result['evToOperatingCashFlowTTM'], 0]

    def ev_to_sales(self, result):
        if result['evToSalesTTM'] < 3:
            return ['EV to sales', result['evToSalesTTM'], 'ok']
        else:
            return ['EV to sales', result['evToSalesTTM'], 0]

    def free_cash_flow_per_share(self, result):
        if result['freeCashFlowPerShareTTM'] > 5:
            return ['Free cash flow per share', result['freeCashFlowPerShareTTM'], 'ok']
        else:
            return ['Free cash flow per share', result['freeCashFlowPerShareTTM'], 0]

    def free_cash_flow_yield(self, result):
        if result['freeCashFlowYieldTTM'] > 0.05:
            return ['Free cash flow yield', result['freeCashFlowYieldTTM'], 'ok']
        else:
            return ['Free cash flow yield', result['freeCashFlowYieldTTM'], 0]

    def graham_net_net(self, result):
        if result['grahamNetNetTTM'] > 0:
            return ['Graham net net', result['grahamNetNetTTM'], 'ok']
        else:
            return ['Graham net net', result['grahamNetNetTTM'], 0]

    def graham_number(self, result):
        if result['grahamNumberTTM'] > 1.5:
            return ['Graham number', result['grahamNumberTTM'], 'ok']
        else:
            return ['Graham number', result['grahamNumberTTM'], 0]

    def intangibles_to_total_assets(self, result):
        if result['intangiblesToTotalAssetsTTM'] < 0.3:
            return ['Intangibles to total assets', result['intangiblesToTotalAssetsTTM'], 'ok']
        else:
            return ['Intangibles to total assets', result['intangiblesToTotalAssetsTTM'], 0]

    def interest_coverage(self, result):
        if result['interestCoverageTTM'] > 3:
            return ['Interest coverage', result['interestCoverageTTM'], 'ok']
        else:
            return ['Interest coverage', result['interestCoverageTTM'], 0]

    def inventory_turnover(self, result):
        if result['inventoryTurnoverTTM'] > 8:
            return ['Inventory turnover', result['inventoryTurnoverTTM'], 'ok']
        else:
            return ['Inventory turnover', result['inventoryTurnoverTTM'], 0]

    def net_current_asset_value(self, result):
        if result['netCurrentAssetValueTTM'] > 1:
            return ['Net current asset value', result['netCurrentAssetValueTTM'], 'ok']
        else:
            return ['Net current asset value', result['netCurrentAssetValueTTM'], 0]

    def net_debt_to_ebitda(self, result):
        if result['netDebtToEBITDATTM'] < 2:
            return ['Net debt to EBITDA', result['netDebtToEBITDATTM'], 'ok']
        else:
            return ['Net debt to EBITDA', result['netDebtToEBITDATTM'], 0]

    def net_income_per_share(self, result):
        if result['netIncomePerShareTTM'] > 5:
            return ['Net income per share', result['netIncomePerShareTTM'], 'ok']
        else:
            return ['Net income per share', result['netIncomePerShareTTM'], 0]

    def operating_cash_flow_per_share(self, result):
        if result['operatingCashFlowPerShareTTM'] > 5:
            return ['Operating cash flow per share', result['operatingCashFlowPerShareTTM'], 'ok']
        else:
            return ['Operating cash flow per share', result['operatingCashFlowPerShareTTM'], 0]

    def payables_turnover(self, result):
        if result['payablesTurnoverTTM'] > 8:
            return ['Payables turnover', result['payablesTurnoverTTM'], 'ok']
        else:
            return ['Payables turnover', result['payablesTurnoverTTM'], 0]

    def payout_ratio(self, result):
        if result['payoutRatioTTM'] < 0.5:
            return ['Payout ratio', result['payoutRatioTTM'], 'ok']
        else:
            return ['Payout ratio', result['payoutRatioTTM'], 0]

    def pb_ratio(self, result):
        if result['pbRatioTTM'] < 3:
            return ['PB ratio', result['pbRatioTTM'], 'ok']
        else:
            return ['PB ratio', result['pbRatioTTM'], 0]

    def pe_ratio(self, result):
        if result['peRatioTTM'] < 20:
            return ['PE ratio', result['peRatioTTM'], 'ok']
        else:
            return ['PE ratio', result['peRatioTTM'], 0]

    def pfcf_ratio(self, result):
        if result['pfcfRatioTTM'] < 15:
            return ['PFCF ratio', result['pfcfRatioTTM'], 'ok']
        else:
            return ['PFCF ratio', result['pfcfRatioTTM'], 0]

    def pocf_ratio(self, result):
        if result['pocfratioTTM'] < 15:
            return ['POCF ratio', result['pocfratioTTM'], 'ok']
        else:
            return ['POCF ratio', result['pocfratioTTM'], 0]

    def price_to_sales_ratio(self, result):
        if result['priceToSalesRatioTTM'] < 3:
            return ['Price to sales ratio', result['priceToSalesRatioTTM'], 'ok']
        else:
            return ['Price to sales ratio', result['priceToSalesRatioTTM'], 0]

    def ptb_ratio(self, result):
        if result['ptbRatioTTM'] < 3:
            return ['PTB ratio', result['ptbRatioTTM'], 'ok']
        else:
            return ['PTB ratio', result['ptbRatioTTM'], 0]

    def receivables_turnover(self, result):
        if result['receivablesTurnoverTTM'] > 8:
            return ['Receivables turnover', result['receivablesTurnoverTTM'], 'ok']
        else:
            return ['Receivables turnover', result['receivablesTurnoverTTM'], 0]

    def return_on_tangible_assets(self, result):
        if (result['returnOnTangibleAssetsTTM'] > 0.1):
            return ['Return on tangible assets', 'returnOnTangibleAssetsTTM', 'ok']
        else:
            return ['Return on tangible assets', 'returnOnTangibleAssetsTTM', 0]

    def return_on_equity(self, result):
        if (result['roeTTM'] > 0.15):
            return ['Return on equity (ROE)', 'roeTTM', 'ok']
        else:
            return ['Return on equity (ROE)', 'roeTTM', 0]

    def return_on_invested_capital(self, result):
        if (result['roicTTM'] > 0.1):
            return ['Return on invested capital (ROIC)', 'roicTTM', 'ok']
        else:
            return ['Return on invested capital (ROIC)', 'roicTTM', 0]

    def sales_general_and_administrative_to_revenue(self, result):
        if (0.1 <= result['salesGeneralAndAdministrativeToRevenueTTM'] <= 0.15):
            return ['Sales, general and administrative expenses to revenue',
                    'salesGeneralAndAdministrativeToRevenueTTM', 'ok']
        else:
            return ['Sales, general and administrative expenses to revenue',
                    'salesGeneralAndAdministrativeToRevenueTTM', 0]

    def researchAndDevelopementToRevenueTTM(self, result):
        if (result['researchAndDevelopementToRevenueTTM'] <= 0.1):
            return ['Research and development to revenue', 'researchAndDevelopementToRevenueTTM', 'ok']
        else:
            return ['Research and development to revenue', 'researchAndDevelopementToRevenueTTM', 0]

    def returnOnTangibleAssetsTTM(self, result):
        if (0.1 <= result['returnOnTangibleAssetsTTM'] <= 0.15):
            return ['Return on tangible assets', 'returnOnTangibleAssetsTTM', 'ok']
        else:
            return ['Return on tangible assets', 'returnOnTangibleAssetsTTM', 0]

    def shareholdersEquityPerShareTTM(self, result):
        if (result['shareholdersEquityPerShareTTM'] > 0):
            return ['Shareholders equity per share', 'shareholdersEquityPerShareTTM', 'ok']
        else:
            return ['Shareholders equity per share', 'shareholdersEquityPerShareTTM', 0]

    def stockBasedCompensationToRevenueTTM(self, result):
        if (result['stockBasedCompensationToRevenueTTM'] <= 0.05):
            return ['Stock based compensation to revenue', 'stockBasedCompensationToRevenueTTM', 'ok']
        else:
            return ['Stock based compensation to revenue', 'stockBasedCompensationToRevenueTTM', 0]

    def tangibleAssetValueTTM(self, result):
        if (result['tangibleAssetValueTTM'] > 0):
            return ['Tangible assets value', 'tangibleAssetValueTTM', 'ok']
        else:
            return ['Tangible assets value', 'tangibleAssetValueTTM', 0]

    def tangibleBookValuePerShareTTM(self, result):
        if result['tangibleBookValuePerShareTTM'] > 0:
            return ['tangible book value per share', result['tangibleBookValuePerShareTTM'], 'ok']
        else:
            return ['tangible book value per share', result['tangibleBookValuePerShareTTM'], 0]

    def workingCapitalTTM(self, result):
        if result['workingCapitalTTM'] > 0:
            return ['working capital', result['workingCapitalTTM'], 'ok']
        else:
            return ['working capital', result['workingCapitalTTM'], 0]
