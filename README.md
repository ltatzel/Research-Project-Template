# Research Project Template

This repository provides a *minimal* template for research projects in Python.
It includes a basic structure for organizing code, results, and documentation,
and demonstrates how to incorporate good practices in software engineering such
as testing, continuous integration, and automated linting and formatting. The
template is designed to be lightweight such that it can be easily adapted to
your specific needs.

**Motivation:** Research projects often grow organically: Experiments
accumulate, code gets copied across notebooks, and results become difficult to
trace. A small amount of structure helps prevent this and makes it easier to
understand, reproduce, and maintain your code, or share it with collaborators.

**Credits & License:** This template was created by Lukas Tatzel and is
available at https://github.com/ltatzel/Research-Project-Template. If you find
it useful, feel free to reference the original repository. In case you have any
questions or suggestions for improvement, please open an issue on GitHub.

---

## 1. Good Practices in Software Engineering

This template implements a minimal set of practices that help keep research
code organized and reliable. 

- **Version Control:** Version control allows you to track the history of a
    project. Every change to the codebase is recorded and can be inspected or
    reverted later. It also facilitates collaboration, as multiple people can
    work on in different branches and merge their changes together. This
    repository is a GitHub template, which means that when you create a new
    repository based on this template, it will already be set up with git for
    version control.

- **Testing:** Automated tests help ensure that your code behaves as expected.
    For example, if you know the expected output of a function for certain
    inputs, you can write a test that verifies this behavior automatically. This
    template uses the pytest package for running tests.

- **Continuous Integration:** Whenever code changes are made, it is useful to
    automatically check whether everything still works. This process is called
    *Continuous Integration (CI)*. This template includes a GitHub workflow in
    `.github/workflows` that automatically creates a fresh environment on
    GitHub, installs the project dependencies, and runs the tests using
    `pytest`. If something fails, the workflow reports the error. CI also
    ensures that all required dependencies are *explicitly* listed in the
    `project_template_env.yml` file, which is important for reproducibility.

