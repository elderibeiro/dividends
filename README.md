# dividends
Python application to search for stocks with high yeld dividends

Sample output:

% python main.py 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11045 entries, 0 to 11044
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype         
---  ------                       --------------  -----         
 0   shortName                    10707 non-null  object        
 1   symbol                       11045 non-null  object        
 2   fullExchangeName             10898 non-null  object        
 3   dividendDate                 3894 non-null   datetime64[ns]
 4   trailingAnnualDividendRate   8207 non-null   object        
 5   trailingAnnualDividendYield  8207 non-null   object        
dtypes: datetime64[ns](1), object(5)
memory usage: 517.9+ KB
None
                                      shortName  symbol fullExchangeName        dividendDate trailingAnnualDividendRate trailingAnnualDividendYield
2280            Qwest Corporation 6.5% Notes du    CTBB             NYSE 2019-02-28 18:00:00               1000000000.0                  62893084.0
2282            Qwest Corporation 6.75% Notes d    CTDD             NYSE 2018-12-16 18:00:00               1000000000.0                  60386476.0
7740                        POSCO Holdings Inc.     PKX             NYSE 2022-09-08 19:00:00                    12000.0                   200.76962
5796                             KT Corporation      KT             NYSE 2014-04-24 19:00:00                     1960.0                   171.92982
8992                       SK Telecom Co., Ltd.     SKM             NYSE 2022-08-23 19:00:00                     3320.0                   165.25635
5633                     KB Financial Group Inc      KB             NYSE 2022-08-14 19:00:00                     2950.0                    81.46921
8907             Shinhan Financial Group Co Ltd     SHG             NYSE 2022-09-01 19:00:00                     2065.0                    78.42765
10619                Woori Financial Group Inc.      WF             NYSE 2022-08-17 19:00:00                     1130.0                   45.491142
6352            Mizuho Financial Group, Inc. Sp     MFG             NYSE 2017-12-14 18:00:00                       82.5                    30.21978
9068            Sumitomo Mitsui Financial Group    SMFG             NYSE 2022-07-07 19:00:00                      220.0                   28.608582
6051            Loma Negra Compania Industrial     LOMA             NYSE 2023-01-16 18:00:00                    117.956                   18.872961
9530            Takeda Pharmaceutical Company L     TAK             NYSE 2009-12-14 18:00:00                      180.0                    11.19403
9291            Presidio Property Trust, Inc. S   SQFTW         NasdaqGM                 NaT                      0.406                    7.041154
1662                 Catalyst Biosciences, Inc.    CBIO         NasdaqCM 2023-01-11 18:00:00                       1.43                    6.626506
6921                        Nomura Holdings Inc     NMR             NYSE 2017-12-10 18:00:00                       19.0                    5.163043
4661                  Honda Motor Company, Ltd.     HMC             NYSE 2022-06-12 19:00:00                      125.0                    5.022098
6682            Mitsubishi UFJ Financial Group,    MUFG             NYSE 2022-07-10 19:00:00                       30.5                    4.967427
7684                        PLDT Inc. Sponsored     PHI             NYSE 2022-09-19 19:00:00                       89.0                    3.827957
9335                                 Sasol Ltd.     SSL             NYSE 2023-03-23 19:00:00                       21.7                    1.772876
10658                             Wipro Limited     WIT             NYSE 2023-02-13 18:00:00                        6.0                    1.321586
1268                           Banco Macro S.A.     BMA             NYSE 2023-01-03 18:00:00                      22.18                    1.319453
4196   Generation Income Properties Inc Warrant   GIPRW         NasdaqCM                 NaT                       0.65                    1.280536
7519            Petroleo Brasileiro S.A.- Petro   PBR-A             NYSE 2023-01-25 18:00:00                     11.156                    1.264853
7518            Petroleo Brasileiro S.A.- Petro     PBR             NYSE 2023-01-25 18:00:00                     11.156                    1.117836
5402                                  Orix Corp      IX             NYSE 2022-12-12 18:00:00                       89.4                    1.095991
5281            IRSA Inversiones Y Representaci     IRS             NYSE 2022-12-04 18:00:00                      5.414                    1.035182
9344                         SuRo Capital Corp.    SSSS         NasdaqGS 2022-04-14 19:00:00                       2.86                    0.950166
4167            GreenTree Hospitality Group Ltd     GHG             NYSE 2022-01-20 18:00:00                      3.494                    0.848058
9173                     Sony Group Corporation    SONY             NYSE 2022-06-09 19:00:00                       70.0                    0.835921
2732                            DRDGOLD Limited     DRD             NYSE 2023-03-22 19:00:00                        6.0                    0.811908
6116                          Lufax Holding Ltd      LU             NYSE 2022-10-27 19:00:00                      1.517                    0.806915
4154                                Gerdau S.A.     GGB             NYSE 2023-03-29 19:00:00                       3.63                     0.75625
6032            Brasilagro Brazilian Agric Real     LND             NYSE 2022-11-27 18:00:00                      3.239                    0.679036
6785                   National CineMedia, Inc.    NCMI         NasdaqGS 2022-09-05 19:00:00                       0.11                    0.647059
1870                     China Fund, Inc. (The)     CHN             NYSE 2019-01-10 18:00:00                      7.267                    0.594195
1773                        Central Puerto S.A.    CEPU             NYSE 2023-01-08 18:00:00                       2.88                    0.586558
8296               Dr. Reddy's Laboratories Ltd     RDY             NYSE 2022-08-11 19:00:00                       30.0                    0.562008
1904                        Comp En De Mn Cemig     CIG             NYSE 2017-12-12 18:00:00                      0.892                    0.437255
10087           United Microelectronics Corpora     UMC             NYSE 2022-07-20 19:00:00                        3.6                    0.432692
10350           Vinci Partners Investments Ltd.    VINP         NasdaqGS 2023-03-14 19:00:00                      3.753                    0.428914
9768                   Toyota Motor Corporation      TM             NYSE 2017-12-06 18:00:00                       53.0                    0.396766
9289              Presidio Property Trust, Inc.    SQFT         NasdaqCM 2022-12-29 18:00:00                      0.335                    0.320574
8711            D/B/A Sibanye-Stillwater Limite    SBSW             NYSE 2023-04-05 19:00:00                        2.6                    0.316302
10736           Bank Of Montreal MicroSectors E    WTIU         NYSEArca                 NaT                       5.44                    0.306806
8126                                   QIWI plc    QIWI         NasdaqGS 2021-12-13 18:00:00                      1.724                    0.304056
2204                                      33138     CRF             NYSE 2019-03-28 19:00:00                      2.081                    0.297711
10008                          CVR Partners, LP     UAN             NYSE 2023-03-12 19:00:00                      24.58                    0.296323
1961                                     111422     CLM             NYSE                 NaT                       2.17                    0.294038
1905                        Comp En De Mn Cemig   CIG-C             NYSE 2017-12-12 18:00:00                      0.892                    0.293421
1775            Crestwood Equity Partners LP Pr  CEQP-P             NYSE 2023-02-13 18:00:00                       2.62                    0.292737