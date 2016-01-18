![](https://knowledgeme.s3.amazonaws.com/uploads/collection/background_image/43/cover_step3.jpg)

# Lucy

A CLI tool to generate `license` file for your project.

![](http://i.imgur.com/ttyy7nk.gif?1)

> **Features**

> - Written in simple Python
> - Easy to [install](https://github.com/pattu777/Lucy#installation)
> - [Easy to use](https://github.com/pattu777/Lucy#usage)
> - Uses Github v3 API to create your [`license`](https://github.com/karan/joe#list-all-available-files) file.

## Python libraries used

- [Click](http://click.pocoo.org/5/) 				                                 
- [requests](http://docs.python-requests.org/en/latest/user/quickstart/)		

## Installation

### Option 1: via [Pip](https://pypi.python.org/pypi/Lucy)

```bash
$ pip install lucy
```

### Option 2: From source

```bash
$ git clone --recursive git@github.com:pattu777/Lucy.git
$ cd Lucy/
$ python setup.py install
```

## Usage

### List all available licenses

```bash
$ lucy list
```

Output:

```bash
mit
mpl-2.0
gpl-3.0
lgpl-3.0
unlicense
bsd-2-clause
isc
lgpl-2.1
gpl-2.0
apache-2.0
cc0-1.0
artistic-2.0
bsd-3-clause
agpl-3.0
epl-1.0
```

### Generate a new license.

```bash
$ lucy create <License Name> --name=<Author Name>             
$ lucy create mit --name=Chinmaya                     # Creates a MIT license for your project.
```

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
$ python lucy/lucy.py list
```
