# baidu_tts

A Python lib of Baidu TTS.

## Installation

    $ pip install baidu_tts

## Usage

```python
from baidu_tts import BaiduTTS


tts = BaiduTTS(YOUR_API_KEY, YOUR_SECRET_KEY)
sound_buffer = tts.say('你好')  # get sound buffer

sound_buffer.write('/tmp/hello.mp3')  # save to file
content = sound_buffer.read()  # get binary content

stream = sound_buffer.stream  # get binary stream

# iter content
for chunk in sound_buffer.iter_content(chunk_size=1024):
    if chunk:
        ...
```

## License

MIT
