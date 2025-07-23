from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube

app = Flask(__name__)

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        video_id = YouTube(video_url).video_id
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify({'transcript': transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
