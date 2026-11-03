
## Current Implementation Status

Version 1 is a working rule-based Python prototype.

### Implemented
- Transcript file reading
- Speaker statement extraction
- Decision keyword detection
- Possible action item identification
- Markdown meeting minutes generation

### Planned Enhancements
- Whisper-based audio transcription
- LLM-powered summarization
- Improved action item extraction
- Speaker attribution
- Human-in-the-loop accuracy verification

### Running the Project

```bash
python main.py sample_transcript.txt
```

### Limitations

The current implementation uses keyword-based extraction. It does not understand context like an LLM and may incorrectly classify statements. All generated minutes require human verification.
