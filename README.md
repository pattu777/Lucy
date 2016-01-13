![]()

# Lucy

A CLI tool to generate `license` file for your project.

> **Features**

> - Written in simple Python
> - Easy to [install](https://github.com/pattu777/Lucy#installation)
> - [Easy to use](https://github.com/pattu777/Lucy#usage)
> - Uses Github API to search and create your [`license` files](https://github.com/karan/joe#list-all-available-files).
> - Works on Linux, Windows and Mac

## Python libraries used

- [Click]() 				# For parsing command line arguements.
- [requests]()				# For making Github API calls.

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

### Basic usage


```bash
$ lucy mit    # Creates a MIT license for your project.
```

### Overwrite an existing `.license` file

```bash
$ lucy apache-2.0 > LICENSE    # Replaces the old license file with Apache-2.0
```

### List all available licenses

```bash
$ lucy ls    # OR `lucy list`
```

Output:

> 
[
  {
    "key": "agpl-3.0",
    "name": "GNU Affero General Public License v3.0",
    "url": "https://api.github.com/licenses/agpl-3.0",
    "featured": false
  },
  {
    "key": "apache-2.0",
    "name": "Apache License 2.0",
    "url": "https://api.github.com/licenses/apache-2.0",
    "featured": true
  },
  {
    "key": "artistic-2.0",
    "name": "Artistic License 2.0",
    "url": "https://api.github.com/licenses/artistic-2.0",
    "featured": false
  },
  {
    "key": "gpl-2.0",
    "name": "GNU General Public License v2.0",
    "url": "https://api.github.com/licenses/gpl-2.0",
    "featured": true
  },
  {
    "key": "unlicense",
    "name": "The Unlicense",
    "url": "https://api.github.com/licenses/unlicense",
    "featured": false
  },
  {
    "key": "lgpl-2.1",
    "name": "GNU Lesser General Public License v2.1",
    "url": "https://api.github.com/licenses/lgpl-2.1",
    "featured": false
  },
  {
    "key": "gpl-3.0",
    "name": "GNU General Public License v3.0",
    "url": "https://api.github.com/licenses/gpl-3.0",
    "featured": false
  },
  {
    "key": "lgpl-3.0",
    "name": "GNU Lesser General Public License v3.0",
    "url": "https://api.github.com/licenses/lgpl-3.0",
    "featured": false
  },
  {
    "key": "mit",
    "name": "MIT License",
    "url": "https://api.github.com/licenses/mit",
    "featured": true
  },
  {
    "key": "mpl-2.0",
    "name": "Mozilla Public License 2.0",
    "url": "https://api.github.com/licenses/mpl-2.0",
    "featured": false
  },
  {
    "key": "bsd-2-clause",
    "name": "BSD 2-clause \"Simplified\" License",
    "url": "https://api.github.com/licenses/bsd-2-clause",
    "featured": false
  },
  {
    "key": "epl-1.0",
    "name": "Eclipse Public License 1.0",
    "url": "https://api.github.com/licenses/epl-1.0",
    "featured": false
  },
  {
    "key": "bsd-3-clause",
    "name": "BSD 3-clause \"New\" or \"Revised\" License",
    "url": "https://api.github.com/licenses/bsd-3-clause",
    "featured": false
  },
  {
    "key": "isc",
    "name": "ISC License",
    "url": "https://api.github.com/licenses/isc",
    "featured": false
  },
  {
    "key": "cc0-1.0",
    "name": "Creative Commons Zero v1.0 Universal",
    "url": "https://api.github.com/licenses/cc0-1.0",
    "featured": false
  }
]

## Contributing

#### Bug Reports & Feature Requests

Report any bugs through the [issue tracker](https://github.com/pattu777/Lucy/issues).

#### Developing

Create a new branch and send a pull request. To begin developing, do this:

```bash
# Create a virtual environment
$ git clone --recursive git@github.com:pattu777/Lucy.git
$ cd Lucy/
$ git checkout -b <feature-branch-name>
$ python lucy/lucy.py mit
```