import helpers.helpers as helper
import json
import os


def process(fileToProcess, pathToWrite, projectName):
    with open(fileToProcess) as f:
        metacode = json.load(f)

    className = helper.capitalizeFirstWord(
        fileToProcess.split("/")[-1].split(".")[0])

    fileName = className + ".cs"
    header = "namespace " + projectName + \
        "\n{" + "\n\tpublic class " + className + "\n\t{"

    with open(os.path.join(pathToWrite, fileName), "w+") as f:
        f.write(header)
        for value in metacode:
            line = "\n\t\tpublic "
            if metacode[value] == "int":
                line += "int "
            if metacode[value] == "string":
                line += "string "
            line += helper.capitalizeFirstWord(value) + " { get; set; }"
            f.write(line)

        f.write("\n\t}\n}")
