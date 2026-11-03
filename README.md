
# Meeting Minutes Generator

## 1. Project Overview

The Meeting Minutes Generator is an AI-powered system designed to convert recorded meeting conversations into structured meeting minutes.

The system uses speech-to-text technology and Large Language Models (LLMs) to extract important information from meeting recordings.

## 2. Problem Statement

Manually preparing meeting minutes can be time-consuming. Important decisions and action items may also be overlooked during manual note-taking.

This project explores how AI can automate the process while maintaining the accuracy and reliability of meeting information.

## 3. System Workflow

1. Upload a meeting audio recording.
2. Convert speech into text using Whisper.
3. Process the transcript.
4. Generate structured meeting minutes using an LLM.
5. Organize the output into predefined sections.
6. Review the generated minutes for accuracy.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend processing |
| Whisper | Speech-to-text transcription |
| Large Language Model | Meeting summarization |
| Prompt Engineering | Structured output generation |

## 5. Expected Output

The generated meeting minutes contain:

- Meeting summary
- Key discussion points
- Decisions made
- Action items
- Assigned owners, when explicitly identifiable

## 6. Accuracy and Reliability

AI-generated content may contain hallucinations or incorrect interpretations.

To reduce these risks, the system should:

- Compare generated decisions against the original transcript.
- Verify action items before assigning owners.
- Avoid inventing missing information.
- Preserve uncertainty when speaker attribution is unclear.
- Include human review before finalizing meeting minutes.

## 7. Future Improvements

- Speaker identification.
- Support for longer recordings.
- Automatic detection of missed action items.
- Export to PDF and DOCX.
- Evaluation of summary faithfulness.

## 8. Conclusion

This project demonstrates the application of Generative AI and speech recognition to automate a practical documentation task.

**Project Category:** Generative AI  
**Language:** Python  
**Status:** Academic project / development
