# The Configuration Management Task

Your task is to create a backend service that stores information about servers in our data center. At the top level, we want to collect the OS implementations and their respective versions, and then we want to collect some detail about the servers running each version. We want to be able to do CRUD operations via a REST API. We also need it to provide some additional information about the stored data, e.g., some summary information, maybe some other calculations.

### Couple of ground rules:

- Use common sense; if there is something that is not clear or not specified, feel free to make reasonable assumptions and decisions (i.e., naming, tech choices, etc).
- Feel free to use python libraries if it will make your life simpler.
- Use git for source version control (ideally push somewhere where you can give us access, for example github.com, but not mandatory, the code can also be exported with `git bundle create my_repo.bundle --all` and send us the resulting `my_repo.bundle` bundle).
- The tasks are split into 4 tiers, from easiest (tier 1) to hardest (tier 4). If you get stuck at any of the tiers, please write down what the exact problem is, and what are the things you tried to solve the problem. We would like to discuss your thought process even if you don't have a solution for a particular tier task.

## The Tasks

### Core (Tier 1)

- Create a web app for this purpose
  - As an example you can use Flask: [https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application](https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application)
- Add an API endpoint that returns the current time and date (of MIME type `application/json`, i.e. the response should be a json)
- Add an POST endpoint (again MIME type `application/json`) that accepts json array of strings as input and returns a summary, counting how many times each string appears in that array.
  Example input: ["Oracle Linux", "Debian", "Oracle Linux", "Debian", "Ubuntu"]
  Expected output: {"Oracle Linux": 2, "Debian": 2, "Ubuntu": 1}
- (**important!!!**) Add a README file (text or markdown) that provides all details about:
  - Running the project locally (for someone who might not be familiar with flask)
  - If anything else needs to be done to run the project, what are the exact steps? Lets assume that whoever is going to be running it has python installed.

### More functionality (Tier 2)

- Add an endpoint that takes list of operating systems and their versions and returns a summary of the highest and lowest version of each operating system.
  Example input:

```
[
  {"name": "Debian", "version": "11"},
  {"name": "Debian", "version": "10"},
  {"name": "Debian", "version": "9"},
  {"name": "Oracle Linux", "version": "9.2.3"},
  {"name": "Oracle Linux", "version": "10.2.3"},
  {"name": "Oracle Linux", "version": "11.2.3"},
]
```

Expected output:

```
{
    "Debian": {
        "highest": "21.2.3"
        "lowest": "1.2.3"
    },
    "Oracle Linux": {
        "highest": "11.2.3"
        "lowest": "9.2.3"
    }
}
```

- With this we can limit it to the numeric part of the [https://semver.org/](https://semver.org/) versioning, i.e. `<major>.<minor>.<patch>`.

### Testing (Tier 3)

- Write some automated tests for all the functionality ([https://flask.palletsprojects.com/en/2.2.x/testing/?highlight=tests](https://flask.palletsprojects.com/en/2.2.x/testing/?highlight=tests) can be an inspiration)
  - Decide for yourself what makes sense to test. The goal is to be quite sure the code works as expected and that it doesn't break in edge cases (i.e. data input is malformed, etc)

### Database (Tier 4)

- Create two tables in a relational database:
  - OS Version (which needs to track the following):
    - name of the OS (e.g. `Oracle Linux`, `Debian`, `Fedora`, `Ubuntu`, etc) - varchar
    - the OS version (e.g. `8.3`, or `2`, or `2.3.4`) - varchar
  - Compute instance (which needs to track the following):
    - OS Version (i.e. a foreign key to the table above) - foreign key
    - IP address - varchar
    - hostname (e.g. `somedb.company.org`) - varchar
    - date and time of when it was created - datetime
- Use a relational database (of your choice, feel free to do what makes the most sense or what is the easiest) to store the data of the models above. To manage the models consider using SQLAlchemy ([https://flask.palletsprojects.com/en/2.2.x/patterns/sqlalchemy/](https://flask.palletsprojects.com/en/2.2.x/patterns/sqlalchemy/) and [https://www.sqlalchemy.org/](https://www.sqlalchemy.org/))
- Create http REST endpoints for creating/reading/updating/deleting these two models. ([https://flask.palletsprojects.com/en/2.2.x/views/?highlight=rest#method-dispatching-and-apis](https://flask.palletsprojects.com/en/2.2.x/views/?highlight=rest#method-dispatching-and-apis) is an option, or any other way you can figure out.

### Modifications (Tier 5)

- Add endpoints that will work the same way as the previously added endpoints, but instead of taking the input from the request, take input from the previously created database.
- Otherwise the behaviour should be the same.

### Final tier (Tier 6)

This is free for all, feel free to add any or all of the below.

- Add whatever else you find interesting/want to try/want to learn. Feel free to add more logic, models, broswer views, endpoints, tests.
- Want to standardize code formatting? Add a code formatting tool.
- Maybe you want to try fetching some additional data in the backend code? Add that ([https://reqres.in/](https://reqres.in/) can be used as a publically available sample API).
- Think about what else needs to be done to make this production-ready.
- Want to showcase some datastructure/algorithm? Code away.
