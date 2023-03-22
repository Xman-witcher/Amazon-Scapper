-To run this file 'scrapper.py', we need to install the necessary packages,
-to install, open command prompt or shell,
-run the following commands:
  pip install requests
  pip install bs4
  pip install csv   (if you get an error, ignore it)

-Now we can execute 'scrapper.py' in the cmd itself, or
 we can open it in an ide, then run it.

Important Notes:

1)  This will take some time depending on the system and internet. 
    (in my laptop, it took 2-3 minutes.) Because it fetches product information from
    20 pages, and in each page, there are so many products, and from each product, it 
    tries to get description, etc.

2) sometimes due to network issues, it would fail to fetch some information.
   So in those cases, python returns None, so I've replaced it with empty string ''.

3) once the scrapper.py finishes running, it will create a csv file in the same directory.
 