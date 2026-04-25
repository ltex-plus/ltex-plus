#!/usr/bin/python3

# Copyright (C) 2019-2025
# Julian Valentin, Daniel Spitzer, LTeX+ Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import functools
import json
import pathlib
import re
import subprocess
import sys
from typing import Any, Callable, Dict, Optional, Sequence, Tuple, Union

sys.path.append(str(pathlib.Path(__file__).parent))
import common
from linkSettingsAndCommands import linkSettingsAndCommands



licenseHeader = """
# Copyright (C) 2019-2025
# Julian Valentin, Daniel Spitzer, LTeX+ Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

i18nStrings = {
      "en" : {
        "arrayWhereEachEntryHasTheFollowingType" : "Array where each entry has the following type",
        "arrayWithTheFollowingEntries" : "Array with the following entries",
        "clickToShowHide" : "Click to show/hide",
        "commandIntroduction" : "To run a command, open the Command Palette (`Ctrl+Shift+P`) and "
          "start typing the name of the command.",
        "default" : "Default",
        "example" : "Example",
        "examples" : "Examples",
        "fullTypeDescription" : "Full type description",
        "objectWithArbitraryPropertyNames" : "Object with arbitrary property names, "
          "where the value of each property has the following type",
        "objectKeyedByLanguageCode" : "Object keyed by language code "
          "(see `ltex.language` for accepted values), "
          "where the value of each property has the following type",
        "objectWithTheFollowingProperties" : "Object with the following properties",
        "oneOfTheFollowingTypes" : "One of the following types",
        "oneOfTheFollowingValues" : "One of the following values",
        "oneType" : "`{}`",
        "possibleValues" : "Possible values",
        "scalarOfType" : "Scalar of type {}",
        "threePlusTypesSuffix" : ", `{}`, or `{}`",
        "twoTypes" : "`{}` or `{}`",
        "type" : "Type",
      },
      "de" : {
        "arrayWhereEachEntryHasTheFollowingType" : "Array, bei dem jeder Eintrag folgenden Typ hat",
        "arrayWithTheFollowingEntries" : "Array mit folgenden Einträgen",
        "clickToShowHide" : "Klick zum Zeigen/Verbergen",
        "commandIntroduction" : "Um einen Befehl auszuführen, öffnen Sie die Befehlspalette "
          "(`Ctrl+Shift+P`) und beginnen Sie mit der Eingabe des Befehlsnamens.",
        "default" : "Voreinstellung",
        "example" : "Beispiel",
        "examples" : "Beispiele",
        "fullTypeDescription" : "Vollständige Beschreibung des Typs",
        "objectWithArbitraryPropertyNames" : "Objekt mit beliebigen Eigenschaftsnamen, "
          "wobei die Werte jeder Eigenschaft folgenden Typ hat",
        "objectKeyedByLanguageCode" : "Objekt mit Sprachcode als Eigenschaftsname "
          "(siehe `ltex.language` für gültige Werte), "
          "wobei die Werte jeder Eigenschaft folgenden Typ hat",
        "objectWithTheFollowingProperties" : "Objekt mit folgenden Eigenschaften",
        "oneOfTheFollowingTypes" : "Einer der folgenden Typen",
        "oneOfTheFollowingValues" : "Einer der folgenden Werte",
        "oneType" : "`{}`",
        "possibleValues" : "Mögliche Werte",
        "scalarOfType" : "Skalar vom Typ {}",
        "threePlusTypesSuffix" : ", `{}` oder `{}`",
        "twoTypes" : "`{}` oder `{}`",
        "type" : "Typ",
      },
    }



def formatList(json_: Sequence[Any]) -> str:
  return "\n".join(f"- {formatAsJson(x)}" for x in json_)



def formatType(type_: str, packageNlsJson: Dict[str, str]) -> str:
  if isinstance(type_, str) or (len(type_) == 1):
    return packageNlsJson["oneType"].format(type_)
  elif len(type_) == 1:
    return packageNlsJson["oneType"].format(type_[0])
  elif len(type_) == 2:
    return packageNlsJson["twoTypes"].format(type_[0], type_[1])
  else:
    return (", ".join(packageNlsJson["oneType"].format(x) for x in type_[:-2]) +
        packageNlsJson["threePlusTypesSuffix"].format(type_[-2], type_[-1]))



def formatEnum(enumNames: Sequence[str], enumDescriptions: Sequence[str],
      packageNlsJson: Dict[str, str], indent: int = 0) -> str:
  formatEnumEntries: Callable[[str, str], str] = (lambda x, y: formatAsJson(x) +
      (f": {formatDescription(y, packageNlsJson)}" if y is not None else ""))
  markdown = "\n".join(f"- {formatEnumEntries(x, y)}" for x, y in zip(enumNames, enumDescriptions))
  markdown += "\n"
  return markdown



def formatAsJson(json_: Any) -> str:
  return f"`{json.dumps(json_)}`"



def replaceNlsKey(packageNlsJson: Dict[str, str], match: re.Match[str]) -> Any:
  key = match.group(1)

  keys = [key]
  if key.endswith(".markdownDescription"): keys.insert(0, f"{key[:-20]}.fullMarkdownDescription")

  for curKey in keys:
    if curKey in packageNlsJson: return packageNlsJson[curKey]

  raise RuntimeError("unknown NLS key '{}'".format(key))



def formatDescription(description: str, packageNlsJson: Dict[str, str]) -> str:
  return re.sub(r"%([A-Za-z0-9\-_\.]+)%", functools.partial(replaceNlsKey, packageNlsJson),
      description)



def formatFullType(settingJson: Dict[str, Any], packageNlsJson: Dict[str, str],
      indent: int = 0) -> str:
  markdown = ""
  description = settingJson.get("markdownDescription", None)

  if (description is not None) and (indent > 0):
    markdown += f"{formatDescription(description, packageNlsJson)}\n\n{indent * ' '}"

  if "oneOf" in settingJson:
    itemTypes = settingJson["oneOf"]
    markdown += f"{packageNlsJson['oneOfTheFollowingTypes']}:\n\n"
    markdown += "".join(
        f"{indent * ' '}- {formatFullType(x, packageNlsJson, indent+2)}" for x in itemTypes)
  elif "type" not in settingJson:
    markdown += formatAsJson(settingJson) + "\n"
  elif settingJson["type"] == "object":
    if "patternProperties" in settingJson:
      assert len(settingJson["patternProperties"]) == 1
      assert "^.*$" in settingJson["patternProperties"]
      propertyType = settingJson["patternProperties"]["^.*$"]
      markdown += f"{packageNlsJson['objectWithArbitraryPropertyNames']}:\n\n"
      markdown += f"{indent * ' '}- {formatFullType(propertyType, packageNlsJson, indent+2)}"
    elif (("enum" in settingJson.get("propertyNames", {})) and
        all(re.match(r"^[a-z]{2,3}(-[A-Za-z\-]+)*$", k)
            for k in settingJson["propertyNames"]["enum"])):
      propsDict = settingJson.get("properties", {})
      firstKey = next(iter(propsDict))
      propertyType = {k: v for k, v in propsDict[firstKey].items() if k != "markdownDescription"}
      markdown += f"{packageNlsJson['objectKeyedByLanguageCode']}:\n\n"
      markdown += f"{indent * ' '}- {formatFullType(propertyType, packageNlsJson, indent+2)}"
    else:
      markdown += f"{packageNlsJson['objectWithTheFollowingProperties']}:\n\n"
      markdown += "".join(
          f"{indent * ' '}- {formatAsJson(x)}: {formatFullType(y, packageNlsJson, indent+2)}"
          for x, y in settingJson["properties"].items())
  elif settingJson["type"] == "array":
    itemTypes = settingJson["items"]

    if isinstance(itemTypes, dict):
      markdown += f"{packageNlsJson['arrayWhereEachEntryHasTheFollowingType']}:\n\n"
      markdown += f"{indent * ' '}- {formatFullType(itemTypes, packageNlsJson, indent+2)}"
    else:
      markdown += f"{packageNlsJson['arrayWithTheFollowingEntries']}:\n\n"
      markdown += "".join(
          f"{indent * ' '}- {formatFullType(x, packageNlsJson, indent+2)}" for x in itemTypes)
  elif "enum" in settingJson:
    enumNames = settingJson["enum"]
    enumDescriptions = (settingJson["markdownEnumDescriptions"]
        if "markdownEnumDescriptions" in settingJson else settingJson["enumDescriptions"])
    markdown += f"{packageNlsJson['oneOfTheFollowingValues']}:\n\n"
    markdown += "".join(
        f"{indent * ' '}- {formatAsJson(x)}: {formatDescription(y, packageNlsJson)}\n"
        for x, y in zip(enumNames, enumDescriptions))
  else:
    markdown += "{}\n".format(packageNlsJson["scalarOfType"].format(
        formatType(settingJson['type'], packageNlsJson)))

  return markdown



def mergeAliasesIntoCanonical(settingName: str, enum: Sequence[Any],
      enumDescriptions: Sequence[Any], packageNlsJson: Dict[str, str]
      ) -> Tuple[Sequence[Any], Sequence[Any]]:
  aliasOfByCode: Dict[str, str] = {}
  for code in enum:
    if not isinstance(code, str): continue
    nlsCode = code if len(code) > 0 else "emptyString"
    aliasKey = f"ltex.i18n.configuration.{settingName}.{nlsCode}.aliasOf"
    if aliasKey in packageNlsJson:
      aliasOfByCode[code] = packageNlsJson[aliasKey]
  if not aliasOfByCode: return enum, enumDescriptions

  aliasesByCanonical: Dict[str, list] = {}
  for alias, canonical in aliasOfByCode.items():
    aliasesByCanonical.setdefault(canonical, []).append(alias)

  newEnum, newDescriptions = [], []
  for code, desc in zip(enum, enumDescriptions):
    if code in aliasOfByCode: continue
    if code in aliasesByCanonical:
      aliasList = ", ".join(formatAsJson(a) for a in sorted(aliasesByCanonical[code]))
      desc = f"{desc} (also accepts: {aliasList})" if desc is not None else None
    newEnum.append(code)
    newDescriptions.append(desc)
  return newEnum, newDescriptions



def formatSetting(settingName: str, settingJson: Dict[str, Any],
      packageNlsJson: Dict[str, str]) -> Optional[str]:
  if "markdownDescription" not in settingJson: return None
  markdown = (f"## `{settingName}`\n\n"
      f"{formatDescription(settingJson['markdownDescription'], packageNlsJson)}\n")

  if "type" in settingJson:
    type_ = settingJson["type"]
  elif "oneOf" in settingJson:
    type_ = [x["type"] for x in settingJson["oneOf"]]
  else:
    raise ValueError("Missing type")

  examples = settingJson.get("examples", [])
  markdown += f"\n*{packageNlsJson['type']}:* {formatType(type_, packageNlsJson)}\n"

  if "enum" in settingJson:
    enum = settingJson["enum"]
    enumDescriptions = (settingJson["markdownEnumDescriptions"]
        if "markdownEnumDescriptions" in settingJson else
        settingJson.get("enumDescriptions", len(enum) * [None]))
    enum, enumDescriptions = mergeAliasesIntoCanonical(
        settingName, enum, enumDescriptions, packageNlsJson)
    markdown += f"\n*{packageNlsJson['possibleValues']}:*\n\n{formatEnum(enum, enumDescriptions, packageNlsJson)}\n"

  if len(examples) == 1:
    markdown += f"\n*{packageNlsJson['example']}:* {formatAsJson(examples[0])}\n"
  elif len(examples) >= 2:
    markdown += f"\n*{packageNlsJson['examples']}:*\n\n{formatList(examples)}\n"

  if "default" in settingJson:
    markdown += f"\n*{packageNlsJson['default']}:* {formatAsJson(settingJson['default'])}\n"

  if (type_ in ["array", "object"]) or (not isinstance(type_, str)):
    markdown += (f"\n*{packageNlsJson['fullTypeDescription']}:*\n\n"
        f"{formatFullType(settingJson, packageNlsJson)}\n")

  return markdown



def formatCommand(commandJson: Dict[str, Any], packageNlsJson: Dict[str, str]) -> Optional[str]:
  description = f"%ltex.i18n.commands.{commandJson['command']}.fullMarkdownDescription%"
  markdown = (f"## `LTeX: {formatDescription(commandJson['title'], packageNlsJson)}`\n\n"
      f"{formatDescription(description, packageNlsJson)}\n")
  return markdown



def getNlsLanguages(vscodeLtexRepoDirPath: pathlib.Path) -> Sequence[Tuple[str, str, pathlib.Path]]:
  return [
        ("en", "English", vscodeLtexRepoDirPath.joinpath("package.nls.json")),
        ("de", "German", vscodeLtexRepoDirPath.joinpath("package.nls.de.json")),
      ]



def getLtLanguageCode(languageCode: str) -> str:
  return {
        "en" : "en-US",
        "de" : "de-DE",
      }[languageCode]



def updateSupportedLanguages(vscodeLtexRepoDirPath: pathlib.Path,
      pagesRepoDirPath: pathlib.Path) -> None:
  packageNlsJsonPath = vscodeLtexRepoDirPath.joinpath("package.nls.json")
  packageNlsJson = json.loads(common.readFile(packageNlsJsonPath))
  languages: Dict[str, str] = {}
  aliasesByCanonical: Dict[str, list] = {}

  for key in packageNlsJson:
    regexMatch = re.match(
        r"^ltex\.i18n\.configuration\.ltex\.language\.([^.]+?)\.markdownEnumDescription$", key)
    if regexMatch is None: continue
    code = regexMatch.group(1)
    if code == "auto": continue
    aliasKey = f"ltex.i18n.configuration.ltex.language.{code}.aliasOf"
    if aliasKey in packageNlsJson:
      canonical = packageNlsJson[aliasKey]
      aliasesByCanonical.setdefault(canonical, []).append(code)
    else:
      languages[code] = packageNlsJson[key]

  languages = {x: y for x, y in sorted(languages.items(), key=lambda z: z[1])}

  def formatLanguage(code: str, name: str) -> str:
    aliases = sorted(aliasesByCanonical.get(code, []))
    if aliases:
      aliasList = ", ".join(f"`{a}`" for a in aliases)
      return f"{name}&nbsp;(`{code}`, also accepts: {aliasList})"
    return f"{name}&nbsp;(`{code}`)"

  languagesMarkdown = ("<!-- ltex-natural-languages-begin -->\n\n"
      "{}\n\n<!-- ltex-natural-languages-end -->".format(
        ", ".join(formatLanguage(x, y) for x, y in languages.items())))

  dstPath = pagesRepoDirPath.joinpath("pages", "supported-languages.md")
  markdown = common.readFile(dstPath)

  markdown = re.sub(
      r"<!-- ltex-natural-languages-begin -->(.|\n)*?<!-- ltex-natural-languages-end -->",
      languagesMarkdown, markdown)

  common.writeFile(dstPath, markdown)



def updateSettings(vscodeLtexRepoDirPath: pathlib.Path, pagesRepoDirPath: pathlib.Path) -> None:
  packageJsonPath = vscodeLtexRepoDirPath.joinpath("package.json")
  packageJson = json.loads(common.readFile(packageJsonPath))

  nlsLanguages = getNlsLanguages(vscodeLtexRepoDirPath)
  languageLinks = ", ".join((f"[{languageName}](settings-{languageCode}.html)"
        if languageCode != "en" else "[English](settings.html)")
      for languageCode, languageName, _ in nlsLanguages)

  for languageCode, _, packageNlsJsonPath in nlsLanguages:
    pageNameSuffix = (f"-{languageCode}" if languageCode != "en" else "")

    packageNlsJson = json.loads(common.readFile(packageNlsJsonPath))
    packageNlsJson.update(i18nStrings[languageCode])

    settingsJson = packageJson["contributes"]["configuration"]["properties"]
    settingsMarkdown = [formatSetting(x, y, packageNlsJson) for x, y in settingsJson.items()]
    markdown = """---{}
