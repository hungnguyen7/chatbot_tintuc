# Cách cài đặt

***Nên sử dụng Anaconda hoặc virtualenv để tạo môi trường ảo***
1. Cài đặt các package có trong file `requirements.txt`

1.a. Nếu bị lỗi PyAudio hãy tìm hiểu cách khắc phục tại https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14 

1.b. Nếu bị lỗi gói google-api-python-client thì chạy câu lệnh pip install --upgrade google-api-python-client

2. Gõ lệnh `rasa run actions` để chạy custom action: lấy tin tức, lấy lịch

3. Sử dụng lệnh `rasa shell` hoặc `rasa x` để tương tác với chatbot

# Để khởi động voice bot thực hiện các lệnh dưới đây

Terminal 1: `rasa run actions` để chạy file custom action

Terminal 2: `rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml` để kích hoạt Rest API Rasa

Terminal 3: `python voice_bot.py` để chạy file nhận dạng giọng nói