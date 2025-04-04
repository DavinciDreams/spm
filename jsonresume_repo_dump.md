Project Path: resumed

Source Tree:

```txt
resumed
├── README.md
├── examples
│   ├── with-jsonresume-theme
│   │   ├── README.md
│   │   └── package.json
│   ├── with-local-theme
│   │   ├── README.md
│   │   ├── package.json
│   │   └── theme
│   │       ├── index.js
│   │       └── package.json
│   ├── with-node-api
│   │   ├── README.md
│   │   ├── index.js
│   │   └── package.json
│   └── with-pdf-export
│       ├── README.md
│       ├── index.js
│       └── package.json
├── src
│   ├── cli.ts
│   ├── index.ts
│   ├── init.ts
│   ├── render.ts
│   ├── resume-schema.d.ts
│   └── validate.ts
└── test
    ├── cli.test.ts
    ├── init.test.ts
    ├── render.test.ts
    └── validate.test.ts

```

`resumed/README.md`:

````md
# Resumed

[![npm package version](https://img.shields.io/npm/v/resumed)](https://www.npmjs.com/package/resumed)
[![Build status](https://img.shields.io/github/actions/workflow/status/rbardini/resumed/main.yml)](https://github.com/rbardini/resumed/actions)
[![Code coverage](https://img.shields.io/codecov/c/github/rbardini/resumed.svg)](https://codecov.io/gh/rbardini/resumed)
[![Dependencies status](https://img.shields.io/librariesio/release/npm/resumed)](https://libraries.io/npm/resumed)

👔 Lightweight [JSON Resume](https://jsonresume.org/) builder, no-frills [alternative to resume-cli](#motivation).

- 🗜️ Small (~120 LOC)
- 📦 Pure ESM package
- 🧩 CLI and Node.js API
- 🤖 TypeScript typings
- ⏱️ Async render support
- 🧪 100% code coverage

## Installation

```shell
npm install resumed jsonresume-theme-even # or your theme of choice
```
````

## Usage

```console
$ resumed --help

  Usage
    $ resumed <command> [options]

  Available Commands
    render      Render resume
    init        Create sample resume
    validate    Validate resume

  For more info, run any command with the `--help` flag
    $ resumed render --help
    $ resumed init --help

  Options
    -v, --version    Displays current version
    -h, --help       Displays this message
```

See [examples](examples).

## Commands

### `render` (default)

Render resume.

**Usage:** `resumed render [filename] [options]`

**Aliases:** `export`

**Options:**

- `-o`, `--output`: Output filename (default `resume.html`)
- `-t`, `--theme`: Theme to use
- `-h`, `--help`: Display help message

### `init`

Create sample resume.

**Usage:** `resumed init [filename] [options]`

**Aliases:** `create`

**Options:**

- `-h`, `--help`: Display help message

### `validate`

Validate resume.

**Usage:** `resumed validate [filename] [options]`

**Options:**

- `-h`, `--help`: Display help message

## Motivation

[resume-cli](https://github.com/jsonresume/resume-cli) is the original command line tool for [JSON Resume](https://jsonresume.org/), the open source initiative to create a JSON-based standard for resumes. It has served the community well for years, but its broad scope and aging codebase has become increasingly harder to maintain.

Resumed is a _complete reimplementation_ of resume-cli, using more modern technologies while dropping certain features, to remain small and focused.

### Theme resolution

Resumed does not install any themes. You must [pick and install one](https://www.npmjs.com/search?q=jsonresume-theme) yourself, and specify your choice via the `--theme` option or the `.meta.theme` field of your resume.

In contrast, resume-cli comes with a default theme, and only supports the `--theme` option. This is fine for most users, but it ties the default theme package release cycle to that of the CLI, and may be a little more verbose.

### Interface

While both tools can be used from the command line, Resumed also provides a fully-tested, strongly-typed Node.js API to create, validate and render resumes programatically.

### Other features

Resumed makes some compromises in terms of features, such as no PDF export, local previews or YAML format support. If you miss any of these, you can combine Resumed with other tools, (e.g. Puppeteer for PDF generation, see [example](examples/with-pdf-export/)) or continue using resume-cli.

````

`resumed/examples/with-jsonresume-theme/README.md`:

```md
# JSON Resume theme example

This example shows how to use Resumed with a JSON Resume theme, [Even](https://github.com/rbardini/jsonresume-theme-even).

## How to use

Clone this example with [degit](https://github.com/Rich-Harris/degit), install dependencies, create and render resume:

```sh
npx degit rbardini/resumed/examples/with-jsonresume-theme
npm install
npm run init
npm start
````

````

`resumed/examples/with-jsonresume-theme/package.json`:

```json
{
  "private": true,
  "type": "module",
  "scripts": {
    "init": "resumed init",
    "start": "resumed --theme jsonresume-theme-even"
  },
  "dependencies": {
    "jsonresume-theme-even": "^0.17.0",
    "resumed": "^3.0.0"
  }
}

````

`resumed/examples/with-local-theme/README.md`:

````md
# Local theme example

This example shows how to use Resumed with a local theme.

## How to use

Clone this example with [degit](https://github.com/Rich-Harris/degit), install dependencies, create and render resume:

```sh
npx degit rbardini/resumed/examples/with-local-theme
npm install
npm run init
npm start
```
````

````

`resumed/examples/with-local-theme/package.json`:

```json
{
  "private": true,
  "type": "module",
  "scripts": {
    "init": "resumed init",
    "start": "resumed --theme jsonresume-theme-local"
  },
  "dependencies": {
    "jsonresume-theme-local": "file:./theme",
    "resumed": "^3.0.0"
  }
}

````

`resumed/examples/with-local-theme/theme/index.js`:

```js
exports.render = ({ basics }) => `
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>${basics.name}</title>
  </head>
  <body>
    <h1>${basics.name}</h1>
    <h2>${basics.label}</h2>
    <p>${basics.summary}</p>
    <ul>
      <li>${basics.location.city} ${basics.location.countryCode}</li>
      <li><a href="mailto:${basics.email}">${basics.email}</a></li>
      <li><a href="tel:${basics.phone}">${basics.phone}</a></li>
      <li><a href="${basics.url}">${basics.url}</a></li>
      ${basics.profiles
        .map((profile) => `<li>${profile.username} (${profile.network})</li>`)
        .join("")}
    </ul>
  </body>
</html>
`;
```

`resumed/examples/with-local-theme/theme/package.json`:

```json
{
  "private": true
}
```

`resumed/examples/with-node-api/README.md`:

````md
# Node.js API example

This example shows how to use Resumed with its Node.js API.

## How to use

Clone this example with [degit](https://github.com/Rich-Harris/degit), install dependencies, create and render resume:

```sh
npx degit rbardini/resumed/examples/with-node-api
npm install
npm run init
npm start
```
````

````

`resumed/examples/with-node-api/index.js`:

```js
import { promises as fs } from 'fs'
import * as theme from 'jsonresume-theme-even'
import { render } from 'resumed'

const resume = JSON.parse(await fs.readFile('resume.json', 'utf-8'))
const html = await render(resume, theme)

await fs.writeFile('resume.html', html)

````

`resumed/examples/with-node-api/package.json`:

```json
{
  "private": true,
  "type": "module",
  "scripts": {
    "init": "resumed init",
    "start": "node index.js"
  },
  "dependencies": {
    "jsonresume-theme-even": "^0.17.0",
    "puppeteer": "^13.0.0",
    "resumed": "^3.0.0"
  }
}
```

`resumed/examples/with-pdf-export/README.md`:

````md
# PDF export example

This example shows how to use Resumed with [Puppeteer](https://pptr.dev/) to export a resume to PDF.

## How to use

Clone this example with [degit](https://github.com/Rich-Harris/degit), install dependencies, create and render resume:

```sh
npx degit rbardini/resumed/examples/with-pdf-export
npm install
npm run init
npm start
```
````

````

`resumed/examples/with-pdf-export/index.js`:

```js
import { promises as fs } from 'fs'
import * as theme from 'jsonresume-theme-even'
import puppeteer from 'puppeteer'
import { render } from 'resumed'

const resume = JSON.parse(await fs.readFile('resume.json', 'utf-8'))
const html = await render(resume, theme)

const browser = await puppeteer.launch()
const page = await browser.newPage()

await page.setContent(html, { waitUntil: 'networkidle0' })
await page.pdf({ path: 'resume.pdf', format: 'a4', printBackground: true })
await browser.close()

````

`resumed/examples/with-pdf-export/package.json`:

```json
{
  "private": true,
  "type": "module",
  "scripts": {
    "init": "resumed init",
    "start": "node index.js"
  },
  "dependencies": {
    "jsonresume-theme-even": "^0.17.0",
    "puppeteer": "^13.0.0",
    "resumed": "^3.0.0"
  }
}
```

`resumed/src/cli.ts`:

```ts
import { readFile, writeFile } from "node:fs/promises";
import sade from "sade";
import stripJsonComments from "strip-json-comments";
import { red, yellow } from "yoctocolors";
import { init, render, validate } from "./index.js";

// Trick Rollup into not bundling package.json
const pkgPath = "../package.json";
const pkg = JSON.parse(
  await readFile(new URL(pkgPath, import.meta.url), "utf-8")
);

type RenderOptions = {
  output: string;
  theme?: string;
};

export const cli = sade(pkg.name).version(pkg.version);

cli
  .command("render [filename]", "Render resume", {
    alias: "export",
    default: true,
  })
  .option("-o, --output", "Output filename", "resume.html")
  .option("-t, --theme", "Theme to use")
  .action(
    async (
      filename: string = "resume.json",
      { output, theme }: RenderOptions
    ) => {
      const resume = JSON.parse(
        stripJsonComments(await readFile(filename, "utf-8"))
      );

      const themeName = theme ?? resume?.meta?.theme;
      if (!themeName) {
        console.error(
          `No theme to use. Please specify one via the ${yellow(
            "--theme"
          )} option or the ${yellow(".meta.theme")} field of your resume.`
        );

        process.exitCode = 1;
        return;
      }

      let themeModule;
      try {
        themeModule = await import(themeName);
      } catch {
        console.error(
          `Could not load theme ${yellow(themeName)}. Is it installed?`
        );

        process.exitCode = 1;
        return;
      }

      const rendered = await render(resume, themeModule);
      await writeFile(output, rendered);

      console.log(
        `You can find your rendered resume at ${yellow(output)}. Nice work! 🚀`
      );
    }
  );

cli
  .command("init [filename]", "Create sample resume", { alias: "create" })
  .action(async (filename: string = "resume.json") => {
    await init(filename);
    console.log(
      `Done! Start editing ${yellow(filename)} now, and run the ${yellow(
        "render"
      )} command when you are ready. 👍`
    );
  });

cli
  .command("validate [filename]", "Validate resume")
  .action(async (filename: string = "resume.json") => {
    try {
      await validate(filename);
      console.log(`Your ${yellow(filename)} looks amazing! ✨`);
    } catch (err) {
      if (!Array.isArray(err)) {
        throw err;
      }

      console.error(
        `Uh-oh! The following errors were found in ${yellow(filename)}:\n`
      );
      err.forEach((err: { message: string; path: string }) =>
        console.error(` ${red(`❌ ${err.message}`)} at ${yellow(err.path)}.`)
      );

      process.exitCode = 1;
    }
  });
```

`resumed/src/index.ts`:

```ts
export { cli } from "./cli.js";
export { init } from "./init.js";
export { render } from "./render.js";
export { validate } from "./validate.js";
```

`resumed/src/init.ts`:

```ts
import { writeFile } from "node:fs/promises";
import { createRequire } from "node:module";

// ESM can't import JSON yet, fallback to `require`
const require = createRequire(import.meta.url);

export const init = (filename: string) => {
  const resume = require("@jsonresume/schema/sample.resume.json");
  return writeFile(filename, JSON.stringify(resume, undefined, 2));
};
```

`resumed/src/render.ts`:

```ts
type Theme<T> = {
  render: (resume: object) => T | Promise<T>;
};

export const render = (resume: object, theme: Theme<string>) =>
  theme.render(resume);
```

`resumed/src/resume-schema.d.ts`:

```ts
declare module "@jsonresume/schema" {
  export function validate(
    resumeJson: object,
    callback: (err: Error[] | null, result: boolean) => void
  );

  export const schema: object;
}
```

`resumed/src/validate.ts`:

```ts
import schema from "@jsonresume/schema";
import { readFile } from "node:fs/promises";
import { promisify } from "node:util";

const schemaValidate = promisify(schema.validate);

export const validate = async (filename: string) => {
  const resume = await readFile(filename, "utf-8");
  return schemaValidate(JSON.parse(resume));
};
```

`resumed/test/cli.test.ts`:

```ts
import * as theme from "jsonresume-theme-even";
import { readFile, writeFile } from "node:fs/promises";
import { describe, expect, it, vi } from "vitest";
import { cli } from "../src/cli.js";
import { init, render, validate } from "../src/index.js";

vi.mock("node:fs/promises", async () => ({
  readFile: vi
    .fn()
    .mockResolvedValueOnce(
      JSON.stringify({ name: "resumed", version: "0.0.0" })
    ),
  writeFile: vi.fn(),
}));

vi.mock("../src");

const logSpy = vi.spyOn(console, "log").mockImplementation(() => {});
const errorSpy = vi.spyOn(console, "error").mockImplementation(() => {});

describe("init", () => {
  it("creates a sample resume with default filename", async () => {
    await cli.parse(["", "", "init"]);

    expect(init).toHaveBeenCalledTimes(1);
    expect(init).toHaveBeenCalledWith("resume.json");

    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy.mock.calls[0][0]).toMatchInlineSnapshot(
      `"Done! Start editing resume.json now, and run the render command when you are ready. 👍"`
    );
  });

  it("creates a sample resume with custom filename", async () => {
    await cli.parse(["", "", "init", "custom.json"]);

    expect(init).toHaveBeenCalledTimes(1);
    expect(init).toHaveBeenCalledWith("custom.json");

    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy.mock.calls[0][0]).toMatchInlineSnapshot(
      `"Done! Start editing custom.json now, and run the render command when you are ready. 👍"`
    );
  });
});

describe("render", () => {
  it("renders a resume with default filename", async () => {
    const resume = {};

    vi.mocked(readFile).mockResolvedValueOnce(JSON.stringify(resume));
    vi.mocked(render).mockResolvedValueOnce("rendered");

    await cli.parse(["", "", "render", "--theme", "jsonresume-theme-even"]);

    expect(readFile).toHaveBeenCalledTimes(1);
    expect(readFile).toHaveBeenCalledWith("resume.json", "utf-8");

    expect(render).toHaveBeenCalledTimes(1);
    expect(render).toHaveBeenCalledWith(resume, theme);

    expect(writeFile).toHaveBeenCalledTimes(1);
    expect(writeFile).toHaveBeenCalledWith("resume.html", "rendered");

    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy.mock.calls.join("\n")).toMatchInlineSnapshot(
      `"You can find your rendered resume at resume.html. Nice work! 🚀"`
    );
  });

  it("renders a resume with comments ", async () => {
    const resume = `//Template\n{"basics":{"name":"Benny"}}`;

    vi.mocked(readFile).mockResolvedValueOnce(resume);
    vi.mocked(render).mockResolvedValueOnce("rendered");

    await cli.parse(["", "", "render", "--theme", "jsonresume-theme-even"]);

    expect(readFile).toHaveBeenCalledTimes(1);
    expect(readFile).toHaveBeenCalledWith("resume.json", "utf-8");

    expect(render).toHaveBeenCalledTimes(1);

    expect(writeFile).toHaveBeenCalledTimes(1);
    expect(writeFile).toHaveBeenCalledWith("resume.html", "rendered");
  });

  it("renders a resume with custom filename", async () => {
    const resume = {};

    vi.mocked(readFile).mockResolvedValueOnce(JSON.stringify(resume));
    vi.mocked(render).mockResolvedValueOnce("rendered");

    await cli.parse([
      "",
      "",
      "render",
      "custom.json",
      "--theme",
      "jsonresume-theme-even",
    ]);

    expect(readFile).toHaveBeenCalledTimes(1);
    expect(readFile).toHaveBeenCalledWith("custom.json", "utf-8");

    expect(render).toHaveBeenCalledTimes(1);
    expect(render).toHaveBeenCalledWith(resume, theme);

    expect(writeFile).toHaveBeenCalledTimes(1);
    expect(writeFile).toHaveBeenCalledWith("resume.html", "rendered");

    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy.mock.calls.join("\n")).toMatchInlineSnapshot(
      `"You can find your rendered resume at resume.html. Nice work! 🚀"`
    );
  });

  it("renders a resume with custom output", async () => {
    const resume = {};

    vi.mocked(readFile).mockResolvedValueOnce(JSON.stringify(resume));
    vi.mocked(render).mockResolvedValueOnce("rendered");

    await cli.parse([
      "",
      "",
      "render",
      "--theme",
      "jsonresume-theme-even",
      "--output",
      "custom-output.html",
    ]);

    expect(readFile).toHaveBeenCalledTimes(1);
    expect(readFile).toHaveBeenCalledWith("resume.json", "utf-8");

    expect(render).toHaveBeenCalledTimes(1);
    expect(render).toHaveBeenCalledWith(resume, theme);

    expect(writeFile).toHaveBeenCalledTimes(1);
    expect(writeFile).toHaveBeenCalledWith("custom-output.html", "rendered");

    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy.mock.calls.join("\n")).toMatchInlineSnapshot(
      `"You can find your rendered resume at custom-output.html. Nice work! 🚀"`
    );
  });

  it("renders a resume with theme defined via the `.meta.theme` field", async () => {
    const resume = { meta: { theme: "jsonresume-theme-even" } };

    vi.mocked(readFile).mockResolvedValueOnce(JSON.stringify(resume));
    vi.mocked(render).mockResolvedValueOnce("rendered");

    await cli.parse(["", "", "render"]);

    expect(readFile).toHaveBeenCalledTimes(1);
    expect(readFile).toHaveBeenCalledWith("resume.json", "utf-8");

    expect(render).toHaveBeenCalledTimes(1);
    expect(render).toHaveBeenCalledWith(resume, theme);

    expect(writeFile).toHaveBeenCalledTimes(1);
    expect(writeFile).toHaveBeenCalledWith("resume.html", "rendered");

    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy.mock.calls.join("\n")).toMatchInlineSnapshot(
      `"You can find your rendered resume at resume.html. Nice work! 🚀"`
    );
  });

  it("asks to define a theme if none specified and exits with failure code", async () => {
    const resume = {};

    vi.mocked(readFile).mockResolvedValueOnce(JSON.stringify(resume));

    await cli.parse(["", "", "render"]);

    expect(readFile).toHaveBeenCalledTimes(1);
    expect(readFile).toHaveBeenCalledWith("resume.json", "utf-8");

    expect(errorSpy).toHaveBeenCalledTimes(1);
    expect(errorSpy.mock.calls[0][0]).toMatchInlineSnapshot(
      `"No theme to use. Please specify one via the --theme option or the .meta.theme field of your resume."`
    );

    expect(render).not.toHaveBeenCalled();
    expect(process.exitCode).toBe(1);
  });

  it("asks if theme is installed if theme cannot be loaded and exits with failure code", async () => {
    const resume = {};

    vi.mocked(readFile).mockResolvedValueOnce(JSON.stringify(resume));

    await cli.parse(["", "", "render", "--theme", "jsonresume-theme-missing"]);

    expect(readFile).toHaveBeenCalledTimes(1);
    expect(readFile).toHaveBeenCalledWith("resume.json", "utf-8");

    expect(errorSpy).toHaveBeenCalledTimes(1);
    expect(errorSpy.mock.calls[0][0]).toMatchInlineSnapshot(
      `"Could not load theme jsonresume-theme-missing. Is it installed?"`
    );

    expect(render).not.toHaveBeenCalled();
    expect(process.exitCode).toBe(1);
  });
});

describe("validate", () => {
  it("validates a resume with default filename", async () => {
    await cli.parse(["", "", "validate"]);

    expect(validate).toHaveBeenCalledTimes(1);
    expect(validate).toHaveBeenCalledWith("resume.json");

    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy.mock.calls[0][0]).toMatchInlineSnapshot(
      `"Your resume.json looks amazing! ✨"`
    );
  });

  it("validates a resume with custom filename", async () => {
    await cli.parse(["", "", "validate", "custom.json"]);

    expect(validate).toHaveBeenCalledTimes(1);
    expect(validate).toHaveBeenCalledWith("custom.json");

    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy.mock.calls[0][0]).toMatchInlineSnapshot(
      `"Your custom.json looks amazing! ✨"`
    );
  });

  it("rethrows error if not an array", async () => {
    const error = new Error("validate");
    vi.mocked(validate).mockImplementationOnce(() => {
      throw error;
    });

    await expect(cli.parse(["", "", "validate"])).rejects.toThrow(error);
  });

  it("lists validation errors and exits with failure code", async () => {
    const errors = [...Array(3).keys()].map((i) => ({
      message: `message ${i}`,
      path: `path ${i}`,
    }));
    vi.mocked(validate).mockRejectedValueOnce(errors);

    await cli.parse(["", "", "validate"]);

    expect(errorSpy).toHaveBeenCalledTimes(errors.length + 1);
    expect(errorSpy.mock.calls.join("\n")).toMatchInlineSnapshot(`
      "Uh-oh! The following errors were found in resume.json:

       ❌ message 0 at path 0.
       ❌ message 1 at path 1.
       ❌ message 2 at path 2."
    `);
    expect(process.exitCode).toBe(1);
  });
});
```

`resumed/test/init.test.ts`:

```ts
import { writeFile } from "node:fs/promises";
import { expect, it, vi } from "vitest";
import { init } from "../src/init.js";

vi.mock("node:fs/promises", async () => ({
  writeFile: vi.fn(),
}));

it("initializes a resume", async () => {
  vi.mocked(writeFile).mockResolvedValueOnce();
  await expect(init("resume.json")).resolves.toBeUndefined();
});

it("throws if write fails", async () => {
  vi.mocked(writeFile).mockRejectedValueOnce("error");
  await expect(init("resume.json")).rejects.toBe("error");
});
```

`resumed/test/render.test.ts`:

```ts
import { expect, it, vi } from "vitest";
import { render } from "../src/render.js";

it("renders a theme", () => {
  const resume = require("@jsonresume/schema/sample.resume.json");
  const theme = {
    render: vi.fn(({ basics: { name } }) => name),
  };

  expect(render(resume, theme)).toBe(resume.basics.name);
});
```

`resumed/test/validate.test.ts`:

```ts
import { readFile } from "node:fs/promises";
import { expect, it, vi } from "vitest";
import { validate } from "../src/validate.js";

vi.mock("node:fs/promises", async () => ({
  readFile: vi.fn(),
}));

it("passes a valid resume", async () => {
  vi.mocked(readFile).mockResolvedValueOnce(
    JSON.stringify({ basics: { name: "Richard Hendriks" } })
  );

  await expect(validate("resume.json")).resolves.toStrictEqual(true);
});

it("fails an invalid resume", async () => {
  vi.mocked(readFile).mockResolvedValueOnce(
    JSON.stringify({ basics: { name: 123 } })
  );

  await expect(validate("resume.json")).rejects.toStrictEqual([
    expect.objectContaining({
      stack: "instance.basics.name is not of a type(s) string",
    }),
  ]);
});
```
