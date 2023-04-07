import yfinance as yf
import pandas as pd
import json
import matplotlib
from pprint import pprint
import datetime
import requests

from BusinessLogic import sql
from assemble_payload import PayloadAssembler
from fmp_api import FMPapi
from csv_downloader import CSVDownloader

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

"""
DOWNLOAD CSV
dl = CSVDownloader(api_key, ticker)
csv_content = dl.get_balance_sheet_statement_download()
dl.download_from_fmp_api(csv_content)
"""

msft_metrics = PayloadAssembler(api_key, ticker)
# info = msft_metrics.assemble_metrics()
# pprint(info)

info = {'addTotalDebt': 61270000000,
        'address': 'One Microsoft Way',
        'assetTurnoverTTM': 0.5598488007197876,
        'averageInventoryTTM': 3624000000,
        'averagePayablesTTM': 15981500000,
        'averageReceivablesTTM': 33556000000,
        'beta': 0.915117,
        'bookValuePerShareTTM': 24.578714266541404,
        'capexPerShareTTM': -3.324117568111663,
        'capexToDepreciationTTM': -1.7454545454545454,
        'capexToOperatingCashFlowTTM': -0.29350840186760835,
        'capexToRevenueTTM': -0.12135584583574235,
        'capitalExpenditureCoverageRatioTTM': 3.4070574935400515,
        'cashConversionCycleTTM': -18.029236845242124,
        'cashFlowCoverageRatiosTTM': 1.4037661775959012,
        'cashFlowToDebtRatioTTM': 1.4037661775959012,
        'cashPerShareTTM': 13.353241175681116,
        'cashRatioTTM': 0.19146332509361463,
        'ceo': 'Mr. Satya  Nadella',
        'changes': 7.26,
        'cik': '0000789019',
        'city': 'Redmond',
        'companyEquityMultiplierTTM': 1.990608072689149,
        'companyName': 'Microsoft Corporation',
        'country': 'US',
        'currency': 'USD',
        'currentRatioTTM': 1.9313125627156809,
        'cusip': '594918104',
        'date': '2023-03-31',
        'daysOfInventoryOnHandTTM': 16.737966268619967,
        'daysOfInventoryOutstandingTTM': 16.737966268619967,
        'daysOfPayablesOutstandingTTM': 86.23984365382248,
        'daysOfSalesOutstandingTTM': 64.08343704371515,
        'daysPayablesOutstandingTTM': 86.23984365382248,
        'daysSalesOutstandingTTM': 64.08343704371515,
        'dcf': 243.594,
        'dcfDiff': 4.56584,
        'debtEquityRatioTTM': 0.9906080726891491,
        'debtRatioTTM': 0.49764094011279597,
        'debtToAssetsTTM': 0.49764094011279597,
        'debtToEquityTTM': 0.9906080726891491,
        'debtToMarketCapTTM': 0.08357826813543871,
        'defaultImage': False,
        'description': 'Microsoft Corporation develops, licenses, and supports '
                       'software, services, devices, and solutions worldwide. The '
                       'company operates in three segments: Productivity and Business '
                       'Processes, Intelligent Cloud, and More Personal Computing. '
                       'The Productivity and Business Processes segment offers '
                       'Office, Exchange, SharePoint, Microsoft Teams, Office 365 '
                       'Security and Compliance, Microsoft Viva, and Skype for '
                       'Business; Skype, Outlook.com, OneDrive, and LinkedIn; and '
                       'Dynamics 365, a set of cloud-based and on-premises business '
                       'solutions for organizations and enterprise divisions. The '
                       'Intelligent Cloud segment licenses SQL, Windows Servers, '
                       'Visual Studio, System Center, and related Client Access '
                       'Licenses; GitHub that provides a collaboration platform and '
                       'code hosting service for developers; Nuance provides '
                       'healthcare and enterprise AI solutions; and Azure, a cloud '
                       'platform. It also offers enterprise support, Microsoft '
                       'consulting, and nuance professional services to assist '
                       'customers in developing, deploying, and managing Microsoft '
                       'server and desktop solutions; and training and certification '
                       'on Microsoft products. The More Personal Computing segment '
                       'provides Windows original equipment manufacturer (OEM) '
                       'licensing and other non-volume licensing of the Windows '
                       'operating system; Windows Commercial, such as volume '
                       'licensing of the Windows operating system, Windows cloud '
                       'services, and other Windows commercial offerings; patent '
                       'licensing; and Windows Internet of Things. It also offers '
                       'Surface, PC accessories, PCs, tablets, gaming and '
                       'entertainment consoles, and other devices; Gaming, including '
                       'Xbox hardware, and Xbox content and services; video games and '
                       'third-party video game royalties; and Search, including Bing '
                       'and Microsoft advertising. The company sells its products '
                       'through OEMs, distributors, and resellers; and directly '
                       'through digital marketplaces, online stores, and retail '
                       'stores. Microsoft Corporation was founded in 1975 and is '
                       'headquartered in Redmond, Washington.',
        'dividendPaidAndCapexCoverageRatioTTM': 1.9296167566084332,
        'dividendPerShareTTM': 3.2800000000000002,
        'dividendYielPercentageTTM': 1.1248285322359397,
        'dividendYielTTM': 0.011248285322359396,
        'dividendYieldPercentageTTM': 1.1248285322359395,
        'dividendYieldTTM': 0.011248285322359396,
        'earningsYieldTTM': 0.031043696733611584,
        'ebitPerRevenueTTM': 0.4057689104040295,
        'ebtPerEbitTTM': 0.9972589506731873,
        'effectiveTaxRateTTM': 0.18330750230057635,
        'enterpriseValue': 1972536680000,
        'enterpriseValueMultipleTTM': 21.526867259934996,
        'enterpriseValueOverEBITDATTM': 22.42732996508955,
        'enterpriseValueTTM': 2215080098662,
        'evToFreeCashFlowTTM': 37.15455229397162,
        'evToOperatingCashFlowTTM': 26.249379028061526,
        'evToSalesTTM': 10.853234777416288,
        'exchange': 'NASDAQ Global Select',
        'exchangeShortName': 'NASDAQ',
        'fixedAssetTurnoverTTM': 2.1176189833884975,
        'freeCashFlowOperatingCashFlowRatioTTM': 0.7064915981323916,
        'freeCashFlowPerShareTTM': 8.00134210173131,
        'freeCashFlowYieldTTM': 0.027465985302832084,
        'fullTimeEmployees': '221000',
        'grahamNetNetTTM': -7.187793584753725,
        'grahamNumberTTM': 70.75405182681254,
        'grossProfitMarginTTM': 0.6815976951796721,
        'image': 'https://financialmodelingprep.com/image-stock/MSFT.png',
        'incomeQualityTTM': 1.2511082447478836,
        'industry': 'Software—Infrastructure',
        'intangiblesToTotalAssetsTTM': 0.21467444973556585,
        'interestCoverageTTM': 41.63650075414781,
        'interestDebtPerShareTTM': 8.334854381962153,
        'inventoryTurnoverTTM': 21.806711409395973,
        'investedCapitalTTM': 0.3282478595142408,
        'ipoDate': '1986-03-13',
        'isActivelyTrading': True,
        'isAdr': False,
        'isEtf': False,
        'isFund': False,
        'isin': 'US5949181045',
        'lastDiv': 2.72,
        'longTermDebtToCapitalizationTTM': 0.23455087292531338,
        'marketCapTTM': 2170612098662,
        'marketCapitalization': 1925197680000,
        'minusCashAndCashEquivalents': 13931000000,
        'mktCap': 2170612098662,
        'netCurrentAssetValueTTM': -23593000000,
        'netDebtToEBITDATTM': 0.4502313525772778,
        'netIncomePerEBTTTM': 0.8166924976994236,
        'netIncomePerShareTTM': 9.052341967521139,
        'netProfitMarginTTM': 0.3304800729075818,
        'numberOfShares': 7496000000,
        'operatingCashFlowPerShareTTM': 11.325459669842974,
        'operatingCashFlowSalesRatioTTM': 0.4134663439395573,
        'operatingCycleTTM': 32.53936170405658,
        'operatingProfitMarginTTM': 0.4057689104040295,
        'payablesTurnoverTTM': 4.2323824410577044,
        'payoutRatioTTM': 0.28116058058681376,
        'pbRatioTTM': 11.863924078280624,
        'peRatioTTM': 32.21265845305342,
        'pegRatioTTM': 1.6554859913847706,
        'pfcfRatioTTM': 36.4086701778322,
        'phone': '425 882 8080',
        'pocfratioTTM': 25.747299315052263,
        'pretaxProfitMarginTTM': 0.404656677805325,
        'price': 291.6,
        'priceBookValueRatioTTM': 11.863924078280624,
        'priceCashFlowRatioTTM': 25.747299315052263,
        'priceEarningsRatioTTM': 32.21265845305342,
        'priceEarningsToGrowthRatioTTM': -6.778975012231475,
        'priceFairValueTTM': 11.863924078280624,
        'priceSalesRatioTTM': 10.645641714112125,
        'priceToBookRatioTTM': 11.863924078280624,
        'priceToFreeCashFlowsRatioTTM': 36.4086701778322,
        'priceToOperatingCashFlowsRatioTTM': 25.747299315052263,
        'priceToSalesRatioTTM': 10.635354780944073,
        'ptbRatioTTM': 11.863924078280624,
        'quickRatioTTM': 1.6560366137203553,
        'rating': 'A+',
        'ratingDetailsDCFRecommendation': 'Strong Buy',
        'ratingDetailsDCFScore': 5,
        'ratingDetailsDERecommendation': 'Buy',
        'ratingDetailsDEScore': 4,
        'ratingDetailsPBRecommendation': 'Strong Buy',
        'ratingDetailsPBScore': 5,
        'ratingDetailsPERecommendation': 'Strong Buy',
        'ratingDetailsPEScore': 5,
        'ratingDetailsROARecommendation': 'Neutral',
        'ratingDetailsROAScore': 3,
        'ratingDetailsROERecommendation': 'Neutral',
        'ratingDetailsROEScore': 3,
        'ratingRecommendation': 'Strong Buy',
        'ratingScore': 5,
        'receivablesTurnoverTTM': 5.6956994948790225,
        'researchAndDevelopementToRevenueTTM': 0.13046439385773223,
        'returnOnAssetsTTM': 0.18501887247909762,
        'returnOnCapitalEmployedTTM': 0.29280425974246377,
        'returnOnEquityTTM': 0.393192337736531,
        'returnOnTangibleAssetsTTM': 0.2355951266539058,
        'revenuePerShareTTM': 27.391491075023488,
        'roeTTM': 0.393192337736531,
        'roicTTM': 0.2127496467414197,
        'salesGeneralAndAdministrativeToRevenueTTM': 0.03412153223514655,
        'sector': 'Technology',
        'shareholdersEquityPerShareTTM': 24.578714266541404,
        'shortTermCoverageRatiosTTM': 21.112334250688015,
        'state': 'WA',
        'stockBasedCompensationToRevenueTTM': 0.04229913667231766,
        'stockPrice': 256.83,
        'symbol': 'MSFT',
        'tangibleAssetValueTTM': 104876000000,
        'tangibleBookValuePerShareTTM': 14.075426117299692,
        'ticker_range': '213.43-301.12',
        'totalDebtToCapitalizationTTM': 0.24712846865364851,
        'volAvg': 31808980,
        'website': 'https://www.microsoft.com',
        'workingCapitalTTM': 76105000000,
        'zip': '98052-6399'}

