import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import  Image


st.set_page_config(page_title="Mummy's Kichen", page_icon=":tada:", layout="wide")
#def load_lottieurl(url):
   # r = requests.get(url)
    #if r.status_code != 200:
       # return None
    #return r.json()

#---use of css----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


def load_lottiefiles(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_cooking = load_lottiefiles("cooking/cooking.json")
img_tricolor = Image.open("img/tricolor.jpg")
img_mango = Image.open("img/mango.jpg")
img_mirchi = Image.open("img/mirchi.jpg")
img_pav = Image.open("img/pav.jpg")
img_lemon = Image.open("img/lemon.jpg")
img_upm = Image.open("img/upma.jpg")
#---header section---
with st.container():
    st.subheader("Hii , I am Ashu :wave:")
    st.title("A Content Creator and Chef ")
    st.write("I would like to share my knowledge with others and vice versa. Through this blog i am doing that and helping others in getting what they want.")
#st.write("[Learn More](url)")
#---List-----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """ 
            Heloo Guyss....
            - here I am sharing my mom's and granny's  recipe . 
            - Through this blog not only I am sharing my mom's recipe . 
            - I will also share the simple recipe which i have seen others making.
            - By the way this Blog will help full for bachelors.
            """
        )
        # st.write("[Learn More](url)")
    with right_column:
        st_lottie(
            lottie_cooking,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
           #renderer="svg",
            height=400,
            width=300,
            key=None,

        )

#-----start-----
with st.container():
    st.write("---")
    st.header("Here Are The List Of Recipes 😉")
    st.write("##")
    st.subheader("Healthy")
    st.write("##")
    st.subheader("Tricolor Veggie Delight Salad")
    image_column, text_column = st.columns((1,2))
    with image_column:

        st.image(img_tricolor)

    with text_column:

        st.subheader("Ingrediants")
        st.write(
            """ 
            of Tricolor Veggie Delight Salad....
            - 1 Cup cucumber, diced (green)
            - 1 cup carrots, grated (orange)
            - 1 cup white cabbage, finely shredded (white)
            - 1/2 cup corn kernels, boiled
            - 1/4 cup fresh coriander leaves,, chopped
            - Salt and black pepper to taste
            - Lemon juice for dressing
            
            In separate bowls, place the diced cucumber (green), grated carrots (orange), and shredded white cabbage (white).Add boiled corn kernels to each bowl.Toss the contents of each bowl with a pinch of salt and black pepper.Drizzle lemon juice over each bowl for dressing.Gently mix the ingredients in each bowl.To serve, arrange the green, orange, and white components on a plate in a tricolor pattern.Garnish with chopped fresh coriander leaves.
            """
        )
        #st.markdown("[watch video.....](url)")
    st.write("##")
    st.subheader("Mango Litchi Salad")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_mango)
    with text_column:
        st.subheader("Ingrediants")
        st.write(
            """ 
            of Mango Litchi Salad
            - 2 mangoes, diced
            - 1 cup litchis, peeled
            - 1 green chilli, melted
            - 1 tsp chaat masala
            - A handful of coriander leaves
            - 1/2 tsp black salt
            - 1 tsp lemon juice
            - 1/2 tsp roasted cumin powder
            
            To make this salad, add mangoes, litchi, and cucumber in a bowl and combine well. You can add some green chillies for spice.Now, sprinkle some chaat masala, black salt, and cumin powder over the salad.Squeeze lemon juice and gently toss everything together.Let the salad sit for around 10-15 minutes. This allows all the flavours to be absorbed. You could also pop it in the fridge at this point.Serve chilled with a garnish of fresh coriander leaves. Enjoy!
            """
        )
        # st.markdown("[watch video.....](url)")
#-----Snacks, Chinese, etc... ----
with st.container():
    st.write("---")
    st.header("Here Are The List Of Recipes 😉")
    st.write("##")
    st.subheader("Snacks, Chinese etc.....")
    st.write("##")
    st.subheader("Mirchi Bajji")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_mirchi)

    with text_column:
        st.subheader("Ingrediants")
        st.write(
            """ 
            Batter
            - 1 cup besan
            - 2 tbsp rice flour
            - 1/2 tsp salt
            - 1/4 tsp baking soda
            - 2 tbsp boiling oil
            - 3/4-1 cup water
            - 10 Mirchi/ Menshinkai (finger hot peppers)
            Filling
            - 1 tsp jeera/cumin powder
            - 1/4 tsp salt
            
            Make the Batter
            - Combine 1 cup besan, 2 tbsp rice flour, 1/2 tsp salt, and 1/4 tsp baking soda in a mixing bowl.
            Mix the dry ingredients together and then push them to the sides, so there is a little well in the middle.
            Add 2 tbsp boiling oil to the well. Mix in the oil with the dry ingredients.
            Slowly add 3/4 -1 cup water and mix in. Keep adding water and mixing until you get a smooth batter with no lumps and a runny consistency.

            Stuff the Mirchi
            - Slit the mirchi/ menshinkai down the middle, just 3/4 of the way down. It should still be connected on one side.
            Combine 1 tsp jeera powder with 1/4 tsp salt in a small bowl.
            Stuff the mirchi/ menshinkai evenly with this mixture. (Note: you could also add ginger, garlic, and or finely chopped onions.)
            Fry the Mirchi
            - Fill a frying pan about half full with oil. Heat at a medium flame.
            Dip the stuffed mirchi/ menshinkai in the batter. Coat completely with a thick, even layer of batter.
            Slowly drop a coated Mirchi into the frying pan. (Note: Make sure that there is enough oil to completely cover the Mirchi. Place as many Mirchi as you can in the oil, but spread them apart – don’t let them touch each other.)
            Deep fry all the Mirchi in batches until they turn golden and crispy. When you take them out of the oil, place them on a paper towel  (placed on a bowl or plate) to absorb the oil. Enjoy hot! 🙂
            """
        )
        # st.markdown("[watch video.....](url)")
    st.write("##")
    st.subheader("PavBhaji")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_pav)
    with text_column:
        st.subheader("Ingrediants")
        st.write(
            """ 
            Of PavBhaji
            - pav(Bread Roll) . 
            - 3  potatoes chopped in medium size (About 300g).
            - 1 cup cauliflower
            - rinse 1/2 to 3/4 cups of green peas. 
            - 1 cup chopped onions.
            - 1 cup chopped tomatoes.
            - 1/2 cup chopped bell pepper
            - 1 chilli
            - 1 tablespoon ginger garlic paste.
            - butter.
            - pav bhaji masala.
            
            Add all the Vegetables to a pressure cooker. Pour 1&1/2 cups water, it should be just enough to cover them partially.
            Wait for two whistles, When the pressure releases open the lid. Veggies should be soft cooked. Mash them well.
            To prepare masala, heate 1 tablespoon butter & 1 tablespoon oil in a pan. Add onions, saute till they turn translucent.
            Add 1 tablespoon ginger garlic paste and 1 green chilli. Fry until it smells good. Take care not to burn. Add chopped bell pepper fry for 2 min.
            Add chopped tomatoes an a teaspoon salt, fry till it turn mushy, soft and pulpy. Add a teasppon chilli powder and add a tablesppon pav bhaji masala powder. Mix well and fry for 2 to 3 min. add boiled and mashed veggies, add 1/2 to 3/4 cups water to bring consistency.
            Mix well allow it to boil and bring out flavor of masala. Add tablespoon of kasuri methi, when it reaches the desired consistency, add chopped coriender leaves.
            """
        )
        # st.markdown("[watch video.....](url)")
#----Home food-----
with st.container():
    st.write("---")
    st.header("Here Are The List Of Recipes 😉")
    st.write("##")
    st.subheader("Home Food")
    st.write("##")
    st.subheader("Lemon Rice")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lemon)

    with text_column:
        st.subheader("Ingrediants")
        st.write(
            """ 
            for Lemon Rice Recipe
            - Rice boiled 1 1/2 cups
            - Lemon juice 3 tablespoons
            - Oil 2 tablespoons
            - Mustard seeds 1/2 teaspoon
            - Asafoetida a pinch
            - Fenugreek seeds (methi dana) 1/2 teaspoon
            - Split black gram skinless (dhuli urad dal) 1 tablespoon
            - Curry leaves 10-12
            - Whole dry red chillies broken 2
            - Turmeric powder 1/2 tablespoon
            - Peanuts 1/2 cup
            - Salt to taste
            - Coconut fresh scraped 2 tablespoons
            
            Heat oil in a kadai. Add mustard seeds, hing, methi, urad dal and sauté till the dal turns golden.Add curry leaves, broken red chillies, turmeric powder and peanuts and continue to sauté. Add rice and salt and mix. Add lemon juice and mix well.
            Cook on low heat till the rice gets heated through. Garnish with coconut and serve hot.
            """
        )
        # st.markdown("[watch video.....](url)")
    st.write("##")
    st.subheader("Upma")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_upm)
    with text_column:
        st.subheader("Ingrediants")
        st.write(
            """ 
            for  Upma Recipe
            - Semolina (rawa/suji) 1 1/2 cups
            - Carrot cut into ¼ inch cubes and blanched 1 medium
            - French beans cut into ¼ inch cubes and blanched 6-8
            - Green peas blanched 1/4 cup
            - Green capsicum 1 medium
            - Onion 1 medium
            - Green chillies 3
            - Ginger 1 inch piece
            - Extra virgin olive oil 2 tablespoons
            - Mustard seeds 1/2 teaspoon
            - Curry leaves 15-20
            - Split black gram skinless (dhuli urad dal) 2 teaspoons
            - Salt to taste
            
            Chop onion, green chillies and ginger. Heat extra virgin olive oil in a non stick pan. Add mustard seeds, ginger, curry leaves and urad dal and sauté for 1 minute.
            Add onion and sauté for 2 minutes. Heat 3 cups water in another non stick pan. When the onion becomes golden, add semolina and sauté for 2-3 minutes.
            Add green chillies, salt and mix. Sauté for 1 minute. Chop green capsicum and set aside.
            Add hot water to the pan and cook till most of the water is absorbed. Add carrot, beans, peas and mix. Cover and cook for 1-2 minutes.
            Add capsicum and mix. Cover again and cook till the semolina is properly cooked. Serve hot.
            You can also garnish with coriander leaves and/or freshly scraped coconut and serve.
            """
        )
        # st.markdown("[watch video.....](url)")
#----Contact----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/techjuniors114@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="message" placeholder="your message here" required></textarea>
        <button type="submit">Send</button>
    </form
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

