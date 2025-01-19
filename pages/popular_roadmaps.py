import streamlit as st

def show_popular_roadmaps():
    st.title("Popular Roadmaps")
    st.write("Explore some of the most popular roadmaps.")
    
    # Embed the images directly and set the width to a smaller size (e.g., 100px for icon size)
    backend_img = "./thumb/backend.jpg"
    devops_img = "./thumb/devops.jpg"
    aws_img = "./thumb/aws.jpg"

    # Create columns for the row layout
    cols = st.columns(3)

    # Backend Developer Roadmap
    with cols[0]:
        st.image(backend_img, caption="Backend Developer Roadmap", use_container_width=False, width=100)
        with open("roadmap_pdf/backend.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download Backend Roadmap PDF", data=PDFbyte, file_name="backend_roadmap.pdf", mime="application/pdf")
    # DevOps Engineer Roadmap
    with cols[1]:
        st.image(devops_img, caption="DevOps Engineer Roadmap", use_container_width=False, width=100)
        with open("roadmap_pdf/devops.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download DevOps Roadmap PDF", data=PDFbyte, file_name="devops_roadmap.pdf", mime="application/pdf")

    # AWS Cloud Architect Roadmap
    with cols[2]:
        st.image(aws_img, caption="AWS Cloud Architect Roadmap", use_container_width=False, width=100)
        with open("roadmap_pdf/aws.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download AWS Cloud Architect Roadmap PDF", data=PDFbyte, file_name="aws.pdf", mime="application/pdf")

show_popular_roadmaps()
