import streamlit as st
from streamlit_webrtc import webrtc_streamer

import os
from twilio.rest import Client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
token = client.tokens.create()

st.title("ทดสอบกล้อง")


webrtc_streamer(key="test",
                media_stream_constraints={"video": True,"audio": False})
