# admission-checker
This is an application which scrapes admission counselling websites - using BeautifulSoup in python - as per his/her choices . It enables the user to get instant update regarding counselling quickly than social media . 

# front.py
This file contains all the gui stuff . It's a basic gui with a dropdown list and a 'OK' button . User can select any counselling board of his/her choice from drop down list and can add his choices to sql database 'coll_sql.db' . This database is futher used to scrape the user prefered sites one by one . 
There is also json file "coll_data.json" which contains the content of the website .

# back.py
It has logics of the application . Meaning of the functions are as follows :
•	check_json() : it retrieves data from json file and returns it.
•	write_json() : writes new content to the json file .
•	check_sql(): it retrieves user preferred choices from the database file which also has urls of the counselling board websites .
•	write_sql(): it writes data to database whenever user selects a counselling board .
•	matching(): it finds whether there is new update on website or not through use of the json file . If new update is found it gives us notification related to it and appends the update to the json file . 

# bat_file.py
Here we scrape the website . It takes out the data from database , scrape each website one by one and finds whether there is any new content or not thorugh use of matching() in back.py . If new content is found it gives us notification and adds new content back to the json file . 

It has a same_sites() , diff_sites() functions . The websites which has same structure calls same_sites() to scrap and those who has different structure calls the diff_sites() . // currently only JOSSA and JAC-Delhi have the same structue only and IP University has different structure  .

I am a beginner to this software development field that's why you have found that my code structure is ill. Any recommendations to my code structure is highly appreciated .
