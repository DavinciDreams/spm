import fs from "fs";
import { jsonl } from "js-jsonl";
import { generateText } from "ai";
import dotenv from "dotenv";

dotenv.config();
const apiKey = process.env.OPENAI_API_KEY;

import { createOpenAI } from "@ai-sdk/openai";

const openai = createOpenAI({
  apiKey,
});

let lisaQuestions = fs.readFileSync("./new_cli_questions.jsonl", "utf-8");
let travisQuestions = fs.readFileSync("./dataset_Trave.jsonl", "utf-8");

lisaQuestions = jsonl.parse(lisaQuestions);
travisQuestions = jsonl.parse(travisQuestions);

lisaQuestions = lisaQuestions.map((q) => q.instruction);
travisQuestions = travisQuestions.map((q) => q.instruction);

const ajaxQuestions = [
  "What commands does the Resumed CLI expose, and what are their options?",
  "How does the 'render' command resolve which theme to use?",
  "What happens if the theme specified via --theme or .meta.theme cannot be loaded?",
  "How does Resumed differentiate between CLI usage and Node.js API usage?",
  "What is the structure and purpose of the `examples/with-node-api` example?",
  "What are the functional responsibilities of each file in the `src/` directory?",
  "Is the `render` function in Resumed synchronous or asynchronous?",
  "What is the type signature of the `render` function, and what does it return?",
  "How does Resumed validate a resume.json file?",
  "What library provides the sample resume template used by `resumed init`?",
  "Does Resumed support non-JSON formats like YAML?",
  "What happens when a validation error is encountered during `resumed validate`?",
  "How does Resumed ensure themes are compatible with its render engine?",
  "Which design choices make Resumed a 'pure ESM package'?",
  "What are the assumptions made by the `render` method regarding theme shape?",
  "What would happen if a theme module does not export a `render()` function?",
  "What are the limitations of Resumed compared to resume-cli?",
  "What kind of themes does Resumed support: npm-based, local, or both?",
  "Can Resumed be used to generate a PDF resume out of the box?",
  "How does the Puppeteer integration in the PDF example work?",
  "Is Resumed suitable for embedding into a web application backend?",
  "Which parts of the CLI use asynchronous operations, and are they awaited properly?",
  "What is the purpose of the `strip-json-comments` package in CLI input parsing?",
  "Is it possible to extend Resumed with plugins or custom commands?",
  "How does Resumed test for full coverage across CLI, API, and file operations?",
  "What is the default output filename for rendering a resume?",
  "Can the output filename be changed, and if so, how?",
  "How does Resumed ensure users don't accidentally render without specifying a theme?",
  "What happens if you pass a resume with commented-out JSON in `render`?",
  "How would Resumed behave if a circular reference existed in the resume JSON?",
  "How does Resumed differ from `resume-cli` in terms of versioning and modularity?",
  "Which assumptions are made about the environment (Node version, module system, etc.)?",
  "What is the effect of `createRequire(import.meta.url)` in `init.ts`?",
  "How is the theme dynamically imported, and what are the implications of that?",
  "How are test mocks created using `vitest`, and which modules are mocked?",
  "What kind of data is validated in `validate.test.ts`, and what are the failure cases?",
  "How could Resumed be used in a CI pipeline to validate resumes for job board submissions?",
  "What are the trade-offs of not bundling a default theme with the CLI?",
  "How could you write a new theme for Resumed from scratch?",
  "Which examples demonstrate PDF generation, and what tools do they use?",
  "How does Resumed separate concerns between schema validation, rendering, and CLI logic?",
  "How would you extend Resumed to support JSON Resume v1.1 schema?",
  "Could a micro-model built for Resumed predict how to fix resume validation errors?",
  "How much of Resumed’s logic is pure vs side-effectful (e.g., I/O, file writes)?",
  "What minimal context is needed to correctly use Resumed from a Node.js script?",
  "If the resume file contains invalid Unicode, what would be the failure path in the CLI?",
  "How could an agent use Resumed to generate resumes from a GraphQL resume builder frontend?",
  "Is Resumed capable of running in Deno, and what changes would be required if not?",
  "What is the smallest set of files necessary to render a resume with a custom theme?",
  "What is Resumed?",
  "How do I install Resumed?",
  "What commands does Resumed support?",
  "How do I render a resume with a custom theme?",
];

const allQuestions = [...lisaQuestions, ...travisQuestions, ...ajaxQuestions];

const sampleQuestions = allQuestions.slice(0, 2);

const packageCodeAndDocs = fs.readFileSync(
  "./jsonresume_repo_dump.md",
  "utf-8"
);

// loop over samplequestions and output the prompt
for (const question of sampleQuestions) {
  const prompt = `
  You are an expert in software packages, below you will see an entire codebase, code, examples, test, and documentation. Someone is about to ask about the codebase. Only offer questions in the codebase, don't offer guesses, if it is not in the codebase, tell the user you don't know.

  This is the codebase documentation and code:
  ${packageCodeAndDocs}

  This is the user question:
  ${question}

`;

  const result = await generateText({
    model: openai.responses("gpt-4o"),
    prompt: prompt,
  });

  const output = result.text;

  console.log(question);
  console.log("---");
  console.log(output);
  console.log("========");
  console.log("========");
  console.log("========");
  console.log("========");
  console.log("========");
  console.log("========");
  console.log("========");
}
