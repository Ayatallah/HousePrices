import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_train = pd.read_csv('houses-train.csv',  quotechar='"')
data_test = pd.read_csv('houses-test.csv', quotechar='"')

#print(data_train['Condition1'].describe())
#print(data_train['Condition1'].unique())
#print(data_train['Condition2'].describe())
#print(data_train['Condition2'].unique())
#sns.relplot(y='SalePrice',x='YrSold', hue='Condition1', data=data_train)
#sns.relplot(y='SalePrice',x='MoSold', hue='Condition2', data=data_train)
#print(data_train.Alley.describe()) #only 92 rows, drop alley
#print(data_train.OverallQual.describe())
#print(data_train.OverallQual.unique())
#sns.relplot(y='SalePrice',x='OverallQual', data=data_train)

#print(data_train.TotalBsmtSF.describe())
#print(data_train.TotalBsmtSF.unique())
#sns.relplot(y='SalePrice',x='TotalBsmtSF', data=data_train)

#print(data_train.Heating.describe())
#print(data_train.Heating.unique())
#sns.relplot(y='SalePrice',x='OverallQual',hue='Heating', data=data_train)

#print(data_train.HeatingQC.describe())
#print(data_train.HeatingQC.unique())
#sns.relplot(y='SalePrice',x='HeatingQC', data=data_train)
#sns.relplot(y='SalePrice',x='OverallQual',hue='HeatingQC', data=data_train)

#print(data_train.OverallCond.describe())
#print(data_train.OverallCond.unique())
#sns.relplot(y='SalePrice',x='OverallQual', data=data_train)

#print(data_train.YearBuilt.unique())
#print(data_train.YearBuilt.describe())
#sns.relplot(y='SalePrice',x='YearBuilt', data=data_train)

#print(data_train.CentralAir.describe())
#print(data_train.CentralAir.unique())
#sns.relplot(y='SalePrice',x='CentralAir', data=data_train)

#print(data_train.Electrical.describe())
#print(data_train.Electrical.unique())
#sns.relplot(y='SalePrice',x='Electrical', data=data_train)

#print(data_train.BedroomAbvGr.describe())
#print(data_train.BedroomAbvGr.unique())
#sns.relplot(y='SalePrice',x='BedroomAbvGr', data=data_train)
#print(data_train.KitchenAbvGr.describe())
#print(data_train.KitchenAbvGr.unique())
#sns.relplot(y='SalePrice',x='KitchenAbvGr', data=data_train)

#print(data_train.TotRmsAbvGrd.describe())
#print(data_train.TotRmsAbvGrd.unique())
#sns.relplot(y='SalePrice',x='TotRmsAbvGrd', data=data_train)

#print(data_train.Functional.describe())
#print(data_train.Functional.unique())
#sns.relplot(y='SalePrice',x='TotRmsAbvGrd', data=data_train)

#print(data_train.Fireplaces.describe())
#print(data_train.Fireplaces.unique())
#sns.relplot(y='SalePrice',x='Fireplaces', data=data_train)

#print(data_train.FireplaceQu.describe())
#print(data_train.FireplaceQu.unique())
#sns.relplot(y='SalePrice',x='FireplaceQu', data=data_train)

#print(data_train.GarageType.describe())
#print(data_train.GarageType.unique())
#sns.relplot(y='SalePrice',x='GarageType', data=data_train)

#print(data_train.GarageCars.describe())
#print(data_train.GarageCars.unique())
#sns.relplot(y='SalePrice',x='GarageCars', data=data_train)

#print(data_train.GarageQual.describe())
#print(data_train.GarageQual.unique())
#sns.relplot(y='SalePrice',x='GarageQual', data=data_train)

#print(data_train.GarageArea.describe())
#print(data_train.GarageArea.unique())
#sns.relplot(y='SalePrice',x='GarageArea', data=data_train)

#print(data_train.PavedDrive.describe())
#print(data_train.PavedDrive.unique())
#sns.relplot(y='SalePrice',x='PavedDrive', data=data_train)

#print(data_train.WoodDeckSF.describe())
#print(data_train.WoodDeckSF.unique())
#sns.relplot(y='SalePrice',x='WoodDeckSF', data=data_train)

#print(data_train.OpenPorchSF.describe())
#print(data_train.OpenPorchSF.unique())
#sns.relplot(y='SalePrice',x='OpenPorchSF', data=data_train)
#print(data_train.EnclosedPorch.describe())
#print(data_train.EnclosedPorch.unique())
#sns.relplot(y='SalePrice',x='EnclosedPorch', data=data_train)

#print(data_train.PoolArea.describe())
#print(data_train.PoolArea.unique())
#sns.relplot(y='SalePrice',x='PoolArea', data=data_train)

#print(data_train.Fence.describe())
#print(data_train.Fence.unique())
#sns.relplot(y='SalePrice',x='Fence', data=data_train)

#print(data_train.YearRemodAdd.describe())
#print(data_train.YearRemodAdd.unique())
#sns.relplot(y='SalePrice',x='YearRemodAdd', data=data_train)

#print(data_train.SaleType.describe())
#print(data_train.SaleType.unique())
#sns.relplot(y='SalePrice',x='SaleType', data=data_train)

#print(data_train.MiscFeature.describe())
#print(data_train.MiscFeature.unique())
#sns.relplot(y='SalePrice',x='MiscFeature', data=data_train)

#print(data_train.MSSubClass.describe())
#print(data_train.MSSubClass.unique())
#sns.relplot(y='SalePrice',x='MSSubClass', data=data_train)

