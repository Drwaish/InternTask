#libraries
from transformers import pipeline, set_seed
from rembg import remove
import streamlit as st


#initialization
set_seed(32)
generator = pipeline('text-generation', model="facebook/opt-125m", do_sample=True)

#function that generates text
def generatedText(sent):
    var=generator(sent)
    return var[0]['generated_text']


#function to remove background from provided image
def removeBackground(input_path):
    #input = Image.open(input_path)
    output = remove(input_path)
    return output




#print(generatedText(input("Enter Sentence here")))

#Senetence Generation
st.header('Sentence Completion')
inpu=st.text_input("Enter Sentence here ")
if st.button('Generate Sentence'):
   output=generatedText(inpu)
  #st.write(output)
   st.text_area("Output", value=output, height=80)
#End of Sentence Generation


#Background Remover
img = st.file_uploader("Choose a file(.png only)", accept_multiple_files=False)
if img is not None:
    if st.button('Remove BackGround') :
        bytes_data = img.getvalue()
        out_img=removeBackground(bytes_data)
        btn=st.download_button(label='Image Download',
                   data=out_img,
                   file_name='out.png',  #name of every processed image
                   mime='image/png')
#End of Background Remover

