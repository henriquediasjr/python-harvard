# Django Project Setup and Run Guide


## Prerequisites
Python 3.6+ installed on your system.
Basic understanding of terminal commands.
Steps to Set Up and Run the Project


1. **Clone the Repository**
If this project is in a Git repository, clone it:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. **Create a Virtual Environment**
To isolate dependencies, create a virtual environment:

```bash
python3 -m venv myenv
```

3. **Activate the Virtual Environment**
Activate the virtual environment:

Linux/Mac:
```bash
source myenv/bin/activate
```


4. **Install Dependencies**
Install the required Python packages (including Django):

```bash
pip install django
```

5. **Navigate to the Project Directory**

- Change to the project directory containing manage.py:

```bash
cd lecture3
```

6. **Run the Development Server**

- Start the Django development server:

```bash
python manage.py runserver
```

7. **Access the Application**
- Open your browser and go to:
```bash
http://127.0.0.1:8000/
```

8. **Deactivate the Virtual Environment (When Done)**

- When you're finished, deactivate the virtual environment:

```bash
deactivate
```