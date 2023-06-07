#!/usr/bin/python3

import sys
import csv
from os import path
from decimal import Decimal
import copy


def parse_people(filename):
    parsed_data = []
    with open(filename, 'r', encoding="utf8") as data:
        
        for line in csv.DictReader(data):   
            line["email"] = line.pop('\ufeff[email]')
            line["addeddate"] = line.pop('[setdate]')
            line["firstname"] = line.pop('[fname]')
            line["lastname"] = line.pop("[lname]")
            line["middlename"] = ""
            line["nickname"] = ""
            line["maidenname"] = ""
            line["gender"] = ""
            line["status"] = ""
            line["maritalstatus"] = ""
            line["birthdate"] = ""
            line["familyid"] = ""
            line["familyrole"] = ""
            line["school"] = ""
            line["grade"] = ""            
            line["occupation"] = line.pop("[business]")
            line["phone"] = line.pop("[phone]")
            line["homephone"] = ""
            line["workphone"] = ""
            line["campus"] = ""            
            line["grade"] = ""
            line["numstreet"] = line.pop("[address1]")
            line["city"] = line.pop('[city]')
            line["state"] = line.pop('[state]')
            line["zip"] = line.pop('[zip]')
            print(line) 
            name = line["firstname"]
            if len(name) > 0:
                names = name.split(" ")
                if len(line["lastname"]) < 1:
                    if len(names) > 1:
                        line["lastname"] = names[-1]
                    elif len(line["lastname"]) < 1:
                        line["lastname"] = "unknown"
                if (len(names) > 1) and (names[-1] == line["lastname"]):
                    line["firstname"] = " ".join(names[:-1])
                parsed_data.append(line)
    return parsed_data

def save(people_data, csvfilename):
    _data = copy.deepcopy(people_data)
    fieldnames = ["firstname", "lastname",  "middlename", "nickname", "maidenname", "gender", 
                "status", "maritalstatus", "birthdate","familyid","familyrole", "school", "grade",
                "occupation", "phone","homephone","workphone","campus", "email", "numstreet", 
                "city", "state", "zip",]
    topline = "First Name (1063386553),Last Name (1063386553),Middle Name (1063386553),Nickname (1063386553),Maiden Name (1063386553),Gender (1768790167),Status (718533993),Marital Status (871822504),Birthdate (490422159),Family ID (1109850497),Family Role (1109850497),School (1202628958),Grade (1828896449),Employer (1014905818),Mobile (1530627561),Home (1530627561),Work (1530627561),Campus (1771676324),Email (2040842366),Street Address (1363781938),City (1363781938),State (1363781938),Zip (1363781938)"
    
    with open(csvfilename, 'w') as f:
        f.write(topline+'\n')

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        for line in _data:
            for field in list(line.keys()):
                    if field not in fieldnames:
                        del line[field]
            
            writer.writerow(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 makeletters.py  icontact_people.csv")
    else:
        people_data = parse_people(sys.argv[1])
        dir = path.dirname(sys.argv[1])
        file = path.basename(sys.argv[1])
        outfile = '.'.join(file.split(".")[:-1])+"_ready_for_breeze.csv"         
        save(people_data, outfile)
