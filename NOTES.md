
What is Serverless?
-------------------

Basically packing up everthing a request needs (code, url routes, libraries) into on ZIP file and push it to the serverless infrastructur. When a request hits a URL provisioning a worker with the code and run it. 

Everyone has it: AWS Lambda, Azure Functions, Google Cloud Functions

Overview: https://www.martinfowler.com/articles/serverless.html

Cold Start vs Warm Start: https://mikhail.io/2018/08/serverless-cold-start-war/



What is Zeit/Now?
-----------------

Now from zeit.co builds on top of cloud providers (AWS etc) to make it easy to deploy serverless apps.
It includes CDN, Deployment, storing secrets (environment), DNS, SSL Certs, buying domains, CI, Github and Gitlab integration.



What does it cost?
------------------

The first 5 team members are free. If you have more than 5 users working on the team you pay 25 USD from the 6th person on per month.

You pay monthly a small amount (0.99 USD) to Zeit and extra for Bandwith ($0.1 / GB), Memory used ($0.000034 / GB-s) and Invocations/Requests to your functions ($0.0000004 / Inv.) and for logs by line ($0.00001 / Line) and for storage of source files ($0.046 / GB)

Zeit/Now has a pricing calculator: https://zeit.co/pricing/calculator

Serving one million requests per month is about 40 USD / month.



Getting started
---------------

Create an account online (asks you to install Github plugin) - very easy to setup. 

They have a CLI. Very easy to install (npm -g!) and when first called you need to setup account (give email, verify, done. No pwd)

'python-django' is a template from zeit. Has a new Django under Python 3.6 running. No database connection.

```
$ now init python-django
> Success! Initialized "python-django" example in ~/nowstagram/python-django.
- To develop, `cd python-django` and run `now dev`.
- To deploy, `cd python-django` and run `now`.
```

This creates a directory "python-django". I renamed the directory pushed it to Github. 
It appeared in my zeit.co dashboard and also was deployed under the URL: https://python-django.antonpirker.now.sh/
Impressiv.

I changed the name in now.json and pushed it again to Github. It was now deployed to https://nowstagram.antonpirker.now.sh/
Impressiv.



Requirments 
-----------

They use pipenv to manage requirements (https://docs.pipenv.org/en/latest/)

`pip install pipenv` 

`pipenv install djangorestframework` 



Development/Debugging
---------------------

`now dev` in your directory runs your app on http://localhost:3000

In general the developer experience is horrible.
If you change the code there is no autoreload. You have to kill `now dev` and start it again. (Always long load times because of provisioning)

There are no stack straces. Errors are really not good: 

```
...
> Built @now/python:app.py [33s]
<class 'ImportError'>
LambdaError: Unspecified runtime initialization error
    at Lambda.<anonymous> (/snapshot/repo/dist/index.js:1:2514740)
    at Generator.next (<anonymous>)
    at fulfilled (/snapshot/repo/dist/index.js:1:2512881)
    at process._tickCallback (internal/process/next_tick.js:68:7)
> GET /posts
```

Error messages on live deployment are better (normal python stack traces, can be seen in zeit.co dashboard.)

ipdb can not be used out of the box.

Current default bundle size is 15MB, but with django, restframework and ipdb you already have 19MB. (Maximum allowed is 50MB)
(Cold start times always longer)



Deployment
----------

Just push to Github. (Or just call `now` if not using Github integration) A new unique URL will be created where the new commits run.



Databases
---------

For Postgres you need a service that runs Postgres (like Scalegrid, or Firebase or AWS RDS or similar)
You need a special psychopg2 (because the AWS Lambda AMI is missing Postgres libs): https://github.com/jkehler/awslambda-psycopg2 

In your topmost urls.py you need to run the migrations (because `./manage.py migrate` does not work on serverless):

```
from django.core.management import call_command
call_command('migrate')
```
(maybe you need to refresh the home page a couple of times because requests timeout after 10 seconds)

Making migrations was also strange. I had to rename the aws psycopg2 and install the "normal" one. 
And I copied a manage.py from another Django 2.2 project to be able to run makemigrations. After they where created, i activated the AWS psycopg2 again and run in on the server to run the migrations. 
So maybe there is more work to be done to make this easier.



Support
-------

Community support is free (spectrum.chat ~10k members) I have posted a question, never got answer (2 days)
You can buy plans of support levels. (700-2000 USD / month)

Also you can buy security audit, stress testing, architecture review.



Conclusio
---------

Debugging is a nightmare. (Time saved setting up serverless is spent debugging?)

Maybe better run it locally in a Vagrant Box for better development and then deploy to Zeit now and then.

Maybe try something like Zappa if you want to use Django: https://www.zappa.io/?
Or ditch Django and write plain Python (or Go or Rust or Javascript) functions?

