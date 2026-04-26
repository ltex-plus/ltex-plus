---
# Copyright (C) 2019-2025
# Julian Valentin, Daniel Spitzer, LTeX+ Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Settings"
permalink: "/settings-de.html"
sidebar: "sidebar"
---

Change language of this page: [English](settings.html), [German](settings-de.html)

<!-- ltex: language=de-DE -->

## `ltex.enabled`

Steuert, ob die Erweiterung aktiviert ist. Erlaubt die Deaktivierung von LanguageTool für bestimmte Arbeitsbereiche oder für bestimmte Code-Sprachmodi (d. h. Dateitypen).

Sie können entweder einen Boolean-Wert angeben, der bestimmt, ob LTeX+ für alle unterstützten Auszeichnungssprachen aktiviert oder für alle deaktiviert wird, oder eine Liste von [Code-Sprachbezeichnern](https://code.visualstudio.com/docs/languages/identifiers), für die LTeX+ aktiviert werden soll (beachten Sie, dass Erweiterungen zusätzliche Code-Sprachbezeichner definieren können).

Alle unterstützten Auszeichnungssprachen sind in der Voreinstellung dieser Einstellung aufgelistet. Zusätzlich kann LTeX+ Kommentare in vielen populären Programmiersprachen wie C++ oder Java überprüfen, wenn Sie die entsprechenden Code-Sprachbezeichner zu dieser Einstellung hinzufügen. Wenn Sie einen nicht-unterstützten Code-Sprachmodus hinzufügen, dann wird LTeX+ entsprechende Dateien als reinen Text ohne Parsen überprüfen.

<!-- ltex-client-specific-de-begin -->

Die Aktivierungsereignisse werden von dieser Einstellung nicht berührt. Das heißt, dass die Erweiterung aktiviert wird, sobald eine Datei mit einem unterstützten Code-Sprachmodus geöffnet wird. Falls Sie Dateien mit nicht-unterstützten Codi-Sprachmodi überprüfen wollen, müssen Sie eventuell die Erweiterung explizit mithilfe des Befehls [LTeX: Aktiviere Erweiterung`](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/commands-de.html#ltex-aktiviere-erweiterung) aktivieren.

Nach Änderungen muss LTeX+ neugestartet werden.

<!-- ltex-client-specific-end -->

*Typ:* `boolean` oder `array`

*Beispiele:*

- `true`
- `false`
- `["latex", "markdown"]`

*Voreinstellung:* `["bibtex", "context", "context.tex", "html", "latex", "markdown", "mdx", "typst", "asciidoc", "neorg", "org", "quarto", "restructuredtext", "rsweave"]`

*Vollständige Beschreibung des Typs:*

Einer der folgenden Typen:

- Skalar vom Typ `boolean`
- Array, bei dem jeder Eintrag folgenden Typ hat:

  - Skalar vom Typ `string`

## `ltex.language`

Die Sprache (z. B. `"en-US"`), mit der LanguageTool auf Fehler suchen soll.

Die meisten Benutzer wollen **sowohl** Rechtschreib- als auch Grammatikprüfung, weshalb die folgende Unterscheidung wichtig ist. LanguageTools Sprachcodes sehen wie BCP-47-Tags aus (`"en"`, `"en-US"`, `"fr"`, `"fr-FR"`, …), verhalten sich aber nicht einheitlich, und der Code, den Sie wählen, entscheidet, ob Sie beides bekommen oder nur Grammatik:

* Bei **Englisch, Deutsch und Portugiesisch** sind die nackten Codes `"en"`, `"de"`, `"pt"` reine Grammatik-Sammelklassen — sie enthalten kein Rechtschreibwörterbuch. Um auch Rechtschreibprüfung zu bekommen, müssen Sie eine regionale Variante wählen: `"en-US"`, `"en-GB"`, `"de-DE"`, `"de-AT"`, `"pt-BR"`, `"pt-PT"` und so weiter. Dies ist die mit Abstand häufigste Verwechslungsquelle.
* Bei **den meisten anderen Sprachen** (`"es"`, `"fr"`, `"it"`, `"nl"`, `"ru"`, `"uk"` und dem Rest der Liste unten) ist der nackte Code bereits ein vollständiger Rechtschreib- und Grammatikprüfer. Sie können `"fr"` oder `"fr-FR"` austauschbar schreiben und erhalten die gleiche Abdeckung; Varianten wie `"es-AR"` (argentinischer Voseo) oder `"nl-BE"` (belgisches Niederländisch) sind optionale regionale Grammatik-Disambiguierer und keine Voraussetzung für die Rechtschreibprüfung.
* Einige wenige Sprachen (**Katalanisch**) haben gar keine nackte Form: `"ca-ES"` ist der kanonische Code, mit weiteren Varianten `"ca-ES-valencia"` und `"ca-ES-balear"`.

Faustregel: Erscheint eine Sprache mehr als einmal in der Liste unten (z. B. sowohl `"en"` als auch `"en-US"`), ist die nackte Form grammatik-only; wählen Sie die Variante.

Wenn Sie den Sprachcode `"auto"` benutzen, dann wird LTeX+ versuchen, die Sprache des Dokuments zu erkennen. Dies wird nicht empfohlen, da nur generische Sprachen wie `"en"` oder `"de"` erkannt werden und eventuell keine Rechtschreibfehler gemeldet werden. Bei manchen generischen Sprachcodes wie `"es"` (Spanisch) werden Rechtschreibfehler gemeldet, obwohl die Sprachcodes generisch sind.

In der Liste unten können zwei Anmerkungen erscheinen. `(also accepts: "<code>")` markiert einen LanguageTool-Alias — eine alternative Schreibweise eines kanonischen Eintrags, die zum gleichen Prüfer auflöst (zum Beispiel wird `"fr-FR"` wie `"fr"` behandelt, die beiden Codes sind also austauschbar). `(only on api.languagetoolplus.com)` markiert einen Code, der nur von LanguageTools eigener gehosteter API erkannt wird. Der mitgelieferte Prüfer und selbst gehostete Instanzen des Open-Source-LanguageTool-Servers verwenden denselben Code-Satz und erkennen diese Codes nicht — auch nicht, wenn sie über [`ltex.languageToolHttpServerUri`](settings-de.html#ltexlanguagetoolhttpserveruri) erreichbar sind.

*Typ:* `string`

*Mögliche Werte:*

- `"auto"`: Automatische Spracherkennung (nicht empfohlen)
- `"ar"`: Arabic
- `"ast-ES"`: Asturian
- `"be-BY"`: Belarusian
- `"br-FR"`: Breton
- `"ca-ES"`: Catalan
- `"ca-ES-balear"`: Catalan (Balearic)
- `"ca-ES-valencia"`: Catalan (Valencian)
- `"crh-UA"`: Crimean Tatar
- `"da-DK"`: Danish
- `"de"`: German (also accepts: `"de-LU"`)
- `"de-AT"`: German (Austria)
- `"de-CH"`: German (Swiss)
- `"de-DE"`: German (Germany)
- `"de-DE-x-simple-language"`: Simple German (also accepts: `"de-DE-x-simple-language-DE"`)
- `"el-GR"`: Greek
- `"en"`: English
- `"en-AU"`: English (Australian)
- `"en-CA"`: English (Canadian)
- `"en-GB"`: English (GB)
- `"en-NZ"`: English (New Zealand)
- `"en-US"`: English (US)
- `"en-ZA"`: English (South African)
- `"eo"`: Esperanto
- `"es"`: Spanish (also accepts: `"es-ES"`)
- `"es-AR"`: Spanish (voseo)
- `"fa"`: Persian (also accepts: `"fa-IR"`)
- `"fr"`: French (also accepts: `"fr-FR"`)
- `"fr-BE"`: French (Belgium)
- `"fr-CA"`: French (Canada)
- `"fr-CH"`: French (Switzerland)
- `"ga-IE"`: Irish
- `"gl-ES"`: Galician
- `"it"`: Italian (also accepts: `"it-IT"`)
- `"ja-JP"`: Japanese
- `"km-KH"`: Khmer
- `"nb"`: Norwegian (Bokmål) (also accepts: `"no"`; only on api.languagetoolplus.com)
- `"nl"`: Dutch (also accepts: `"nl-NL"`)
- `"nl-BE"`: Dutch (Belgium)
- `"pl-PL"`: Polish
- `"pt"`: Portuguese
- `"pt-AO"`: Portuguese (Angola preAO)
- `"pt-BR"`: Portuguese (Brazil)
- `"pt-MZ"`: Portuguese (Moçambique preAO)
- `"pt-PT"`: Portuguese (Portugal)
- `"ro-RO"`: Romanian
- `"ru-RU"`: Russian
- `"sk-SK"`: Slovak
- `"sl-SI"`: Slovenian
- `"sv"`: Swedish (also accepts: `"sv-SE"`)
- `"ta-IN"`: Tamil
- `"tl-PH"`: Tagalog
- `"uk-UA"`: Ukrainian
- `"zh-CN"`: Chinese

*Voreinstellung:* `"en-US"`

## `ltex.dictionary`

Listen von zusätzlichen Wörtern, die nicht als Schreibfehler gewertet werden sollen.

Diese Einstellung ist sprachabhängig. Benutzen Sie daher ein Objekt der Form `{"<SPRACHE1>": ["<WORT1>", "<WORT2>", ...], "<SPRACHE2>": ["<WORT1>", "<WORT2>", ...], ...}`, wobei `<SPRACHE>` den Sprachcode in [`ltex.language`](settings-de.html#ltexlanguage) bezeichnet.

<!-- ltex-client-specific-de-begin -->

Diese Einstellung ist eine [Multi-Scope-Einstellung](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#multi-scope-settings).

Diese Einstellung unterstützt [externe Dateien](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#external-setting-files).

<!-- ltex-client-specific-end -->

Standardmäßig werden keine zusätzlichen Schreibfehler ignoriert.

*Typ:* `object`

*Beispiel:* `{"en-US": ["adaptivity", "precomputed", "subproblem"], "de-DE": ["B-Splines", ":/path/to/externalFile.txt"]}`

*Voreinstellung:* `{}`

*Vollständige Beschreibung des Typs:*

Objekt mit Sprachcode als Eigenschaftsname (siehe [`ltex.language`](settings-de.html#ltexlanguage) für gültige Werte), wobei die Werte jeder Eigenschaft folgenden Typ hat:

- Array, bei dem jeder Eintrag folgenden Typ hat:

  - Skalar vom Typ `string`

## `ltex.disabledRules`

Listen von zusätzlichen Regeln, die deaktiviert werden sollen (falls standardmäßig durch LanguageTool aktiviert).

Diese Einstellung ist sprachabhängig. Benutzen Sie daher ein Objekt der Form `{"<SPRACHE1>": ["<REGEL1>", "<REGEL2>", ...], "<SPRACHE2>": ["<REGEL1>", "<REGEL2>", ...], ...}`, wobei `<SPRACHE>` den Sprachcode in [`ltex.language`](settings-de.html#ltexlanguage) und `<REGEL>` die ID der LanguageTool-Regel bezeichnet.

<!-- ltex-client-specific-de-begin -->

Diese Einstellung ist eine [Multi-Scope-Einstellung](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#multi-scope-settings).

Diese Einstellung unterstützt [externe Dateien](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#external-setting-files).

<!-- ltex-client-specific-end -->

Standardmäßig werden keine zusätzlichen Regeln deaktiviert.

*Typ:* `object`

*Beispiel:* `{"en-US": ["EN_QUOTES", "UPPERCASE_SENTENCE_START", ":/path/to/externalFile.txt"]}`

*Voreinstellung:* `{}`

*Vollständige Beschreibung des Typs:*

Objekt mit Sprachcode als Eigenschaftsname (siehe [`ltex.language`](settings-de.html#ltexlanguage) für gültige Werte), wobei die Werte jeder Eigenschaft folgenden Typ hat:

- Array, bei dem jeder Eintrag folgenden Typ hat:

  - Skalar vom Typ `string`

## `ltex.enabledRules`

Listen von zusätzlichen Regeln, die aktiviert werden sollen (falls standardmäßig durch LanguageTool deaktiviert).

Diese Einstellung ist sprachabhängig. Benutzen Sie daher ein Objekt der Form `{"<SPRACHE1>": ["<REGEL1>", "<REGEL2>", ...], "<SPRACHE2>": ["<REGEL1>", "<REGEL2>", ...], ...}`, wobei `<SPRACHE>` den Sprachcode in [`ltex.language`](settings-de.html#ltexlanguage) und `<REGEL>` die ID der LanguageTool-Regel bezeichnet.

<!-- ltex-client-specific-de-begin -->

Diese Einstellung ist eine [Multi-Scope-Einstellung](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#multi-scope-settings).

Diese Einstellung unterstützt [externe Dateien](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#external-setting-files).

<!-- ltex-client-specific-end -->

Standardmäßig werden keine zusätzlichen Regeln aktiviert.

*Typ:* `object`

*Beispiel:* `{"en-GB": ["PASSIVE_VOICE", "OXFORD_SPELLING_NOUNS", ":/path/to/externalFile.txt"]}`

*Voreinstellung:* `{}`

*Vollständige Beschreibung des Typs:*

Objekt mit Sprachcode als Eigenschaftsname (siehe [`ltex.language`](settings-de.html#ltexlanguage) für gültige Werte), wobei die Werte jeder Eigenschaft folgenden Typ hat:

- Array, bei dem jeder Eintrag folgenden Typ hat:

  - Skalar vom Typ `string`

## `ltex.hiddenFalsePositives`

Listen von falschen Fehlern, die verborgen werden sollen (indem alle Fehler einer bestimmten Regel in einem bestimmten Satz verborgen werden).

Diese Einstellung ist sprachabhängig. Benutzen Sie daher ein Objekt der Form `{"<SPRACHE1>": ["<JSON1>", "<JSON2>", ...], "<SPRACHE2>": ["<JSON1>", "<JSON2>", ...], ...}`, wobei `<SPRACHE>` den Sprachcode in [`ltex.language`](settings-de.html#ltexlanguage) bezeichnet und `<JSON>` eine JSON-Zeichenfolge ist, die Informationen über die Regel und den Satz enthält.

Obwohl es möglich ist, diese Einstellung manuell zu ändern, ist der bevorzugte Weg, Einträge zu dieser Einstellung hinzuzufügen, die schnelle Problembehebung `Falschen Fehler verbergen`.

Die JSON-Zeichenfolge hat momentan die Form `{"rule": "<REGEL>", "sentence": "<SATZ>"}`, wobei `<REGEL>` die ID der LanguageTool-Regel und `<SATZ>` einen Java-kompatiblen regulären Ausdruck bezeichnet. Alle Vorkommen der gegebenen Regel werden in allen Sätzen (die durch den LanguageTool-Tokenizer bestimmt werden) verborgen, die zum regulären Ausdruck passen. [Siehe die Dokumentation für Details.](https://ltex-plus.github.io/ltex-plus/advanced-usage.html#hiding-false-positives-with-regular-expressions)

<!-- ltex-client-specific-de-begin -->

Diese Einstellung ist eine [Multi-Scope-Einstellung](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#multi-scope-settings).

Diese Einstellung unterstützt [externe Dateien](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#external-setting-files).

<!-- ltex-client-specific-end -->

Die Leistung kann darunter leiden, falls diese Liste sehr lang ist.

*Typ:* `object`

*Beispiel:* `{"en-US": [":/path/to/externalFile.txt"]}`

*Voreinstellung:* `{}`

*Vollständige Beschreibung des Typs:*

Objekt mit Sprachcode als Eigenschaftsname (siehe [`ltex.language`](settings-de.html#ltexlanguage) für gültige Werte), wobei die Werte jeder Eigenschaft folgenden Typ hat:

- Array, bei dem jeder Eintrag folgenden Typ hat:

  - Skalar vom Typ `string`

## `ltex.bibtex.fields`

Liste von BibTeX-Feldern, deren Werte in BibTeX-Dateien auf Fehler überprüft werden sollen.

Diese Einstellung ist ein Objekt mit den Namen der Felder als Schlüssel und Booleans als Werte, wobei `true` heißt, dass der Wert des Feldes überprüft werden soll, und `false` heißt, dass der Wert des Feldes ignoriert werden soll.

Einige gebräuchliche Felder werden bereits ignoriert, selbst, wenn Sie diese Einstellung auf ein leeres Objekt setzen.

*Typ:* `object`

*Beispiel:* `{"maintitle": false, "seealso": true}`

*Voreinstellung:* `{}`

*Vollständige Beschreibung des Typs:*

Objekt mit beliebigen Eigenschaftsnamen, wobei die Werte jeder Eigenschaft folgenden Typ hat:

- Skalar vom Typ `boolean`

## `ltex.latex.commands`

Liste von LaTeX-Befehlen, die vom LaTeX-Parser gesondert behandelt werden sollen, aufgelistet zusammen mit leeren Argumenten (z. B. `"\\ref{}"`, `"\\documentclass[]{}"`).

Diese Einstellung ist ein Objekt mit den Befehlen als Schlüssel und zugehörigen Aktionen als Werte.

<!-- ltex-client-specific-de-begin -->

Falls Sie die `settings.json`-Datei direkt bearbeiten, beachten Sie, dass Sie den Backslash am Anfang durch Ersetzung mit zwei Backslashs escapen müssen. Falls Sie das Einstellungspanel von VS Code benutzen, geben Sie nur ein Backslash ein.

<!-- ltex-client-specific-end -->

Viele gebräuchliche Befehle werden standardmäßig bereits gesondert behandelt, selbst, wenn Sie diese Einstellung auf ein leeres Objekt setzen.

*Typ:* `object`

*Beispiel:* `{"\\label{}": "ignore", "\\documentclass[]{}": "ignore", "\\cite{}": "dummy", "\\cite[]{}": "dummy"}`

*Voreinstellung:* `{}`

*Vollständige Beschreibung des Typs:*

Objekt mit beliebigen Eigenschaftsnamen, wobei die Werte jeder Eigenschaft folgenden Typ hat:

- Einer der folgenden Werte:

  - `"default"`: Der Befehl wird so behandelt, wie unbekannte Befehle standardmäßig behandelt werden: Der Befehlsname an sich wird ignoriert, aber die Befehlsargumente werden nicht ignoriert.
  - `"ignore"`: Der ganze Befehl zusammen mit seinen Argumenten wird ignoriert.
  - `"dummy"`: Der ganze Befehl zusammen mit seinen Argumenten wird durch ein Dummy-Wort ersetzt (d. h. `Dummy0`, `Dummy1` usw.). LTeX+ nutzt diesen Mechanismus intern für Gleichungen, Literaturverweise, Referenzen und ähnliche Konstrukte, die Teil der Satzstruktur sind und für die LanguageTool einen Fehler anzeigen würde, wenn man sie einfach im überprüften Text weglassen würde.
  - `"pluralDummy"`: Der ganze Befehl zusammen mit seinen Argumenten wird durch ein Plural-Dummy-Wort ersetzt (d. h. `Dummies`). Siehe die Beschreibung von `"dummy"`.
  - `"vowelDummy"`: Der ganze Befehl zusammen mit seinen Argumenten wird durch ein Vokal-Dummy-Wort ersetzt (d. h. `Ina`). Siehe die Beschreibung von `"dummy"`.

## `ltex.latex.environments`

Liste von Namen von LaTeX-Umgebungen, die vom LaTeX-Parser gesondert behandelt werden sollen.

Diese Einstellung ist ein Objekt mit den Umgebungsnamen als Schlüssel und zugehörigen Aktionen als Werte.

Manche Umgebungen werden standardmäßig bereits gesondert behandelt, selbst, wenn Sie diese Einstellung auf ein leeres Objekt setzen.

*Typ:* `object`

*Beispiel:* `{"lstlisting": "ignore", "verbatim": "ignore"}`

*Voreinstellung:* `{}`

*Vollständige Beschreibung des Typs:*

Objekt mit beliebigen Eigenschaftsnamen, wobei die Werte jeder Eigenschaft folgenden Typ hat:

- Einer der folgenden Werte:

  - `"default"`: Die Umgebung wird so behandelt, wie unbekannte Umgebungen standardmäßig behandelt werden: Die Argumente der Umgebung werden ignoriert, aber der Inhalt der Umgebung wird nicht ignoriert.
  - `"ignore"`: Die ganze Umgebung zusammen mit ihren Argumenten und ihrem Inhalt wird ignoriert.

## `ltex.markdown.nodes`

Liste von Markdown-Knotentypen, die vom Markdown-Parser gesondert behandelt werden sollen.

Diese Einstellung ist ein Objekt mit den Knotentypen als Schlüssel und zugehörigen Aktionen als Werte.

Der Markdown-Parser erstellt einen AST (abstrakten Syntaxbaum) für das Markdown-Dokument, bei dem alle Blätter den Knotentyp `Text` haben. Sie finden alle möglichen Knotentypen in der [Dokumentation von flexmark-java](https://javadoc.io/static/com.vladsch.flexmark/flexmark/0.62.2/com/vladsch/flexmark/ast/package-summary.html).

Manche gebräuchlichen Knotentypen werden standardmäßig bereits gesondert behandelt, selbst, wenn Sie diese Einstellung auf ein leeres Objekt setzen.

*Typ:* `object`

*Beispiel:* `{"CodeBlock": "ignore", "FencedCodeBlock": "ignore", "AutoLink": "dummy", "Code": "dummy"}`

*Voreinstellung:* `{}`

*Vollständige Beschreibung des Typs:*

Objekt mit beliebigen Eigenschaftsnamen, wobei die Werte jeder Eigenschaft folgenden Typ hat:

- Einer der folgenden Werte:

  - `"default"`: Der Knoten wird nicht gesondert behandelt.
  - `"ignore"`: Der ganze Knoten zusammen mit seinen `Text`-Blättern wird ignoriert.
  - `"dummy"`: Der ganze Knoten zusammen mit seinen `Text`-Blättern wird durch ein Dummy-Wort ersetzt (d. h. `Dummy0`, `Dummy1` usw.). LTeX+ nutzt diesen Mechanismus intern für Gleichungen, Literaturverweise, Referenzen und ähnliche Konstrukte, die Teil der Satzstruktur sind und für die LanguageTool einen Fehler anzeigen würde, wenn man sie einfach im überprüften Text weglassen würde.
  - `"pluralDummy"`: Der ganze Knoten zusammen mit seinen `Text`-Blättern wird durch ein Plural-Dummy-Wort ersetzt (d. h. `Dummies`). Siehe die Beschreibung von `"dummy"`.
  - `"vowelDummy"`: Der ganze Knoten zusammen mit seinen `Text`-Blättern wird durch ein Vokal-Dummy-Wort ersetzt (d. h. `Ina`). Siehe die Beschreibung von `"dummy"`.

## `ltex.configurationTarget`

<!-- ltex-client-specific-de-begin -->

Steuert, welche `settings.json` oder externe Einstellungsdatei ([siehe die Dokumentation](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/setting-scopes-files.html#external-setting-files)) geändert wird, wenn eine der schnellen Problembehebungen verwendet wird.

<!-- ltex-client-specific-end -->

*Typ:* `object`

*Voreinstellung:* `{"dictionary": "workspaceFolderExternalFile", "disabledRules": "workspaceFolderExternalFile", "hiddenFalsePositives": "workspaceFolderExternalFile"}`

*Vollständige Beschreibung des Typs:*

Objekt mit folgenden Eigenschaften:

- `"dictionary"`: Einer der folgenden Werte:

  - `"user"`: Wenn ein Wort zum Wörterbuch hinzugefügt wird, verändere stets die Benutzer-Konfiguration.
  - `"workspace"`: Wenn ein Wort zum Wörterbuch hinzugefügt wird, verändere die Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die Benutzer-Konfiguration.
  - `"workspaceFolder"`: Wenn ein Wort zum Wörterbuch hinzugefügt wird, verändere die Arbeitsbereichsordner-Konfiguration, falls gerade ein Arbeitsbereichsordner geöffnet ist, ansonsten die Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die Benutzer-Konfiguration.
  - `"userExternalFile"`: Wenn ein Wort zum Wörterbuch hinzugefügt wird, verändere stets die erste externe Einstellungsdatei in der Benutzer-Konfiguration.
  - `"workspaceExternalFile"`: Wenn ein Wort zum Wörterbuch hinzugefügt wird, verändere die erste externe Einstellungsdatei in der Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die analoge Datei in der Benutzer-Konfiguration.
  - `"workspaceFolderExternalFile"`: Wenn ein Wort zum Wörterbuch hinzugefügt wird, verändere die erste externe Einstellungsdatei in der Arbeitsbereichsordner-Konfiguration, falls gerade ein Arbeitsbereichsordner geöffnet ist, ansonsten die analoge Datei in der Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die analoge Datei in der Benutzer-Konfiguration.
- `"disabledRules"`: Einer der folgenden Werte:

  - `"user"`: Wenn eine Regel deaktiviert wird, verändere stets die Benutzer-Konfiguration.
  - `"workspace"`: Wenn eine Regel deaktiviert wird, verändere die Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die Benutzer-Konfiguration.
  - `"workspaceFolder"`: Wenn eine Regel deaktiviert wird, verändere die Arbeitsbereichsordner-Konfiguration, falls gerade ein Arbeitsbereichsordner geöffnet ist, ansonsten die Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die Benutzer-Konfiguration.
  - `"userExternalFile"`: Wenn eine Regel deaktiviert wird, verändere stets die erste externe Einstellungsdatei in der Benutzer-Konfiguration.
  - `"workspaceExternalFile"`: Wenn eine Regel deaktiviert wird, verändere die erste externe Einstellungsdatei in der Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die analoge Datei in der Benutzer-Konfiguration.
  - `"workspaceFolderExternalFile"`: Wenn eine Regel deaktiviert wird, verändere die erste externe Einstellungsdatei in der Arbeitsbereichsordner-Konfiguration, falls gerade ein Arbeitsbereichsordner geöffnet ist, ansonsten die analoge Datei in der Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die analoge Datei in der Benutzer-Konfiguration.
- `"hiddenFalsePositives"`: Einer der folgenden Werte:

  - `"user"`: Wenn ein falscher Fehler verborgen wird, verändere stets die Benutzer-Konfiguration.
  - `"workspace"`: Wenn ein falscher Fehler verborgen wird, verändere die Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die Benutzer-Konfiguration.
  - `"workspaceFolder"`: Wenn ein falscher Fehler verborgen wird, verändere die Arbeitsbereichsordner-Konfiguration, falls gerade ein Arbeitsbereichsordner geöffnet ist, ansonsten die Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die Benutzer-Konfiguration.
  - `"userExternalFile"`: Wenn ein falscher Fehler verborgen wird, verändere stets die erste externe Einstellungsdatei in der Benutzer-Konfiguration.
  - `"workspaceExternalFile"`: Wenn ein falscher Fehler verborgen wird, verändere die erste externe Einstellungsdatei in der Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die analoge Datei in der Benutzer-Konfiguration.
  - `"workspaceFolderExternalFile"`: Wenn ein falscher Fehler verborgen wird, verändere die erste externe Einstellungsdatei in der Arbeitsbereichsordner-Konfiguration, falls gerade ein Arbeitsbereichsordner geöffnet ist, ansonsten die analoge Datei in der Arbeitsbereich-Konfiguration, falls gerade ein Arbeitsbereich geöffnet ist, ansonsten die analoge Datei in der Benutzer-Konfiguration.

## `ltex.additionalRules.enablePickyRules`

Aktiviere LanguageTool-Regeln, die als pedantisch ("picky") markiert und standardmäßig deaktiviert sind, z. B. Regeln bzgl. Passiv, Satzlänge etc., mit dem Nachteil von mehr falschen Fehlern.

*Typ:* `boolean`

*Voreinstellung:* `false`

## `ltex.additionalRules.motherTongue`

Optionale Muttersprache des Benutzers (z. B. `"de-DE"`).

Falls diese Einstellung gesetzt ist, werden zusätzliche Regeln verwendet, um falsche Freunde zu erkennen. Es kann sein, dass pedantische Regeln aktiviert werden müssen, damit diese Einstellung eine Auswirkung hat (siehe [`ltex.additionalRules.enablePickyRules`](settings-de.html#ltexadditionalrulesenablepickyrules)). Die Erkennung von falschen Freunden verbessert sich, falls ein Sprachmodell bereitgestellt wird (siehe [`ltex.additionalRules.languageModel`](settings-de.html#ltexadditionalruleslanguagemodel)).

*Typ:* `string`

*Mögliche Werte:*

- `""`: Keine Muttersprache
- `"ar"`: Arabic
- `"ast-ES"`: Asturian
- `"be-BY"`: Belarusian
- `"br-FR"`: Breton
- `"ca-ES"`: Catalan
- `"ca-ES-balear"`: Catalan (Balearic)
- `"ca-ES-valencia"`: Catalan (Valencian)
- `"crh-UA"`: Crimean Tatar
- `"da-DK"`: Danish
- `"de"`: German (also accepts: `"de-LU"`)
- `"de-AT"`: German (Austria)
- `"de-CH"`: German (Swiss)
- `"de-DE"`: German (Germany)
- `"de-DE-x-simple-language"`: Simple German (also accepts: `"de-DE-x-simple-language-DE"`)
- `"el-GR"`: Greek
- `"en"`: English
- `"en-AU"`: English (Australian)
- `"en-CA"`: English (Canadian)
- `"en-GB"`: English (GB)
- `"en-NZ"`: English (New Zealand)
- `"en-US"`: English (US)
- `"en-ZA"`: English (South African)
- `"eo"`: Esperanto
- `"es"`: Spanish (also accepts: `"es-ES"`)
- `"es-AR"`: Spanish (voseo)
- `"fa"`: Persian (also accepts: `"fa-IR"`)
- `"fr"`: French (also accepts: `"fr-FR"`)
- `"fr-BE"`: French (Belgium)
- `"fr-CA"`: French (Canada)
- `"fr-CH"`: French (Switzerland)
- `"ga-IE"`: Irish
- `"gl-ES"`: Galician
- `"it"`: Italian (also accepts: `"it-IT"`)
- `"ja-JP"`: Japanese
- `"km-KH"`: Khmer
- `"nb"`: Norwegian (Bokmål) (also accepts: `"no"`; only on api.languagetoolplus.com)
- `"nl"`: Dutch (also accepts: `"nl-NL"`)
- `"nl-BE"`: Dutch (Belgium)
- `"pl-PL"`: Polish
- `"pt"`: Portuguese
- `"pt-AO"`: Portuguese (Angola preAO)
- `"pt-BR"`: Portuguese (Brazil)
- `"pt-MZ"`: Portuguese (Moçambique preAO)
- `"pt-PT"`: Portuguese (Portugal)
- `"ro-RO"`: Romanian
- `"ru-RU"`: Russian
- `"sk-SK"`: Slovak
- `"sl-SI"`: Slovenian
- `"sv"`: Swedish (also accepts: `"sv-SE"`)
- `"ta-IN"`: Tamil
- `"tl-PH"`: Tagalog
- `"uk-UA"`: Ukrainian
- `"zh-CN"`: Chinese

*Voreinstellung:* `""`

## `ltex.additionalRules.languageModel`

Optionaler Pfad zu einem Verzeichnis mit Regeln eines Sprachmodells mit *n*-Gramm-Vorkommniszahlen. Setzen Sie diese Einstellung auf das Elternverzeichnis, das Verzeichnisse für Sprachen enthält (z. B. `en`).

*Typ:* `string`

*Voreinstellung:* `""`

## `ltex.languageToolHttpServerUri`

Falls dies auf eine nicht-leere Zeichenfolge gesetzt ist, dann verwendet LTeX+ nicht die eingebaute Version von LanguageTool. Stattdessen verbindet sich LTeX+ zu einem externen [LanguageTool-HTTP-Server](https://dev.languagetool.org/http-server). Setzen Sie dies auf die Haupt-URI des Servers — zum Beispiel `https://api.languagetoolplus.com` für die gehostete API von LanguageTool oder `http://localhost:8081` für einen selbst gehosteten Server. LTeX+ hängt den API-Pfad (`/v2/check`) automatisch an; die URI sollte ihn daher nicht enthalten.

Beachten Sie, dass in diesem Modus die Einstellung [`ltex.additionalRules.languageModel`](settings-de.html#ltexadditionalruleslanguagemodel) ignoriert wird. Bitte beachten Sie, dass die Premium-API von [languagetool.org](https://languagetool.org) ein Größenlimit pro Anfrage hat (siehe [languagetool.org/http-api/](https://languagetool.org/http-api/)). Als Abhilfe können Sie magische Kommentare verwenden, um eine größere Datei in mehrere Fragmente aufzuteilen, die dann separat zur Überprüfung gesendet werden (siehe [Magische Kommentare](https://ltex-plus.github.io/ltex-plus/advanced-usage.html#magic-comments)).

*Typ:* `string`

*Beispiele:*

- `"https://api.languagetoolplus.com"`
- `"http://localhost:8081"`

*Voreinstellung:* `""`

## `ltex.languageToolOrg.username`

Benutzername/E-Mail-Adresse, wie zum Login auf languagetool.org benutzt, für Zugriff auf die Premium-API. Nur relevant, falls [`ltex.languageToolHttpServerUri`](settings-de.html#ltexlanguagetoolhttpserveruri) gesetzt ist.

*Typ:* `string`

*Voreinstellung:* `""`

## `ltex.languageToolOrg.apiKey`

API-Schlüssel für Zugriff auf die Premium-API. Nur relevant, falls [`ltex.languageToolHttpServerUri`](settings-de.html#ltexlanguagetoolhttpserveruri) gesetzt ist.

*Typ:* `string`

*Voreinstellung:* `""`

## `ltex.ltex-ls.path`

<!-- ltex-client-specific-de-begin -->

Falls dies auf eine leere Zeichenfolge gesetzt ist, dann lädt LTeX+ automatisch [ltex-ls von GitHub](https://github.com/ltex-plus/ltex-ls-plus/releases) herunter, speichert es im Erweiterungsordner, und benutzt es für die Textüberprüfung. Sie können diese Einstellung auf den Ort eines ltex-ls-plus-Releases setzen, das Sie selbst heruntergeladen haben. `$VAR` wird durch den Wert der Umgebungsvariable ersetzt.

Benutzen Sie dafür den Pfad zum Hauptverzeichnis von ltex-ls-plus (dieses enthält die Unterverzeichnisse `bin` und `lib`).

Nach Änderungen muss LTeX+ neugestartet werden.

<!-- ltex-client-specific-end -->

*Typ:* `string`

*Voreinstellung:* `""`

## `ltex.ltex-ls.logLevel`

Protokollierungslevel (Ausführlichkeit) des Server-Protokolls von ltex-ls-plus, das unter `Anzeigen` › `Ausgabe` › LTeX Language Server` verfügbar ist.

Die Levels sind in absteigender Reihenfolge `"severe"`, `"warning"`, `"info"`, `"config"`, `"fine"`, `"finer"`, und `"finest"`. Alle Meldungen, die den angegebenen Level oder einen höheren Level haben, werden protokolliert.

ltex-ls benutzt nicht alle Protokollierungslevel.

*Typ:* `string`

*Mögliche Werte:*

- `"severe"`: Minimale Ausführlichkeit. Protokolliere ausschließlich schwere Fehler.
- `"warning"`: Sehr niedrige Ausführlichkeit. Protokolliere ausschließlich schwere Fehler und Warnungen.
- `"info"`: Niedrige Ausführlichkeit. Protokolliere zusätzlich Start- und Beendingungsmeldungen.
- `"config"`: Mittlere Ausführlichkeit. Protokolliere zusätzlich Konfigurationsmeldungen.
- `"fine"`: Mittlere bis hohe Ausführlichkeit (Standard). Protokolliere zusätzlich, wenn LanguageTool aufgerufen wird oder wenn LanguageTool aufgrund geänderter Einstellungen neu initialisiert werden muss.
- `"finer"`: Hohe Ausführlichkeit. Protokolliere zusätzliche Debugging-Informationen wie ganze Texte, die überprüft werden.
- `"finest"`: Maximale Ausführlichkeit. Protokolliere alle verfügbaren Debugging-Informationen.

*Voreinstellung:* `"fine"`

## `ltex.java.path`

<!-- ltex-client-specific-de-begin -->

Falls dies auf eine leere Zeichenfolge gesetzt ist, dann benutzt LTeX+ eine Java-Distribution, die in ltex-ls-plus enthalten ist. Sie können diese Einstellung auf den Ort einer bereits bestehenden Java-Installation setzen, um stattdessen diese Java-Installation zu benutzen. `$VAR` wird durch den Wert der Umgebungsvariable ersetzt.

Benutzen Sie denselben Pfad, den Sie für die Umgebungsvariable `JAVA_HOME` benutzen würden (dieser enthält üblicherweise neben anderen die Unterverzeichnisse `bin` und `lib`).

Nach Änderungen muss LTeX+ neugestartet werden.

<!-- ltex-client-specific-end -->

*Typ:* `string`

*Voreinstellung:* `""`

## `ltex.java.initialHeapSize`

<!-- ltex-client-specific-de-begin -->

Anfängliche Größe des Java-Heap-Speichers in Megabytes (korrespondiert zur Java-Option `-Xms`, muss eine positive Ganzzahl sein).

Eine Verkleinerung kann dazu führen, dass der Java-Prozess weniger RAM-Speicher benötigt.

Nach Änderungen muss LTeX+ neugestartet werden.

<!-- ltex-client-specific-end -->

*Typ:* `integer`

*Voreinstellung:* `64`

## `ltex.java.maximumHeapSize`

<!-- ltex-client-specific-de-begin -->

Maximale Größe des Java-Heap-Speichers in Megabytes (korrespondiert zur Java-Option `-Xmx`, muss eine positive Ganzzahl sein).

Eine Verkleinerung kann dazu führen, dass der Java-Prozess weniger RAM-Speicher benötigt. Wenn Sie diese Einstellung zu klein setzen, kann dies dazu führen, dass der Java-Prozess die Heap-Größe überschreitet, sodass der Fehler `OutOfMemoryError` angezeigt wird.

Nach Änderungen muss LTeX+ neugestartet werden.

<!-- ltex-client-specific-end -->

*Typ:* `integer`

*Voreinstellung:* `2048`

## `ltex.sentenceCacheSize`

Größe des LanguageTool-Zwischenspeichers `ResultCache` in Sätzen (muss eine positive Ganzzahl sein).

Falls nur ein kleiner Teil des Textes geändert wird (z. B. ein einziger Tastendruck im Editor), dann benutzt LanguageTool den Zwischenspeicher, um zu vermeiden, dass der komplette Text nochmals überprüft werden muss. LanguageTool teilt den Text intern in Sätze auf; Sätze, die bereits überprüft worden sind, werden übersprungen.

Eine Verkleinerung kann dazu führen, dass der Java-Prozess weniger RAM-Speicher benötigt. Wenn Sie diese Einstellung auf einen zu kleinen Wert setzen, dann kann sich die Zeit, die LanguageTool zur Überprüfung benötigt, deutlich erhöhen.

Nach Änderungen muss LTeX+ neugestartet werden.

*Typ:* `integer`

*Voreinstellung:* `2000`

## `ltex.completionEnabled`

Steuert, ob Vervollständigung aktiviert ist (auch bekannt als Auto-Vervollständigung, Schnellvorschläge und IntelliSense).

Falls diese Einstellung aktiviert ist, dann wird eine Liste von Wörtern angezeigt, die das aktuelle Wort ergänzen (jedes Mal, wenn der Editor eine Vervollständigungs-Anfrage sendet).

<!-- ltex-client-specific-begin -->

In VS Code ist Vervollständigung während des Tippens standardmäßig aktiviert (via `editor.quickSuggestions`). Daher ist diese Einstellung standardmäßig deaktiviert, weil ständig angezeigte Vervollständigungs-Listen den Benutzer stören könnten. Es wird empfohlen, diese Einstellung zu aktivieren, aber `editor.quickSuggestions` zu deaktivieren. Dann können LTeX+-Vervollständigungen durch Drücken von `Strg+Leertaste` angefordert werden.

<!-- ltex-client-specific-end -->

*Typ:* `boolean`

*Voreinstellung:* `false`

## `ltex.diagnosticSeverity`

Schwere, mit der Schreibfehler angezeigt werden.

Erlaubt die Steuerung, wie und wo die Fehler in Visual Studio Code erscheinen. Die möglichen Schweren sind `"error"`, `"warning"`, `"information"` und `"hint"`.

Diese Einstellung kann entweder ein String mit der Schwere sein, die für alle Schreibfehler benutzt werden soll, oder ein Objekt mit regelabhängigen Schweren. Falls ein Objekt verwendet wird, ist jeder Schlüssel die ID einer LanguageTool-Regel und jeder Wert einer der möglichen Schweren. In diesem Fall muss die Schwere anderer Regeln, die nicht zu einer der Schlüssel passen, mit dem besonderen Schlüssel `"default"` angegeben werden.

*Typ:* `string` oder `object`

*Beispiele:*

- `"information"`
- `{"PASSIVE_VOICE": "hint", "default": "information"}`

*Voreinstellung:* `"information"`

*Vollständige Beschreibung des Typs:*

Einer der folgenden Typen:

- Einer der folgenden Werte:

  - `"error"`: Fehler mit der Schwere `error` sind üblicherweise mit einer roten geschlängelten Linie unterstrichen und erscheinen im Editor, in der Minimap, im Probleme-Reiter und im Explorer.
  - `"warning"`: Fehler mit der Schwere `warning` sind üblicherweise mit einer gelben geschlängelten Linie unterstrichen und erscheinen im Editor, in der Minimap, im Probleme-Reiter und im Explorer.
  - `"information"`: Fehler mit der Schwere `information` sind üblicherweise mit einer blauen geschlängelten Linie unterstrichen und erscheinen im Editor, in der Minimap und im Probleme-Reiter, aber nicht im Explorer.
  - `"hint"`: Fehler mit der Schwere `hint` sind nicht unterstrichen (nur unauffällig markiert) und erscheinen nur im Editor, aber nicht in der Minimap, im Probleme-Reiter oder im Explorer.
- Objekt mit beliebigen Eigenschaftsnamen, wobei die Werte jeder Eigenschaft folgenden Typ hat:

  - Einer der folgenden Werte:

    - `"error"`: Fehler mit der Schwere `error` sind üblicherweise mit einer roten geschlängelten Linie unterstrichen und erscheinen im Editor, in der Minimap, im Probleme-Reiter und im Explorer.
    - `"warning"`: Fehler mit der Schwere `warning` sind üblicherweise mit einer gelben geschlängelten Linie unterstrichen und erscheinen im Editor, in der Minimap, im Probleme-Reiter und im Explorer.
    - `"information"`: Fehler mit der Schwere `information` sind üblicherweise mit einer blauen geschlängelten Linie unterstrichen und erscheinen im Editor, in der Minimap und im Probleme-Reiter, aber nicht im Explorer.
    - `"hint"`: Fehler mit der Schwere `hint` sind nicht unterstrichen (nur unauffällig markiert) und erscheinen nur im Editor, aber nicht in der Minimap, im Probleme-Reiter oder im Explorer.

## `ltex.checkFrequency`

Steuert, wann Dokumente überprüft werden sollen.

Eines von `"edit"`, `"save"` und `"manual"`.

*Typ:* `string`

*Mögliche Werte:*

- `"edit"`: Dokumente werden überprüft, wenn sie geöffnet oder bearbeitet werden (bei jedem Tastendruck), oder wenn sich die Einstellungen ändern.
- `"save"`: Dokumente werden überprüft, wenn sie geöffnet oder gespeichert werden, oder wenn sich die Einstellungen ändern.
- `"manual"`: Dokumente werden nicht automatisch überprüft, außer wenn sich die Einstellungen ändern. Verwenden Sie Befehle wie [LTeX: Aktuelles Dokument prüfen`](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/commands-de.html#ltex-aktuelles-dokument-pr%C3%BCfen), um manuell Überprüfungen zu veranlassen.

*Voreinstellung:* `"edit"`

## `ltex.clearDiagnosticsWhenClosingFile`

Falls dies auf `true` gesetzt ist, dann werden von LTeX+ gemeldete Schreibfehler einer Datei gelöscht, wenn die Datei geschlossen wird.

*Typ:* `boolean`

*Voreinstellung:* `true`

## `ltex.statusBarItem`

<!-- ltex-client-specific-de-begin -->

Falls dies auf `true` gesetzt ist, dann wird ein Eintrag über den Status von LTeX+ ständig in der Statusleiste angezeigt.

<!-- ltex-client-specific-end -->

*Typ:* `boolean`

*Voreinstellung:* `false`

## `ltex.trace.server`

<!-- ltex-client-specific-de-begin -->

Debugging-Einstellung, um die Kommunikation zwischen Language Client und Language Server zu protokollieren.

Wenn Sie einen Bug melden, setzen Sie diese Einstellung auf `"verbose"` und öffnen Sie das Protokoll LTeX Language Client` unter `Anzeigen` › `Ausgabe`. Hängen Sie den relevanten Teil an das GitHub-Problem an.

Nach Änderungen muss LTeX+ neugestartet werden.

<!-- ltex-client-specific-end -->

*Typ:* `string`

*Mögliche Werte:*

- `"off"`: Protokolliere keinerlei Kommunikation zwischen Language Client und Language Server.
- `"messages"`: Protokolliere den Typ von Anfragen und Antworten zwischen Language Client und Language Server.
- `"verbose"`: Protokolliere den Typ und den Inhalt von Anfragen und Antworten zwischen Language Client und Language Server.

*Voreinstellung:* `"off"`
