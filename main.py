import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy.io.wavfile
import numpy as np
from typing import Dict, Optional
import gradio as gr
import os
from datetime import datetime

class SimpleMusicGenerator:
    def __init__(self):
        # Load the pretrained MusicGen model
        self.processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
        self.model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
        
        # Available voice/melody styles (these are what MusicGen was trained on)
        self.available_styles = [
            "pop", "rock", "hip hop", "electronic", "jazz", 
            "classical", "ambient", "folk", "metal"
        ]
        
    def generate_music(
        self,
        prompt: str,
        style: str = "pop",
        duration: int = 10,
        temperature: float = 1.0
    ) -> Dict:
        """
        Generate music based on text prompt
        
        Args:
            prompt: Text description of the desired music
            style: Music style/genre
            duration: Duration in seconds (max 30)
            temperature: Controls randomness (0.0-1.0)
        """
        try:
            # Combine prompt with style
            full_prompt = f"{style} music {prompt}"
            
            # Set generation parameters
            inputs = self.processor(
                text=[full_prompt],
                padding=True,
                return_tensors="pt",
            )
            
            # Generate audio
            audio_values = self.model.generate(
                **inputs,
                do_sample=True,
                guidance_scale=3,
                max_new_tokens=duration * 50,  # Approximate tokens per second
                temperature=temperature
            )
            
            # Convert to numpy array
            audio_data = audio_values[0, 0].numpy()
            
            # Save the audio file
            output_path = self._save_audio(audio_data)
            
            return {
                "status": "success",
                "output_path": output_path,
                "prompt": full_prompt
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def _save_audio(self, audio_data: np.ndarray) -> str:
        """Save the generated audio to a WAV file"""
        # Create output directory if it doesn't exist
        output_dir = "generated_music"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"music_{timestamp}.wav"
        output_path = os.path.join(output_dir, filename)
        
        # Save as WAV file
        scipy.io.wavfile.write(
            output_path,
            rate=32000,  # MusicGen's sample rate
            data=(audio_data * 32767).astype(np.int16)  # Convert to 16-bit PCM
        )
        
        return output_path

def create_gradio_interface():
    """Create a simple web interface using Gradio"""
    generator = SimpleMusicGenerator()
    
    def generate(prompt, style, duration, temperature):
        result = generator.generate_music(
            prompt=prompt,
            style=style,
            duration=min(int(duration), 30),  # Limit to 30 seconds
            temperature=float(temperature)
        )
        
        if result["status"] == "success":
            return result["output_path"]
        else:
            return f"Error: {result['message']}"
    
    # Create the interface
    iface = gr.Interface(
        fn=generate,
        inputs=[
            gr.Textbox(label="Describe your music", placeholder="A happy melody with piano..."),
            gr.Dropdown(choices=generator.available_styles, label="Style", value="pop"),
            gr.Slider(minimum=5, maximum=30, value=10, label="Duration (seconds)"),
            gr.Slider(minimum=0.1, maximum=1.0, value=0.8, label="Creativity (temperature)")
        ],
        outputs=gr.Audio(label="Generated Music"),
        title="AI Music Generator",
        description="Generate music from text descriptions using MusicGen"
    )
    
    return iface

def main():
    # Create and launch the web interface
    iface = create_gradio_interface()
    iface.launch()

if __name__ == "__main__":
    main()