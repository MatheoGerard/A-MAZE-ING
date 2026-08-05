*This project has been created as part of the 42 curriculum by mgerard, dmonseur.*

# A-MAZE-ING

## Description

A-MAZE-ING is a Python project whose goal is to generate and solve mazes using classical graph algorithms.

The program generates a maze according to a configuration file, displays it in the terminal using Rich, and computes a valid solution from the entrance to the exit.

---

# Features

- Generate perfect mazes
- Random generation with optional seed
- Solve mazes using the shortest path
- Terminal visualization using Rich
- Configurable symbols
- Configurable maze size
- Configurable entrance and exit
- Colored terminal interface using Rich
- Optional random seed for reproducible mazes
- Bonus features (music, enhanced display, gameplay.)

---

# Instructions

A Python maze generator and solver.

## Requirements

- Python 3.10+
- pip

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd A-Maze-ing
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or:

```bash
make install
```

## Run the project

Start the maze generator:

```bash
python3 a_maze_ing.py
```

or:

```bash
make run
```

## Export the Maze Generator as a package

Install the build dependency:

```bash
pip install build
```

Build the package:

```bash
python3 -m build
```

The generated package will be available in the `dist/` folder.

## Use the package

Install the generated wheel:

```bash
pip install dist/mazegen-1.0.0-py3-none-any.whl
```

Create a `test.py` file and use the generator:
```python
import mazegen

maze = mazegen.MazeGenerator(
    25,
    25,
    "0, 0",
    "24, 24",
    "maze.txt",
    "False",
    None
)
```

The output file will be generated using the provided parameters.

---

# Configuration File

The project uses a configuration file to customize maze generation.

Example:

```txt
WIDTH=31
HEIGHT=21
ENTRY=0,0
EXIT=30,20
PERFECT=True
SEED=42
OUTPUT_FILE=maze.txt
```

## Parameters

| Parameter | Description |
|------------|-------------|
| WIDTH | Maze width |
| HEIGHT | Maze height |
| ENTRY | Entry position |
| EXIT | Exit position |
| PERFECT | Generate a perfect maze |
| SEED | Optional random seed |
| OUTPUT_FILE | Output filename |

---

# Maze Generation Algorithm

The maze is generated using a **Depth-First Search (DFS)** approach with backtracking.

## Principle

The algorithm starts from an initial cell and explores the maze as deeply as possible before backtracking.

The process is the following:

1. Start from the initial cell.
2. Mark the current cell as visited.
3. Randomly select an unvisited neighbouring cell.
4. Remove the wall between both cells.
5. Move to the neighbour and continue exploring.
6. When no unvisited neighbour remains, backtrack to the previous cell.
7. Repeat until every cell has been visited.

This approach generates a **perfect maze**, meaning there is exactly one path between any two cells.

---

# Maze Solving Algorithm

Once the maze has been generated, it is solved using a **Breadth-First Search (BFS)** algorithm.

The BFS explores the maze level by level from the entrance until it reaches the exit.

Using a queue guarantees that the first path found is also the **shortest path**, making BFS particularly well suited for maze solving.

---

# Why These Algorithms?

Two different graph traversal algorithms were chosen because they each excel at a different task.

### DFS for Generation

Depth-First Search naturally produces long corridors and perfect mazes while remaining simple to implement and efficient.

### BFS for Solving

Breadth-First Search guarantees the shortest path between the entrance and the exit. It is reliable, easy to understand and perfectly complements the DFS-generated maze.
---

# Project Structure

```
AMAZEING/
│
├── assets/
│   └── 06. Unknown Planet.mp3
│
├── gameplay/
│   ├── __init__.py
│   ├── game.py
│   └── input_reader.py
│
├── mazegen/
│   ├── __init__.py
│   ├── bfs_solver.py
│   ├── cells_class.py
│   ├── gen.py
│   ├── generator.py
│   ├── hex_traductor.py
│   ├── maze_generator.py
│   ├── parsing_config.py
│   ├── print42.py
│   └── wall_destroyer.py
│
├── music/
│   ├── __init__.py
│   └── music_manager.py
│
├── visualization/
│   ├── __init__.py
│   └── visualization_format.py
│
├── a_maze_ing.py
├── config.txt
├── maze.txt
├── requirements.txt
├── pyproject.toml
├── Makefile
├── README.md
└── LICENSE.md
```

(The exact structure may differ depending on your implementation.)

---

# Reusable Components

Several parts of the project were designed to be reusable:

## Configuration parser

The parser can easily be reused for any project using key/value configuration files.

## Maze generator

The generator is independent from the display and can generate mazes for another application.

## Maze solver

The solving algorithm can be reused on any compatible maze representation.

---

# Technical Choices

- Python
- Object-Oriented Programming
- Rich for terminal rendering
- Modular architecture
- Type hints
- Docstrings
- Configuration-based execution

---

# Team & Project Management

## Team Members

- **mgerard**
- **dmonseur**

## Work Distribution

The project was developed collaboratively, with both team members participating in every major aspect of the application, including design, implementation, debugging and testing.
All major architectural decisions were discussed and validated together.

- **mgerard** is the main architect of the bonus features implementation.

## Planning

Our initial objective was to complete the mandatory part first by implementing:

1. Configuration parsing
2. Maze representation
3. Maze generation
4. Maze solving
5. Terminal rendering

Once the mandatory features were stable, we focused on refactoring the codebase before implementing the bonus features.

Throughout the project, the planning evolved as we continuously improved the project architecture, reduced duplicated code and reorganized modules to increase readability and maintainability.

## What Worked Well

- Continuous communication.
- Shared code reviews.
- Modular architecture.
- Progressive refactoring.
- Clear task distribution while keeping both members involved in all major decisions.

## What Could Be Improved

- Plan Maze Genator earlier.
- Plan bonus features sooner.
- Improve performance on very large mazes.


## Tools Used

- Python
- Neovim
- Visual Studio Code
- Git
- GitHub
- Rich

---

# AI Usage

Artificial Intelligence was used as a development assistant.

It was used for:

- generating documentation;
- explaining package concepts;

All implementation choices, testing and validation were performed by the project author.

---

# Resources

Python Documentation

https://docs.python.org/3/

Rich Documentation

https://rich.readthedocs.io/

Depth-First Search

https://en.wikipedia.org/wiki/Depth-first_search

Maze Algorithms

https://en.wikipedia.org/wiki/Maze_generation_algorithm
https://en.wikipedia.org/wiki/Maze-solving_algorithm


---

# License

MIT License

Copyright (c) 2026 dmonseur, mgerard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
