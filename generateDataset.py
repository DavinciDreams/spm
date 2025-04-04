from transformers import pipeline

# List below is a list of questions that can be used to generate synthetic data

chatGPTDeepResearchQuestions = [
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
    

]


questions = [{
  "question": "What does this code do?",
}]

dataset = []

for question in questions:
    generator = pipeline("text-generation", model="YWZBrandon/openai-gsm8k_meta-llama-Llama-3.2-3B_2e-5", device="cuda")

    messages = []

    # make a system prompt 
    messages.append({"role": "system", "content": "You are a helpful assistant."})

    # load the codebase in maybase as an assitent role
    # import the jsonresume_repo_dump.md file from local
    with open("jsonresume_repo_dump.md", "r") as f:
        codebase = f.read()
    messages.append({"role": "system", "content": codebase})

    messages.append({"role": "user", "content": question})

    output = generator(messages, max_new_tokens=128, return_full_text=False)[0]

    dataset.append({"question": question, "answer": output["generated_text"]})

dataset.push_to_hub("ajaxdavis/lisa-spm")