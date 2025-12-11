import gradio as gr
import pandas as pd

# Load dataset
df = pd.read_csv("Metro_House_Rent.csv")


# --- Dynamic Area Options ---
def load_areas(selected_city):
    if selected_city is None:
        return gr.Dropdown(choices=[])
    areas = sorted(df[df["city"] == selected_city]["area"].unique())
    return gr.Dropdown(choices=areas, value=None)

# --- Prediction Logic ---
def predict(city, area, rooms, bath, park, floor, animal, furniture):
    total = (rooms * 1200) + (bath * 800) + (park * 500)

    return f"""
### 🏡 **Predicted Rent**
💰 **Estimated Rent:** ₹ {total:,}

📍 **City:** {city}  
📌 **Area:** {area}  
🛏️ Rooms: {rooms}  
🛁 Bathrooms: {bath}  
🚗 Parking: {park}  
🏢 Floor: {floor}  
🐾 Animal Allowance: {animal}  
🪑 Furniture: {furniture}  
"""

# --- UI ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple")) as app:

    gr.Markdown("""
    # 🏙️ **Metro House Rent Predictor**
    Choose City → Area updates automatically  
    Area is locked (No typing)
    """)

    with gr.Row():
        city = gr.Dropdown(
            choices=sorted(df["city"].unique()),
            label="🏙️ Select City",
            allow_custom_value=False
        )

        area = gr.Dropdown(
            choices=[],
            label="📍 Select Area",
            allow_custom_value=False
        )

    # Update area dropdown based on selected city
    city.change(fn=load_areas, inputs=city, outputs=area)

    with gr.Row():
        rooms = gr.Number(label="🛏️ Rooms", precision=0, value=1)
        bath = gr.Number(label="🛁 Bathrooms", precision=0, value=1)
        park = gr.Number(label="🚗 Parking Spaces", precision=0, value=0)

    with gr.Row():
        floor = gr.Dropdown(df["floor"].unique().tolist(), label="🏢 Floor")
        animal = gr.Dropdown(df["animal_allowance"].unique().tolist(), label="🐾 Animal Allowance")
        furniture = gr.Dropdown(df["furniture"].unique().tolist(), label="🪑 Furniture")

    btn = gr.Button("🔮 Predict Rent", variant="primary")
    out = gr.Markdown("")

    btn.click(
        predict,
        inputs=[city, area, rooms, bath, park, floor, animal, furniture],
        outputs=out
    )

app.launch()