title: "Settings"
permalink: "/settings{}.html"
sidebar: "sidebar"
---

Change language of this page: {}

<!-- ltex: language={} -->

""".format(licenseHeader, pageNameSuffix, languageLinks, getLtLanguageCode(languageCode))
    markdown += "\n".join(x for x in settingsMarkdown if x is not None)
    markdown = re.sub("\n\n+", "\n\n", markdown)

    dstPath = pagesRepoDirPath.joinpath("pages", f"settings{pageNameSuffix}.md")
    common.writeFile(dstPath, markdown)
    linkSettingsAndCommands(dstPath, pagesRepoDirPath.joinpath("pages"), vscodeLtexRepoDirPath)



def updateCommands(vscodeLtexRepoDirPath: pathlib.Path, pagesRepoDirPath: pathlib.Path) -> None:
  packageJsonPath = vscodeLtexRepoDirPath.joinpath("package.json")
  packageJson = json.loads(common.readFile(packageJsonPath))

  nlsLanguages = getNlsLanguages(vscodeLtexRepoDirPath)
  languageLinks = ", ".join((f"[{languageName}](commands-{languageCode}.html)"
        if languageCode != "en" else "[English](commands.html)")
      for languageCode, languageName, _ in nlsLanguages)

  for languageCode, _, packageNlsJsonPath in nlsLanguages:
    pageNameSuffix = (f"-{languageCode}" if languageCode != "en" else "")

    packageNlsJson = json.loads(common.readFile(packageNlsJsonPath))
    packageNlsJson.update(i18nStrings[languageCode])

    commandsJson = packageJson["contributes"]["commands"]
    commandsMarkdown = [formatCommand(x, packageNlsJson) for x in commandsJson]
    markdown = """---{}
