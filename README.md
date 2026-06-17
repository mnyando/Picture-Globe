# Picture-Globe  
## Redesigned & Presented By
>[Martin Nyandigisi (mnyando)](https://github.com/mnyando)

*Note: This project is a visual and functional redesign fork of the original repository by [Owiti-Charles](https://github.com/Owiti-Charles). I have updated it to present the project differently with custom dark glassmorphic styling, side-by-side modals, and a frontend image upload feature.*
  
# Description  
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.
  
##  Live Link  
 Click [View Site](https://picture-globe.onrender.com) to visit the site
  
## Screenshots 
###### Home page (Hero)
<img src="https://raw.githubusercontent.com/mnyando/Picture-Globe/master/static/images/landingpage.png" width="100%">
 
###### Home page (Gallery Grid)
<img src="https://raw.githubusercontent.com/mnyando/Picture-Globe/master/static/images/gallery.png" width="100%">

###### Expanded Image Details Modal
<img src="https://raw.githubusercontent.com/mnyando/Picture-Globe/master/static/images/modalscrn.png" width="100%">
 
## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/mnyando/Picture-Globe.git 
 ```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
```
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python 3.9](https://www.python.org/)  
* [Django 2.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any questions or contributions, please contact me at [matonyando@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/mnyando/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2019 **Owiti Charles** | Redesigned (c) 2026 **Martin Nyandigisi**