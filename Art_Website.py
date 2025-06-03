import streamlit as st

image_path='/Users/hanchang/mu_code/image.py/Background_photo.jpg'
st.image(image_path, use_column_width=True)

st.title(":rainbow[Basic Knowledge of Art] 🥳")
st.subheader("Have fun with art: Learn about art elements, art principles and famous artworks!")

st.write(" ")
st.write(" ")
st.write("What is art? It is more than just drawing or painting, it is a way to share thoughts, emotions and imagination with the world. Some people appreciate art for its aesthetic beauty, whereas others see art as a window into humanity. As Pablo Picasso once said, :rainbow[‘The purpose of art is washing the dust of daily life off our souls.’]  In this website, let's dive into the exciting world of art, explore its basic knowledge and view some of the world’s most famous masterpieces!")
st.write("什么是艺术？它不仅仅是绘画或素描，更是一种与世界分享思想、情感和想象的方式。有些人欣赏艺术的美学之美，而另一些人则将艺术视为了解人性的窗口。正如巴勃罗·毕加索曾经说过的那样：:rainbow[‘艺术的目的在于洗去我们灵魂中日常生活的尘埃。’] 在这个网站上，让我们一起深入艺术的精彩世界，探索其基础知识，并欣赏一些世界上最著名的杰作！")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.subheader(":red[Art Elements 艺术元素] 🖌️")
image_path='/Users/hanchang/mu_code/image.py/art_elements.png'
st.image(image_path, use_column_width=True)
st.write("The seven elements of art are line, shape, form, space, value, color, and texture. They are the building blocks of any artworks and learning them can help you create a more expressive and impactful artwork.")
st.write("艺术的七个元素是线条、形状、形态、空间、明暗、色彩和肌理。它们是任何艺术作品的基本构成要素，学习它们有助于你创作出更具表现力和感染力的艺术作品。")
if st.button(":red[Find out more about art elements here! 点击这里了解更多艺术元素！]"):
    st.switch_page("pages/Art_Elements.py")

st.write(" ")
st.write(" ")
st.subheader(":orange[Art Principles 艺术原则] 🎨")
image_path='/Users/hanchang/mu_code/image.py/art_principles.png'
st.image(image_path, use_column_width=True)
st.write("Art principles are also known as the principles of art and design. The nine principles of art are pattern, balance, variety, emphasis, movement, scale, harmony, unity and contrast. They are the ways art elements are applied and arranged and they can help you create a more visually interesting or aesthetically pleasing artwork.")
st.write("艺术原则也被称为艺术与设计原则。艺术的九个原则是图案、平衡、变化、强调、运动、比例、和谐、统一和对比。它们是艺术元素的应用与安排，能够帮助你创作出更具视觉吸引力或更令人赏心悦目的艺术作品。")
if st.button(":orange[Find out more about art principles here! 点击这里了解更多艺术原则！]"):
    st.switch_page("pages/Art_Principles.py")

st.write(" ")
st.write(" ")
st.subheader(":blue[Famous Artworks 著名艺术作品] 🖼️")
image_path='/Users/hanchang/mu_code/image.py/famous_artworks.png'
st.image(image_path, use_column_width=True)
st.write("Across the globe, there are numerous famous artworks, many of which have a long-lasting impact on society. Seven of these well-known artworks are Mona Lisa, Girl with a Pearl Earring, The Persistence of Memory, Starry Night, Guernica, Impression, Sunrise, and The Great Wave off Kanagawa. Feel Free to search for more famous artworks online if you are interested!")
st.write("在世界各地，有无数著名的艺术作品，其中许多都对社会产生了深远的影响。这些知名的艺术作品包括《蒙娜丽莎》《戴珍珠耳环的少女》《记忆的永恒》《星夜》《格尔尼卡》《印象·日出》和《神奈川冲浪里》。如果你感兴趣，可以随时在网上搜索更多著名艺术作品！")
if st.button(":blue[Find out more about famous artworks here! 点击这里了解更多艺术作品！]"):
    st.switch_page("pages/Famous_Artworks.py")

st.write(" ")
st.write(" ")
st.divider()
st.subheader(":rainbow[Game Section] 👾")
st.write("Bluey is a cute little dog, and she's on a quest to find her little sister, Bingo. Along the way, Bluey meets a wizard who tells her that Bingo has been taken and is now under the wizard’s spell. The only way Bluey can rescue her sister is by answering some art-related questions correctly. Do you want to help Bluey answer the questions and save Bingo?")
st.write("布鲁伊是一只可爱的小狗，她正在寻找自己的妹妹宾果。途中，布鲁伊遇到了一位巫师，巫师告诉她宾果已被带走，现在正处于他的魔法控制之下。布鲁伊要想救出妹妹，就必须正确回答一些与艺术相关的问题。你想帮助布鲁伊回答问题并救出宾果吗？")
image_path='/Users/hanchang/mu_code/image.py/Game1.png'
st.image(image_path, use_column_width=True)