title: "Commands"
permalink: "/vscode-ltex-plus/commands{}.html"
sidebar: "sidebar"
---

Change language of this page: {}

<!-- ltex: language={} -->

{}

""".format(licenseHeader, pageNameSuffix, languageLinks, getLtLanguageCode(languageCode),
        packageNlsJson["commandIntroduction"],)
    markdown += "\n".join(x for x in commandsMarkdown if x is not None)
    markdown = re.sub("\n\n+", "\n\n", markdown)

    dstPath = pagesRepoDirPath.joinpath("pages", "vscode-ltex-plus", f"commands{pageNameSuffix}.md")
    common.writeFile(dstPath, markdown)
    linkSettingsAndCommands(dstPath, pagesRepoDirPath.joinpath("pages"), vscodeLtexRepoDirPath)



def copyMarkdown(srcPathOrMarkdown: Union[pathlib.Path, str], dstPath: pathlib.Path, metaData: str,
      vscodeLtexRepoDirPath: pathlib.Path, pagesRepoDirPath: pathlib.Path) -> None:
  if isinstance(srcPathOrMarkdown, str):
    markdown = srcPathOrMarkdown
  else:
    markdown = common.readFile(srcPathOrMarkdown)

  lines = markdown.split("\n")
  i = next(i for i, line in enumerate(lines) if line.startswith("#"))
  markdown = metaData + "\n".join(lines[i+1:])
  markdown = markdown.replace("L<sup>A</sup>T<sub>E</sub>X", "LaTeX").replace(
      "T<sub>E</sub>X", "TeX")
  common.writeFile(dstPath, markdown)
  linkSettingsAndCommands(dstPath, pagesRepoDirPath.joinpath("pages"), vscodeLtexRepoDirPath)



def updateCodeOfConduct(vscodeRepoDirPath: pathlib.Path, pagesRepoDirPath: pathlib.Path) -> None:
  copyMarkdown(vscodeRepoDirPath.joinpath("CODE_OF_CONDUCT.md"),
      pagesRepoDirPath.joinpath("pages", "code-of-conduct.md"), """---
