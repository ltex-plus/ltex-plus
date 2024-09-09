---
# Copyright (C) 2019-2021 Julian Valentin, LTeX+ Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "LTeX+ – Grammar/Spell Checker Using LanguageTool with Support for LaTeX, Markdown, and Others"
permalink: "/index.html"
sidebar: "sidebar"
toc: false
---

**LTeX+** provides offline grammar checking of various markup languages using [LanguageTool&nbsp;(LT)](https://languagetool.org/). LTeX+ can be used standalone as a command-line tool, as a language server using the Language Server Protocol (LSP), or directly in various editors using extensions.

LTeX+ currently supports BibTeX, ConTeXt, LaTeX, Markdown, Org, reStructuredText, R Sweave, and XHTML documents.

The difference to regular spell checkers is that LTeX+ not only detects spelling errors, but also many grammar and stylistic errors such as:

- `This is an mistake.`
- `The bananas is tasty.`
- `We look forward to welcome you.`
- `Are human beings any different than animals?`

A classic use case of LTeX+ is checking scientific LaTeX papers, but why not check your next blog post, book chapter, or long e-mail before you send it to someone else?

LTeX+ is a successor/fork of the abandoned [LTeX Extension for VS Code](https://github.com/valentjn/vscode-ltex) by Julian Valentin and [LanguageTool for Visual Studio Code extension](https://github.com/adamvoss/vscode-languagetool) by Adam Voss<sup>†</sup>.

Be aware that this documentation was also forked from [LTeX](https://github.com/valentjn/ltex) and the terms LTeX, LTeX+ are mixed up. Feel free to submit a Pull Request if you notice a mistake in this documentation.

<div style="margin-bottom:30px;"></div>

## Features

![Grammar/Spell Checker for VS Code with LanguageTool and LaTeX Support](https://github.com/ltex-plus/vscode-ltex-plus/raw/release/img/banner-ltex.png)

- **Supported markup languages:** BibTeX, ConTeXt, LaTeX, Markdown, Org, reStructuredText, R Sweave, XHTML
- Comes with **everything included,** no need to install Java or LanguageTool
- **Offline checking:** Does not upload anything to the internet
- Supports **over 20 languages:** English, French, German, Dutch, Chinese, Russian, etc.
- **Issue highlighting** with hover description
- **Replacement suggestions** via quick fixes
- **User dictionaries**
- **Multilingual support** with babel commands or magic comments
- Possibility to use **external LanguageTool servers**
- **Extensive documentation**

<div style="margin-bottom:30px;"></div>
