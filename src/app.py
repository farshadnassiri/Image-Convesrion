from io import BytesIO

from PIL import Image
import streamlit as st

from utils import convert_image_type, resize_image


def main():
    st.title(':zap: Image Processing App')
    upload_file=st.file_uploader("Choose an image",type=["jpg", "jpeg", "png"])
    if upload_file is None:
        return
    image=Image.open(upload_file,)
    st.image(image,caption="Your Image")
    process_type=st.radio("Select the process type:",["Resize", "Type Conversion"])  

    if process_type =="Resize":
        keep_aspect_ratio=st.checkbox("Keep aspect ratio",True)
        col1, col2 = st.columns(2)

        if keep_aspect_ratio:
            width=col1.number_input("Width",value=image.width)
            aspect_ratio=image.width/image.height  
            height=col2.number_input("height",value=int(width/aspect_ratio),disabled=True)
        else:
            width=col1.number_input("Width",value=image.width)
            height=col2.number_input("height",value=image.height)

        if st.button("Resize image"):
            resized_image=resize_image(image,width,height,keep_aspect_ratio) 
            st.image(caption="Resized image:",image=resized_image)
            result_buffer=BytesIO()
            resized_image.save(result_buffer,"PNG")  
            st.download_button("Download Image",
                data=result_buffer.getvalue(),
                file_name="resized image.png",
                mime="image/png"

            ) 

    else:
        output_format = st.selectbox("Select output format", ["JPEG", "PNG"])
        if st.button("Convert Image Type"):
            converted_image = convert_image_type(image, output_format)
            st.image(converted_image, caption=f'Image Converted to {output_format}')
            result_buffer = BytesIO()
            converted_image.save(result_buffer, format=output_format.upper())
            st.download_button(
                label="Download Image",
                data=result_buffer.getvalue(),
                file_name=f"converted_image.{output_format.lower()}",
                mime=f"image/{output_format.lower()}"
            )





        