title: "Code of Conduct"
permalink: "/code-of-conduct.html"
sidebar: "sidebar"
---
""", vscodeRepoDirPath, pagesRepoDirPath)



def updateChangelog(sourceRepoDirPath: pathlib.Path, sourceRepoName: str,
      vscodeRepoDirPath: pathlib.Path, pagesRepoDirPath: pathlib.Path) -> None:
  changelogFilePath = sourceRepoDirPath.joinpath("changelog.xml")

  if common.isRemotePath(sourceRepoDirPath):
    remoteHostName, remoteSourceRepoDirPath = common.getRemotePathParts(sourceRepoDirPath)
    convertChangelogArguments = ["ssh", remoteHostName, "python",
        str(remoteSourceRepoDirPath.joinpath("tools", "convertChangelog.py")),
        "--xml-file", str(common.getRemotePathParts(changelogFilePath)[1])]
  else:
    convertPath: Callable[[pathlib.Path], str] = (
        lambda path: re.sub(r"^\\([a-z])\\", r"\1:\\", str(path)))
    convertChangelogArguments = ["python",
        convertPath(sourceRepoDirPath.joinpath("tools", "convertChangelog.py")),
        "--xml-file", convertPath(changelogFilePath)]

  process = subprocess.run(convertChangelogArguments, stdout=subprocess.PIPE)
  markdown = process.stdout.decode().replace("\r\n", "\n")

  copyMarkdown(markdown,
      pagesRepoDirPath.joinpath("pages", sourceRepoName, "changelog.md"), """---{}
