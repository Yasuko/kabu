
from model.db.Information import Information
from model.db.Industry import Industry


def finance_average():
    # Informationから全企業のデータを取得し、各指標の平均を求める
    informations = Information().get_all_records()
    #print(informations[0])

    # dividendYield(配当利回り)の平均を求める
    dividendYield = (sum([float(row[21]) for row in informations if row[21] is not None]) / len(informations))
    print('dividendYield:', dividendYield)

    # beta(ベータ)の平均を求める
    beta = (sum([float(row[22]) for row in informations if row[22] is not None]) / len(informations))
    print('beta:', beta)
    
    # profitMargins(利益率)の平均を求める
    profitMargins = (sum([float(row[45]) for row in informations if row[45] is not None]) / len(informations))
    print('profitMargins:', profitMargins)

    # priceToBook(株価純資産倍率)の平均を求める
    priceToBook = (sum([float(row[52]) for row in informations if row[52] is not None]) / len(informations))
    print('priceToBook:', priceToBook)

    # enterpriseToEbitda(企業価値EBITDA)の平均を求める
    enterpriseToEbitda = (sum([float(row[63]) for row in informations if row[63] is not None]) / len(informations))
    print('enterpriseToEbitda:', enterpriseToEbitda)

    # enterpriseToRevenue(企業価値売上高)の平均を求める
    enterpriseToRevenue = (sum([float(row[62]) for row in informations if row[62] is not None]) / len(informations))
    print('enterpriseToRevenue:', enterpriseToRevenue)

    # quickRatio(当座比率)の平均を求める
    quickRatio = (sum([float(row[92]) for row in informations if row[92] is not None]) / len(informations))
    print('quickRatio:', quickRatio)

    # currentRatio(流動比率)の平均を求める
    currentRatio = (sum([float(row[93]) for row in informations if row[93] is not None]) / len(informations))
    print('currentRatio:', currentRatio)

    # debtToEquity(負債対資本比率)の平均を求める
    debtToEquity = (sum([float(row[95]) for row in informations if row[95] is not None]) / len(informations))
    print('debtToEquity:', debtToEquity)

    # returnOnAssets(総資産利益率)の平均を求める
    returnOnAssets = (sum([float(row[97]) for row in informations if row[97] is not None]) / len(informations))
    print('returnOnAssets:', returnOnAssets)

    # returnOnEquity(自己資本利益率)の平均を求める
    returnOnEquity = (sum([float(row[98]) for row in informations if row[98] is not None]) / len(informations))
    print('returnOnEquity:', returnOnEquity)

    # revenueGrowth(売上高成長率)の平均を求める
    revenueGrowth = (sum([float(row[101]) for row in informations if row[101] is not None]) / len(informations))
    print('revenueGrowth:', revenueGrowth)

    # grossMargins(粗利益率)の平均を求める
    grossMargins = (sum([float(row[102]) for row in informations if row[102] is not None]) / len(informations))
    print('grossMargins:', grossMargins)

    # editdaMargin(EBITDA利益率)の平均を求める
    editdaMargin = (sum([float(row[103]) for row in informations if row[103] is not None]) / len(informations))
    print('editdaMargin:', editdaMargin)

    # operatingMargin(営業利益率)の平均を求める
    operatingMargin = (sum([float(row[104]) for row in informations if row[104] is not None]) / len(informations))
    print('operatingMargin:', operatingMargin)
    