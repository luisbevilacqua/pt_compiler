# PT COMPILER
PT is a programming language c-similar, but written in Brazilian Portuguese.
The compiler is capable of transpiling PT code to C+- and Java.

## Getting started

1. Clone this repo.
2. Install the prerequisites.

### Prerequisites

You need to have antlr4, python3 and pip installed. If you don't, check the install instructions.
The python libraries needed are indicated in `requirements.txt`.

#### Setup using virtualenv

Execute the following command to install the requirements using a virtualenv:
```bash
$ virtualenv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
```


## PT Syntax 

A PT code example containing all reserved words is in /code_examples/basic_syntax.

## Running

Run the following command to execute the compiler:

```bash
python3 PtCompiler.py <language> [--input_file <input_file>] [--output_file <output_filee>]
```
Where `language` is C or Java.

The input and output file parameters are optional; if not given, the compiler will use the standard IO.

## Built with
- [ANTLR](http://www.antlr.org/) - (ANother Tool for Language Recognition)


## About

The PT language and its compiler was developed as a project for the Compilers course at Universidade Federal do ABC by Ana de Paula and Luis Bevilacqua, under the orientation of professor Francisco Isidro Masseto, in winter/2019.
