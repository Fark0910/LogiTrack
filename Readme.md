<img src="./Screenshot 2024-12-07 020007.png" alt="Project Banner-1" width="100%" height="60%" />
<br>
<img src="./Screenshot 2024-12-07 020154.png" alt="Project Banner-1" width="100%" height="60%" />
<br>
<img src="./Screenshot 2024-12-07 020447.png" alt="Project Banner-1" width="100%" height="60%" />
<br>
<img src="./Screenshot 2024-12-07 020534.png" alt="Project Banner-1" width="100%" height="60%" />

<br>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
</head>
<body>

<h1>Python Project for Beginners</h1>

<h2>Requirements</h2>

<p><strong>Python Version:</strong> 3.10 (updated from 3.8)</p>

<h3>Libraries List</h3>
<ul>
    <li>Tkinter (tk and ttk)</li>
    <li>mySQL.connector</li>
    <li>os (path)</li>
    <li>PIL (image)</li>
    <li>reportlab (pdf)</li>
    <li>CSV</li>
    <li>pandas (optional)</li>
</ul>

<h3>Project Structure</h3>
<p>All the files in the repository must be present inside a single directory on your machine:</p>
<ul>
    <li>images</li>
    <li>Two CSV files (regdatabase, truckdatabase)</li>
    <li>Sample memo PDF (generated from the program)</li>
    <li>Python (.py) files</li>
</ul>

<h3>Paths Configuration</h3>
<p>Paths are used at many places, so it is necessary to navigate to your project directory:</p>
<ol>
    <li>Open this entire directory in VS Code and ensure the terminal is pointing inside the directory (use 'cd' if necessary).</li>
    <li>This step ensures you avoid errors due to incorrect paths, and you won't need to update image paths individually.</li>
</ol>

<h3>MySQL Setup</h3>
<p>You should have MySQL installed on your system as well as the MySQL connector library in Python:</p>
<ol>
    <li>Add your password and database name inside the program and ensure that the table and database names match those you will create in MySQL beforehand:
    <pre>
b1=mc.connect(host="localhost", user="root", passwd="enter_here", database="Truckinfo", auth_plugin='mysql_native_password')
c=b1.cursor()
    </pre>
    </li>
    <li>Create the following in MySQL beforehand:
        <ul>
            <li>Database: <code>Truckinfo</code></li>
            <li>Tables:
                <ul>
                    <li><code>Truckinfo</code></li>
                    <li><code>registeruser</code></li>
                </ul>
            </li>
        </ul>
    </li>
</ol>

<h2>Final Note</h2>
<p>This project is designed for Python beginners and students in classes 11-12 who are exploring Python as part of their curriculum. Using Tkinter, Python’s built-in GUI library, this project provides a practical example to understand basic Python concepts and build simple applications. It aims to help students strengthen their coding skills and prepare effectively for their exams by applying what they’ve learned in an interactive and fun way.</p>

</body>
</html>


      
   
           
   


