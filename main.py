import streamlit as st

st.title("Animal Liking App")

animals = ['cat', 'dog', 'fish', 'turtle', 'hare', 'hamster']

liked_animals = []
disliked_animals = []

for animal in animals:
    st.subheader(f"Do you like {animal}?")

    yes_key = f"yes_{animal}"
    no_key = f"no_{animal}"

    yes_button = st.button("YES", key=yes_key)
    no_button = st.button("NO", key=no_key)

    while not yes_button and not no_button:
        pass

    if yes_button:
        liked_animals.append(animal)
    elif no_button:
        disliked_animals.append(animal)
    
# Display the list of liked animals
st.subheader("Liked Animals:")
st.write(liked_animals)