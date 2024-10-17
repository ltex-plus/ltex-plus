<!--
   - Copyright (C) 2019-2021 Julian Valentin, LTeX+ Development Community
   -
   - This Source Code Form is subject to the terms of the Mozilla Public
   - License, v. 2.0. If a copy of the MPL was not distributed with this
   - file, You can obtain one at https://mozilla.org/MPL/2.0/.
   -->

# LT<sub>E</sub>X+ Documentation Repository

This is the repository for the documentation of LT<sub>E</sub>X+. It is published at <https://ltex-plus.github.io/ltex-plus>.

## Build the Documentation Locally

To build and serve the documentation on your local machine, follow these steps:

1. **Build the Docker Image:**

    ```bash
    docker compose build
    ```

2. **Start the Jekyll Server with Live Reload:**

    ```bash
    docker compose up
    ```

    This command executes `jekyll serve --livereload -H 0.0.0.0` inside the Docker container and maps port 4000 from the container to the host machine.

Once the server is running, you can access the documentation at [http://0.0.0.0:4000/ltex-plus/](http://0.0.0.0:4000/ltex-plus/). Changes to Markdown files (e.g., [pages/faq.md](pages/faq.md)) will be automatically reflected after refreshing your browser.
