from datetime import datetime
import os

import pandas as pd

PROJECT_DIR = os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)))


raw_data = pd.read_csv(os.path.join(PROJECT_DIR, "data", "raw", "mdt", "all_mdt.csv"))

MDT_PLASTIC_MAPPINGS = {
    ("CLOTH", "Buoys and floats") : "SUM_Other_BuoysAndFloats",
    ("CLOTH", "Fishing Gear") : "SUM_Other_FishingLineLureRope",
    ("CLOTH", "Fishing Net") : "SUM_Other_Net",
    ("CLOTH", "Fishing Traps") : "SUM_OtherFishing",
    ("CLOTH", "Fishing lures and lines") : "SUM_Other_FishingLineLureRope",
    ("CLOTH", "Lobster Claw Bands") : "SUM_OtherFishing",
    ("CLOTH", "Other Fishing Gear") : "SUM_OtherFishing",
    ("CLOTH", "Plastic Rope or Net") : "SUM_Other_Net",
    ("OTHER ITEMS", "Bait Containers") : "SUM_OtherHardPlastic",
    ("OTHER ITEMS", "Bulk Bags") : "SUM_Soft_Bag",
    ("OTHER ITEMS", "Condoms") : "SUM_HardSoft_PersonalCareProduc",
    ("OTHER ITEMS", "Feminine Hygeine Products") : "SUM_HardSoft_PersonalCareProduc",
    ("OTHER ITEMS", "Foam or Plastic Take Out Containers") : "SUM_Other_PlasticOrFoamFoodContainer",
    ("OTHER ITEMS", "Industrial or Chemical Plastic Packaging") : "SUM_Other_OtherPlasticDebris",
    ("OTHER ITEMS", "Other Plastic") : "SUM_Other_OtherPlasticDebris",
    ("OTHER ITEMS", "Other Plastic Packaging") : "SUM_Other_OtherPlasticDebris",
    ("OTHER ITEMS", "Plastic Film") : "SUM_Soft_WrapperOrLabel",
    ("OTHER ITEMS", "Plastic Food Containers") : "SUM_Other_PlasticOrFoamFoodContainer",
    ("OTHER ITEMS", "Plastic Piping") : "SUM_Other_OtherPlasticDebris",
    ("OTHER ITEMS", "Plastic Sheeting or Tarps") : "SUM_Soft_sheets",
    ("OTHER ITEMS", "Plastic Shipping Waste") : "SUM_Other_OtherPlasticDebris",
    ("OTHER ITEMS", "Plastic String") : "SUM_Other_StringRingRibbon",
    ("OTHER ITEMS", "Styrofoam Packaging") : "SUM_Foam_OtherPlasticDebris",
    ("OTHER ITEMS", "Syringes") : "SUM_Other_OtherPlasticDebris",
    ("PLASTIC", "Aquaculture Gear") : "SUM_Other_OtherPlasticDebris",
    ("PLASTIC", "Balloon and/or String") : "SUM_Other_StringRingRibbon",
    ("PLASTIC", "Cigarettes/Cigars") : "SUM_Soft_CigaretteButts",
    ("PLASTIC", "Fishing Line") : "SUM_Other_FishingLineLureRope",
    ("PLASTIC", "Foam Fragment") : "SUM_Foam_OtherPlasticDebris",
    ("PLASTIC", "Foam or Plastic Cups or Plates") : "SUM_PlasticOrFoamPlatesBowlsCup",
    ("PLASTIC", "Other Plastic Jugs") : "SUM_Hard_OtherPlasticBottle",
    ("PLASTIC", "Other Rubber Items") : "SUM_Other_OtherPlasticDebris",
    ("PLASTIC", "Personal Care Products") : "SUM_HardSoft_PersonalCareProduc",
    ("PLASTIC", "Plastic Bags") : "SUM_Soft_Bag",
    ("PLASTIC", "Plastic Bottle") : "SUM_Hard_PlasticBeverageBottle",
    ("PLASTIC", "Plastic Caps or Lids") : "SUM_HardOrSoft_PlasticBottleCap",
    ("PLASTIC", "Plastic Fiber") : "SUM_Other_OtherPlasticDebris",
    ("PLASTIC", "Plastic Food Wrappers") : "SUM_Soft_WrapperOrLabel",
    ("PLASTIC", "Plastic Pellet") : "SUM_Other_OtherPlasticDebris",
    ("PLASTIC", "Plastic Utensils") : "SUM_PlasticOrFoamPlatesBowlsCup",
    ("PLASTIC", "Plastic or Foam Fragments") : "SUM_Other_OtherPlasticDebris",
    ("PLASTIC", "Rubber Bands") : "SUM_Other_StrapsTiesBands",
    ("PLASTIC", "Rubber Fragments") : "SUM_Other_OtherPlasticDebris",
    ("PLASTIC", "Rubber Gloves") : "SUM_Other_OtherPlasticDebris",
    ("PLASTIC", "Six-pack rings") : "SUM_Soft_WrapperOrLabel",
    ("PLASTIC", "Strapping Bands") : "SUM_Other_StrapsTiesBands",
    ("PLASTIC", "Straws") : "SUM_Soft_Straw",
    ("PLASTIC", "Tobacco Packaging or Lighters") : "SUM_Hard_Lighter",
    ("PLASTIC", "Toys") : "SUM_Other_OtherPlasticDebris",
    ("RUBBER", "Flip-flops") : "SUM_Other_OtherPlasticDebris",
    ("RUBBER", "Tires") : "SUM_Other_OtherPlasticDebris"
}

