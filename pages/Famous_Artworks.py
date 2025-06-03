import streamlit as st

if st.button("Back to home page"):
    st.switch_page("Art_website.py")

st.title(":rainbow[Famous Artworks] 🌌")

st.write("The slider below is a timeline of some of the world’s most famous artworks. Play with this slider to view these artworks and read some important information about them!")
st.write("下面的滑块是世界上一些著名艺术作品的时间线。拖动滑块查看这些艺术品，并阅读有关它们的一些重要信息吧!")

selected_year = st.select_slider(
    "Select a time in history (请选择一个时间点）",
    options=[
        "1503-1519",
        "1665",
        "1830-1832",
        "1872",
        "1889",
        "1931",
        "1937",
    ],
)

if selected_year == "1503-1519":
    image_path='/Users/hanchang/mu_code/image.py/Monalisa.png'
    st.image(image_path, use_column_width=True)
    st.subheader("Mona Lisa 《蒙娜丽莎》🧐")
    st.markdown("**Artist:** Leonardo da Vinci (Italian)  \n**Media:** oil painting on a poplar wood panel  \n**Year:** 1503-1519  \n**Current museum:** Louvre Museum, Paris  \n**Keywords:** half-body portrait, Renaissance *(period in European civilization characterized by revival of Classical learning and wisdom)*, Sfumato *(the use of fine shading)*")
    st.markdown("**艺术家:** 列奥纳多·达·芬奇（意大利）  \n**媒介:** 木板油画  \n**创作时间:** 1503 - 1519 年  \n**现藏博物馆:** 巴黎卢浮宫  \n**关键词:** 半身肖像画、文艺复兴 *(欧洲文明中以古典学识和智慧复兴为特征的时期)*、晕涂法 *(精细的明暗过渡技法)*")

if selected_year == "1665":
    image_path='/Users/hanchang/mu_code/image.py/Girl_with_a_Pearl_Earring.jpg'
    st.image(image_path, use_column_width=True)
    st.subheader("Girl with a Pearl Earring 《戴珍珠耳环的少女》😉")
    st.markdown("**Artist:** Johannes Vermeer (Dutch)  \n**Media:** oil painting on canvas  \n**Year:** Around 1665  \n**Current museum:** Mauritshuis museum in The Hague  \n**Keywords:** tronie *(a painting of an imaginary figure)*, captures fleeting moment, represents light")
    st.markdown("**艺术家:** 约翰内斯·维米尔（荷兰）  \n**媒介:** 布面油画  \n**创作时间:** 约 1665 年  \n**现藏博物馆:** 海牙莫瑞泰斯皇家美术馆  \n**关键词:** 人像画 *(虚构人物的绘画)*、捕捉瞬间、表现光线")

if selected_year == "1830-1832":
    image_path='/Users/hanchang/mu_code/image.py/The_Great_Wave_Off_Kanagawa.jpg'
    st.image(image_path, use_column_width=True)
    st.subheader("The Great Wave Off Kanagawa 《神奈川冲浪里》🌊️")
    st.markdown("**Artist:** Katsushika Hokusai (Japanese)  \n**Media:** Woodblock print  \n**Year:** Around 1830-1832  \n**Current museum:** Copy available in many museums across the world  \n**Keywords:** Ukiyo-e, part of the series Thirty-six Views of Mount Fuji, use of perspective")
    st.markdown("**艺术家:** 葛饰北斋（日本）  \n**媒介:** 木刻版画  \n**创作时间:** 约 1830 - 1832 年  \n**现藏博物馆:** 世界各地许多博物馆均有复制品  \n**关键词:** 浮世绘、《富士三十六景》系列之一、透视法的运用")

if selected_year == "1872":
    image_path='/Users/hanchang/mu_code/image.py/Impression,sunrise.png'
    st.image(image_path, use_column_width=True)
    st.subheader("Impression, sunrise 《印象·日出》🌅")
    st.markdown("**Artist:** Claude Monet (French)  \n**Media:** oil on canvas  \n**Year:** 1872  \n**Current museum:** Musée Marmottan Monet, Paris  \n**Keywords:** Impressionism *(record contemporary life and focus on the transient effects of light and color)*, quick and loose brushstrokes, controversial *(some people think this painting is a sketch instead of a finished artwork)*")
    st.markdown("**艺术家:** 克劳德·莫奈（法国）  \n**媒介:** 布面油画  \n**创作时间:** 1872 年  \n**现藏博物馆:** 巴黎马摩丹莫奈博物馆  \n**关键词:** 印象派 *(记录当代生活，注重光与色彩的瞬时效果)* 、笔触快速且松散、有争议 *(有人认为这幅画是草图而非完成的作品)*")

