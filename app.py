import streamlit as st
import tempfile
import os
import sys
from PIL import Image

# ==========================================
# Add Project Root
# ==========================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# ==========================================
# Imports
# ==========================================

from src.classifier import predict_image
from src.recommendation import get_recommendation

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="E-Waste Disposal Assistant",
    page_icon="♻️",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("♻️ E-Waste Disposal Assistant")

st.markdown("""
### AI-Powered Sustainable E-Waste Management

Upload an image of an electronic item.

The AI will:

✅ Identify the item  
✅ Show confidence score  
✅ Determine recyclability  
✅ Classify waste category  
✅ Suggest disposal methods  
✅ Provide sustainability tips  
✅ Measure environmental impact  
✅ Support SDG 12
""")

# ==========================================
# Upload Image
# ==========================================

uploaded_file = st.file_uploader(
    "📤 Upload Electronic Item Image",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# Prediction Section
# ==========================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("🔍 Analyze E-Waste"):

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        )

        temp_file.write(
            uploaded_file.getbuffer()
        )

        temp_file.close()

        try:

            # ==================================
            # AI Prediction
            # ==================================

            label, confidence = predict_image(
                temp_file.name
            )

            normalized_label = label.lower()
            normalized_label = normalized_label.replace(" ", "_").replace("-", "_")

            # ==================================
            # Recommendation Engine
            # ==================================

            info = get_recommendation(normalized_label)


            # ==================================
            # Safe Defaults
            # ==================================

            recyclable = info.get(
                "recyclable",
                "⚠️ Check Local Recycling Guidelines"
            )

            category = info.get(
                "category",
                "General Electronic Waste"
            )

            disposal = info.get(
                "disposal",
                "Take the item to a certified e-waste recycling center."
            )

            tips = info.get(
                "tips",
                [
                    "Repair before replacing.",
                    "Donate if still functional.",
                    "Use certified recycling centers."
                ]
            )

            impact = info.get(
                "impact",
                "Responsible recycling reduces landfill waste."
            )

            sdg = info.get(
                "sdg",
                "SDG 12 – Responsible Consumption and Production"
            )

            # ==================================
            # Display Results
            # ==================================

            st.success("✅ Analysis Complete")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("📱 Detected Item")

                st.write(
                    label.replace(
                        "_",
                        " "
                    ).title()
                )

                st.subheader("🎯 Confidence Score")

                st.metric(
                    "AI Confidence",
                    f"{confidence * 100:.2f}%"
                )

            with col2:

                st.subheader("♻️ Recyclable?")

                if recyclable.startswith("✅"):
                    st.success(recyclable)
                elif recyclable.startswith("⚠️"):
                    st.warning(recyclable)
                else:
                    st.info(recyclable)

                st.subheader("🗂 Waste Category")

                st.info(
                    category
                )

            # ==================================

            st.subheader(
                "🛠 Disposal Method"
            )

            st.write(
                disposal
            )

            # ==================================

            st.subheader(
                "🌱 Sustainability Tips"
            )

            for tip in tips:

                st.write(
                    f"✅ {tip}"
                )

            # ==================================

            st.subheader(
                "🌍 Environmental Impact"
            )

            st.success(
                impact
            )

            # ==================================

            st.subheader(
                "🎯 SDG Impact"
            )

            st.info(
                sdg
            )

            # ==================================

            st.subheader(
                "📊 Sustainability Score"
            )

            score = int(
                confidence * 100
            )

            st.progress(
                score / 100
            )

            st.write(
                f"Sustainability Awareness Score: {score}/100"
            )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

        finally:

            if os.path.exists(
                temp_file.name
            ):
                os.remove(
                    temp_file.name
                )

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.markdown("""
### About This Project

This AI-powered E-Waste Disposal Assistant helps users:

- Identify electronic waste using AI
- Learn proper disposal methods
- Promote recycling and reuse
- Reduce environmental pollution
- Support sustainable consumption

🌍 **Supported Sustainable Development Goal**

**SDG 12 – Responsible Consumption and Production**
""")