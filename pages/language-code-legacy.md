---
# Copyright (C) 2019-2025
# Julian Valentin, Daniel Spitzer, LTeX+ Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Language Codes in Older Versions"
permalink: "/language-code-legacy.html"
toc: false
---

> **Best effort, no guarantee.** This page is intended to help users still running ltex-ls-plus releases **before 18.7.x** find a `ltex.language` value that works on their version. We do not attempt to specify exactly when each code started or stopped working. If a configuration does not check your text as expected, try one of the alternatives below until something works.

## Background

[ltex-ls-plus#150](https://github.com/ltex-plus/ltex-ls-plus/pull/150) is the change that made the modern fully-spelled codes (`fr-FR`, `it-IT`, `es-ES`, `nl-NL`, `sv-SE`, `fa-IR`) work reliably with the bundled checker. Before that PR landed in 18.7.x, those codes were not accepted in many configurations and could silently disable checking. On older releases the working values were the bare ISO 639-1 codes; the documentation you are reading on the [Supported Languages](supported-languages.html) page does not apply directly to those versions.

## Umbrella codes

LanguageTool's code set has long contained a few "umbrella" entries — codes that exist for backward compatibility or as a convenience but do not provide the full set of checks that a more specific code does. The umbrella case applies in two flavours, and on older releases neither was hidden from the user the way 18.7.x hides them.

- **Bare codes without a default spell-checker.** `en` and `de` are language-family entries that run grammar checks but carry no default spelling dictionary on their own. To get spell-check you have to pick a regional variant: `en-US`, `en-GB`, `en-AU`, `en-CA`, `en-NZ`, `en-ZA` for English; `de-DE`, `de-AT`, `de-CH` for German.
- **Catalan with variant-specific grammar.** `ca-ES` is the canonical Catalan code and runs both grammar and spell-check. The variants `ca-ES-valencia` (Valencian) and `ca-ES-balear` (Balearic) reuse the same Catalan spell-check dictionary but add variant-specific grammar rules. Picking `ca-ES` instead of `ca-ES-valencia` for a Valencian text means those Valencian-specific rules will not fire.

The same logic still applies on 18.7.x — pick the most specific code that matches your text — but recent releases at least keep the umbrella forms out of the advertised list so you are less likely to choose them by mistake.

## Codes that typically worked on older releases

- **Bare ISO 639-1 codes** (`fr`, `it`, `es`, `nl`, `sv`, `fa`, `pt`, …) for languages that are not in the umbrella set above. These ran both grammar and spell-checking and were the safe default on older releases.
- **Region-specific canonicals** (`en-US`, `en-GB`, `de-DE`, `de-AT`, `de-CH`, `fr-CA`, `fr-CH`, `fr-BE`, `pt-BR`, `pt-PT`, `pt-AO`, `pt-MZ`, `es-AR`, `nl-BE`, `ca-ES`, `ca-ES-valencia`, `ca-ES-balear`, …) were exact-match codes and worked identically across older and newer releases.
- **Modern fully-spelled codes** (`fr-FR`, `it-IT`, `es-ES`, `nl-NL`, `sv-SE`, `fa-IR`) were **not** generally accepted on older releases — that is the gap [ltex-ls-plus#150](https://github.com/ltex-plus/ltex-ls-plus/pull/150) closes. If you are on an older release and one of these silently disables checking, switch to the bare ISO 639-1 form (e.g., `fr` instead of `fr-FR`).
- **Hosted-API-only codes** (`nb`, `no` for Norwegian) require [`ltex.languageToolHttpServerUri`](settings.html#ltexlanguagetoolhttpserveruri) pointed at LanguageTool's hosted API (`https://api.languagetoolplus.com`); this has not changed across versions.

## Practical recommendation

If your existing configuration works today on an older release, you can leave it as-is. For new configurations, upgrade to ltex-ls-plus 18.7.x or newer and use the modern fully-spelled codes shown in [Supported Languages](supported-languages.html).
