# Levenshtein Distance

A repertoire for Levenshtein Distance calculation functions to be used in other projects. 

Project is still being worked on.

## License

This project is licensed under the [GNU GPL-3.0](https://github.com/ErtyumPX/hashiwokakero/blob/main/LICENSE) license.

## Setup

There is no third-party dependency.

Easily clone the project.

```
> git clone <repo-url>
> cd levenshtein-distance
```

### Python

The project is written in Python 3.11.6, although should work on any Python Interpreter above 3.5.x.

Main library is `python3/distance.py` where all the functions are defined.

To run the general tests:

```
> cd python/
> make test
```

### C++

Project is currently compiled with GNU G++ 13.2.1.

For compiling and linking rules GNU Make 4.4.1 was used.

After fulfilling dependencies, download or clone the project and use Makefile to easily compile:

```
> cd cpp/ 
> make all
> make run
```

### TypeScript

Project is written in TypeScript 5.3.3 with ES2021 target.

For package management Yarn 1.22.21 is used.

There is no dependancy for library, but for testing Jest 27.4.7 is used.

```
> cd typescript/
> yarn install
```

Assuming that you will compile the source here and rather use the code somewhere else, there is no need for a build script.

Still, there are some tests that you can run with Jest:

```
> yarn test 
```



## Project

Will be written soon...
