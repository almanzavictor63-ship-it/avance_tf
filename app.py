import streamlit as st
import pandas as pd

# Configura el título y presenta una startup ficticia de tienda en línea.
st.set_page_config(page_title="Calculadora de descuentos", page_icon="🛍️")
st.title("Calculadora de precio con descuento")
st.caption("Ejemplo hipotético: una tienda en línea calcula el precio de sus pedidos.")

# Pide los datos del pedido; los valores iniciales son solo ejemplos.
precio = st.number_input("Precio por producto (COP)", min_value=0.0, value=120_000.0, step=1_000.0)
cantidad = st.number_input("Cantidad de productos", min_value=1, value=2, step=1)
descuento = st.slider("Descuento (%)", min_value=0, max_value=90, value=15)

# Calcula el subtotal, el ahorro y el total que pagará el cliente.
subtotal = precio * cantidad
ahorro = subtotal * descuento / 100
total = subtotal - ahorro

# Muestra el resultado principal y cuánto dinero ahorra el pedido.
st.metric("Total a pagar (COP)", f"$ {total:,.0f}", delta=f"Ahorro: $ {ahorro:,.0f} COP")

# Organiza los datos del cálculo en una tabla sencilla.
resumen = pd.DataFrame({
    "Concepto": ["Precio por producto", "Cantidad", "Descuento", "Subtotal", "Ahorro", "Total a pagar"],
    "Valor": [precio, cantidad, f"{descuento}%", subtotal, ahorro, total],
})
st.dataframe(resumen, hide_index=True, use_container_width=True)