- **Code Linting and Formatting:** Linting checks your code for errors, bad
    practices, and style violations (e.g. unused imports or undefined
    variables). A formatter automatically rewrites your code to follow
    consistent style rules (e.g. a specific maximum line length). This template
    uses [Ruff](https://docs.astral.sh/ruff/) which is a fast Python linter and
    formatter that supports both Python files and Jupyter notebooks. 

- **Clean Code:** Writing clean and readable code is always advisable. Some
    useful principles include:

    - Use meaningful names for variables, functions, etc.
    - Avoid duplicating code. If you find yourself copying and pasting code,
      the alarm bells should be ringing in your head. It will often make sense
      to extract the common code into a reusable function or module. 
    - Prefer simple solutions over complex ones.
    - Each code unit should only perform a single, clearly defined task (this
      is also known as the *Single Responsibility Principle*).
    - Write docstrings describing what your code does. Here's an example with a
      simple one-line docstring:
      ```python
      def add_10(input_number):
          """Add 10 to the given number `input_number`."""
          return input_number + 10
      ```     
      There are different conventions for docstrings that you can adopt, e.g.
      the *Google* or *NumPy* style. But even a short description as in the
      example above is better than no docstring at all.
      

    These small habits make your code easier to understand for collaborators
    and your future self.

---

## 2. Structure of this Template

The repository is organized into four main folders.

- **`source`**: The `source` folder contains *reusable code* that may be used
    across *multiple* experiments. Since we want to be able to import this code,
    it should be organized in Python files (not Jupyter notebooks). Also, since
    this code is meant to be reused, it should include basic documentation and
    tests. All files live in `source/our_library`. This folder can be installed
    as a local Python package via `pip install -e .` (details in section 3).
    After installation, functions can be imported in experiments very
    conveniently: `from our_library.some_functions import add_10`.

    The `source` folder also contains a `tests` directory for automated
    testing. A useful convention is to mirror the structure of the library and
    the tests. For instance, if you have a file
    `source/our_library/some_functions.py`, you should implement the
    corresponding tests in `source/tests/test_some_functions.py`.

- **`experiments`:** The `experiments` folder contains the *actual research
    experiments*. Each experiment has its own numbered folder, e.g.
    `experiments/01_first_experiment`. Experiments can be implemented using
    Jupyter notebooks or Python scripts. Separating reusable code (`source`)
    from experiment-specific code (`experiments`) helps keep projects
    organized. A good rule of thumb: If you find yourself copying code between
    experiments, it should probably be moved to `source`.

- **`results`:** The `results` folder stores outputs generated by our
    experiments. Its structure mirrors the `experiments` folder. So, if you
    have an experiment in `experiments/01_first_experiment`, the corresponding
    results should be stored in `results/01_first_experiment`. This makes it
    easy to keep track of which results belong to which experiment.
        
    Typical outputs include plots, tables, trained models, or intermediate
    data. Because result files can be large, the contents of the `results`
    folder are excluded from git tracking by default. However, if your files
    are small, you can explicitly track a subfolder by adding an exception such
    as `!results/01_first_experiment/` to the `.gitignore` file. An alternative
    for large files is to use [Git LFS](https://git-lfs.com/).

- **`documentation`:** The `documentation` folder contains project
    documentation. Currently it includes a minimal LaTeX paper template in
    `documentation/paper`. Additional material such as slides or reports can
    also be placed here. Since everything lives in the same repository, figures
    from the `results` folder can easily be included in the paper.

    If you prefer writing papers in an online LaTeX editor, platforms such as
    *Overleaf* can also be connected to GitHub repositories. This allows you to
    edit the paper collaboratively in Overleaf while keeping the source files
    synchronized with the repository. More information on this can be found
    [here](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration).

---

## 3. How To Use This Template

**Prerequisites:** To use this template, you need a GitHub account and git
installed on your local machine. In addition, you need `conda` installed to
create and manage the Python environment used in this project. If you want to
compile the LaTeX paper, you will also need a LaTeX distribution such as [TeX
Live](https://www.tug.org/texlive/) installed on your machine.

If this is the first time you are using this template, it is recommended to
work through all of the following steps:

1. **Use the Template and Clone:** On the GitHub page of this repository, click
    on "Use this template" to create a new repository based on this template.
    Give the new repository a name that makes sense for your project and set it
    to private if you do not want to share it publicly. You can also add a
    project description here. After creating the new repository, use `git
    clone` to download it to your local machine.

2. **Setup the Environment:** First create and activate the environment.

    > OPTIONAL: If you want, you can already modify the template here to give
    > the environment a meaningful name. For this, change the name of the
    > `.yml` file, the `name` field in that file and the GitHub workflow in
    > `.github/workflows` accordingly.

    ```
    conda env create -f project_template_env.yml
    conda activate project_template_env
    ```

    This will install the required external dependencies listed in
    `project_template_env.yml`. Next, install the *local* library.

    > OPTIONAL: Again, you can modify the template here and rename the
    > `our_library` folder. Note, however, that this requires additional
    > changes (e.g. in the `setup.py` file and import statements).

    ```
    cd source
    pip install -e .
    ```

    For this to work, we need the `setup.py` file in `source`. Take a look at
    that file. We also need the `__init__.py` file in `source/our_library`.
    This ensures that the `our_library` folder is recognized as a Python
    package. The `-e` flag installs the package in *editable mode*, meaning
    that changes to the source code immediately become available without
    reinstalling the package.

    You can verify the installation with `conda list`. Make sure that the local
    package `our_library` appears in the list of installed packages.

3. **Explore the Repository:** Explore the structure of the repository. Note
    that the structure of the `tests` folder mirrors the structure of the
    `our_library` folder; and `results` mirrors `experiments`. This is a useful
    convention that helps keep things organized.

4. **Run the Tests and Ruff:** Take a look at
    `source/our_library/some_functions.py` and the corresponding tests in
    `source/tests/test_some_functions.py`. Note that the tests use
    `@pytest.mark.parametrize`, which is a convenient way to run the same test
    with multiple inputs. Run `pytest .` from the `source` directory to see the
    automated tests in action. Feel free to extend `our_library` and add
    additional tests.s 

    In addition, you can manually run the linter and formatter via
    ```
    ruff check .
    ruff format .
    ```

5. **Trigger the GitHub Workflow:** Take a look at the GitHub workflow
    `run_pytest.yml` in `.github/workflows`. This workflow is triggered
    automatically whenever you push changes to GitHub (see the section beginning
    with `on`). It creates a fresh environment, installs the dependencies,
    checks the code using Ruff, and runs the tests using `pytest`. You can make
    a small change to the code (e.g. by adding another test case to
    `test_some_functions.py`) and push it to GitHub. Then, open your browser, go
    to your repository and click on the *Actions* tab to inspect the workflow.

6. **Enable Automatic Checks Before Commits:** You can run formatting and
    linting automatically before each commit using the `pre-commit` package.
    This helps catch issues early and keeps the codebase clean without any extra
    effort. Run `pre-commit install`, which uses the configuration specified in
    the `.pre-commit-config.yaml` file. After this, every time you create a
    commit (e.g. via the terminal or an editor like VS Code), the code will be
    automatically checked and formatted using Ruff. If issues are found, the
    commit will be blocked until they are resolved. You can also run the
    pre-commit checks manually via `pre-commit run --all-files`.

7. **Run the Experiments:** Take a look at the experiments in the `experiments`
    folder. Note how reusable code from `source/our_library` is imported and how
    results are written to the `results` folder. Run the first experiment to see
    this in action. Feel free to add an additional experiment. For this, you
    could add code to `source/our_library`, write a corresponding test, import
    the new function in your experiment and finally generate and save some
    results.

8. **Compile the LaTeX Paper:** Try compiling the LaTeX paper in
    `documentation/paper`. The template demonstrates how figures from the
    `results` folder can be included in the paper.

9. **Adapt and Extend the Template:** Adapt and extend the template as needed
    for your own research project.
