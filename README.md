# Treety Assignment

## Instructions

### Environment setup instructions

1. Set up a virtual environment with python 3.6
```bash
pip install virtualenv
virtualenv <env_name>
source <env_name>/scripts/activate
 ```
2. Clone this repository on your local system using this
```bash
git clone https://github.com/adittyashrivastava/treetyassignment.git
 ```

 3. Open terminal and enter working directory

 4. Install requirements using pip or pip3. Using pip -
```bash
pip install -Ur requirements.txt
```

Using pip3 -
```bash
pip3 install -Ur requirements.txt
```
5. Since we are using Django's inbuilt SQLite as backend for this project, we need not configure a database by ourselves. We can directly migrate the schema using the following command -

```bash
python manage.py migrate
```
6. After this, we migrate raw data from sp500_companies.csv (located at BASE_DIR/companies/scripts) to our database using the following series of commands -

```bash
python manage.py shell

>> from companies.scripts.add_raw_data import inject_data
>> inject_data()
```

7. After this our backend is ready to serve APIs for the frontend client. Start the django server using the following command -

```bash
python manage.py runserver
```

8. Open the git repositpory of frontend colient and proceed by following instructions from there.