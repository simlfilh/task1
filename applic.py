import streamlit as st

st.title("🔘 Простое приложение с кнопками")

# Кнопка 1
if st.button("О проекте"):
    st.write("Это учебный проект на Streamlit!")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)

# Кнопка 2
if st.button("Контакты"):
    st.write("📧 Email: example@mail.com")
    st.write("📞 Телефон: +7 (123) 456-78-90")

# Кнопка 3 (секретная)
if st.button("Секретный раздел 🔒"):
    st.balloons()  # Запускает анимацию шариков
    st.success("🎉 Вы нашли секретную функцию!")
    st.write("Попробуйте другие кнопки :)")