#print(data_train.MSZoning.describe())
#print(data_train.MSZoning.unique())
#sns.relplot(y='SalePrice',x='MSZoning', data=data_train)

#print(data_train.LotFrontage.describe())
#print(data_train.LotFrontage.unique())
#sns.relplot(y='SalePrice',x='LotFrontage', data=data_train)

#print(data_train.LotArea.describe())
#print(data_train.LotArea.unique())
#sns.relplot(y='SalePrice',x='LotArea', data=data_train)

#print(data_train.Street.describe())
#print(data_train.Street.unique())
#sns.relplot(y='SalePrice',x='Street', data=data_train)

#print(data_train.LotShape.describe())
#print(data_train.LotShape.unique())
#sns.relplot(y='SalePrice',x='LotShape', data=data_train)

#print(data_train.LandContour.describe())
#print(data_train.LandContour.unique())
#sns.relplot(y='SalePrice',x='LandContour', data=data_train)

#print(data_train.Utilities.describe())
#print(data_train.Utilities.unique())
#sns.relplot(y='SalePrice',x='Utilities', data=data_train)

#print(data_train.LotConfig.describe())
#print(data_train.LotConfig.unique())
#sns.relplot(y='SalePrice',x='LotConfig', data=data_train)

#print(data_train.LandSlope.describe())
#print(data_train.LandSlope.unique())
#sns.relplot(y='SalePrice',x='LandSlope', data=data_train)

#print(data_train.Neighborhood.describe())
#print(data_train.Neighborhood.unique())
#sns.relplot(y='SalePrice',x='Neighborhood', data=data_train)

#print(data_train.BldgType.describe())
#print(data_train.BldgType.unique())
#sns.relplot(y='SalePrice',x='BldgType', data=data_train)

#print(data_train.HouseStyle.describe())
#print(data_train.HouseStyle.unique())
#sns.relplot(y='SalePrice',x='HouseStyle', data=data_train)

#print(data_train.RoofStyle.describe())
#print(data_train.RoofStyle.unique())
#sns.relplot(y='SalePrice',x='RoofStyle', data=data_train)

#print(data_train.RoofMatl.describe())
#print(data_train.RoofMatl.unique())
#sns.relplot(y='SalePrice',x='RoofMatl', data=data_train)

#print(data_train.Exterior1st.describe())
#print(data_train.Exterior1st.unique())
#sns.relplot(y='SalePrice',x='Exterior1st', data=data_train)

#print(data_train.Exterior2nd.describe())
#print(data_train.Exterior2nd.unique())
#sns.relplot(y='SalePrice',x='Exterior2nd', data=data_train)

#print(data_train.MasVnrArea.describe())
#print(data_train.MasVnrArea.unique())
#sns.relplot(y='SalePrice',x='MasVnrArea', data=data_train)

#print(data_train.ExterQual.describe())
#print(data_train.ExterQual.unique())
#sns.relplot(y='SalePrice',x='ExterQual', data=data_train)

#print(data_train.ExterCond.describe())
#print(data_train.ExterCond.unique())
#sns.relplot(y='SalePrice',x='ExterCond', data=data_train)

#print(data_train.Foundation.describe())
#print(data_train.Foundation.unique())
#sns.relplot(y='SalePrice',x='Foundation', data=data_train)

#print(data_train.BsmtQual.describe())
#print(data_train.BsmtQual.unique())
#sns.relplot(y='SalePrice',x='BsmtQual', data=data_train)

#print(data_train.BsmtCond.describe())
#print(data_train.BsmtCond.unique())
#sns.relplot(y='SalePrice',x='BsmtCond', data=data_train)

#print(data_train.BsmtFinSF2.describe())
#print(data_train.BsmtFinSF2.unique())
#sns.relplot(y='SalePrice',x='BsmtFinSF2', data=data_train)

#print(data_train['1stFlrSF'].describe())
#print(data_train['1stFlrSF'].unique())
#sns.relplot(y='SalePrice',x='1stFlrSF', data=data_train)

#print(data_train['2ndFlrSF'].describe())
#print(data_train['2ndFlrSF'].unique())
#sns.relplot(y='SalePrice',x='2ndFlrSF', data=data_train)

#print(data_train.GrLivArea.describe())
#print(data_train.GrLivArea.unique())
#sns.relplot(y='SalePrice',x='GrLivArea', data=data_train)

#print(data_train.FullBath.describe())
#print(data_train.FullBath.unique())
#sns.relplot(y='SalePrice',x='FullBath', data=data_train)

#print(data_train.KitchenQual.describe())
#print(data_train.KitchenQual.unique())
#sns.relplot(y='SalePrice',x='KitchenQual', data=data_train)

#print(data_train.GarageYrBlt.describe())
#print(data_train.GarageYrBlt.unique())
#sns.relplot(y='SalePrice',x='GarageYrBlt', data=data_train)

#print(data_train.GarageFinish.describe())
#print(data_train.GarageFinish.unique())
#sns.relplot(y='SalePrice',x='GarageFinish', data=data_train)

#print(data_train.PavedDrive.describe())
#print(data_train.PavedDrive.unique())
#sns.relplot(y='SalePrice',x='PavedDrive', data=data_train)

#print(data_train['PoolQC'].describe())
#print(data_train['PoolQC'].unique())
#sns.relplot(y='SalePrice',x='PoolQC', data=data_train)

#print(data_train.SaleCondition.describe())
#print(data_train.SaleCondition.unique())
#sns.relplot(y='SalePrice',x='SaleCondition', data=data_train)

#print(data_train.LotArea.describe())
#print(data_train.LotArea.unique())
#sns.relplot(y='SalePrice',x='LotArea', data=data_train)

#plt.show()