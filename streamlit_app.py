import streamlit as st
import time

html_string = """
            <audio id='audio' controls autoplay>
  <source src="https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
<script type="application/javascript">
const myTimeout = setTimeout(playAudio, 5000);

function playAudio() {
  document.getElementById('audio').play()
  clearTimeout(myTimeout);
}
</script>
            """

sound = st.empty()
sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
time.sleep(2)
