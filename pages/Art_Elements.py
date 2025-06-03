import streamlit as st

if st.button("Back to home page"):
    st.switch_page("Art_website.py")

st.title(":rainbow[Art Elements (艺术元素)] 😍")

st.subheader(":red[Element#1 Line (线条)]")
image_path='/Users/hanchang/mu_code/image.py/Line.png'
st.image(image_path, use_column_width=True)
st.write("Line is the most basic art element. It is a one-dimensional figure, which means that it only has length. You can think it as a set of dots that has a beginning and an end. If these dots overlap each other, the line becomes a solid line, whereas if they don’t, the line becomes a dotted line. There are varies kinds of lines, each giving a different feeling. Click the buttons below for more information!")
st.write("线条是最基本的艺术元素。它是一维图形，意味着它只有长度。你可以把它想象成一组有起点和终点的点。如果这些点相互重叠，线就变成实线；如果它们不重叠，线就变成虚线。线有各种各样的类型，每种类型给人的感觉都不同。点击下面的按钮获取更多信息！")
option = st.selectbox(
    "Which type of line do you want to learn? (你想学习哪一种线条？)",
    ("Choose a type of line... (选择一种线条...)", "Thick lines(粗线条)", "Thin lines (细线条)", "Straight lines (直线)", "Curved lines (曲线)", "Zigzag lines (折线)", "Horizontal lines (水平线)", "Vertical lines (垂直线)"),
)

if option == "Thick lines(粗线条)":
    st.write("Thick lines give the sense of emphasis.")
    st.write("粗线条给人以强调的感觉。")
if option == "Thin lines (细线条)":
    st.write("Thin lines make people feel that it is receding.")
    st.write("细线条让人感觉它在消退。")
if option == "Straight lines (直线)":
    st.write("Straight lines convey a sense of clarity, order and strength, since they are often used in architecture and mechanism.")
    st.write("直线常用于建筑和机械中，因而传达出清晰、有序和力量的感觉。")
if option == "Curved lines (曲线)":
    st.write("Curved lines suggest the feeling of comfort and ease, and are often related to nature.")
    st.write("曲线给人舒适和轻松的感觉，且常常与自然相关。")
if option == "Zigzag lines (折线)":
    st.write("Zigzag lines create the sense of unrest, chaos and movement.")
    st.write("折线营造出不安、混乱和运动的感觉。")
if option == "Horizontal lines (水平线)":
    st.write("Horizontal lines, such as big lawns, evoke feelings of stability and calm.")
    st.write("水平线，比如广阔的草坪，会让人产生稳定和宁静的感觉。")
if option == "Vertical lines (垂直线)":
    st.write("Vertical lines, like high castles, give people the impression of height and strength.")
    st.write("垂直线，比如高高的城堡，给人以高大和坚固的印象。")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":orange[Element#2 Shape (形状)]")
