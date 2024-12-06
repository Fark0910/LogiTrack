![Project Banner](./light color vector background for truck app window.png)
python version:3.10(updated from 3.8)
Requirements:
  (a.)Libraries list:
        1.)Tkinter(tk and ttk)
        2.)mySQL.connector
        3.)os(path)
        4.)PIL(image)  
        5.)reportlab(pdf)
        6.)CSV
        7.)pandas(optional)
  
  (b.)All the files in repo must be present inside single file in your machine
        1.)images
        2.)Two csv file(regdatabase,truckdatabase)
        3.)sample memo pdf(generated from the programme)
        4.)py files

  (c.)paths are used at many places hence its necessary that u should migrate inside your file(whch contains stuff listed in (b.))
        1.)just open this whole file in vs code and ensure the terminal is pointing inside  the file(if not use 'cd' to migrate)
        2.)above step ensure you want end up getting weird errors for wrong path(also you dont have to update imagespath individually)

  (d.)should have mysql on system as well as mysql connector library installed in python
        1.)Dont forget to add your password and database name inside programme (everytwhere)and ensure that name of table and database matches that u will create in Mysql before hand
         "b1=mc.connect(host="localhost",user="root",passwd="enter her ",database="Truckinfo",auth_plugin='mysql_native_password')
          c=b1.cursor()"

        2.)so before hand just create this In Myql
          creat database=Truckinfo
             1.)Table1-Truckinfo
             2.)Table2- registeruser

Final note:
This project is designed for Python beginners and students in classes 11-12 who are exploring Python as part of their curriculum. Using Tkinter, Python’s built-in GUI library, this project provides a practical example to understand basic Python concepts and build simple applications. It aims to help students strengthen their coding skills and prepare effectively for their exams by applying what they’ve learned in an interactive and fun way.


        -


      
   
           
   


