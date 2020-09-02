import importlib
import sys
import os


def main(argv):
    if(not argv):
        readme = open("README.md")
        readme_content = readme.read()
        readme.close()
        # TODO: if there are no arguments provided,
        # take the #usage section of the README file and print it
        print(readme_content)
    else:
        print(argv[0])
        if not os.path.isdir(argv[0]):
            print("Please provide a valid path")
            return

        # TODO: read metadata.json for information about the languages to
        # execute the script for and the paths to write the generated files to

        # langs = input("provide the languages\n")
        # langs = langs.split(",")

        # TODO: for each txt file containing the metacode,
        # generate the specific class for each language from the metadata
        # file

        # modules = []
        # for lang in langs:
        #     modules.append(importlib.import_module("languages." + lang))

        # for module in modules:
        #     module.test()


if __name__ == "__main__":
    main(sys.argv[1:])