easy_questions = [
    {"question": "How many dimensions do shapes have?", "options": ["one", "two", "three"], "correct": "two"},
    {"question": "What is the two extremes of the value scale?", "options": ["warm and cool", "light and dark", "soft and hard"], "correct": "light and dark"},
    {"question": "What does soft textures make people feel?", "options": ["calm and serene", "confused and anxious", "energy and tension"], "correct": "calm and serene"},
    {"question": "Which type of symmetry does the seeds of a dandelion follow?", "options": ["Bilateral symmetry", "asymmetry", "radial symmetry"], "correct": "radial symmetry"},
    {"question": "What is one effect of creating movement in art?", "options": ["adds compositional interest", "gives a sense of stillness", "makes artwork seem three-dimensional"], "correct": "adds compositional interest"},
    {"question": "Who is the painter of Girl with a Pearl Earring?", "options": ["Leonardo da Vinci", "Pablo Picasso", "Johannes Vermeer"], "correct": "Johannes Vermeer"},
    {"question": "What technique did Vincent van Gogh use in his Starry Night?", "options": ["pointillism", "impasto", "sfumato"], "correct": "impasto"}
]

hard_questions = [
    {"question": "What feeling do zigzag lines evoke?", "options": ["unrest and chaos", "harmony and relaxation", "symmetry and order"], "correct": "unrest and chaos"},
    {"question": "Which of these is the technique artists use to create an illusion of form on canvas?", "options": ["proximity", "trompe l’oeil", "overlapping"], "correct": "trompe l’oeil"},
    {"question": "Which color is used to draw mountains in the distance to suggest they are far away from the viewer?", "options": ["grayish color", "bluish color", "yellowish color"], "correct": "bluish color"},
    {"question": "Which of these is a tertiary color?", "options": ["magenta", "lavender", "green"], "correct": "magenta"},
    {"question": "What is one effect of creating pattern in art?", "options": ["make composition appear chaotic", "reduce the use of art elements", "creates visual interest and rhythm"], "correct": "creates visual interest and rhythm"},
    {"question": "Which of these is a way to create variety in art?", "options": ["repeat", "elaboration", "symmetrical balance"], "correct": "elaboration"},
    {"question": "Which of these is NOT small scale art?", "options": ["Mona Lisa", "The Persistence of Memory", "Guernica"], "correct": "Guernica"},
    {"question": "Which is NOT a way to create unity?", "options": ["simplicity", "continuation", "contrast"], "correct": "contrast"},
    {"question": "Which of these shows the strongest contrast?", "options": ["amber and violet", "chartreuse and teal", "vermillion and magenta"], "correct": "amber and violet"},
    {"question": "Which year was Impression, sunrise created?", "options": ["1889", "1872", "1881"], "correct": "1872"},
    {"question": "Which art movement does The Persistence of Memory belong?", "options": ["surrealism", "cubism", "futurism"], "correct": "surrealism"},
    {"question": "What is the nationality of the painter of The Starry Night?", "options": ["French", "English", "Dutch"], "correct": "Dutch"},
    {"question": "Which statement about The Great Wave Off Kanagawa is NOT correct?", "options": ["this artwork is painted on a large mural.", "this artwork is painted during the Edo period.", "the genre of this artwork is ukiyo-e."], "correct": "this artwork is painted on a large mural."}
]

def score(user_answers, questions):
    correct_answers = 0
    for i, answer in enumerate(user_answers):
        if answer == questions[i]['correct']:
            correct_answers += 1
    return correct_answers

def game_section():
    mode = st.selectbox("Select Difficulty Mode(请选择一个难度等级）:", ["Easy (简单)", "Hard (困难)"])

    if mode == "Easy (简单)":
        questions = easy_questions
        score_threshold = 6
        success_message = "Congratulations! You won the game and helped Bluey meet her sister!"
        failure_message = "Sorry, you lost the game... It’s okay! Let’s try again!"
    else:
        questions = hard_questions
        score_threshold = 12
        success_message = "Awesome! You won the game and helped Bluey meet her sister!"
        failure_message = "Sorry, you lost the game... It’s okay! You are already doing great! Let’s try again!"

    user_answers = []

    for i, q in enumerate(questions):
        st.write(q["question"])
        answer = st.radio("", q["options"], key=f"q{i}", index=None)
        user_answers.append(answer)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Submit"):
        correct_count = score(user_answers, questions)
        st.write(f"Your accuracy is: {correct_count}/{len(questions)}")

        if correct_count >= score_threshold:
            st.success(success_message)
            st.image('/Users/hanchang/mu_code/image.py/Game2.png', use_column_width=True)
        else:
            st.warning(failure_message)

if __name__ == "__main__":
    game_section()
