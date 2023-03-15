# Brief description
**bot-parser of site castorama.ru**
___
## Full description
1. Project is realized on the scrapy framework
2. Bot-parser search data of products and write it into database MongoDb
3. Data saves in database on localhost in adress: `mongodb://localhost:27017`
4. Photos of product saves in directory "files"
___
## Launch project
write this code with parametrs: `python runner.py` *first param  second param*

- first param its section of site
- second param its category of product in choosen section

### default parametrs for demonstation are: *gardening-and-outdoor* and *pochtovye-jaschiki*


Castorama store parser.
The spider collects data about products from the "mailboxes" section.
All data is saved to the MongoDB database collection.
Photos are saved separately in the project directory.
The runner file.py launches the project
