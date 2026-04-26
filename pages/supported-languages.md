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

By default, LTeX+ uses American English (`en-US`) when checking documents. If your documents are written in a different language, change [`ltex.language`](settings.html#ltexlanguage). In addition, there are ways to change the checking language in the middle of documents. For details, see the questions [“How can I check multiple languages at once?”](faq.html#how-can-i-check-multiple-languages-at-once) and [“Why does LTeX+ check in a different language than expected?”](faq.html#why-does-ltex-check-in-a-different-language-than-expected) in the FAQ.

Most users want **both** spell-check and grammar check, so understanding this next distinction matters. LanguageTool's language codes look like BCP-47 tags (`en`, `en-US`, `fr`, `fr-FR`, …) but they do not behave uniformly, and the code you choose decides whether you get both or only grammar:

* For **English, German, and Portuguese**, the bare codes `en`, `de`, and `pt` are grammar-only umbrella classes — they carry no spelling dictionary. To also get spell-check you must pick a regional variant: `en-US`, `en-GB`, `de-DE`, `de-AT`, `pt-BR`, `pt-PT`, and so on. This is the single most common source of confusion.
* For **most other languages** (`es`, `fr`, `it`, `nl`, `ru`, `uk`, and the rest of the list below), the bare code is already a full spell + grammar checker. You can write `fr` or `fr-FR` interchangeably and get the same coverage; variants like `es-AR` (Argentinian voseo) or `nl-BE` (Belgian Dutch) are optional regional refinements (different vocabulary, regional spellings, or region-specific grammar).
* A few languages (**Catalan**) have no bare form at all: `ca-ES` is the canonical code, with further variants `ca-ES-valencia` and `ca-ES-balear`.

Rule of thumb: if a language appears more than once in the list below (e.g. both `en` and `en-US`), the bare form is grammar-only; prefer the variant.

The natural languages supported by LTeX+ are identical to those supported by [LanguageTool](https://languagetool.org/), which is LTeX+'s backend. Therefore, the supported languages (and how well they are supported) might change if a new LTeX+ version comes with an updated version of LanguageTool.

Two annotations appear in the list below. `(also accepts: <code>)` marks a LanguageTool alias — an alternative spelling of a canonical entry that resolves to the same checker (for example, `fr-FR` is treated as `fr`, so the two codes are interchangeable). `(remote-only)` marks a code accepted only when checking against a remote LanguageTool server, hosted or self-hosted via [`ltex.languageToolHttpServerUri`](settings.html#ltexlanguagetoolhttpserveruri), not by the bundled checker.

The following languages are currently supported:

<!-- ltex-natural-languages-begin -->

Arabic&nbsp;(`ar`), Asturian&nbsp;(`ast-ES`), Belarusian&nbsp;(`be-BY`), Breton&nbsp;(`br-FR`), Catalan&nbsp;(`ca-ES`), Catalan (Balearic)&nbsp;(`ca-ES-balear`), Catalan (Valencian)&nbsp;(`ca-ES-valencia`), Chinese&nbsp;(`zh-CN`), Crimean Tatar&nbsp;(`crh-UA`), Danish&nbsp;(`da-DK`), Dutch&nbsp;(`nl`, also accepts: `nl-NL`), Dutch (Belgium)&nbsp;(`nl-BE`), English&nbsp;(`en`), English (Australian)&nbsp;(`en-AU`), English (Canadian)&nbsp;(`en-CA`), English (GB)&nbsp;(`en-GB`), English (New Zealand)&nbsp;(`en-NZ`), English (South African)&nbsp;(`en-ZA`), English (US)&nbsp;(`en-US`), Esperanto&nbsp;(`eo`), French&nbsp;(`fr`, also accepts: `fr-FR`), French (Belgium)&nbsp;(`fr-BE`), French (Canada)&nbsp;(`fr-CA`), French (Switzerland)&nbsp;(`fr-CH`), Galician&nbsp;(`gl-ES`), German&nbsp;(`de`, also accepts: `de-LU`), German (Austria)&nbsp;(`de-AT`), German (Germany)&nbsp;(`de-DE`), German (Swiss)&nbsp;(`de-CH`), Greek&nbsp;(`el-GR`), Irish&nbsp;(`ga-IE`), Italian&nbsp;(`it`, also accepts: `it-IT`), Japanese&nbsp;(`ja-JP`), Khmer&nbsp;(`km-KH`), Norwegian (Bokmål)&nbsp;(`nb`, also accepts: `no`, remote-only), Persian&nbsp;(`fa`, also accepts: `fa-IR`), Polish&nbsp;(`pl-PL`), Portuguese&nbsp;(`pt`), Portuguese (Angola preAO)&nbsp;(`pt-AO`), Portuguese (Brazil)&nbsp;(`pt-BR`), Portuguese (Moçambique preAO)&nbsp;(`pt-MZ`), Portuguese (Portugal)&nbsp;(`pt-PT`), Romanian&nbsp;(`ro-RO`), Russian&nbsp;(`ru-RU`), Simple German&nbsp;(`de-DE-x-simple-language`, also accepts: `de-DE-x-simple-language-DE`), Slovak&nbsp;(`sk-SK`), Slovenian&nbsp;(`sl-SI`), Spanish&nbsp;(`es`, also accepts: `es-ES`), Spanish (voseo)&nbsp;(`es-AR`), Swedish&nbsp;(`sv`, also accepts: `sv-SE`), Tagalog&nbsp;(`tl-PH`), Tamil&nbsp;(`ta-IN`), Ukrainian&nbsp;(`uk-UA`)

<!-- ltex-natural-languages-end -->
