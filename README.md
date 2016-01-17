![]()

# Lucy

A CLI tool to generate `license` file for your project.

> **Features**

> - Written in simple Python
> - Easy to [install](https://github.com/pattu777/Lucy#installation)
> - [Easy to use](https://github.com/pattu777/Lucy#usage)
> - Uses Github API to search and create your [`license`](https://github.com/karan/joe#list-all-available-files) file.

## Python libraries used

- [Click](http://click.pocoo.org/5/) 				                                 # For parsing command line arguements.
- [requests](http://docs.python-requests.org/en/latest/user/quickstart/)		 # For making Github API calls.

## Installation

### Option 1: via [Pip](https://pypi.python.org/pypi/Lucy)

```bash
$ pip install lucy
```

### Option 2: From source

```bash
$ git clone --recursive git@github.com:pattu777/lucy.git
$ cd Lucy/
$ python setup.py install
```

## Usage

### Generate a new license.


```bash
$ lucy create <License Name> --name=<Author Name>             
```

### 

```bash
$ lucy create mit --name=Chinmaya                     # Creates a MIT license for your project.
```

### List all available licenses

```bash
$ lucy list
```

Output:

> 
[
  'gpl-3.0', 'lgpl-2.1', 'mit', 'isc', 'bsd-3-clause', 'mpl-2.0', 'lgpl-3.0', 'agpl-3.0', 'gpl-2.0', 'epl-1.0', 'apache-2.0', 'artistic-2.0', 'cc0-1.0', 'bsd-2-clause', 'unlicense'
]

## Contributing

#### Bug Reports & Feature Requests

Report any bugs through the [issue tracker](https://github.com/pattu777/Lucy/issues).

#### Developing

Create a new branch and send a pull request. To begin developing, do this:

```bash
# Create a virtual environment
$ git clone --recursive git@github.com:pattu777/Lucy.git
$ cd Lucy
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ git checkout -b <feature-branch-name>
$ python lucy/lucy.py mit
```