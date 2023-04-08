from pprint import pprint

from business_logic import sql

api_key = '07f36a5b1c35e69f0046d0e6a3ab12d6'
ticker = "MSFT"
payload = {'apikey': api_key}

# msft = FMPapi(api_key, ticker)

# pprint(msft.get_key_metrics_ttm())
# pprint(msft.get_financial_ratios_ttm())
# pprint(msft.get_news_articles())
# pprint(msft.get_company_profile())
# pprint(msft.get_fmp_rating())
# pprint(msft.get_enterprise_value())
# pprint(msft.get_sec_filings())
# pprint(msft.get_income_statement())
# pprint(msft.get_cash_flow_statement())
# pprint(msft.get_balance_sheet_statement())

c = sql.Handler(api_key, ticker)
# c.update_ticker_metrics()
# c.update_sec_filings()
# c.update_balance_sheet()
# c.update_cash_flow_statement()
# c.update_income_statement()

query = "select * from sec_filings"
res = c.read(query)
pprint(res)


"""
DOWNLOAD CSV
dl = CSVDownloader(api_key, ticker)
csv_content = dl.get_balance_sheet_statement_download()
dl.download_from_fmp_api(csv_content)
"""
# url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?datatype=csv"
# response = requests.get(url, params=payload)
# print(response.status_code)
# with open(f"C:/Users/Public/Downloads/{ticker}_cash_flow_statement.csv", "w") as f:
#     f.write(response.content.decode('utf-8'))

# km = {
#     'averageInventoryTTM': 3624000000,
#     'averagePayablesTTM': 15981500000,
#     'averageReceivablesTTM': 33556000000,
#     'bookValuePerShareTTM': 24.578714266541404,
#     'capexPerShareTTM': -3.324117568111663,
#     'capexToDepreciationTTM': -1.7454545454545454,
#     'capexToOperatingCashFlowTTM': -0.29350840186760835,
#     'capexToRevenueTTM': -0.12135584583574235,
#     'cashPerShareTTM': 13.353241175681116,
#     'currentRatioTTM': 1.9313125627156809,
#     'daysOfInventoryOnHandTTM': 16.737966268619967,
#     'daysPayablesOutstandingTTM': 86.23984365382248,
#     'daysSalesOutstandingTTM': 64.08343704371515,
#     'debtToAssetsTTM': 0.49764094011279597,
#     'debtToEquityTTM': 0.9906080726891491,
#     'debtToMarketCapTTM': 0.09537970800052062,
#     'dividendPerShareTTM': 2.6,
#     'dividendYieldPercentageTTM': 1.0175328741390106,
#     'dividendYieldTTM': 0.010175328741390106,
#     'earningsYieldTTM': 0.03542713669192681,
#     'enterpriseValueOverEBITDATTM': 19.708078531827432,
#     'enterpriseValueTTM': 1946507792353,
#     'evToFreeCashFlowTTM': 32.64966607992553,
#     'evToOperatingCashFlowTTM': 23.066714767295522,
#     'evToSalesTTM': 9.537310221530275,
#     'freeCashFlowPerShareTTM': 8.00134210173131,
#     'freeCashFlowYieldTTM': 0.03134424434214754,
#     'grahamNetNetTTM': -7.187793584753725,
#     'grahamNumberTTM': 70.75405182681254,
#     'incomeQualityTTM': 1.2511082447478836,
#     'intangiblesToTotalAssetsTTM': 0.21467444973556585,
#     'interestCoverageTTM': 41.63650075414781,
#     'interestDebtPerShareTTM': 8.334854381962153,
#     'inventoryTurnoverTTM': 21.806711409395973,
#     'investedCapitalTTM': 0.3282478595142408,
#     'marketCapTTM': 1902039792353,
#     'netCurrentAssetValueTTM': -23593000000,
#     'netDebtToEBITDATTM': 0.4502313525772778,
#     'netIncomePerShareTTM': 9.052341967521139,
#     'operatingCashFlowPerShareTTM': 11.325459669842974,
#     'payablesTurnoverTTM': 4.2323824410577044,
#     'payoutRatioTTM': 0.28116058058681376,
#     'pbRatioTTM': 10.395987244452211,
#     'peRatioTTM': 28.22694954706519,
#     'pfcfRatioTTM': 31.903783963786108,
#     'pocfratioTTM': 22.5615566563174,
#     'priceToSalesRatioTTM': 9.319430225058062,
#     'ptbRatioTTM': 10.395987244452211,
#     'receivablesTurnoverTTM': 5.6956994948790225,
#     'researchAndDevelopementToRevenueTTM': 0.13046439385773223,
#     'returnOnTangibleAssetsTTM': 0.2355951266539058,
#     'revenuePerShareTTM': 27.391491075023488,
#     'roeTTM': 0.393192337736531,
#     'roicTTM': 0.29280425974246377,
#     'salesGeneralAndAdministrativeToRevenueTTM': 0.03412153223514655,
#     'shareholdersEquityPerShareTTM': 24.578714266541404,
#     'stockBasedCompensationToRevenueTTM': 0.04229913667231766,
#     'tangibleAssetValueTTM': 104876000000,
#     'tangibleBookValuePerShareTTM': 14.075426117299692,
#     'workingCapitalTTM': 76105000000
# }
