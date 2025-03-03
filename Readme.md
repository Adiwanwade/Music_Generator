# 🎵 AI Song Generator
A cutting-edge AI-powered tool that generates original songs and music from text prompts. Built with state-of-the-art pretrained models, this project makes song creation accessible to everyone.

![AI Song Generator Banner](./Screenshots/Screenshot%202025-03-03%20130023.png)

## ✨ Features

- 🎶 **Music Generation**: Create instrumental tracks based on text descriptions
- 🎤 **Lyrics Generation**: Generate song lyrics based on themes and topics
- 🎸 **Style Control**: Choose from various musical genres and styles
- 🔊 **Voice Options**: Select different vocal styles for your songs
- ⏱️ **Duration Control**: Specify the length of your generated tracks
- 🖥️ **Simple Interface**: User-friendly interface for easy song creation

## 📋 Requirements

- Python 3.8+
- PyTorch 2.0+
- Transformers 4.30.0+
- CUDA-capable GPU (recommended)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Adiwanwade/Music_Generator

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 💻 Usage

### Local Installation

```python
from song_generator import ColabSongGenerator

# Initialize the generator
generator = ColabSongGenerator()

# Generate a song
audio = generator.generate_song(
    prompt="a summer day at the beach",
    style="pop",
    duration=15
)

# Play or save the audio
audio.write_audiofile("summer_song.wav")
```

### Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/ai-song-generator/blob/main/notebooks/song_generator.ipynb)

1. Open the notebook in Google Colab
2. Run the installation cell
3. Follow the interactive prompts to generate your song
4. Download your creation or play it directly in the notebook

## 🖼️ Screenshots

![Generator Interface](./Screenshots/Screenshot%202025-03-03%20130023.png)
*The song generator interface with style selection and generation controls*

![Song Visualization](./Screenshots/Screenshot%202025-03-03%20125624.png)
*Waveform visualization of a generated song with lyrics*

![Mobile Interface](./Screenshots/WhatsApp%20Image%202025-03-03%20at%202.40.43%20PM.jpeg)
*Mobile-friendly interface for on-the-go creation*

## 🔍 How It Works

This project combines several powerful AI models:

1. **Text Processing**: Analyzes your prompt to understand the musical intent
2. **Lyrics Generation**: Uses language models to create contextually relevant lyrics
3. **Music Generation**: Leverages Facebook's MusicGen to create the instrumental track
4. **Voice Synthesis** (Advanced version): Uses Bark to generate vocal performances
5. **Audio Mixing**: Combines the elements into a cohesive song

## ⚙️ Models

The project supports multiple model configurations:

| Model | Memory | Quality | Speed | Features |
|-------|--------|---------|-------|----------|
| Basic | Low    | Good    | Fast  | Music only |
| Standard | Medium | Better | Medium | Music + simple lyrics |
| Advanced | High | Best | Slow | Full songs with vocals |

## 🎮 Demo

Check out our [live demo](https://huggingface.co/spaces/Adiwanwade/AI_Music_Generator) on Hugging Face Spaces!

![Hugging Face Work Tree](./Screenshots/Screenshot%202025-03-03%20145013.png)
*The working Tree of the Hugging Face Spaces demo*

## 🔮 Future Development

- [ ] Fine-tuned models for better quality
- [ ] More vocal styles and voice cloning capabilities
- [ ] Improved mixing and mastering
- [ ] Export to multiple formats
- [ ] Collaborative editing features

## 📊 Performance

| Configuration | Generation Time | RAM Usage | GPU Memory |
|---------------|-----------------|-----------|------------|
| Basic (10s)   | ~10 seconds     | 4GB       | 2GB        |
| Standard (20s)| ~30 seconds     | 8GB       | 4GB        |
| Advanced (30s)| ~2 minutes      | 16GB      | 8GB+       |

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Facebook AI](https://ai.facebook.com/) for the MusicGen model
- [Suno AI](https://suno.ai) for inspiration
- [Hugging Face](https://huggingface.co/) for model hosting and transformers library
- [Bark](https://github.com/suno-ai/bark) for voice synthesis technology

## 📬 Contact

For questions, feedback, or collaboration, reach out to:

- 📧 Email:[Adiwanwade@gmail.com](Adiwanwade@gmail.com)
- 🐦 Twitter: [ADWanwade](https://twitter.com/ADWanwade)
- 💼 LinkedIn: [Adiwanwade](https://linkedin.com/in/Adiwanwade)

---
<div align="center">

Made with ❤️ and 🚀✨



</div>