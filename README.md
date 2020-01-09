# Codespell Action

A GitHub workflow action to check for common misspellings in the edited files.
It uses the idea, name and dictionary from https://github.com/codespell-project/codespell

After running the action, it adds a comment if misspellings were found.

## Example usage

`uses: plettich/python_codespell_action@master`

## TODO

- [x] implement PR comment
- [ ] add tests
- [ ] update PR comment and don't post new ones on each run
- [ ] check filenames as well
- [ ] add configuration file for adding excludes, dictionaries and ignores
- [ ] make avatar and messages configurable (if possible)
