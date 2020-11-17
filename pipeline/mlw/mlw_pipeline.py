import pandas as pd

# MLW_Meta = pd.read_csv('MLW_Meta.csv')

MLW = pd.read_csv('data/raw/mlw/MLW - MLW.csv') #Problem with encoding of raw csv file. had to upload to google sheets and re-download

# MLW

# MLW.columns

col = ['X','Y','FID','RecordSequenceID','UniqueID','SourceID','LocationFreqID','Location','Dataset','Organization','Other',
'CountryName_FromSource','SubCountry_L1_FromSource','SubCountry_L2_FromSource','Longitude1',
'Latitude1','Longitude2','Latitude2','TotalWidth_m',
'TotalLength_m','TotalArea_Sq_m','ShorelineName','WaterfrontName','BeachAreaLandcover','BeachType',
'EventType','TotalVolunteers','DateOriginal',
'DateStandardized','MonthYear','Year','MonthNum','Month',
'Day','StartTime',
'DOW','FieldObsevations',
'DebrisDescription','Totalltems_EventRecord','TotalClassifiedItems_EC2020',
'PCT_PlasticAndFoam','PCT_Glass_Rubber_Lumber_Metal','SUM_Hard_PlasticBeverageBottle','SUM_Hard_OtherPlasticBottle','SUM_HardOrSoft_PlasticBottleCap',
'SUM_other_PlasticOrFoamFoodContainer',
'SUM_Hard_BucketOrCrate','SUM_Hard_Lighter','SUM_OtherHardPlastic','SUM_PlasticOrFoamPlatesBowlsCup','SUM_HardSoft_PersonalCareProduc',
'SUM_Hard_LollipopStick_EarBu','SUM_Soft_Bag','SUM_Soft_WrapperOrLabel','SUM_Soft_Straw','SUM_Soft_OtherPlastic','SUM_Soft_CigaretteButts','SUM_Other_StringRingRibbon',
'SUM_Other__Net','SUM_Other_FishingLineLureRope','SUM_other_BuoysAndFloats','SUM_Foam_OtherPlasticDebris','SUM_Other_OtherPlasticDebris','NAME','COUNTRY','ISO_CODE',
'ISO_CC','ISO_SUB',
'ADMINTYPE','DISPUTED','NOTES','AUTONOMOUS',
'COUNTRYAFF','CONTINENT','LAND_TYPE','LAND_RANK','Shape__Area','Shape__Length','Count_',
'Soft_sheets','Other_StrapsTiesBands','Other_Glowsticks','OtherFishing']

df = pd.DataFrame(columns = col) #Creating our new dataframe in EC2020 schema

MLW.fillna(0, inplace = True) #replace NaN with 0 for analysis

df['X'] = MLW.iloc[:,10]

df['Y'] = MLW.iloc[:,11]

df['Totalltems_EventRecord'] = MLW.iloc[:,14:176].sum(axis=1) #38

df['TotalClassifiedItems_EC2020'] = MLW.iloc[:,14:104].sum(axis=1) #39

df['PCT_PlasticAndFoam'] = MLW.iloc[:,14:104].sum(axis=1) / MLW.iloc[:,14:176].sum(axis=1) #40

df['PCT_Glass_Rubber_Lumber_Metal'] = MLW.iloc[:,104:176].sum(axis=1) / MLW.iloc[:,14:176].sum(axis=1) #41

df['SUM_Hard_PlasticBeverageBottle'] = MLW.iloc[:,18:20].sum(axis=1) #42

df.iloc[:,43] = MLW.iloc[:,20] + MLW.iloc[:,22:29].sum(axis=1)

df.iloc[:,44] = MLW.iloc[:,31:34].sum(axis=1)
df.iloc[:,45] = MLW.iloc[:,21]
df.iloc[:,46] = MLW.iloc[:,29] + MLW.iloc[:,69]
df.iloc[:,47] = MLW.iloc[:,36]
df.iloc[:,48] = MLW.iloc[:,30] + MLW.iloc[:,38] + MLW.iloc[:,42] + MLW.iloc[:,68] + MLW.iloc[:,73:75].sum(axis=1) + MLW.iloc[:,84] + MLW.iloc[:,88] + MLW.iloc[:,90]

df.iloc[:,49] = MLW.iloc[:,43:45].sum(axis=1)

df.iloc[:,50] = MLW.iloc[:,39] + MLW.iloc[:,95] + MLW.iloc[:,97:100].sum(axis=1)

df.iloc[:,51] = MLW.iloc[:,41] + MLW.iloc[:,94]
df.iloc[:,52] = MLW.iloc[:,90] + MLW.iloc[:,15:18].sum(axis=1) + MLW.iloc[:,46:48].sum(axis=1)
df.iloc[:,53] = MLW.iloc[:,35] + MLW.iloc[:,40] + MLW.iloc[:,85]
df.iloc[:,54] = MLW.iloc[:,45]
df.iloc[:,55] = MLW.iloc[:,48] + MLW.iloc[:,87] + MLW.iloc[:,92]
df.iloc[:,56] = MLW.iloc[:,32]
df.iloc[:,57] = MLW.iloc[:,14] + MLW.iloc[:,34]
df.iloc[:,58] = MLW.iloc[:,53] + MLW.iloc[:,58:62].sum(axis=1)
df.iloc[:,59] = MLW.iloc[:,64] + MLW.iloc[:,56:58].sum(axis=1)
df.iloc[:,60] = MLW.iloc[:,66:68].sum(axis=1)
#no data in 61
df.iloc[:,62] = MLW.iloc[:,49:53].sum(axis=1) + MLW.iloc[:,54] + MLW.iloc[:,62:64].sum(axis=1) + MLW.iloc[:,77:84].sum(axis=1) + MLW.iloc[:,101:103].sum(axis=1) + MLW.iloc[:,86] + MLW.iloc[:,89] + MLW.iloc[:,91] + MLW.iloc[:,96]

df.iloc[:,79] = MLW.iloc[:,55] + MLW.iloc[:,71]
df.iloc[:,80] = MLW.iloc[:,70] + MLW.iloc[:,93]
df.iloc[:,81] = MLW.iloc[:,66] 

MLW.iloc[:,103]

MLW.iloc[:,14:104].sum(axis=1)

df.to_csv("data/processed/mlw__ec2020-format.csv")
