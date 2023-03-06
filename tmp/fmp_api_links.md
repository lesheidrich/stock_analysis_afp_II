##most active stocks
https://financialmodelingprep.com/api/v3/stock_market/actives?apikey=YOUR_API_KEY

##most loser stocks
https://financialmodelingprep.com/api/v3/stock_market/losers?apikey=YOUR_API_KEY

##gainers
https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=YOUR_API_KEY

##sector performance
https://financialmodelingprep.com/api/v3/stock/sector-performance?apikey=YOUR_API_KEY
[ {
    "sector" : "Basic Materials",
    "changesPercentage" : "0.0849%"
  }, {
    "sector" : "Building",
    "changesPercentage" : "2.4699%"
  }, {
    "sector" : "Communication Services",
    "changesPercentage" : "-0.7655%"
  }, {
    "sector" : "Conglomerates",
    "changesPercentage" : "0.0000%"
  }, ...
]

##FMP news articles
https://financialmodelingprep.com/api/v3/fmp/articles?page=0&size=5&apikey=YOUR_API_KEY

##market capitalization
https://financialmodelingprep.com/api/v3/market-capitalization/AAPL?apikey=YOUR_API_KEY
[ {
    "symbol" : "AAPL",
    "date" : "2020-07-24",
    "marketCap" : 1641007358213.16797
} ]

