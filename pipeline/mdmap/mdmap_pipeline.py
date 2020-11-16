import numpy as np
import pandas as pd
import datetime



raw_data = pd.read_csv('data/raw/mdmap/RawStandingStockReport.csv')


# OCPDS = pd.read_csv('Ocean_Plastics_dataset_schemas.csv')


#Getting all variable names from column 1, which will be the column names for the new data frame
# col_names = OCPDS.iloc[1:,:1].to_numpy().flatten()
# print(col_names, len(col_names), end = '\n\n')

#Columns for the raw data, that must be matched
# print(raw_data.columns)
# print(len(raw_data.columns))



#Getting all records for column 1 of raw data
# raw_data[raw_data.columns[84]]

# I've indentified which variables from the old data set can be directly
# put under new variable names, these are highlighted in green under my variable_matchup document.
# 
# Everything in yellow I have to lookup either by researching the surroundinf documentation
# Or looking at what my team members did in thier python scripts


#Creating DataSet Columns
name_dataset = 'MDMAP'
Dataset = []
for i in range(len(raw_data)):
    Dataset.append(name_dataset)



#Creating DateStandardized, MonthYear, Year, MonthNum, Month
DateStandardized = []
for i in range(len(raw_data)):
    date_time_obj = datetime.datetime.strptime(raw_data.iloc[i,2], '%m-%d-%Y')
    date_time_str_final = str(date_time_obj.month) + '/' + str(date_time_obj.day) + '/' + str(date_time_obj.year) + ' 00:00:00'
    DateStandardized.append(date_time_str_final)



TotalItems_EventRecord = np.array(raw_data[raw_data.columns[84]])



#TotalClassifiedItems_EC2020
#Total number of plastics debris items recovered as reported by data source that are plastic (plastic defined as item listed in modified CSIRO"EC2020_DataModel1" these include  plastics, foams and fishing items and included cigarette butts) Please see here, here and here for more details

#Hard Plastic Fragments index 32
#Foamed Plastic Fragments index 33
#Filmed Plastic Fragments index 34
#Food Wrappers index 35
#Plastic Beverage Bottles index 36
#Other Jugs/Containers index 37
#Bottle/Container Caps index 38
#Cigar Tips index 39
#Cigarettes index 40
#Disposable Cigarette Lighters index 41
#6-Pack Rings index 42
#Bags index 43
#Plastic Rope/Net index 44
#Buoys & Floats index 45
#Fishing Lures & Line index 46
#Cups index 47
#Plastic Utensils index 48
#Straws index 49
#Balloons Mylar index 50
#Personal Care Products index 51
#Plastic Other index 52

TotalClassifiedItems_EC2020 = np.array([])

for i in range(len(raw_data)):
    
    num1 = raw_data.iloc[i,32] + raw_data.iloc[i,33] + raw_data.iloc[i,34] + raw_data.iloc[i,35] + raw_data.iloc[i,36] 
    num2 = raw_data.iloc[i,37] + raw_data.iloc[i,38] + raw_data.iloc[i,39] + raw_data.iloc[i,40] + raw_data.iloc[i,41] 
    num3 = raw_data.iloc[i,42] + raw_data.iloc[i,43] + raw_data.iloc[i,44] + raw_data.iloc[i,45] + raw_data.iloc[i,46] 
    num4 = raw_data.iloc[i,47] + raw_data.iloc[i,48] + raw_data.iloc[i,49] + raw_data.iloc[i,50] + raw_data.iloc[i,51] 
    num5 = raw_data.iloc[i,52] 
    num_total = num1+num2+num3+num4+num5
    TotalClassifiedItems_EC2020 = np.append(TotalClassifiedItems_EC2020,num_total)



#PCT_Glass_Rubber_Lumber_Metal
#PCT= percentage total percent of marine debris that are non-plastic (glass, rubber, lumber, metal) compared to overall marine debris collected
glass_rubber_lumber_metal_total = np.array([])

for i in range(len(raw_data)):
        num1 = raw_data.iloc[i,53] #metal
        num2 = raw_data.iloc[i,58] #glass
        num3 = raw_data.iloc[i,63] #rubber
        num4 = raw_data.iloc[i,70] #lumber
        num_total = num1 + num2 + num3 + num4
        glass_rubber_lumber_metal_total = np.append(glass_rubber_lumber_metal_total, num_total)

PCT_Glass_Rubber_Lumber_Metal_Total = np.divide(glass_rubber_lumber_metal_total, TotalItems_EventRecord)



#PCT_PlasticAndFoam
#PCT= percentage total percent of marine debris that are plastic and foam compared to overall marine debris collected
PCT_PlasticAndFoam =  np.divide(TotalClassifiedItems_EC2020, TotalItems_EventRecord)