if selected_year == "1889":
    image_path='/Users/hanchang/mu_code/image.py/Starry_Night.png'
    st.image(image_path, use_column_width=True)
    st.subheader("The Starry Night 《星夜》🤩")
    st.markdown("**Artist:** Vincent van Gogh (Dutch)  \n**Media:** oil on canvas  \n**Year:** 1889  \n**Current museum:** Museum of Modern Art, New York City  \n**Keywords:** abstract, landscape painting, Impasto and intense hues")
    st.markdown("**艺术家:** 文森特·梵高（荷兰）  \n**媒介:** 布面油画  \n**创作时间:** 1889 年  \n**现藏博物馆:** 纽约市现代艺术博物馆  \n**关键词:** 抽象、风景画、厚涂法和强烈色彩")

if selected_year == "1931":
    image_path='/Users/hanchang/mu_code/image.py/The_Persistence_of_Memory.png'
    st.image(image_path, use_column_width=True)
    st.subheader("The Persistence of Memory 《记忆的永恒》😲")
    st.markdown("**Artist:** Salvador Dalí (Spanish)  \n**Media:** oil on canvas  \n**Year:** completed in 1931  \n**Current museum:** Museum of Modern Art, New York City  \n**Keywords:** Surrealist movement, small dimensions, explores the concept of time")
    st.markdown("**艺术家:** 萨尔瓦多·达利（西班牙）  \n**媒介:** 布面油画  \n**创作时间:** 1931年  \n**现藏博物馆:** 纽约市现代艺术博物馆  \n**关键词:** 超现实主义运动、尺寸较小、探索时间的概念")

if selected_year == "1937":
    image_path='/Users/hanchang/mu_code/image.py/Guernica.jpg'
    st.image(image_path, use_column_width=True)
    st.subheader("Guernica 《格尔尼卡》😖")
    st.markdown("**Artist:** Pablo Picasso (Spanish)  \n**Media:** oil on canvas  \n**Year:** 1937  \n**Current museum:** Museo Nacional Centro de Arte Reina Sofía, Madrid  \n**Keywords:** black-and-white, political statement *(reaction to Nazi’s bombing practice on the Basque town of Guernica during the Spanish Civil War)*, Cubist figures *(transform three-dimensional reality into geometrical shapes on two-dimensional canvas)* ")
    st.markdown("**艺术家:** 巴勃罗·毕加索（西班牙）  \n**媒介:** 布面油画  \n**创作时间:** 1937 年  \n**现藏博物馆:** 马德里国家艺术中心雷纳索菲亚博物馆  \n**关键词:** 黑白、政治声明 *(作品是对西班牙内战期间纳粹轰炸巴斯克小镇格尔尼卡的回应)*、立体主义人物 *(将三维现实转化为二维画布上的几何形状)*")

st.divider()
st.subheader("References（参考文献）")
st.write("[1] Davies, and William. “Impression, Sunrise | Painting by Claude Monet.” Encyclopedia Britannica, 17 Mar. 2023, www.britannica.com/topic/Impression-Sunrise.")
st.write("[2] Gromley, and Jessica. “The Persistence of Memory | Description and Facts.” Encyclopedia Britannica, 15 Dec. 2023, www.britannica.com/topic/The-Persistence-of-Memory.")
st.write("[3] “Guernica, 1937 by Pablo Picasso.” Pablo Picasso, www.pablopicasso.org/guernica.jsp.")
st.write("[4] “Katsushika Hokusai | Under the Wave off Kanagawa (Kanagawa Oki Nami Ura), Also Known as the Great Wave, From the Series Thirty-six Views of Mount Fuji (Fugaku Sanjūrokkei) | Japan | Edo Period (1615–1868) | the Metropolitan Museum of Art.” The Metropolitan Museum of Art, www.metmuseum.org/art/collection/search/45434.")
st.write("[5] The Editors of Encyclopaedia Britannica. “Mona Lisa | Painting, Painter, History, Meaning, and Facts.” Encyclopedia Britannica, 30 Apr. 2025, www.britannica.com/topic/Mona-Lisa-painting.")
st.write("[6] Zelazko, and Alicja. “Girl With a Pearl Earring | Artist, History, and Facts.” Encyclopedia Britannica, 31 Mar. 2025, www.britannica.com/topic/Girl-with-a-Pearl-Earring-by-Vermeer.")
st.write("[7] ---. “The Starry Night | Vincent Van Gogh, Painting, History, and Facts.” Encyclopedia Britannica, 9 Apr. 2025, www.britannica.com/topic/The-Starry-Night.")
