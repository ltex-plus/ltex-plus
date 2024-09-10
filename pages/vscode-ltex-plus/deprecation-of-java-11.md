---
# Copyright (C) 2019-2021 Julian Valentin, LTeX+ Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Deprecation of Java 11"
permalink: "/vscode-ltex-plus/deprecation-of-java-11.html"
sidebar: "sidebar"
---

Java 11 has been published in 2018 and is approaching its end of life. Also, there are no builds of [AdoptOpenJDK](https://adoptopenjdk.net/) for ARM processors which are used in recent MacBooks. Fortunately, with Java 21, a new long-term support (LTS) release of Java is available. Therefore, starting with LTeX+ 18.0.0, LTeX+ requires Java 21 or newer (in the following: “Java 21+”).

## What Do I Have to Do?

Due to LTeX+'s feature of automatically downloading LTeX+ LS inclduing Java 21 (via [AdoptOpenJDK](https://adoptopenjdk.net/)), the impact on most users is minimal. The necessary actions you should perform depend on how you used LTeX+ with Java in the past (substitute “Java 11” with any other version older than Java 21):

* **Scenario:** You already have Java 21+ installed and you are using the [`ltex.java.path`](../settings.html#ltexjavapath) setting.

  *Necessary actions:* Nothing to do, you're all set!
  
* **Scenario:** You have Java 11 installed and you are **not** using the [`ltex.java.path`](../settings.html#ltexjavapath) setting.

  *Necessary actions:* Nothing to do. LTeX+ should continue to work as it used to do, as LTeX+ already downloads LTeX+ LS including Java 21.

* **Scenario:** You have Java 11 installed and you are using the [`ltex.java.path`](../settings.html#ltexjavapath) setting.

  *Necessary actions:* You should update your installation of Java, i.e., remove your old Java installation via the Windows Control Panel or your Linux package manager, and install Java 21+ via Windows installer, Linux package, etc. 

* **Scenario:** You don't have Java installed at all.

  *Necessary actions:* Nothing to do. LTeX+ should continue to work as it used to do, as LTeX+ already downloads LTeX+ LS including Java 21.

If one of the necessary actions includes updating your installation of Java, LTeX+ recommends AdoptOpenJDK to do so (although there are many more Java distributions). Just go to <https://adoptopenjdk.net/> and click on the blue “Latest release” button, leaving the default settings (OpenJDK 21 (LTS) and HotSpot) as they are.

If you need more choices (e.g., an archive instead of an installer, JRE instead of JDK, or a different platform), click on “Other platforms” instead. As long as you choose a Java version of 21 or newer, you should be good to go. (Note that the JRE suffices for LTeX+, but the JDK also works, as the JRE is a subset of the JDK.)

## Details on How LTeX+ Decides Which Java Installation to Use

In order to determine which Java installation to use, LTeX+ performs the following steps during startup:

1. Search an installation of Java 21+ on your system (via [`ltex.java.path`](../settings.html#ltexjavapath) and/or the environment variable `PATH`).
2. If none can be found, search for Java 21+ in the `lib/` directory of the extension.
3. If none can be found, download LTeX+ LS inclduing Java 21 to `lib/` and use that.
4. If that doesn't work, an error is displayed and LTeX+ cannot be used.
