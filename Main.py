import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor

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

sale_price = data_train['SalePrice']
data_train = data_train.drop(columns=['SalePrice'])
#DataFrame with training and test data for one time manipulation
data = pd.concat([data_train, data_test])
#Drop Ineffective feature as per visualizations
data = data.drop(columns=['YrSold','MiscFeature','MiscVal','LowQualFinSF','BsmtFullBath','BsmtHalfBath', 'HalfBath','GarageCond', '3SsnPorch',
                          'BsmtFinType1', 'BsmtFinType2', 'BsmtFinSF1', 'BsmtFinSF2', 'ScreenPorch', 'PoolQC','BsmtExposure', 'CentralAir','Electrical',
                          'BedroomAbvGr','SaleType','Fence','Utilities','PoolArea', 'PoolQC', 'MasVnrType', 'Condition1', 'Condition2','Functional', 'Alley','OpenPorchSF',
                          'EnclosedPorch', 'Id', 'FireplaceQu'])
#print(data.info())
#Fill Missing Values
#print(data['GarageQual'].describe())
#print(data['GarageQual'].isnull().values.any())
data['GarageQual'].fillna(str(data.GarageQual.mode()[0]), inplace=True)
#print(data['GarageQual'].describe())
#print(data['GarageQual'].isnull().values.any())
data['GarageQual'].fillna(str(data.GarageQual.mode()[0]), inplace=True)
data['GarageArea'].fillna(data.GarageArea.mean(), inplace=True)
data['GarageCars'].fillna(data.GarageCars.median(), inplace=True)
data['GarageFinish']=data['GarageFinish'].replace(np.nan, str(data.GarageFinish.mode()[0]), regex=True)
data['GarageYrBlt']=data['GarageYrBlt'].replace(np.nan, data.GarageYrBlt.median(), regex=True)
data['GarageType']=data['GarageType'].replace(np.nan, str(data.GarageType.mode()[0]), regex=True)
data['KitchenQual'].fillna(str(data.KitchenQual.mode()[0]), inplace=True)
data['TotalBsmtSF'].fillna(data.TotalBsmtSF.mean(), inplace=True)
data['BsmtUnfSF'].fillna(data.BsmtUnfSF.mean(), inplace=True)
data['BsmtCond'].fillna(str(data.BsmtCond.mode()[0]), inplace=True)
data['BsmtQual'].fillna(str(data.BsmtQual.mode()[0]), inplace=True)
data['MasVnrArea'].fillna(data.MasVnrArea.mean(), inplace=True)
data['Exterior2nd'].fillna(str(data.Exterior2nd.mode()[0]), inplace=True)
data['Exterior1st'].fillna(str(data.Exterior1st.mode()[0]), inplace=True)
data['LotFrontage'].fillna(data['LotFrontage'].mean(), inplace=True)
data['MSZoning']=data['MSZoning'].replace(np.nan, str(data.MSZoning.mode()[0]), regex=True)
print(data.info())
#Turning Categorical Data into Numerical
print(data_train['MSZoning'].unique())
print(data_train['MSZoning'].describe())

print(data['Street'].unique())
print(data['Street'].describe())

print(data['LotShape'].unique())
print(data['LotShape'].describe())

print(data['LandContour'].unique())
print(data['LandContour'].describe())

print(data['LotConfig'].unique())
print(data['LotConfig'].describe())

print(data['LandSlope'].unique())
print(data['LandSlope'].describe())

print(data['Neighborhood'].unique())
print(data['Neighborhood'].describe())

print(data['BldgType'].unique())
print(data['BldgType'].describe())

print(data['HouseStyle'].unique())
print(data['HouseStyle'].describe())

print(data['RoofStyle'].unique())
print(data['RoofStyle'].describe())

print(data['RoofMatl'].unique())
print(data['RoofMatl'].describe())

print(data['Exterior1st'].unique())
print(data['Exterior1st'].describe())

print(data['Exterior2nd'].unique())
print(data['Exterior2nd'].describe())

print(data['ExterQual'].unique())
print(data['ExterQual'].describe())

print(data['ExterCond'].unique())
print(data['ExterCond'].describe())

print(data['Foundation'].unique())
print(data['Foundation'].describe())

print(data['BsmtQual'].unique())
print(data['BsmtQual'].describe())

print(data['BsmtCond'].unique())
print(data['BsmtCond'].describe())

print(data['Heating'].unique())
print(data['Heating'].describe())

print(data['HeatingQC'].unique())
print(data['HeatingQC'].describe())

print(data['KitchenQual'].unique())
print(data['KitchenQual'].describe())

print(data['GarageType'].unique())
print(data['GarageType'].describe())

print(data['GarageFinish'].unique())
print(data['GarageFinish'].describe())

print(data['GarageQual'].unique())
print(data['GarageQual'].describe())

print(data['PavedDrive'].unique())
print(data['PavedDrive'].describe())

print(data['SaleCondition'].unique())
print(data['SaleCondition'].describe())

## Features with seemingly effective variations
data = pd.get_dummies(data, columns={'MSZoning', 'LotShape','LandContour','LotConfig','LandSlope','Neighborhood','HouseStyle','RoofStyle','Exterior1st','Exterior2nd','ExterQual',
                                          'ExterCond','BsmtQual', 'HeatingQC','KitchenQual','GarageFinish','SaleCondition'})
## Features with only two category or only two distictive categories
data['BldgType']= data['BldgType'].replace({'1Fam':1, '2fmCon':0, 'Duplex':0,'TwnhsE':0,'Twnhs':0})
data['Street']= data['Street'].replace({'Pave':1, 'Grvl':0})
data['RoofMatl']= data['RoofMatl'].replace({'CompShg':1, 'WdShngl':0, 'Metal':0, 'WdShake':0, 'Membran':0, 'Tar&Grv':0, 'Roll':0, 'ClyTile':0})
data['Foundation']= data['Foundation'].replace({'PConc':1, 'CBlock':0, 'BrkTil':0, 'Wood':0, 'Slab':0, 'Stone':0})
data['BsmtCond']= data['BsmtCond'].replace({'TA':1, 'Gd':0, 'Fa':0, 'Po':0})
data['Heating']= data['Heating'].replace({'GasA':1, 'GasW':0, 'Grav':0, 'Wall':0, 'OthW':0, 'Floor':0})
data['GarageType']= data['GarageType'].replace({'Attchd':1, 'BuiltIn':1, 'Detchd':0, 'CarPort':0, 'Basment':0, '2Types':0})
data['GarageQual']= data['GarageQual'].replace({'TA':1, 'Gd':0, 'Fa':0, 'Po':0, 'Ex':0})
data['PavedDrive']= data['PavedDrive'].replace({'Y':1, 'N':0, 'P':0})
print(data.info())