image_path='/Users/hanchang/mu_code/image.py/Shape.png'
st.image(image_path, use_column_width=True)
st.write("Shape is formed when two lines meets up and enclose a space. Shapes are two-dimensional, they have height and width, but no depth. All shapes can be divided into two categories, geometric shapes and organic shapes. Common geometric shapes include circle, semi-circle, oval, triangle, square, rectangle, parallelogram, kite and many more. They are all regular and perfect. Organic shapes are the opposite, they are irregular and imperfect. They are all the other shapes that don’t belong to geometric shapes, and they often appeared to be freeform and unpredictable. Nevertheless, they make the artwork seem more realistic and natural.")
st.write("当两条线相遇并围成一个空间时，形状就形成了。形状是二维的，它们有高度和宽度，但没有深度。所有形状可分为两类，几何形状和有机形状。常见的几何形状包括圆形、半圆形、椭圆形、三角形、正方形、长方形、平行四边形、菱形等等。它们都是规则且完美的。有机形状则相反，它们是不规则且不完美的。它们是所有不属于几何形状的形状，通常看起来是自由的、难以预测的。然而，它们能让作品看起来更真实、更自然。")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":green[Element#3 Form (形体)]")
image_path='/Users/hanchang/mu_code/image.py/Form.png'
st.image(image_path, use_column_width=True)
st.write("Finally, when we add depth to shapes, we result in having three-dimensional forms. Similar to shapes, forms also have two categories: geometric (such as cube, cylinder, cone and sphere that are more commonly used in architecture and artificial items) and organic (for example the realistic forms in nature, like the form of a lemon). It is important to note that in drawings or paintings, forms can only be implied because we cannot create a three-dimensional figure on a two-dimensional medium. Therefore, a technique called Trompe I’oeil, is used. The term stand for artists using tricks to deceive the viewers’ eyes to create an illusion. In drawings and paintings, artists often use tools like shading or color to depict the objects so that the painting seems to have depth.")
st.write("最后，当我们给形状增加深度时，就形成了三维形体。与形状类似，形体也有两类：几何形体（如在建筑和人造物品中常用的立方体、圆柱体、圆锥体和球体）和有机形体（例如自然界中真实的形体，比如柠檬的形状）。值得注意的是，在绘画或素描中，形体只能通过暗示来表现，因为我们无法在二维媒介上创造出三维的物体。因此，艺术家们会使用一种叫做“错视画”的技巧。这个词指的是艺术家使用技巧来欺骗观众的眼睛，从而产生一种错觉。在绘画和素描中，艺术家经常使用阴影或色彩之类的工具来描绘物体，使画面看起来有深度。")
col1 = st.columns(1)[0]
if col1.button("Click here to see a realistic drawing！ 点击这里查看一个逼真的画作！"):
    image_path = '/Users/hanchang/mu_code/image.py/Realistic_art.jpg'
    st.image(image_path, use_column_width=True)

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":blue[Element#4 Space (空间)]")
image_path='/Users/hanchang/mu_code/image.py/Space.png'
st.image(image_path, use_column_width=True)
st.write("Space is the area that lies between, around or within objects. There are two types of space, negative space (background or the area around the object) and positive space (the subject of the drawing or painting). Just like how artists use color and shading to show form, they also create an illusion of space on two-dimensional medium. The table below demonstrates some of the techniques.")
st.write("空间是指物体之间、周围或内部的区域。空间有两种类型，即负空间（背景或物体周围的区域）和正空间（绘画或素描的对象）。就像艺术家们利用色彩和明暗来表现形体一样，他们也在二维媒介上营造出空间的错觉。下面这张表格展示了其中一些技巧。")
data = [
    ["Overlapping (重叠)", "This is when an object is drawn or painted on top of another object, covering some part of that object. As viewers, we see that object as in front of the other one. (当一个物体被画在另一个物体之上，遮住部分该物体时，我们就会觉得这个物体在前面。)"],
    ["Size & detail (大小与细节)", "When an object is drawn smaller and blurrier than another object, it will look as if it is further away. For instance, in a drawing, a house may be drawn smaller and lacking more details than a flower. For viewers, this seems like the house is in the distance, while the flower is just in front. (当一个物体被画得比另一个物体小且模糊时，它看起来就会像是在远处。例如，在一幅画中，房子可能被画得比花小且细节更少。对于观者来说，这意味着房子在远处，而花就在眼前。)"],
    ["Color & value (色彩与明暗)", "Especially in drawings or paintings that have a grand scene, artists use cooler, especially bluer, and lighter color to depict the objects in distance. Whereas for close up objects, warmer and darker values are used. (尤其是在描绘宏大场景的绘画中，艺术家会用更冷（尤其是更蓝）且更浅的色彩来表现远处的物体。而对于近处的物体，他们则使用更暖、更暗的色调。)"]
]
table_md = ""
for row in data:
    table_md += f"| {row[0]} | {row[1]} |\n"
