# Project Title

Puget Financial Technical Challenge Bonus1

## Prerequisites
Python Packages Reuqired:
* shelve (optional)
* json
* tqdm
* pandas
* time

## Structure of the Folders, Files and Description
```
PugetFinancialTecChallange
│   README.md
│   pugetAggOperator.py
│   
└───wellData
│       wellData.json
│
└───wellProductionData
│       ProductionData1.json
│       ProductionData2.json
│       ...
|       ProductionData49.json
|
└───aggWellProduction
│       aggOperator.json (just part of the whole data, if running the code, the complete version will be in the file)   
│       apiOperaIndex.json
│
```

## Description of .py Files
pugetAggOperator.py:  
For this script, I provided two methods to aggregate well and production data according to operator. The first is still directly using dictionary in python, then dump them into local disc as .json file. However, because of the large amoumt of production data, my poor laptop which only has 8GB RAM cannot handle them. I also provided another method by using shelve. It is kind of a database, which could be used as dictionary, but it will not directly read all the content into memory. The main problem is that it is too slow.

## Structure of the Json Data
apiOperaIndex.json: {api1: operatorName, api2: operatorName,...}
aggOperator.json: {operator1: {api1: {api: ,wellName: ,..., productionData:\[...\]}, api2:{}}, operatpr2: ...}
I only run a part of data, for my aggOperator.json file, most of the operator will lack productionData because my computer's RAM is not big emough.

## Challenges and Solutions
```
Challenge 1. The data amount is too large.

Solution: I did not manage to solve this problem with my poor laptop. I tried to use shelve as an alternative to store data. There is a parameter called 'writeback' in shelve.open, if wtriteback = True, it will store the data I use into the memory and the speed will be increased. But still, this will cause the problem of too much data. So you know, it is kind of a tradeoff between the running time and memory. For details of shelve see [http://oricohen.com/dev/2011/04/25/python-import-shelve-when-dictionary-doesnt-have-enough-memory/] 
```

## Future Development
1. I could write them as objects but not functions. So that others could input some parameters and use it to get data without the necessary to read the .py files.