import mysql.connector

secfilings = msft_metrics.get_sec_filings()
# pprint(secfilings)


c = sql.Handler(api_key, ticker)
# c.insert(info, "ticker_metrics")

c.update_ticker_metrics()
# c.update_sec_filings()

#sec filings
# for json_package in secfilings:
#     try:
#         c.insert(json_package, "sec_filings")
#         print("Row inserted successfully!")
#     except mysql.connector.Error as e:
#         if e.errno == 1062:
#             print("DUPLICATE ERROR: Row was not updated, it's already in the table.")
#         else:
#             print(f"ERROR: {e}")



# url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?datatype=csv"
# response = requests.get(url, params=payload)
# print(response.status_code)
# with open(f"C:/Users/Public/Downloads/{ticker}_cash_flow_statement.csv", "w") as f:
#     f.write(response.content.decode('utf-8'))

km = {
    'averageInventoryTTM': 3624000000,
    'averagePayablesTTM': 15981500000,
    'averageReceivablesTTM': 33556000000,
    'bookValuePerShareTTM': 24.578714266541404,
    'capexPerShareTTM': -3.324117568111663,
    'capexToDepreciationTTM': -1.7454545454545454,
    'capexToOperatingCashFlowTTM': -0.29350840186760835,
    'capexToRevenueTTM': -0.12135584583574235,
    'cashPerShareTTM': 13.353241175681116,
    'currentRatioTTM': 1.9313125627156809,
    'daysOfInventoryOnHandTTM': 16.737966268619967,
    'daysPayablesOutstandingTTM': 86.23984365382248,
    'daysSalesOutstandingTTM': 64.08343704371515,
    'debtToAssetsTTM': 0.49764094011279597,
    'debtToEquityTTM': 0.9906080726891491,
    'debtToMarketCapTTM': 0.09537970800052062,
    'dividendPerShareTTM': 2.6,
    'dividendYieldPercentageTTM': 1.0175328741390106,
    'dividendYieldTTM': 0.010175328741390106,
    'earningsYieldTTM': 0.03542713669192681,
    'enterpriseValueOverEBITDATTM': 19.708078531827432,
    'enterpriseValueTTM': 1946507792353,
    'evToFreeCashFlowTTM': 32.64966607992553,
    'evToOperatingCashFlowTTM': 23.066714767295522,
    'evToSalesTTM': 9.537310221530275,
    'freeCashFlowPerShareTTM': 8.00134210173131,
    'freeCashFlowYieldTTM': 0.03134424434214754,
    'grahamNetNetTTM': -7.187793584753725,
    'grahamNumberTTM': 70.75405182681254,
    'incomeQualityTTM': 1.2511082447478836,
    'intangiblesToTotalAssetsTTM': 0.21467444973556585,
    'interestCoverageTTM': 41.63650075414781,
    'interestDebtPerShareTTM': 8.334854381962153,
    'inventoryTurnoverTTM': 21.806711409395973,
    'investedCapitalTTM': 0.3282478595142408,
    'marketCapTTM': 1902039792353,
    'netCurrentAssetValueTTM': -23593000000,
    'netDebtToEBITDATTM': 0.4502313525772778,
    'netIncomePerShareTTM': 9.052341967521139,
    'operatingCashFlowPerShareTTM': 11.325459669842974,
    'payablesTurnoverTTM': 4.2323824410577044,
    'payoutRatioTTM': 0.28116058058681376,
    'pbRatioTTM': 10.395987244452211,
    'peRatioTTM': 28.22694954706519,
    'pfcfRatioTTM': 31.903783963786108,
    'pocfratioTTM': 22.5615566563174,
    'priceToSalesRatioTTM': 9.319430225058062,
    'ptbRatioTTM': 10.395987244452211,
    'receivablesTurnoverTTM': 5.6956994948790225,
    'researchAndDevelopementToRevenueTTM': 0.13046439385773223,
    'returnOnTangibleAssetsTTM': 0.2355951266539058,
    'revenuePerShareTTM': 27.391491075023488,
    'roeTTM': 0.393192337736531,
    'roicTTM': 0.29280425974246377,
    'salesGeneralAndAdministrativeToRevenueTTM': 0.03412153223514655,
    'shareholdersEquityPerShareTTM': 24.578714266541404,
    'stockBasedCompensationToRevenueTTM': 0.04229913667231766,
    'tangibleAssetValueTTM': 104876000000,
    'tangibleBookValuePerShareTTM': 14.075426117299692,
    'workingCapitalTTM': 76105000000
}