table_md = "|   |   |\n|---|---|\n" + table_md
st.markdown(table_md)

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":violet[Element#5 Value (明度)]")
image_path='/Users/hanchang/mu_code/image.py/Value.png'
st.image(image_path, use_column_width=True)
st.write("In simple words, value is how light or dark something is. In art, there is a scale of light and dark from pure white (the lightest value) to pitch black (the darkest value). To determine the value of a color, you can compare it with the value scale. If a painting is mostly done with colors from the darker side of the value scale, it often evokes the feeling of heavy and mysterious. On the other hand, if a painting is mostly done with colors from the lighter side of the value scale, it will give people the impression of lightness and spirituality. Value is sometimes more important than color in a painting because it is the element that transform two-dimensional shape to three-dimensional form. Value changes are also crucial. Gradual transition creates soft edge (looks rounded), and rapid transition creates hard edge (looks sharp). In addition, value is used to create shadows.")
st.write("简单来说，明度指的是物体的亮暗程度。在艺术中，从纯白色（最亮的明度）到纯黑色（最暗的明度）有一个明暗的等级。要确定一种颜色的明度，可以将其与明度等级进行比较。如果一幅画主要使用明度等级较暗的颜色，往往会给人沉重和神秘的感觉。相反，如果一幅画主要使用明度等级较亮的颜色，就会给人轻盈和灵性的印象。在绘画中，明度有时比色彩更重要，因为它是能将二维形状转化为三维形式的元素。明度的变化也很关键。渐变过渡会形成柔和的边缘（看起来圆润），而快速过渡会形成硬朗的边缘（看起来尖锐）。此外，明度还用于创造阴影。")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":red[Element#6 Color (色彩)]")
image_path='/Users/hanchang/mu_code/image.py/Color.png'
st.image(image_path, use_column_width=True)
st.write("Color is defined as what our eyes see when light is reflected off an object. In art, colors are arranged on a color wheel consisting of three categories of colors. Click the tabs below to see these categories!")
st.write("色彩被定义为当光线从物体反射时我们眼睛所看到的东西。在艺术中，色彩被排列在一个色轮上，由三类颜色组成。点击下面的按钮查看这些类别！")
tab1, tab2, tab3 = st.tabs(["Primary Colors", "Secondary Colors", "Tertiary Colors"])

with tab1:
    st.write("Primary colors are colors that can’t be mixed, this category include red, yellow and blue.")
    st.write("原色是无法混合而成的颜色，这一类包括红色、黄色和蓝色。")
with tab2:
    st.write("Secondary colors are colors created by equally mixing two primary colors, this category include orange (red + yellow), purple (red + blue) and green (blue + yellow).")
    st.write("间色是由两种原色等量混合而成的颜色，这一类包括橙色（红色 + 黄色）、紫色（红色 + 蓝色）和绿色（蓝色 + 黄色）。")
with tab3:
    st.write("Tertiary colors are colors made by equally mixing a primary color with a secondary color, this category include amber, vermillion, magenta, violet, teal and chartreuse.")
    st.write("复色是由一种原色与一种间色等量混合而成的颜色，这一类包括琥珀色、朱红色、洋红色、紫罗兰色、蓝绿色和黄绿色。")

st.divider()
st.write("Below is a tertiary color mixer, have fun! 下面是一个复色混合器，玩得开心！")
color_translations = {
    "Red": "红色",
    "Blue": "蓝色",
    "Yellow": "黄色",
    "Orange": "橙色",
    "Purple": "紫色",
    "Green": "绿色",
    "Vermillion": "朱红色",
    "Magenta": "洋红色",
    "Violet": "紫罗兰色",
    "Teal": "蓝绿色",
    "Amber": "琥珀色",
    "Chartreuse": "黄绿色"
}

def blend_colors(primary, secondary):
    valid_combinations = {
        ("Red", "Orange"): "Vermillion",
        ("Red", "Purple"): "Magenta",
        ("Blue", "Purple"): "Violet",
        ("Blue", "Green"): "Teal",
        ("Yellow", "Orange"): "Amber",
        ("Yellow", "Green"): "Chartreuse"
    }

    if (primary, secondary) in valid_combinations:
        return valid_combinations[(primary, secondary)], True
    elif (secondary, primary) in valid_combinations:
        return valid_combinations[(secondary, primary)], True
    else:
        return None, False

