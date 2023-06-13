import streamlit as st

def convert_length(value, from_unit, to_unit):
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }

    result = value * units[from_unit] / units[to_unit]
    return result

st.title("Konversi Ukuran")
st.write("Masukkan nilai dan satuan awal, serta satuan yang diinginkan.")

value = st.number_input("Masukkan nilai", min_value=0.0)
from_unit = st.selectbox("Satuan awal", ("mm", "cm", "m", "km", "in", "ft", "yd", "mi"))
to_unit = st.selectbox("Satuan yang diinginkan", ("mm", "cm", "m", "km", "in", "ft", "yd", "mi"))

result = convert_length(value, from_unit, to_unit)

st.write(f"Hasil: {result} {to_unit}")