#Total number of hard plastic, beverage bottles as counted by clean up event volunteers
SUM_Hard_PlasticBeverageBottle = np.array(raw_data[raw_data.columns[36]])
#SUM_Hard_PlasticBeverageBottle



#SUM_Hard_OtherPlasticBottle
#I am putting other Jugs/Containers
SUM_Hard_OtherPlasticBottle = np.array(raw_data[raw_data.columns[37]])
#SUM_Hard_OtherPlasticBottle



#SUM_HardOrSoft_PlasticBottleCap
#Total number of hard or soft, plastic bottle caps as counted by clean up event volunteers
SUM_HardOrSoft_PlasticBottleCap = np.array(raw_data[raw_data.columns[38]])
#SUM_HardOrSoft_PlasticBottleCap                                    



#SUM_other_PlasticOrFoamFoodContainer
#Total number of plastic or foam, food containers as counted by clean up event volunteers
#This field doesn't exist in the RawStandingStockReport
SUM_other_PlasticOrFoamFoodContainer = np.array([])

for i in range(len(raw_data)):
    SUM_other_PlasticOrFoamFoodContainer = np.append(SUM_other_PlasticOrFoamFoodContainer, ' ') 



#SUM_Hard_BucketOrCrate
#Total number of hard plastic, bucket or crates as counted by clean up event volunteers
#This field doesn't exist in the RawStandingStockReport
SUM_Hard_BucketOrCrate = np.array([])
for i in range(len(raw_data)):
    SUM_Hard_BucketOrCrate = np.append(SUM_Hard_BucketOrCrate, ' ') 



#SUM_Hard_Lighter
#Total number of hard plastic, lighters as counted by clean up event volunteers
SUM_Hard_Lighter = np.array(raw_data[raw_data.columns[41]])



#SUM_OtherHardPlastic
#Total number of hard plastic, not represented in the other hard plastic fields as counted by clean up event volunteers
#otherhard plastics is represented by Hard Plastic Fragments index 32 and cigar tips index 39

SUM_OtherHardPlastic = np.array([])

for i in range(len(raw_data)):
    num1 = raw_data.iloc[i,32]
    num2 = raw_data.iloc[i,39]
    num_total = num1 + num2
    SUM_OtherHardPlastic = np.append(SUM_OtherHardPlastic, num_total) 



#SUM_PlasticOrFoamPlatesBowlsCup
#Total number of plastic, (plastic or foam) plates bowls or cups as counted by clean up event volunteers
#this is represented as cups and plastic Utensils index 47 and index 48

SUM_PlasticOrFoamPlatesBowlsCup = np.array([])

for i in range(len(raw_data)):
    num1 = raw_data.iloc[i,47]
    num2 = raw_data.iloc[i,48]
    num_total = num1 + num2
    SUM_PlasticOrFoamPlatesBowlsCup = np.append(SUM_PlasticOrFoamPlatesBowlsCup, num_total) 



#SUM_HardSoft_PersonalCareProduct
#Total number of hard plastics, that are lollypopsticks or earbuds as counted by clean up event volunteers
#personal care products is index 51

SUM_HardSoft_PersonalCareProduct = np.array(raw_data[raw_data.columns[51]])
#SUM_HardSoft_PersonalCareProduct



#SUM_Hard_LollipopStick_EarBud
#Total number of hard or soft plastics, that are lollypopsticks or earbuds as counted by clean up event volunteers
#This field doesn't exist in the RawStandingStockReport
SUM_Hard_LollipopStick_EarBud = np.array([])
for i in range(len(raw_data)):
    SUM_Hard_LollipopStick_EarBud = np.append(SUM_Hard_LollipopStick_EarBud, ' ') 



#SUM_Soft_Bag
#Total number of soft plastics, bags as counted by clean up event volunteers
#this is represented in index 43
SUM_Soft_Bag = np.array(raw_data[raw_data.columns[43]])



#SUM_Soft_WrapperOrLabel
#Total number of soft plastics, wrapper or label as counted by clean up event volunteers
SUM_Soft_WrapperOrLabel = np.array(raw_data[raw_data.columns[35]])



#SUM_Soft_Straw
#Total number of soft plastics, straws as counted by clean up event volunteers
SUM_Soft_Straw = np.array(raw_data[raw_data.columns[49]])



#SUM_Soft_OtherPlastic
#Total number of soft plastic, not represented in the other hard plastic fields as counted by clean up event volunteers
#other_soft plastic is represented by: filmed plastic fragments and ballons mylar

SUM_Soft_OtherPlastic = np.array([])

for i in range(len(raw_data)):
    num1 = raw_data.iloc[i,34]
    num2 = raw_data.iloc[i,50]
    num_total = num1 + num2
    SUM_Soft_OtherPlastic = np.append(SUM_Soft_OtherPlastic, num_total) 



#SUM_Soft_CigaretteButts
#Total number of soft plastic, cigarette butts as counted by clean up event volunteers
SUM_Soft_CigaretteButts = np.array(raw_data[raw_data.columns[40]])



