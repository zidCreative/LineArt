import streamlit as st
from skimage import io
from skimage import color
from skimage import filters
from skimage import exposure
from skimage import img_as_float

st.title("Program Deteksi Garis Tepi")
st.sidebar.image("zidCreative_putih.png")
gamb = st.file_uploader("Upload gambar yang ingin anda konversi", type=['jpg' , 'jpeg', 'png' ])	

if gamb is not None :
    img = io.imread(gamb)
    atur = st.slider("Atur ketajaman",0.0,2.0,0.1)
    col1, col2 = st.columns(2)
    col1.write("Gambar Asli")
    col1.image(img)
    
    if atur > 0.0:
        imge = color.rgb2gray(img)
        edge = filters.sobel(imge)
        pad = img_as_float(edge)
        gamma_corrected = exposure.adjust_gamma(pad, atur)
        col2.write("Gambar Line Art")        
        col2.image(gamma_corrected)
        
        st.success("Selamat, gambar berhasil dikonversi. klik kanan dan simpan untuk menyimpan")
        
        

        
    