##company profile
https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=YOUR_API_KEY
[ {
  "symbol" : "AAPL",
  "price" : 145.85,
  "beta" : 1.201965,
  "volAvg" : 79766736,
  "mktCap" : 2410929717248,
  "lastDiv" : 0.85,
  "range" : "105.0-157.26",
  "changes" : 2.4200134,
  "companyName" : "Apple Inc.",
  "currency" : "USD",
  "cik" : "0000320193",
  "isin" : "US0378331005",
  "cusip" : "037833100",
  "exchange" : "Nasdaq Global Select",
  "exchangeShortName" : "NASDAQ",
  "industry" : "Consumer Electronics",
  "website" : "http://www.apple.com",
  "description" : "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services.

##historical dividends
https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/AAPL?apikey=YOUR_API_KEY
{
  "symbol" : "AAPL",
  "historical" : [ {
    "date" : "2020-08-07",
    "label" : "August 07, 20",
    "adjDividend" : 0.2050000000,
    "dividend" : 0.82,
    "recordDate" : "2020-08-10",
    "paymentDate" : "2020-08-13",
    "declarationDate" : "2020-07-30"
  }, {
    "date" : "2020-05-08",
    "label" : "May 08, 20",

##dividend calendar
https://financialmodelingprep.com/api/v3/stock_dividend_calendar?from=2020-01-01&to=2020-09-01&apikey=YOUR_API_KEY
[ {
    "date" : "2020-09-02",
    "label" : "September 02, 20",
    "adjDividend" : 0.02,
    "symbol" : "BOL.PA"
  }, {
    "date" : "2020-09-01",
    "label" : "September 01, 20",
    "adjDividend" : 0.47,
    "symbol" : "WKL.AS"
  }, {
    "date" : "2020-09-01",
    "label" : "September 01, 20",
    "adjDividend" : 0.002809,
    "symbol" : "ITUB"
  }, {
    "date" : "2020-09-01",
    "label" : "September 01, 20",
    "adjDividend" : 0.05,
    "symbol" : "FEI"
  }, ...
]

##rating
https://financialmodelingprep.com/api/v3/rating/AAPL?apikey=YOUR_API_KEY
[ {
    "symbol" : "AAPL",
    "date" : "2020-09-04",
    "rating" : "S-",
    "ratingScore" : 5,
    "ratingRecommendation" : "Strong Buy",
    "ratingDetailsDCFScore" : 5,
    "ratingDetailsDCFRecommendation" : "Strong Buy",
    "ratingDetailsROEScore" : 4,
    "ratingDetailsROERecommendation" : "Buy",
    "ratingDetailsROAScore" : 3,
    "ratingDetailsROARecommendation" : "Neutral",
    "ratingDetailsDEScore" : 5,
    "ratingDetailsDERecommendation" : "Strong Buy",
    "ratingDetailsPEScore" : 5,
    "ratingDetailsPERecommendation" : "Strong Buy",
    "ratingDetailsPBScore" : 5,
    "ratingDetailsPBRecommendation" : "Strong Buy"
} ]

##key metrics
https://financialmodelingprep.com/api/v3/key-metrics-ttm/AAPL?limit=40&apikey=YOUR_API_KEY
#no ttm is just annual, AAPL?period=quarter&limit=200 for quarterly
[ {
  "revenuePerShareTTM" : 15.721603439708202,
  "netIncomePerShareTTM" : 3.354009425946797,
  "operatingCashFlowPerShareTTM" : 1.1429947910208258,
  "freeCashFlowPerShareTTM" : 0.9835725642671928,
  "cashPerShareTTM" : 1.916453797521257,
  "bookValuePerShareTTM" : 4.149570541665863,
  "tangibleBookValuePerShareTTM" : 18.218108436047864,
  "shareholdersEquityPerShareTTM" : 4.149570541665863,
  "interestDebtPerShareTTM" : 6.2513376081682965,
  "marketCapTTM" : 2029331208000,
  "enterpriseValueTTM" : 2101792208000,
  "peRatioTTM" : 34.73454758318499,
  "priceToSalesRatioTTM" : 7.410185637029544,
  "pocfratioTTM" : 101.92522390758413,
  "pfcfRatioTTM" : 118.44576011206443,
  "pbRatioTTM" : 28.075194488254336,
  "ptbRatioTTM" : 28.075194488254336,
  "evToSalesTTM" : 7.674779932592558,
  "enterpriseValueOverEBITDATTM" : 25.353649718331948,
  "evToOperatingCashFlowTTM" : 105.56465133098945,
  "evToFreeCashFlowTTM" : 122.67508363975954,
  "earningsYieldTTM" : 0.028789780480230016,
  "freeCashFlowYieldTTM" : 0.0084426829550832,
  "debtToEquityTTM" : 3.3903599789712513,
  "debtToAssetsTTM" : 0.7722282444287587,
  "netDebtToEBITDATTM" : 0.874087745328653,
  "currentRatioTTM" : 1.4694496317589543,
  "interestCoverageTTM" : 22.406362741882585,
  "incomeQualityTTM" : 0.34078460906476793,
  "dividendYieldTTM" : 0.006824034334763949,
  "dividendYieldPercentageTTM" : 0.682403433476394900,
  "payoutRatioTTM" : 0.23702974531014653,
  "salesGeneralAndAdministrativeToRevenueTTM" : null,
  "researchAndDevelopementToRevenueTTM" : 0.06530415508823949,
  "intangiblesToTotalAssetsTTM" : 0.0,
  "capexToOperatingCashFlowTTM" : -7.169607490097227,
  "capexToRevenueTTM" : -98.61613251710479,
  "capexToDepreciationTTM" : -1.1447605329492259,
  "stockBasedCompensationToRevenueTTM" : 0.005473659610672723,
  "grahamNumberTTM" : 17.695994489813657,
  "roicTTM" : 0.30769819750839994,
  "returnOnTangibleAssetsTTM" : 0.1841030553594837,
  "grahamNetNetTTM" : -7.232943945836169,
  "workingCapitalTTM" : 44747000000,
  "tangibleAssetValueTTM" : null,
  "netCurrentAssetValueTTM" : -6.0276757444908915,
  "investedCapitalTTM" : null,
  "averageReceivablesTTM" : 31376000000,
  "averagePayablesTTM" : 33873000000,
  "averageInventoryTTM" : 3656000000,
  "daysSalesOutstandingTTM" : 10.541085310946954,
  "daysPayablesOutstandingTTM" : 18.781346550328752,
  "daysOfInventoryOnHandTTM" : 2.1149949491070847,
  "receivablesTurnoverTTM" : 8.538020265003897,
  "payablesTurnoverTTM" : 4.791988676574664,
  "inventoryTurnoverTTM" : 42.55329311211664,
  "roeTTM" : 0.808278686256606,
  "capexPerShareTTM" : -0.15942222675363302
} ]

##annual enterprise value
https://financialmodelingprep.com/api/v3/enterprise-values/AAPL?limit=40&apikey=YOUR_API_KEY
[ {
    "symbol" : "AAPL",
    "date" : "2019-09-28",
    "stockPrice" : 62.262501,
    "numberOfShares" : 4648913000,
    "marketCapitalization" : 289452950311.413,
    "minusCashAndCashEquivalents" : 48844000000,
    "addTotalDebt" : 97787000000,
    "enterpriseValue" : 338395950311.413
  },
  {
    "symbol" : "AAPL",
    "date" : "2018-09-29",
    "stockPrice" : 53.060001,
    "numberOfShares" : 5000109000,
    "marketCapitalization" : 265305788540.109,
    "minusCashAndCashEquivalents" : 25913000000,
    "addTotalDebt" : 105699000000,
    "enterpriseValue" : 345091788540.109
  }, ...
]

##financial ratios
https://financialmodelingprep.com/api/v3/ratios-ttm/AAPL?apikey=YOUR_API_KEY
[ {
  "dividendYielTTM" : 0.0056837178201270475,
  "dividendYielPercentageTTM" : 0.5683717820127047500,
  "peRatioTTM" : 29.277605,
  "pegRatioTTM" : 2.75947190433071,
  "payoutRatioTTM" : 0.16284147081864472,
  "currentRatioTTM" : 1.0618909738849602,
  "quickRatioTTM" : 0.8872431649869147,
  "cashRatioTTM" : 0.31599754997494295,
  "daysOfSalesOutstandingTTM" : 35.650991631979956,
  "daysOfInventoryOutstandingTTM" : 9.228188902560497,
  "operatingCycleTTM" : 18.018844373459665,
  "daysOfPayablesOutstandingTTM" : 72.01658659010566,
  "cashConversionCycleTTM" : -34.090151119138184,
  "grossProfitMarginTTM" : 0.4100502657314456,
  "operatingProfitMarginTTM" : 0.2878771730206968,
  "pretaxProfitMarginTTM" : 0.29053304719793754,
  "netProfitMarginTTM" : 0.25003816738920653,
  "effectiveTaxRateTTM" : 0.13938132064247472,
  "returnOnAssetsTTM" : 0.26316395828280376,
  "returnOnEquityTTM" : 1.3101150474868029,
  "returnOnCapitalEmployedTTM" : 0.4499968480678656,
  "netIncomePerEBTTTM" : 0.8606186793575252,
  "ebtPerEbitTTM" : 1.0092257199463668,
  "ebitPerRevenueTTM" : 0.2878771730206968,
  "debtRatioTTM" : 0.8051176327916566,
  "debtEquityRatioTTM" : 4.131300560049782,
  "longTermDebtToCapitalizationTTM" : 0.6219535146325398,
  "totalDebtToCapitalizationTTM" : 0.6545404711104901,
  "interestCoverageTTM" : 38.33448408131952,
  "cashFlowToDebtRatioTTM" : 0.857321148524932,
  "companyEquityMultiplierTTM" : 5.131300560049782,
  "receivablesTurnoverTTM" : 10.238144390704258,
  "payablesTurnoverTTM" : 5.068276869014328,
  "inventoryTurnoverTTM" : 39.552723059096174,
  "fixedAssetTurnoverTTM" : 8.990159264534507,
  "assetTurnoverTTM" : 1.0524951491632306,
  "operatingCashFlowPerShareTTM" : 6.278890524482255,
  "freeCashFlowPerShareTTM" : 5.698832505450747,
  "cashPerShareTTM" : 3.7100621544855787,
  "operatingCashFlowSalesRatioTTM" : 0.3007705491783209,
  "freeCashFlowOperatingCashFlowRatioTTM" : 0.9076177524086808,
  "cashFlowCoverageRatiosTTM" : 0.857321148524932,
  "shortTermCoverageRatiosTTM" : 6.510006858282935,
  "capitalExpenditureCoverageRatioTTM" : -10.824590503835786,
  "dividendPaidAndCapexCoverageRatioTTM" : -10.824590504789644,
  "priceBookValueRatioTTM" : 38.68889908291848,
  "priceToBookRatioTTM" : 38.68889908291848,
  "priceToSalesRatioTTM" : 7.163723504054386,
  "priceEarningsRatioTTM" : 28.650519954033317,
  "priceToFreeCashFlowsRatioTTM" : 26.242217130782542,
  "priceToOperatingCashFlowsRatioTTM" : 23.817902130461434,
  "priceCashFlowRatioTTM" : 23.817902130461434,
  "priceEarningsToGrowthRatioTTM" : 2.75947190433071,
  "priceSalesRatioTTM" : 7.163723504054386,
  "dividendYieldTTM" : 0.0056837178201270475,
  "enterpriseValueMultipleTTM" : 22.493215622815907,
  "priceFairValueTTM" : 38.68889908291848,
  "dividendPerShareTTM" : 0.85
} ]

##sec filings
https://financialmodelingprep.com/api/v3/sec_filings/AAPL?page=0&apikey=YOUR_API_KEY
[ {
    "symbol" : "AAPL",
    "fillingDate" : "2020-10-05 00:00:00",
    "acceptedDate" : "2020-10-05 18:33:56",
    "cik" : "0000320193",
    "type" : "4",
    "link" : "https://www.sec.gov/Archives/edgar/data/320193/000032019320000084/0000320193-20-000084-index.htm",
    "finalLink" : "https://www.sec.gov/Archives/edgar/data/320193/000032019320000084/xslF345X03/wf-form4_160193720275669.xml"
  }, {
    "symbol" : "AAPL",
    "fillingDate" : "2020-10-05 00:00:00",
    "acceptedDate" : "2020-10-05 18:32:48",
    "cik" : "0000320193",
    "type" : "4",
    "link" : "https://www.sec.gov/Archives/edgar/data/320193/000032019320000083/0000320193-20-000083-index.htm",
    "finalLink" : "https://www.sec.gov/Archives/edgar/data/320193/000032019320000083/xslF345X03/wf-form4_160193715587800.xml"
  }, {
    "symbol" : "AAPL",
    "fillingDate" : "2020-10-05 00:00:00",
    "acceptedDate" : "2020-10-05 18:30:48",
    "cik" : "0000320193",
    "type" : "4",
    "link" : "https://www.sec.gov/Archives/edgar/data/320193/000032019320000082/0000320193-20-000082-index.htm",
    "finalLink" : "https://www.sec.gov/Archives/edgar/data/320193/000032019320000082/xslF345X03/wf-form4_160193701297920.xml"
  }, ...
]

##income statement
https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=YOUR_API_KEY'

##cashflow statement
https://financialmodelingprep.com/api/v3/cash-flow-statement/AAPL?apikey=YOUR_API_KEY&limit=120

##balance sheet
https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?apikey=YOUR_API_KEY&limit=120'




**********************************************************************************************************

##most active stocks
https://financialmodelingprep.com/api/v3/stock_market/actives?apikey=YOUR_API_KEY

##most loser stocks
https://financialmodelingprep.com/api/v3/stock_market/losers?apikey=YOUR_API_KEY

##gainers
https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=YOUR_API_KEY

##sector performance
https://financialmodelingprep.com/api/v3/stock/sector-performance?apikey=YOUR_API_KEY

----------------------------------------------------------------------------------

##FMP news articles
https://financialmodelingprep.com/api/v3/fmp/articles?page=0&size=5&apikey=YOUR_API_KEY

##company profile
https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=YOUR_API_KEY

##historical dividends
https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/AAPL?apikey=YOUR_API_KEY

##dividend calendar
https://financialmodelingprep.com/api/v3/stock_dividend_calendar?from=2020-01-01&to=2020-09-01&apikey=YOUR_API_KEY

##rating
https://financialmodelingprep.com/api/v3/rating/AAPL?apikey=YOUR_API_KEY

##done: key metrics
https://financialmodelingprep.com/api/v3/key-metrics-ttm/AAPL?limit=40&apikey=YOUR_API_KEY

##annual enterprise value
https://financialmodelingprep.com/api/v3/enterprise-values/AAPL?limit=40&apikey=YOUR_API_KEY

##financial ratios
https://financialmodelingprep.com/api/v3/ratios-ttm/AAPL?apikey=YOUR_API_KEY

##sec filings
https://financialmodelingprep.com/api/v3/sec_filings/AAPL?page=0&apikey=YOUR_API_KEY

##income statement
https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=YOUR_API_KEY'

##cashflow statement
https://financialmodelingprep.com/api/v3/cash-flow-statement/AAPL?apikey=YOUR_API_KEY&limit=120

##balance sheet
https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?apikey=YOUR_API_KEY&limit=120'
