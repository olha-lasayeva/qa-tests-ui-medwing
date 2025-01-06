# qa-tests

> Automated tests for Medical Employment Management
>
> - Web application
> - Registration flow (heyflow)
> - Recruiting App
> - Job Portal
> - Logged-In Area

##### TODO: Kanban board - JIRA

## Installation

_Note: The installation instructions are for macOS._

### GitHub package authentication

1. Create a Personal Access Token(PAS) at your GitHub profile > settings > developer settings > personal access tokens with 'read, write, repo' scopes
2. Authenticate to GitHub Package Registry(GPR) and install the package.

```
npm login -registry=https://npm.pkg.github.com
# you will be prompted to enter your credentials
username: #enter github username
password: #enter the PAS you created at step 1
email: #enter github email
```

### Requirements

#### Local Development

1. [Python](https://www.python.org/downloads/)

2. [Git](https://git-scm.com/downloads)

3. [Brew](https://brew.sh/)

4. Install dependencies:

```
$ pip install -r requirements.txt
```

Then you can run all tests by running:

```
$ pytest -s -v
```

Or a specific one like:

```
$ pytest -s -v tests_ui/test_login.py
```

##### Testing on a different browser

At the moment we support:

- Chromium (Default)
##### TODO:
- Firefox

To override the default option when running tests, pass the `--browser_name` argument, for example:

```
$ pytest -s -v --browser_name firefox
```

### Getting started

I. Create a new project in PyCharm

II. Add Python Interpreter:

_PyCharm > Preferences > Project > Python Interpreter_ (/PycharmProject/ProjectName/venv/bin/python)

After that ‘playwright’ should be in the list of packages.

III. Clone the repository to your local machine and install required dependencies

```
git clone git@github.com:medwing/qa-tests-ui-medwing.git
cd qa-tests-ui-medwing
```

##### TODO:
IV. [TBD] Download the environment variable files and place them at the root of your projects

1. Staging .env file
2. Production .env file

##### TODO:
### Run on Docker

1. Build the image: `docker build . -t qa-test:latest`
2. Run the container: `docker run -it --name qa_tests qa-test:latest /bin/sh`
3. Run all the tests: `./drun all`
4. Stop and remove the container: `docker stop qa_tests && docker rm qa_tests`


### Environments

There are 2 environments:

1. Testing:
   - https://mdwng.dev/DE/de/
   - https://my.mdwng.dev/
   - https://recruiting.mdwng.dev/
   - https://mdwng.dev/jobs/
2. Production:
   - https://medwing.com/DE/de/
   - https://my.medwing.com/
   - https://recruiting.medwing.com/
   - https://medwing.com/jobs/

### Locales

- /DE/de/ (/DE/en/)

### Considerations

_When playing around with the app, if you're going to use an email to sign up be sure to add +test before the domain so that our agents won't get notified (and waste time trying to contact us). For example, something like my.normal.address+test@medwing.com. If it says something about email already in use, you can add a number in front of the +test like my.normal.address+123test@medwing.com.
Besides, add Test as a Name in the registration form when creating an account._

### Making a PR

- Always make a new branch

- When making a PR, make sure to briefly describe what the PR solves and if possible, add an image of the work

- Make sure to rebase the feature branch off the base branch if the base branch has new commits

- Commit message should start with what this commit does (and ticket number if possible)

- If the task is still in progress, make sure to add a **WIP:** flag in the commit message

  `WIP: add navbar for the page`

- Once the PR passes all the tests and is approved by one of the team members, add a `MERGE` label to the PR and Github will automatically select the best possible way to merge the PR in the base branch
