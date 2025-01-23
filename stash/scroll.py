import streamlit as st
from PIL import Image

st.markdown("<h2 style='text-align: center'>For OCR app</h1>", unsafe_allow_html=True)
image = st.file_uploader("Upload Image",type=['jpg','png','jpeg','JPG'])

col1, col2 = st.columns(2)

if image is not None:
    with col1:
        input_image = Image.open(image) #read image
        width, height = input_image.size
        st.image(input_image, caption="Input Image is: ") #display image
        extract_button = st.button("Extract text")

        if extract_button:
            with col2:
                text = "OCR text with a lot of errors and need to edit it "
                output = st.text_area("Output is: ", text, height=220)
                st.download_button(label="Download data as docx", data=output, file_name='output.docx', mime='docx')
                st.success('Text Extraction Completed!')

else:
    st.write("Upload an Image")
