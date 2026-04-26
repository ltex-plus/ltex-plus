---
# Copyright (C) 2019-2025
# Julian Valentin, Daniel Spitzer, LTeX+ Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Supported Languages"
permalink: "/supported-languages.html"
sidebar: "sidebar"
---

## Code Languages

### Markup Languages

LTeX+ supports checking grammar and spelling in the following markup languages. These markup languages are exactly those languages for which LTeX+ is enabled by default, so no further configuration is necessary. Change [`ltex.enabled`](settings.html#ltexenabled) to manually configure for which languages LTeX+ is enabled/disabled.

| Language | Language ID | LTeX+ support |
| -------- | ----------- | ------------ |
| BibTeX | `bibtex`&nbsp;∗ | Basic |
| ConTeXt | `context`&nbsp;∗ | Advanced |
| LaTeX | `latex`&nbsp;∗ | Extensive |
| Markdown | `markdown` | Advanced |
| MDX | `mdx`&nbsp;∗ | Basic |
| Typst | `typst`&nbsp;∗ | Good |
| AsciiDoc | `asciidoc`&nbsp;∗ | Basic |
| Neorg | `neorg`&nbsp;∗ | Basic |
| Org | `org`&nbsp;∗ | Good |
| Quarto | `quarto`&nbsp;∗ | Basic |
| reStructuredText | `restructuredtext`&nbsp;∗ | Good |
| R Sweave | `rsweave`&nbsp;∗ | Good |
| XHTML | `html` | Basic |

“[Language ID](https://code.visualstudio.com/docs/languages/identifiers)” denotes the code language identifier that has to be used when changing [`ltex.enabled`](settings.html#ltexenabled). An asterisk (∗) indicates that the language is not supported by VS Code out-of-the-box, and an additional extension that adds support for the language has to be installed in order for vscode-ltex-plus to work (e.g., [LaTeX Workshop Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) for LaTeX).

### Programming Languages

In addition to markup languages, LTeX+ can also check comments in many popular programming languages. This is disabled by default, as LTeX+ is currently not able to reliably detect if a comment is source code that has been commented out. To enable checking for programming languages, add the respective code language identifier to [`ltex.enabled`](settings.html#ltexenabled).

A line comment is only checked if its start delimiter is only preceded by whitespace on the same line and followed by a whitespace character. A block comment is only checked if its start delimiter is only preceded by whitespace on the same line and followed by a whitespace character, and its end delimiter is preceded by a whitespace character and only followed by whitespace on the same line. These rules try to minimize the amount of false positives, accounting for both comment delimiters inside code (e.g., strings) and commented out code. If you comment out code that should not be checked by LTeX+, don't insert whitespace after the start delimiter.

LTeX+ assumes comments are written in Markdown, except for Python, where reStructuredText is used.

There is a list of all supported programming languages below. Again, an asterisk (∗) indicates that the language is not supported by VS Code out-of-the-box, and an additional extension that adds support for the language has to be installed in order for vscode-ltex-plus to work (e.g., [MATLAB Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Gimly81.matlab) for MATLAB).

Bash/Shell&nbsp;Script&nbsp;(`shellscript`),
C&nbsp;(`c`),
C#&nbsp;(`csharp`),
C++&nbsp;(`cpp`),
Clojure&nbsp;(`clojure`),
CoffeeScript&nbsp;(`coffeescript`),
Dart&nbsp;(`dart`),
Elixir&nbsp;(`elixir`&nbsp;∗),
Elm&nbsp;(`elm`&nbsp;∗),
Erlang&nbsp;(`erlang`&nbsp;∗),
F#&nbsp;(`fsharp`),
FORTRAN&nbsp;(`fortran-modern`&nbsp;∗),
Go&nbsp;(`go`),
Groovy&nbsp;(`groovy`),
Haskell&nbsp;(`haskell`&nbsp;∗),
Java&nbsp;(`java`),
JavaScript&nbsp;(`javascript`),
JavaScript&nbsp;React&nbsp;(`javascriptreact`),
Julia&nbsp;(`julia`),
Kotlin&nbsp;(`kotlin`&nbsp;∗),
Lisp&nbsp;(`lisp`&nbsp;∗),
Lua&nbsp;(`lua`),
MATLAB&nbsp;(`matlab`&nbsp;∗),
Perl&nbsp;(`perl`),
Perl&nbsp;6&nbsp;(`perl6`),
PHP&nbsp;(`php`),
PowerShell&nbsp;(`powershell`),
Puppet&nbsp;(`puppet`&nbsp;∗),
Python&nbsp;(`python`),
R&nbsp;(`r`),
Ruby&nbsp;(`ruby`),
Rust&nbsp;(`rust`),
Scala&nbsp;(`scala`&nbsp;∗),
SQL&nbsp;(`sql`),
Swift&nbsp;(`swift`),
TypeScript&nbsp;(`typescript`),
TypeScript&nbsp;React&nbsp;(`typescriptreact`),
Verilog&nbsp;(`verilog`&nbsp;∗),
Visual&nbsp;Basic&nbsp;(`vb`)

## Natural Languages

Apart from code languages like markup and programming languages, there is also the notion of natural languages. Natural languages are the languages in which the contents of documents can be written, like English or German.

By default, LTeX+ uses American English (`en-US`) when checking documents. If your documents are written in a different language, change [`ltex.language`](settings.html#ltexlanguage) to the BCP-47 code that best matches your text (e.g., `en-US`, `fr-FR`, `de-DE`, `ca-ES-valencia`). There are also ways to change the checking language in the middle of documents. For details, see the questions [“How can I check multiple languages at once?”](faq.html#how-can-i-check-multiple-languages-at-once) and [“Why does LTeX+ check in a different language than expected?”](faq.html#why-does-ltex-check-in-a-different-language-than-expected) in the FAQ.

The natural languages supported by LTeX+ are identical to those supported by [LanguageTool](https://languagetool.org/), which is LTeX+'s backend. Therefore, the supported languages (and how well they are supported) might change if a new LTeX+ version comes with an updated version of LanguageTool.

The modern fully-spelled codes shown below require ltex-ls-plus 18.7.x or newer (see [ltex-ls-plus#150](https://github.com/ltex-plus/ltex-ls-plus/pull/150)). Earlier releases only accepted the legacy bare codes such as `fr`, `it`, `de`, or `en`; for a best-effort description of how language codes were handled on those versions, see [Language Codes in Older Versions](language-code-legacy.html). Current versions still accept those legacy codes for backward compatibility but they are no longer advertised below and should not be used in new configurations.

Two annotations may appear in the list below. `(also accepts: <code>)` marks a LanguageTool alias — an alternative spelling of a canonical entry that resolves to the same checker (for example, `no` is treated as `nb`, so the two codes are interchangeable). `(only on api.languagetoolplus.com)` marks a code recognized only by LanguageTool's own hosted API. The bundled checker and self-hosted instances of the open-source LanguageTool server share the same code set and do not recognize these codes — even when reached via [`ltex.languageToolHttpServerUri`](settings.html#ltexlanguagetoolhttpserveruri).

The following languages are currently supported:

<!-- ltex-natural-languages-begin -->

Arabic&nbsp;(`ar`), Asturian&nbsp;(`ast-ES`), Belarusian&nbsp;(`be-BY`), Breton&nbsp;(`br-FR`), Catalan&nbsp;(`ca-ES`), Catalan (Balearic)&nbsp;(`ca-ES-balear`), Catalan (Valencian)&nbsp;(`ca-ES-valencia`), Chinese&nbsp;(`zh-CN`), Crimean Tatar&nbsp;(`crh-UA`), Danish&nbsp;(`da-DK`), Dutch&nbsp;(`nl-NL`), Dutch (Belgium)&nbsp;(`nl-BE`), English (Australian)&nbsp;(`en-AU`), English (Canadian)&nbsp;(`en-CA`), English (GB)&nbsp;(`en-GB`), English (New Zealand)&nbsp;(`en-NZ`), English (South African)&nbsp;(`en-ZA`), English (US)&nbsp;(`en-US`), Esperanto&nbsp;(`eo`), French&nbsp;(`fr-FR`), French (Belgium)&nbsp;(`fr-BE`), French (Canada)&nbsp;(`fr-CA`), French (Switzerland)&nbsp;(`fr-CH`), Galician&nbsp;(`gl-ES`), German (Austria)&nbsp;(`de-AT`), German (Germany)&nbsp;(`de-DE`), German (Swiss)&nbsp;(`de-CH`), Greek&nbsp;(`el-GR`), Irish&nbsp;(`ga-IE`), Italian&nbsp;(`it-IT`), Japanese&nbsp;(`ja-JP`), Khmer&nbsp;(`km-KH`), Norwegian (Bokmål)&nbsp;(`nb`, also accepts: `no`, only on api.languagetoolplus.com), Persian&nbsp;(`fa-IR`), Polish&nbsp;(`pl-PL`), Portuguese (Angola preAO)&nbsp;(`pt-AO`), Portuguese (Brazil)&nbsp;(`pt-BR`), Portuguese (Moçambique preAO)&nbsp;(`pt-MZ`), Portuguese (Portugal)&nbsp;(`pt-PT`), Romanian&nbsp;(`ro-RO`), Russian&nbsp;(`ru-RU`), Simple German&nbsp;(`de-DE-x-simple-language`, also accepts: `de-DE-x-simple-language-DE`), Slovak&nbsp;(`sk-SK`), Slovenian&nbsp;(`sl-SI`), Spanish&nbsp;(`es-ES`), Spanish (voseo)&nbsp;(`es-AR`), Swedish&nbsp;(`sv-SE`), Tagalog&nbsp;(`tl-PH`), Tamil&nbsp;(`ta-IN`), Ukrainian&nbsp;(`uk-UA`)

<!-- ltex-natural-languages-end -->
