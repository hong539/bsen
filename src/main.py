# answer from Bing
# 如果您想使用其他語言，例如 C/C++ 或 Python，您可以使用 Native Messaging API 將其與 Chrome/Edge 擴充功能進行通信。
# Native Messaging API 允許本機應用程序與瀏覽器擴充程序進行通信，從而實現更高級的功能。以下是一個簡單的範例程式碼，可用於使用 Python 創建書籤：
import json
import struct
import sys

def send_message(message):
    # Write message size.
    sys.stdout.write(struct.pack('I', len(message)))
    # Write the message itself.
    sys.stdout.write(message)
    sys.stdout.flush()

def read_message():
    # Read the message length (first 4 bytes).
    text_length_bytes = sys.stdin.read(4)
    if not text_length_bytes:
        sys.exit(0)
    # Unpack message length as 4 byte integer.
    text_length = struct.unpack('i', text_length_bytes)[0]
    # Read the text (JSON object) of the message.
    text = sys.stdin.read(text_length).decode('utf-8')
    return json.loads(text)

def main():
    while True:
        # Read a message from stdin and decode it.
        message = read_message()
        if message.get('type') == 'ping':
            send_message(json.dumps({'type': 'pong'}))
        elif message.get('action') == 'create_bookmark':
            chrome.bookmarks.create({'title': message.get('title'), 'url': message.get('url')})
            send_message(json.dumps({'result': 'success'}))

if __name__ == '__main__':
    main()