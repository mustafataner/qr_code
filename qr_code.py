import streamlit as st
import pyqrcode
from PIL import Image
import io
import png



st.title('QR Kod Oluşturucu')

# Kullanıcıdan URL alın
url = st.text_input("QR kod oluşturmak istediğiniz linki giriniz:")

# QR kodu oluştur ve göster
if st.button('QR Kodu Oluştur'):
    if url:
        qr = pyqrcode.create(url)
        qr_buffer = io.BytesIO()
        qr.png(qr_buffer, scale=6)
        qr_buffer.seek(0)
        st.image(qr_buffer, use_column_width=True)

        # QR kodunu indirme butonu
        st.download_button(
            label="QR Kodunu İndir",
            data=qr_buffer,
            file_name='qr.png',
            mime='image/png'
        )