title: "Changelog"
permalink: "/{}/changelog.html"
sidebar: "sidebar"
toc: false
---
""".format(licenseHeader, sourceRepoName), vscodeRepoDirPath, pagesRepoDirPath)



def updateContributing(sourceRepoDirPath: pathlib.Path, sourceRepoName: str,
      vscodeRepoDirPath: pathlib.Path, pagesRepoDirPath: pathlib.Path) -> None:
  copyMarkdown(sourceRepoDirPath.joinpath("CONTRIBUTING.md"),
      pagesRepoDirPath.joinpath("pages", sourceRepoName, "contributing.md"), """---{}
title: "Contributing"
permalink: "/{}/contributing.html"
sidebar: "sidebar"
---
""".format(licenseHeader, sourceRepoName), vscodeRepoDirPath, pagesRepoDirPath)



def main() -> None:
  parser = argparse.ArgumentParser(description="Update Markdown according to vscode-ltex-plus  repo")
  parser.add_argument("--vscode-ltex-repo", default="../vscode-ltex-plus",
      type=pathlib.Path, help="Path to vscode-ltex-plus repo")
  parser.add_argument("--ltex-ls-repo", default="../ltex-ls-plus",
      type=pathlib.Path, help="Path to ltex-ls-plus repo")
  args = parser.parse_args()

  vscodeLtexRepoDirPath = args.vscode_ltex_repo
  ltexLsRepoDirPath = args.ltex_ls_repo

  pagesRepoDirPath = pathlib.Path(__file__).parent.parent
  updateSupportedLanguages(vscodeLtexRepoDirPath, pagesRepoDirPath)
  updateSettings(vscodeLtexRepoDirPath, pagesRepoDirPath)
  updateCommands(vscodeLtexRepoDirPath, pagesRepoDirPath)
  updateCodeOfConduct(vscodeLtexRepoDirPath, pagesRepoDirPath)

  for sourceRepoName in ["vscode-ltex-plus", "ltex-ls-plus"]:
    sourceRepoDirPath = (vscodeLtexRepoDirPath if sourceRepoName == "vscode-ltex-plus" else
        ltexLsRepoDirPath)
    updateChangelog(sourceRepoDirPath, sourceRepoName, vscodeLtexRepoDirPath, pagesRepoDirPath)
    updateContributing(sourceRepoDirPath, sourceRepoName, vscodeLtexRepoDirPath, pagesRepoDirPath)



if __name__ == "__main__":
  main()
