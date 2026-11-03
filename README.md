
# 📝 Meeting Minutes Generator

### An Automated Python-Based Meeting Documentation Tool

## 📌 Project Overview

The Meeting Minutes Generator is a Python application that converts raw meeting transcripts into structured meeting minutes.

Preparing meeting minutes manually can be time-consuming. Important decisions, discussion points, and action items may also be missed during manual note-taking.

This project aims to simplify the process by automatically extracting relevant information from meeting transcripts and organizing it into a readable Markdown document.

## 🎯 Objectives

- Automate the generation of meeting minutes.
- Extract important discussion points.
- Identify possible decisions from conversations.
- Detect potential action items and their speakers.
- Generate structured and readable documentation.
- Reduce repetitive manual documentation work.

## ⚙️ System Workflow

```text
Meeting Transcript (.txt)
          |
          v
   Python Application
          |
          v
   Transcript Processing
          |
          v
   Information Extraction
          |
     +----+----+
     |         |
     v         v
  Decisions  Action Items
     |         |
     +----+----+
          |
          v
   Markdown Generator
          |
          v
   Meeting Minutes (.md)
```

## ✨ Features

- **Transcript Processing:** Reads meeting conversations from text files.
- **Speaker Extraction:** Identifies speakers using a structured transcript format.
- **Summary Generation:** Creates a concise list of discussion points.
- **Decision Detection:** Identifies possible decisions using predefined keywords.
- **Action Item Detection:** Identifies statements that may represent tasks.
- **Markdown Export:** Generates a structured meeting minutes document.
- **Error Handling:** Handles missing input files and file access errors.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Application development |
| Regular Expressions | Speaker and keyword extraction |
| pathlib | File handling |
| argparse | Command-line interface |
| Markdown | Structured output documentation |

## 📂 Project Structure

```text
meeting-minutes-generator/
│
├── main.py
├── sample_transcript.txt
├── requirements.txt
├── .gitignore
└── README.md
```

## 💻 Installation and Setup

### Prerequisites

- Python 3 installed on your computer.
- Git installed on your computer.
- Basic knowledge of command-line operations.

### Step 1: Clone the Repository

```bash
git clone https://github.com/DIKSHA1303/meeting-minutes-generator.git
```

### Step 2: Navigate to the Project Directory

```bash
cd meeting-minutes-generator
```

### Step 3: Run the Application

```bash
python main.py sample_transcript.txt
```

### Step 4: View the Generated Output

After successful execution, a file named `meeting_minutes.md` will be generated in the project directory.

Open this file using any Markdown editor or text editor.

## 📥 Sample Input

Example meeting transcript:

```text
Project Planning Meeting

Priya: We need to complete the website homepage by Friday.
Sneha: I will finish the homepage design by Wednesday.
Aditi: I will work on the backend API integration.
Priya: We agreed to use React for the frontend.
Sneha: The team decided to conduct testing on Saturday.
Aditi: I will prepare the API documentation by Thursday.
Priya: We need to review the final application before submission.
```

## 📤 Expected Output

The generated Markdown document contains:

### 1. Meeting Summary
- Priya discussed completing the website homepage by Friday.
- Sneha discussed finishing the homepage design by Wednesday.
- Aditi discussed working on backend API integration.
- Priya discussed using React for the frontend.
- Sneha discussed conducting testing on Saturday.

### 2. Decisions
- Priya: We agreed to use React for the frontend.
- Sneha: The team decided to conduct testing on Saturday.

### 3. Action Items
- Sneha: I will finish the homepage design by Wednesday.
- Aditi: I will work on the backend API integration.
- Aditi: I will prepare the API documentation by Thursday.

*Note: This is illustrative output. The actual program uses its extraction rules and may also flag other statements as possible action items.*

## ⚠️ Limitations

The current version uses rule-based keyword extraction rather than a Large Language Model.

- It does not understand the full context of conversations.
- Keyword matching may identify irrelevant statements.
- Action item ownership is not independently verified.
- It does not currently process audio recordings.
- Generated minutes require human verification.

## 🔮 Future Enhancements

- Integrate Whisper for audio-to-text transcription.
- Introduce LLM-based meeting summarization.
- Improve decision and action item extraction.
- Implement speaker identification.
- Support long meeting transcripts.
- Add PDF and DOCX export.
- Introduce automated faithfulness evaluation.
- Implement human-in-the-loop review.

## 🔍 Accuracy and Reliability

Automated meeting documentation must preserve the meaning of the original conversation.

Future versions will focus on:
- Comparing generated information with the original transcript.
- Preventing fabricated decisions and action items.
- Maintaining accurate speaker attribution.
- Identifying missing or uncertain information.
- Requiring human review before final publication.

## 👩‍💻 Author

**Diksha Gadhave**

Computer Science Engineering Student

[GitHub Profile](https://github.com/DIKSHA1303)

---

*This project explores the use of Python and intelligent automation to simplify meeting documentation workflows.*

**Project Status:** Version 1 – Working Rule-Based Prototype
