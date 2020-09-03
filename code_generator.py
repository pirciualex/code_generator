import importlib
import sys
import os
import json


def main(argv):
    if(not argv):
        with open("README.md") as readme:
            readme_content = readme.read()
        # TODO: if there are no arguments provided,
        # take the #usage section of the README file and print it
        print(readme_content)
    else:
        if not os.path.isdir(argv[0]):
            print("Please provide a valid path")
            return

        # read the files in the provided path and select the metadata
        # file from the rest of the files
        files = []
        for f in os.listdir(argv[0]):
            fileToAdd = os.path.join(argv[0], f)
            if(f == "metadata.json"):
                global metadata
                metadata = fileToAdd
            else:
                files.append(fileToAdd)

        # read metadata.json for information about the languages to
        # execute the script for and the paths to write the generated files to
        with open(metadata) as jsonMetadata:
            metadataInfo = json.load(jsonMetadata)
            languages = metadataInfo["languages"]
            languages = languages.split(",")
            pathsToWrite = metadataInfo["paths"]
            pathsToWrite = pathsToWrite.split(",")
            projectName = metadataInfo["projectName"]

        if len(languages) != len(pathsToWrite):
            print("The metadata provided is incorrect...")
            print("Please review the metadata file!")
            return

        # pass the file containing the metacode to each module for
        # every language specified
        modules = []
        for language in languages:
            modules.append(importlib.import_module("languages." + language))

        for f in files:
            for i in range(len(languages)):
                modules[i].process(f, pathsToWrite[i], projectName)


if __name__ == "__main__":
    main(sys.argv[1:])
