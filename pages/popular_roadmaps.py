import streamlit as st

def show_popular_roadmaps():
    # Title with green color
    st.markdown("<h1 style='color: green; text-align: center;'>Popular Roadmaps</h1>", unsafe_allow_html=True)
    st.write("Explore some of the most popular roadmaps. Download the PDF versions to get started on your journey!")

    # Add some spacing
    st.markdown("<hr>", unsafe_allow_html=True)

    # Roadmap Images and Download Buttons
    # Embed the images directly and set the width to a smaller size (e.g., 200px for better visibility)
    backend_img = "./thumb/backend.jpg"
    devops_img = "./thumb/devops.jpg"
    aws_img = "./thumb/aws.jpg"

    # Create a layout with columns for better visual arrangement
    cols = st.columns(3)

    # Backend Developer Roadmap
    with cols[0]:
        st.image(backend_img, caption="Backend Developer Roadmap", use_container_width=True, width=100)
        st.markdown("<br>", unsafe_allow_html=True)  # Add some space between the image and the button
        with open("roadmap_pdf/backend.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="Download Backend Roadmap PDF",
            data=PDFbyte,
            file_name="backend_roadmap.pdf",
            mime="application/pdf",
            use_container_width=True,
            key="backend_roadmap"
        )

    # DevOps Engineer Roadmap
    with cols[1]:
        st.image(devops_img, caption="DevOps Engineer Roadmap", use_container_width=True, width=200)
        st.markdown("<br>", unsafe_allow_html=True)
        with open("roadmap_pdf/devops.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="Download DevOps Roadmap PDF",
            data=PDFbyte,
            file_name="devops_roadmap.pdf",
            mime="application/pdf",
            use_container_width=True,
            key="devops_roadmap"
        )

    # AWS Cloud Architect Roadmap
    with cols[2]:
        st.image(aws_img, caption="AWS Cloud Architect Roadmap", use_container_width=True, width=200)
        st.markdown("<br>", unsafe_allow_html=True)
        with open("roadmap_pdf/aws.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="Download AWS Cloud Architect Roadmap PDF",
            data=PDFbyte,
            file_name="aws_roadmap.pdf",
            mime="application/pdf",
            use_container_width=True,
            key="aws_roadmap"
        )

# Call the function to display the page
show_popular_roadmaps()
