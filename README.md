# Study
A personal study tool that automates tasks that I do regularly.

I wanted to use the opportunity presented in wanting to learn tooling & AI integration to create something that I could use. The goal with this tool is to able to automate a few tasks that I do regularly with LLMs for university, namely note summarisation and anki / flash card generation.

## Structure
study-automation-tool/
│
├── pyproject.toml
├── README.md
├── LICENSE
└── src/
    └── study_tool/
        ├── __init__.py
        ├── cli.py
        ├── config.py
        └── core/
            ├── __init__.py
            ├── pdf_parser.py
            ├── summariser.py
            └── card_generator.py

## Usage
In command line type: `study`