#SUM_Other_StringRingRibbon
#Total number of other plastic, string, ring, or ribbon as counted by clean up event volunteers
#represented as 6-pack rings

SUM_Other_StringRingRibbon = np.array(raw_data[raw_data.columns[42]])



#SUM_Other_Net
#Total number of other plastic, nets as counted by clean up event volunteers
SUM_Other_Net = np.array(raw_data[raw_data.columns[44]])



#SUM_Other_FishingLineLureRope
#Total number of fishing line, lure, or rope as counted by clean up event volunteers
SUM_Other_FishingLineLureRope = np.array(raw_data[raw_data.columns[46]])



#SUM_other_BuoysAndFloats, METIS to upload this data as SUM_Fishing_Buoys and Floats
#Total number of other plastics, all foam items as counted by clean up event volunteers
SUM_other_BuoysAndFloats = np.array(raw_data[raw_data.columns[45]])



#SUM_Foam_OtherPlasticDebris (foam from everything else)
#Total number of other plastics, all foam items as counted by clean up event volunteers
SUM_Foam_OtherPlasticDebris = np.array(raw_data[raw_data.columns[33]])



#SUM_Other_OtherPlasticDebris (all other)
#Total number of other plastics, that are not represented in any other plastics category as counted by clean up event volunteers
SUM_Other_OtherPlasticDebris = np.array(raw_data[raw_data.columns[52]])


data = {'X':raw_data[raw_data.columns[12]], 'Y': raw_data[raw_data.columns[11]],'UniqueID': raw_data[raw_data.columns[9]],
       'SourceID':raw_data[raw_data.columns[8]],'Dataset': Dataset,'Organization': raw_data[raw_data.columns[1]],
       'Longitude1':raw_data[raw_data.columns[12]],'Latitude1': raw_data[raw_data.columns[11]], 'Longitude2': raw_data[raw_data.columns[13]],
       'Latitude2': raw_data[raw_data.columns[14]],'TotalWidth_m': raw_data[raw_data.columns[16]], 'TotalLength_m': raw_data[raw_data.columns[17]],
       'ShorelineName': raw_data[raw_data.columns[10]],'TotalVolunteers': raw_data[raw_data.columns[25]], 'DateOriginal': raw_data[raw_data.columns[2]],
       'DateStandardized': DateStandardized,'StartTime':raw_data[raw_data.columns[19]], 'TotalItems_EventRecord': TotalItems_EventRecord ,
       'TotalClassifiedItems_EC2020': TotalClassifiedItems_EC2020, 'PCT_PlasticAndFoam': PCT_PlasticAndFoam, 'PCT_Glass_Rubber_Lumber_Metal_Total': PCT_Glass_Rubber_Lumber_Metal_Total,
       'SUM_Hard_PlasticBeverageBottle': SUM_Hard_PlasticBeverageBottle, 'SUM_Hard_OtherPlasticBottle': SUM_Hard_OtherPlasticBottle,
       'SUM_HardOrSoft_PlasticBottleCap':SUM_HardOrSoft_PlasticBottleCap,'SUM_other_PlasticOrFoamFoodContainer':SUM_other_PlasticOrFoamFoodContainer,'SUM_Hard_BucketOrCrate':SUM_Hard_BucketOrCrate,
       'SUM_Hard_Lighter':SUM_Hard_Lighter, 'SUM_OtherHardPlastic':SUM_OtherHardPlastic, 'SUM_PlasticOrFoamPlatesBowlsCup':SUM_PlasticOrFoamPlatesBowlsCup,'SUM_HardSoft_PersonalCareProduct':SUM_HardSoft_PersonalCareProduct,
        'SUM_Hard_LollipopStick_EarBud':SUM_Hard_LollipopStick_EarBud, 'SUM_Soft_Bag':SUM_Soft_Bag, 'SUM_Soft_WrapperOrLabel':SUM_Soft_WrapperOrLabel, 'SUM_Soft_Straw':SUM_Soft_Straw,
        'SUM_Soft_OtherPlastic':SUM_Soft_OtherPlastic,'SUM_Soft_CigaretteButts': SUM_Soft_CigaretteButts, 'SUM_Other_StringRingRibbon':SUM_Other_StringRingRibbon,'SUM_Other_Net':SUM_Other_Net,
        'SUM_Other_FishingLineLureRope':SUM_Other_FishingLineLureRope,'SUM_other_BuoysAndFloats':SUM_other_BuoysAndFloats,'SUM_Foam_OtherPlasticDebris':SUM_Foam_OtherPlasticDebris,
        'SUM_Other_OtherPlasticDebris':SUM_Other_OtherPlasticDebris}


OCPDF = pd.DataFrame(data)
OCPDF.to_csv("data/processed/mdmap__ec2020-format.csv", index=False)
