# Research Project Template

This is a minimalistic template for research projects in Python.

TODO: General principles and purpose of this template. This is also relevant
even if you work on the code on your own. In order to keep your code organizsed
and maintainable, it is good to think about how to structure your project and
how to work on it. This template is a minimalistic starting point for that. 



---

## 1. Good Practices in Software Engineering

TODO: Intro, list below is limited/minimalistic, i.e. it does not include
automated formatting (there exist tools like `black`, `isort`, `flake8`, ...)
... so think of it as a minimalistic starting point that you can further adjust
depending on your specific circumstances.

- **Version control:** Version control means that we keep track of the entire
  project history. In this project, we use git for that. This is a great tool
  also for working on one codebase collaboratively. 
- **Automated testing:** You can check the correctness of your code by running
  tests. For instance, in some cases, you might know the desired outcome of a
  function. So, here, a simple test could check if the output of the function
  is as expected. In this project, we use the `pytest` package for running
  tests. More on this later. 
- **Continuous integration:** Whenever you make a change to your code, you want
  to make sure that the change does not break anything. Running these checks in
  an automated way is called Continuous Integration (CI). In this project
  template, we use a Github workflow for that. Whenever we push a change to the
  repo, Github sets up a virtual environment, installs all the required
  packages and runs `pytest`. If anything crashes, we'll receive an e-mail.
  This also forces you to state all the dependencies of your code explicitly
  (because if there are for instance missing packages or version conflicts, the
  execution of the Github workflow will fail).
- **Clean code:** Of course, you should also try to write clean code. Some
  basic principles include:
   - Use meaningful names for variables/functions/...
   - Avoid duplication
   - Try to avoid unnecessary complexity
   - Each code unit should only perform a single, clearly defined task (this is
     also known as the Single Responsibility Principle).
   - Document what your code does. For instance, write a brief docstring what
     your function/method/class does and what its parameters are.



## 2. Project Structure and Principles

The project has four main folders:
1. **`source`:** This is the place for code that you want to *re-use* in
   multiple of your experiments. So here, we will use Python files (*not*
   Jupyter notebooks) and put a larger emphasis on code quality (e.g. proper
   testing, docstrings that briefly describe what the functions/methods do and
   what their arguments are, etc.). One little trick is to use a pip command
   that installs the `our_library` sub-folder as a Python module (see section
   2). For this to work, we need the `setup.py` file in `source` and an (empty)
   `__init__.py` file in `our_library`. So, in our experiments, you can do
   something like `from our_library.some_functions import add_10` (see
   experiment 1 for a demo). 
   
   The `source` folder also contains a `tests` folder. Here, you can use e.g.
   `pytest` to systematically test your code. To do that, simply run `pytest
   .`. This command will look for test functions (and find
   `source/tests/test_some_functions.py`) and give a quick report if all tests
   ran through. 
   
    One useful convention is that the structure within the folders `tests` and
   `our_library` are basically identical. For instance, for the file
   `our_library/some_functions.py` we implement tests in
   `tests/test_some_functions.py`. This way, it is always clear where you can
   find the tests or a given file from `our_library`.
2. **`experiments`:** This folder contains an enumerated sub-folder for each
   new experiment. I usually use Jupyter notebooks at least for smaller
   experiments because I like that I can play with and interact with the code
   more intuitively and immediately see the output of the code. But, of course,
   you can also use Python scripts here, if you prefer. 

   I think, this separation between re-usable code in `source` and single-use
   code in `experiments` makes a lot of sense. A good indication that something
   should be in `source` is if you find yourself copying larger chunks of code.
   Then, the alarm clocks in your head should go off! 
3. **`results`:** This folder contains the results of your experiments. To keep
   things clear, we use the same folder structure as in `experiments`. So,
   you'll find the results for `experiments/01_fist_experiment` in
   `results/01_first_experiment`. 
4. **`documentation`:** This folder is for documentation. At the moment, it
   contains a mimalistic LaTeX paper in the `paper` subfolder. You could also
   have other folders, e.g. for slides. Because everything is in the same repo,
   we can easily import plots and other results from the `results` folder into
   the paper (as demonstrated in the paper template).

Additional stuff:
- CI implemented in `.github/workflows`. This file contains the instructions
  that Github performs whenever we push a code change. It tells Github which
  packages to install and how to run tests (in our case using `pytest`).



## 3. Setup

TODO: Intro

First, we create a virtual environment for our project with conda. 
```
conda env create -f project_template_env.yml
conda activate project_template_env
cd our_own_library
pip install -e .
```
You can check with `conda list` that the local package `our_library` is
installed.



## 4. How to work with this template? 

Recommended steps for working with this template:
- Make a fork of the repo such that you have your own copy of the code on
  Github. I guess that is necessary for the CI to work properly? Then, clone
  the repo.
- Set up the virtual environment and install the required packages as described
  above. 
- After installation of the packages, explore the structure of the repo and
  take a look at the files (there aren't very many). 
- In particular, take a look at `source/our_library` and `source/tests`. Note
  the "parallel" structure of these folders. Then, run the tests from the
  `source` folder with `pytest .` and check the output.
- Try to run the code in `experiments` and check that it works and puts results
  in the correct place (the `results` folder).
- Try to compile the paper in `documentation/paper` and check that it works.
  Since we have everything in the same repo, you can easily import results from
  the `results` folder into the paper (as demonstrated in the paper template).
  