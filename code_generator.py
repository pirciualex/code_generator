# import languages.cs as cs
import importlib
langs = input("provide the languages\n")
langs = langs.split(",")

modules = []
for lang in langs:
    modules.append(importlib.import_module("languages." + lang))

for module in modules:
    module.test()