transformed_data = []


test_raw = raw_data.head(10)

for item in raw_data.itertuples():
    try: # if row contains plastic, get type
        plastics_col = MDT_PLASTIC_MAPPINGS[(item.material, item.itemname)]
    except KeyError: # otherwise skip this row
        continue
    new_row = {
        "X": item.longitude,
        "Y": item.latitude,
        "Dataset": "Marine Debris Tracker",
        "Organization": item.list_name,
        "SUM_Hard_PlasticBeverageBottle": 0,
        "SUM_Hard_OtherPlasticBottle": 0,
        "SUM_HardOrSoft_PlasticBottleCap": 0,
        "SUM_Other_PlasticOrFoamFoodContainer": 0,
        "SUM_Hard_BucketOrCrate": 0,
        "SUM_Hard_Lighter": 0,
        "SUM_OtherHardPlastic": 0,
        "SUM_PlasticOrFoamPlatesBowlsCup": 0,
        "SUM_HardSoft_PersonalCareProduc": 0,
        "SUM_Hard_LollipopStick_EarBu": 0,
        "SUM_Soft_Bag": 0,
        "SUM_Soft_WrapperOrLabel": 0,
        "SUM_Soft_Straw": 0,
        "SUM_Soft_OtherPlastic": 0,
        "SUM_Soft_CigaretteButts": 0,
        "SUM_Other_StringRingRibbon": 0,
        "SUM_Other_Net": 0,
        "SUM_Other_FishingLineLureRope": 0,
        "SUM_Other_BuoysAndFloats": 0,
        "SUM_Foam_OtherPlasticDebris": 0,
        "SUM_Other_OtherPlasticDebris": 0,
        "SUM_Soft_sheets": 0,
        "SUM_Other_StrapsTiesBands": 0,
        "SUM_Other_Glowsticks": 0,
        "SUM_OtherFishing": 0
    }

    # create date & time columns using Python's datetime module:
    dt = datetime.strptime(item.timestamp, "%Y-%m-%d %H:%M:%S")
    new_row["DateOriginal"] = dt.strftime("%m/%d/%Y, %H:%M %p")
    new_row["DateOriginal"] = dt.strftime("%m/%d/%Y, %H:%M %p")
    new_row["MonthYear"] = dt.strftime("%b-%Y")
    new_row["Year"]= dt.strftime("%Y")
    new_row["MonthNum"]= dt.strftime("%m").lstrip("0")
    new_row["Month"]= dt.strftime("%b")
    new_row["Day"]= dt.strftime("%d").lstrip("0")
    new_row["DOW"]= dt.strftime("%A")

    # Add type of plastic
    new_row[plastics_col] = item.quantity
    new_row["TotalClassifiedItems_EC2020"] = item.quantity

    transformed_data.append(new_row)


final_data = pd.DataFrame.from_records(transformed_data)
final_data.to_csv(
    os.path.join(PROJECT_DIR, "data", "processed" , "marine-debris-tracker__ec2020-format.csv"), 
    index=False
    )
