### How this usermanagement is developed
    1. Using Django restAPI i extended the user model which can be adapted for anyusecase
    2. POST,PUT,DELETE methods were allowed if user have admin permission

### How to run this
1. Clone the [repository|https://github.com/RakeshNagarajan/lowes-user-management]
2. install below package
``` pip install djangorestframework```
3. Create a super user for managing 
``` cd lowes-user-management/lowes_usermanagement_project```
``` python manage.py createsuperuser```
4. configure admin username and password
5. start the restapi server
``` python manage.py runserver 0.0.0.0:8000```

### How to access the end points
http://127.0.0.1:8000/api/usermanagement/

### Expected result
### login screen
![login_screen](/lowes_usermanagement_project/2021-05-14_11h59_59.png "login")
### default landing endpoint
![post_screen](/lowes_usermanagement_project/2021-05-14_11h59_44.png "post")
### post call
![default_screen](/lowes_usermanagement_project/2021-05-14_12h00_33.png "default page")
### retrive user management data
![get_screen](/lowes_usermanagement_project/2021-05-14_11h58_35.png "get")




