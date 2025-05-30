'''
The data in this dataset was not available as a csv, but only as a .data file with a python file to read it. Both of those
files (school_scores.data and school_scores.py) are included in the /data folder.

This also meant that I had to process the data slightly differently. The format_data.py puts all of the data into a file
called data_original.json, and it also makes a data.json file which has only the relevant data in it (SAT scores for
students with yearly family income >100k and <20k)
'''



import school_scores as school_scores
import json

record=school_scores.get_record()



f2 = open("data/data_original.json", "w")
json.dump(record, f2, indent = 4)

f2.close()


'''
f = open("data/school_scores.json", "r")
data = json.load(f)
f.close()




'''


new_dict={}



#state_code:year:<20 score, >100 scores

state_abbreviations = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
    "DC"
]

for state in state_abbreviations:
    new_dict[state]={}


#handle WV missing data
new_dict["WV"]={'2005':[0, 0], '2006': [0, 0]}

for i in record:
    year=str(i["Year"])
    state=i["State"]["Code"]
    if state in state_abbreviations:#get rid of PR and VI with incomplete data
        low_income_score=i["Family Income"]["Less than 20k"]["Math"]+i["Family Income"]["Less than 20k"]["Verbal"]
        high_income_score=i["Family Income"]["More than 100k"]["Math"]+i["Family Income"]["More than 100k"]["Verbal"]

        if low_income_score<600:#eliminate missing data
            new_dict[state][year]=[0, 0]
        else:
            new_dict[state][year]=[low_income_score, high_income_score]



f2 = open("data/data.json", "w")
json.dump(new_dict, f2, indent = 4)

f2.close()
    