color_hex = {
    "Vermillion": "#FF5722",
    "Magenta": "#FF00FF",
    "Violet": "#8A2BE2",
    "Teal": "#008080",
    "Amber": "#FF8000",
    "Chartreuse": "#7FFF00"
}

primary_color = st.selectbox("Pick the primary color (选择原色)", ["Red", "Blue", "Yellow"])
secondary_color = st.selectbox("Pick the secondary color (选择间色)", ["Orange", "Purple", "Green"])

tertiary_name, is_valid = blend_colors(primary_color, secondary_color)

if is_valid:
    zh_name = color_translations[tertiary_name]
    st.markdown(f'<p style="color: green; font-size: 16px;">⭐ Now you got {tertiary_name}! (你得到了{zh_name}!)</p>', unsafe_allow_html=True)
    st.markdown(
        f'<div style="width: 100px; height: 100px; background-color: {color_hex[tertiary_name]}; border-radius: 5px; margin-top: 10px;"></div>',
        unsafe_allow_html=True
    )
else:
    st.markdown('<p style="color: orange; font-size: 16px;">⚠️ Sorry! You need to change a color combination(抱歉！你需要更换颜色组合)</p>', unsafe_allow_html=True)
st.divider()

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":orange[Element#7 Texture (肌理)]")
image_path='/Users/hanchang/mu_code/image.py/Texture.png'
st.image(image_path, use_column_width=True)
st.write("Texture refers to how something feels. Texture in art can be both actual texture or visual texture. Actual texture, just as its name implies, is the way an object feels to touch. Artist can create actual texture in their work through applying a variety of technique and materials, such as clay, fabric, paint and impasto. The other type of texture, visual texture, is the illusion of texture. Some methods the artists use to create visual texture are shading, cross-hatching and stippling. Different textures can also provoke different feelings, an example will be smooth and soft textures make people feel calm, comfortable and serene, whilst rough textures stimulate tension, rawness and energy.")
st.write("肌理指的是某物的触感。艺术中的肌理可以是实际肌理或视觉肌理。实际肌理，顾名思义，就是物体触摸起来的感觉。艺术家可以通过运用各种技法和材料，如黏土、织物、颜料和厚涂法来在作品中创造实际肌理。另一种肌理类型，视觉肌理，是肌理的错觉。艺术家用来创造视觉肌理的一些方法有明暗法、交叉排线法和点绘法。不同的肌理还能引发不同的感受，比如平滑柔软的肌理会让人感到平静、舒适和宁静，而粗糙的肌理则会激发紧张、原始和活力的感觉。")

st.write(" ")
st.write(" ")
st.write(" ")

st.divider()
st.subheader("References（参考文献）")
st.write("[1] “7 Elements of Art.” Online Art Lessons, onlineartlessons.com/tutorial/7-elements-of-art.")
st.write("[2] “Organic Forms - Form - Higher Art and Design Revision - BBC Bitesize.” BBC Bitesize, 4 Jan. 2023, www.bbc.co.uk/bitesize/guides/zm83vk7/revision/3.")
st.write("[3] Teacher, Arty. “What Is Texture in Art?” The Arty Teacher, 1 Dec. 2024, theartyteacher.com/what-is-texture-in-art.")
st.write("[4] “Tertiary Colours - Colour - National 5 Art and Design Revision - BBC Bitesize.” BBC Bitesize, 18 Oct. 2023, www.bbc.co.uk/bitesize/guides/z3bqycw/revision/4.")
st.write("[5] “What Is Texture - Texture - National 5 Art and Design Revision - BBC Bitesize.” BBC Bitesize, 3 Mar. 2023, www.bbc.co.uk/bitesize/guides/zccx6fr/revision/1.")
