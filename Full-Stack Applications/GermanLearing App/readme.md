# German learning App
This app is desinged for german students to adquiere new vocabulary. 

## Getting Started

Follow these steps to set up and run the app on your computer.

### Prerequisites

- Python 3.x **Note: Download the 64-bits version**
- Visual Studio Code
- MySQL
- flask
   
### Installation

1. Download the app files and open the files on VisualStudio.
 **Note: make sure to be in the correct folder. If you are not in the correct folder, the next step is not going to work**
2. Open the **config.py** file and change the following with your actual information form your local computer and your MySQL information. "SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database_name'"
3. Open a new terminal on Visual Studio and write "pip install -r requirements.txt" then press enter.If there is an "Error", don't worry, it should be fine (if you find problems check the note at the end of the document) 
4. Start the database. Open a new terminal and type "python". Once you are in the python interpreter type and press enter after each command.
- "from app import app, db"
- "db.create_all()"
- "exit()"
5. To upload the data to the database open the terminal and write the following in the python interpreter (make sure to type "python" to access to it.)
  - "from app import app, db, push"
  - from data import nouns_data, adjectives_data, verbs_data
  - push( nouns_data, adjectives_data, verbs_data)
  - "exit()"
6. Open a new terminal and type "flask run". The latter is to set up the flask enviorment. If there is an error after pressing enter for the first time, try again.
**note: just make sure you have a pycache folder:)**
7. Get into the link and enjoy!




