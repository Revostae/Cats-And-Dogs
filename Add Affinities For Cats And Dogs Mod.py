#Add Affinities For Cats And Dogs Mod
#Created by Revostae#8756
#Requires Python 3.6 or newer.
#Last updated/tested on January 19, 2022
#Please be sure to change the drive letter and folder paths to be correct for your BTA 3062 install! I have added all caps comments where you need to change!

import os
import json
import shutil
from pathlib import Path

#Changes drive to whatever drive you have BTA installed on. Change it to be correct for you!
###       CHANGE THIS!!!      ###
os.chdir(r'D:/') 

#Tells the script where your BT folder installation is located. This is only used for editing the settings.json for the base game to enable the Debug Console.
###       CHANGE THIS!!!      ###
game_folder = Path("Games/Steam/steamapps/common/BATTLETECH")

#Tells the script where your Mods folder is located inside your BATTLETECH/BTA installation. Change it to be correct for you!
###       CHANGE THIS!!!      ###
mods_folder = Path("Games/Steam/steamapps/common/BATTLETECH/Mods")

########################################################################
#                    Mech Affinity - Mad Cat 0.5                       #
########################################################################  

#Specifies location of MechAffinity's settings.json based on the Mods folder above. DO NOT CHANGE!
MechAffinity_location = mods_folder / "MechAffinity" / "settings.json"

#Specifies the string we want to put into the MechAffinity settings for the Mad Cat 0.5's affinity.
MadCatZeroPointFiveAffinity_string = '''
{
    "chassisNames" : ["Timberwolf_35"],
    "affinityLevels" : 
    [
        {
            "missionsRequired" : 15,
            "levelName" : "Tiny Timberwolf",
            "decription" : "Gains 2 bonus evasion on movement",
            "effectData" : 
            [
                {
                    "Description": {
                        "Details": "The pilot's incredible skill with this mech and the Mad Cat 0.5's incredible tinyness improves its evasive pips on movement by 2.",
                        "Icon": "UixSvgIcon_specialEquip_System",
                        "Id": "StatusEffect-Affinity-MoraleBoost",
                        "Name": "Mech Affinity Evasive Pips Boost"
                    },
                    "durationData": {
                        "duration": -1,
                        "stackLimit": -1
                    },
                    "effectType": "StatisticEffect",
                    "nature": "Buff",
                    "statisticData": {
                        "additionalRules": "NotSet",
                        "modType": "System.Int32",
                        "modValue": "2",
                        "operation": "Int_Add",
                        "statName": "EvasivePipsGainedAdditional",
                        "targetAmmoCategory": "NotSet",
                        "targetCollection": "NotSet",
                        "targetWeaponCategory": "NotSet",
                        "targetWeaponSubType": "NotSet",
                        "targetWeaponType": "NotSet"
                    },
                    "targetingData": {
                        "effectTargetType": "Creator",
                        "effectTriggerType": "Passive",
                        "hideApplicationFloatie": true,
                        "showInStatusPanel": false,
                        "showInTargetPreview": false
                    }
                }
            ]
        }
    ]
}
'''

#Converts MadCatZeroPointFiveAffinity_string into Python dictionary for easier use.
MadCatZeroPointFiveAffinity_data = json.loads(MadCatZeroPointFiveAffinity_string)

#Reads the contents of MechAffinity's settings.json and then appends the MadCatZeroPointFive affinity.
with open(MechAffinity_location) as MechAffinity:
    MechAffinity_data = json.load(MechAffinity)
    
    ToDeleteTimberWolf = []
    
    i = 0
    
    while i < len (MechAffinity_data['chassisAffinities']):
        #print(i)
        
        chassisaffinity = MechAffinity_data['chassisAffinities'][i]
        
        for chassis in chassisaffinity['chassisNames']:
            #print(chassis)
            if chassis == "Timberwolf_35":
                ToDeleteTimberWolf.append(i)
            else:
                continue
                
        i+=1
    
    for i in ToDeleteTimberWolf:
        #print (str(ToDeleteTimberWolf))
        del MechAffinity_data['chassisAffinities'][i]
  
    MechAffinity_data["chassisAffinities"].append(MadCatZeroPointFiveAffinity_data)
    
with open(MechAffinity_location, "w") as MechAffinity:
    json.dump(MechAffinity_data, MechAffinity, indent='\t', ensure_ascii=False)
    print('Successfully wrote MechAffinity data for Mad Cat 0.5!')

########################################################################
#                   Mech Affinity - Mad Cat III                        #
########################################################################  

#Reads the contents of MechAffinity's settings.json and then adds MadCatIV_75 to the Unlimited Power affinity.
with open(MechAffinity_location) as MechAffinity:
    MechAffinity_data = json.load(MechAffinity)
    
    i = 0
    
    while i < len (MechAffinity_data['chassisAffinities']):
        #print(i)
        
        chassisaffinity = MechAffinity_data['chassisAffinities'][i]

        if chassisaffinity['affinityLevels'][0]['levelName'] == "Encouraging":

            MadCatIVFound = False

            for chassis in chassisaffinity['chassisNames']:
                #print(chassis)
                if chassis == "MadCatIII_55":
                    MadCatIVFound = True
                    #print('MadCatIII_55 was Found!')
                else:
                    continue
            
            if MadCatIVFound == False:
                MechAffinity_data['chassisAffinities'][i]['chassisNames'].append("MadCatIII_55")
                #print('MadCatIII_55 was not found but was appended!')
        i+=1

#Write the JSON.    
with open(MechAffinity_location, "w") as MechAffinity:
    json.dump(MechAffinity_data, MechAffinity, indent='\t', ensure_ascii=False)
    print('Successfully wrote MechAffinity data for Mad Cat Mk III!')

########################################################################
#                  Mech Affinity - Mad Cat Mk IV                       #
########################################################################  

#Reads the contents of MechAffinity's settings.json and then adds MadCatIV_75 to the Unlimited Power affinity.
with open(MechAffinity_location) as MechAffinity:
    MechAffinity_data = json.load(MechAffinity)
    
    i = 0
    
    while i < len (MechAffinity_data['chassisAffinities']):
        #print(i)
        
        chassisaffinity = MechAffinity_data['chassisAffinities'][i]

        if chassisaffinity['affinityLevels'][0]['levelName'] == "Unlimited Power":

            MadCatIVFound = False

            for chassis in chassisaffinity['chassisNames']:
                #print(chassis)
                if chassis == "MadCatIV_75":
                    MadCatIVFound = True
                    #print('MadCatIV_75 was Found!')
                else:
                    continue
            
            if MadCatIVFound == False:
                MechAffinity_data['chassisAffinities'][i]['chassisNames'].append("MadCatIV_75")
                #print('MadCatIV_75 was not found but was appended!')
        i+=1

#Write the JSON.
with open(MechAffinity_location, "w") as MechAffinity:
    json.dump(MechAffinity_data, MechAffinity, indent='\t', ensure_ascii=False)
    print('Successfully wrote MechAffinity data for Mad Cat Mk IV!')