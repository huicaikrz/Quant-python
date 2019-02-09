# Project Title

Puget Financial Technical Challenge

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

Software required:
* [chromedriver] (https://seleniumhq.github.io/selenium/docs/api/java/org/openqa/selenium/chrome/ChromeDriver.html)
Note to put chromedriver at the same directory as the webcrawlerSetting.py file.

Python Packages Reuqired:
* selenium
* requests
* re
* json
* pickle
* tqdm
* multiprocessing
* pandas


```
pip install selenium
```
### Structure of the Folders, Files and Description
```
PugetFinancialTecChallange
│   README.md
│   chromedriver.exe
│   webcrawlerSetting.py
│   pugetWellData.py
│   pugetProductionData.py
│       
│
└───settings
│   │   post_data.txt
│   │   webSettings.txt
│   │
│   └───subfolder1
│       │   wellData.json
│       │   wellDataRequired.json
│      
│   
└───wellData
│   │   wellData.json
│   │   wellDataRequired.json
│
│
└───wellProductionData
│
│
│

```
### Description of .py Files
webcrawlerSetting.py: The first file that should be ran. It will open the chrome and get the required settings, store those settings into the "settings" folder.

pugetWellData.py: Used to get the well data from the website. Save the json file into the wellData folders. It will generate two json files, the first is called "wellData.json", and the second is called "wellDataRequired.json". wellData.json is a little bit redundanct, and wellDataRequired.json is the final structured well data. It will take a while to run this file, not too long. 

pugetProductionData.py: Used to get the production data of each well. It will provide several json files in "wellProductionData" folder. This .py file will require a long time to run. 

### Structure of the Data
wellData.json: \{'WellData':[]\}
list the keys and values


### Challenges and Solutions
```
Challenge 1. Using selenium.webdriver to get data is too slow.

Solution: Instead, I decided to use requests to get the content of the website
```
```
Challenge 2. When I wanted to use requests.post to get the well data, cookies and token were required.

Solution: I directly use selenium.webdriver to simulate the operation of Chrome, like clicking and I managed to get the cookies, token and some other basic information that could help in my future development.
```
```
Challenge 3. There are more than 240000 wells, which means that there are more than 240000 tables of production data (although most of them are empty). On the one hand, it will take a lot of time to get them, on the other hand, my computer's RAM is not big enough to store all of them and save them to my discs.

Solution: Using multiprocessing to increase the speed. And divided dataset into several parts, get them, store them and then delete them from RAM.
```

Actually, there are many other minor challenges. For example, I could not run a .py file with multiprocessing in IPython console. And I managed to overcome most of them. I am happy with that!

### Future Development
1. I could write them as objects but not functions. So that others could input some parameters and use it to get data without the necessary to read the .py files.

2. I think maybe there are some other methods to get cookies and token without using selenium.webdriver.





### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

