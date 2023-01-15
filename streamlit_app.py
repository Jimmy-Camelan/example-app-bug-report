import streamlit as st
import time

html_string = """
            <audio id='audio' controls autoplay>
  <source src="https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
            """

sound = st.empty()
sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
time.sleep(2)  # wait for 2 seconds to finish the playing of the audio
sound_player = st.empty()
html_string = """
            <script type="application/javascript">
  document.getElementById("audio").play();
  console.log("It's play time!!");
</script>
            """
sound_player.markdown(html_string, unsafe_allow_html=True)
