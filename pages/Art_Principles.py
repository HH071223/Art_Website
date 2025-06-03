import streamlit as st

if st.button("Back to home page"):
    st.switch_page("Art_website.py")

st.title(":rainbow[Art Principles] 😃")

st.subheader(":red[Principle#1 Pattern (图案)]")
image_path='/Users/hanchang/mu_code/image.py/Pattern.png'
st.image(image_path, use_column_width=True)
st.write("Pattern is the regular repetition of any of the elements of art or a combination of them. In fact, everything can be turned into a pattern if you repeat them. Two most common patterns are spirals and grids. In art, pattern is often created using colors, lines, forms or shapes. By applying these art elements, we can create natural patterns (patterns found in natural environment, such as snowflake or even Milky Way galaxy), man-made patterns (like tiles), geometric patterns and irregular patterns.")
st.write("图案是艺术元素中任何一种元素或其组合的有规律重复。实际上，只要重复，任何事物都可以变成图案。两种最常见的图案是螺旋形和网格。在艺术中，图案通常通过颜色、线条、形状或形体来创造。通过运用这些艺术元素，我们可以创造出自然图案（在自然环境中发现的图案，如雪花甚至银河系）、人造图案（如瓷砖）、几何图案和不规则图案。")
if st.button("Why do artists create patterns? (艺术家为何创作图案？)"):
    st.write("Patterns can be powerful in many ways, including  \n1. drawing attention  \n2. calming viewers  \n3. creating balance, rhythm, movement or overall composition  \n4. making decorations  \nMost importantly, if you want to experiment with the elements of art, like color, line or shape, creating a pattern can be very fun and useful!")
    st.write("图案在很多方面都具有强大的力量，包括…  \n1. 引起注意  \n2. 令观众感到平静  \n3. 营造平衡、节奏、动感或整体构图  \n4. 制作装饰品  \n最重要的是，如果你想尝试艺术元素，比如颜色、线条或形状，创作一个图案会非常有趣且实用！")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":orange[Principle#2 Balance (平衡)]")
image_path='/Users/hanchang/mu_code/image.py/Balance.png'
st.image(image_path, use_column_width=True)
st.write("Balance is the way the visual weight of the elements in a composition creates visual equilibrium. This term refers to when one side of artwork seem equal compared with the other side. A balanced artworks make viewers feels stable, whereas an imbalanced one evoke a sense of discomfort. Whether or not to use balance depend on the feeling you want to convey to your viewers, but if you want to achieve balance in your artwork, you can utilize bilateral symmetry, asymmetry or radial symmetry. Click the tabs below to see the definition of these words!")
st.write("平衡是指构图中各元素的视觉重量如何创造出视觉上的均衡。这个词指的是作品的一侧看起来与另一侧相等。平衡的作品会让观众感到稳定，而不平衡的作品则会让人感到不适。是否使用平衡取决于你想向观众传达的感觉，但如果你想在作品中实现平衡，可以利用双侧对称、不对称或辐射对称。点击下面的标签查看这些词的定义！")
tab1, tab2, tab3 = st.tabs(["Bilateral symmetry (双侧对称)", "Asymmetry (不对称)", "Radial symmetry (辐射对称)"])
with tab1:
    st.write("Bilateral symmetry is when both sides of a composition have the exact same elements in the exact same position, like a mirror image or the two sides of a butterfly wing.")
    st.write("双侧对称指构图的两侧具有完全相同的元素且处于完全相同的位置，就像镜像或蝴蝶翅膀的两侧。")
with tab2:
    st.write("Asymmetry is when the composition has two contrasting elements of art. Sometimes, this composition can also create balance, as long as the visual weight on both sides are equal.")
    st.write("不对称是指构图中有两个对比的艺术元素。有时，这种构图也能达到平衡，只要两侧的视觉重量相等。")
with tab3:
    st.write("Radial symmetry is when elements are equally arranged around a central point. This symmetry establishes a very strong focal point. An example of this in nature is the seeds of a dandelion.")
    st.write("辐射对称是指元素围绕一个中心点均匀排列。这种对称会形成一个非常强烈的焦点。自然界中的蒲公英种子就是一个例子。")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":green[Principle#3 Variety (多样性)]")
image_path='/Users/hanchang/mu_code/image.py/Variety.jpg'
st.image(image_path, use_column_width=True)
st.write("Variety refers to using different elements in an artwork to create visual interest. It is also how artist add complexity to their work. Variety can be shown through contrast (using art elements that are different from each other, this can make your artwork more eye-catching), difference and change (repeating similar elements but varying some parts, causing your artwork to be more interesting), and elaboration (add detail and complexity). In art, too less variety make an artwork seem dull, perfect variety make an artwork look unified and guides viewer’s eyes, whilst too much variety result in chaos.")
st.write("多样性指的是在一件艺术作品中运用不同的元素来创造视觉趣味。这也是艺术家为其作品增添复杂性的方法。多样性可以通过对比（使用彼此不同的艺术元素，这能使你的作品更引人注目）、差异和变化（重复相似的元素但改变某些部分，使你的作品更有趣）以及详尽（添加细节和复杂性）来体现。在艺术中，多样性过少会使作品显得单调乏味，恰到好处的多样性能使作品看起来统一，并引导观众的目光，而过多的多样性则会导致混乱。")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":blue[Principle#4 Emphasis (强调)]")
image_path='/Users/hanchang/mu_code/image.py/Emphasis.png'
st.image(image_path, use_column_width=True)
st.write("Emphasis is the special attention or importance given to one area of an artwork. This area, which can either be the focal point or the main subject, is usually visually dominant and attracts most of the viewer’s attention. Emphasis and contrast are often combined and applied together. Several other ways to create emphasis in an artwork are the use of color and the placement of objects. Emphasis is very important in art for it directs the viewer, adds depth and plays a crucial role in telling a visual story - even landscape art has emphasis! In addition, when you are appreciating other artworks and don’t know where to start, finding the emphasis of the artwork can be very helpful. This is because emphasis is usually the place where the artist reveals the concepts, themes or ideas of the artwork.")
st.write("强调是指在一件艺术作品中对某一区域给予特别的关注或重视。这一区域可以是焦点或主要主题，通常在视觉上占主导地位，并吸引观众的大部分注意力。强调和对比常常结合使用。在艺术作品中创造强调的其他几种方式包括使用色彩和物体的布局。强调在艺术中非常重要，因为它引导观众，增加深度，并在讲述视觉故事方面发挥着关键作用——即使是风景画也有强调！此外，当你欣赏其他艺术作品而不知从何入手时，找到作品的强调点会非常有帮助。这是因为强调点通常是艺术家揭示作品概念、主题或想法的地方。")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":violet[Principle#5 Movement (运动)]")
image_path='/Users/hanchang/mu_code/image.py/Movement.png'
st.image(image_path, use_column_width=True)
st.write("Movement is created when using the elements of art such that they move the viewer’s eyes through the image. In art, movement adds excitement, action, drama and compositional interest to the artwork. It can also create intense emotion or even suggest the passing of time within a work and make the work come alive. Just like all art principles, movement can be created in many ways, including diagonal or curvy lines, space, texture, repetition and many more. The placement of elements can also imply movement. Take a look at the artwork below, do you feel the sense of movement?")
st.write("当运用艺术元素时，若能使观者的目光在画面中移动，便形成了运动。在艺术作品中，运动增添了兴奋感、动感、戏剧性和构图上的趣味性。它还能营造出强烈的情感，甚至在作品中暗示时间的流逝，使作品充满生机。和所有艺术原则一样，运动可以通过多种方式实现，包括斜线或曲线、空间、纹理、重复等等。元素的布局也能暗示运动。请看下面的艺术作品，你感受到运动的感觉了吗？")
if st.button("Click here to see the artwork! (点击这里查看艺术作品！)"):
    image_path='/Users/hanchang/mu_code/image.py/Movement_in_art.png'
    st.image(image_path, use_column_width=True)
st.divider()
st.write("On the other hand, in photography and some other art forms, the use of motion blur (the blur seen in moving objects) becomes a strong tool to create movement. Try to create your own motion blur using the camera below!")
st.write("另一方面，在摄影和其他一些艺术形式中，运动模糊（移动物体所呈现的模糊效果）成为创造运动的有力工具。你可以尝试使用下面的相机来创造你自己的运动模糊效果！")
enable = st.checkbox("Enable camera (激活相机)")
picture = st.camera_input("Take a picture (拍一张照片吧）", disabled=not enable)
if picture:
    st.image(picture)

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":red[Principle#6 Scale (比例)]")
image_path='/Users/hanchang/mu_code/image.py/Scale.png'
st.image(image_path, use_column_width=True)
st.write("Scale is the overall physical size of an artwork compared to its surroundings. Large artwork, artwork that is much larger than it would be in real life, grab people’s attention immediately and give them the impression of awe or threatening, depending on the artwork. This type of artwork often acts as a powerful statement and can evoke strong emotions. Monumental sculptures and large canvas are both examples of large scale art. In contrast, small artwork, artwork that is much smaller than it would be in real life, draw people into its details. Miniature sculptures and small canvases are both examples of small scale art. Below are two different scale artworks!")
st.write("比例是指一件艺术品的总体物理大小与其周围环境的对比。大型艺术品，即比现实生活中大得多的艺术品，会立即吸引人们的注意力，并给人以敬畏或威胁的印象，具体取决于不同艺术品。这类艺术品往往能起到强有力的表达作用，并能唤起强烈的情感。巨型雕塑和大幅画布都是大型尺寸艺术的例子。相反，小型艺术品，即比现实生活中小得多的艺术品，会吸引人们去关注其细节。微型雕塑和小幅画布都是小型尺寸艺术的例子。下面是两个有着不同比例的艺术作品！")
on = st.toggle("small scale art")
if on:
    image_path='/Users/hanchang/mu_code/image.py/Small_scale_art.png'
    st.image(image_path, use_column_width=True)
on = st.toggle("large scale art")
if on:
    image_path='/Users/hanchang/mu_code/image.py/Large_scale_art.png'
    st.image(image_path, use_column_width=True)
st.write(" ")
st.write("Despite determining the dimension of the artwork, scale is also crucial in the composition of drawings or paintings. In many circumstances, artists need to create a sense of scale in their composition, and this is when the grid method is applied. In the grid method, artists equally divide up both the reference image and their own canvas into smaller grids, like 3*3 or 5*5, and transfer details in each grids to their own artworks. This method makes it easier to measure, shrink or enlarge their composition accordingly. You can also try to use this method in your art creation as well!")
st.write("除去决定艺术品的尺寸，在绘画或素描的构图中，比例同样至关重要。在很多情况下，艺术家需要在构图中营造出比例，这时就会用到网格法。在网格法中，艺术家将参考图像和自己的画布都等分为更小的网格，比如 3×3 或 5×5，然后将每个网格中的细节转移到自己的作品中。这种方法使得测量、缩小或放大构图变得更加容易。你也可以在自己的艺术创作中尝试使用这种方法！")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":orange[Principle#7 Harmony (和谐)]")
image_path='/Users/hanchang/mu_code/image.py/Harmony.jpg'
st.image(image_path, use_column_width=True)
st.write("Harmony is the purposeful arrangement of art elements that results in a cohesive composition. In an artwork that possesses harmony, different art elements complement one another and appear to work together. The other art principle, balance, is closely related to harmony. Balance can create harmony, but an artwork that has harmony might not be balanced. Harmony can be created by the use of similar colors or shapes, and sometimes even contrast as well. For example, an artist may choose a color scheme and repeat a color in this color scheme throughout the composition. After that, the artist might also use contrasting colors to enhance the overall visual appearance and thereby create harmony. Harmony makes an artwork look united, coherent and visually pleasing. It is created in many famous art piece, including Van Gogh’s well-known The Starry Night (you can see this painting in the Famous Artwork page).")
st.write("和谐是指有目的地安排艺术元素，从而形成一个统一的整体。在具有和谐感的艺术作品中，不同的艺术元素相互补充，看起来像是互相协同。另一个艺术原则——平衡，与和谐密切相关。平衡可以创造和谐，但具有和谐感的艺术作品不一定平衡。和谐可以通过使用相似的颜色或形状来实现，有时甚至可以通过对比来实现。例如，艺术家可能会选择一种配色方案，并在整个构图中重复使用该配色方案中的某种颜色。之后，艺术家还可能使用对比色来增强整体视觉效果，从而创造和谐。和谐使艺术作品看起来统一、连贯且赏心悦目。许多著名艺术作品都运用了和谐这一原则，包括梵高著名的《星夜》（您可以在“著名艺术作品”页面看到这幅画）。")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":green[Principle#8 Unity (统一性)]")
image_path='/Users/hanchang/mu_code/image.py/Unity.jpg'
st.image(image_path, use_column_width=True)
st.write("Unity is how different elements of an artwork come together and create a sense of wholeness (as to be seen as one). Just like harmony, unity can also enhance coherence and make an artwork more aesthetically pleasing. In art, a wide range of technique can be applied to create unity. This includes simplicity (limiting the range of materials and other art elements in an art piece), proximity (when different parts of a composition come close to each other so that the audience is more likely to see them as a group), repetition (repeating similar elements) and continuation (using continuing lines, edges and shapes to connect together different elements in a composition). It is important to note that if an artwork is too unified, it will seem boring. Balancing unity with variety is a key skill in designing compositions.")
st.write("统一性是指一件艺术作品中不同的元素如何组合在一起，从而产生整体感（即被视为一个整体）。就像和谐一样，统一性也能增强连贯性，使艺术作品更具美感。在艺术中，多种技术都可以用来实现统一性。这包括简约（限制艺术作品中材料和其他艺术元素的范围）、接近（当构图的不同部分彼此靠近时，观众更有可能将其视为一个整体）、重复（重复相似的元素）和延续（使用连续的线条、边缘和形状将构图中的不同元素连接在一起）。需要注意的是，如果一件艺术作品过于统一，就会显得单调乏味。在设计构图时，平衡统一性和多样性是一项关键技能。")
if st.button(":orange[⚠️ Distinguish unity and harmony (区分统一与和谐)]"):
    st.write("Unity and harmony are very similar concepts, however, there are still some difference between them. Unity emphasizes more on how elements in an artwork work together as a whole, whereas harmony is how elements complement one another and strengthen each other’s impact.")
    st.write("统一与和谐是十分相似的概念，但它们之间仍存在一些差异。统一更侧重于艺术品中各元素如何作为一个整体协同运作，而和谐则在于各元素如何相互补充、相互强化彼此的效果。")

st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(":blue[Principle#9 Contrast (对比)]")
image_path='/Users/hanchang/mu_code/image.py/Contrast.png'
st.image(image_path, use_column_width=True)
st.write("Contrast is defined as the juxtaposition of different elements of art in order to highlight their differences or create visual interests. In fact, contrast is everywhere, for without contrast, an artwork would become invisible. This principle is closely related to variety and emphasis, in most circumstances, they are applied together. Contrast can be achieved by creating light and dark, utilizing opposite hues of the color wheel (such as red and green or orange and blue), arranging different size or texture, and so on. In art, contrast can show rhythm and strengthen the focus of the artwork. As viewers of the artwork, our eyes will always be first attracted by areas of contrast. Notan, a term in Japanese art referring to the combination of lights and darks, is a great example of contrast. These artwork uses the juxtaposition of lights and darks to imply a sense of balance and harmony. Click the check box below to see some Notan arts!")
st.write("对比是将不同的艺术元素并置，以突出它们的差异或创造视觉兴趣。实际上，对比无处不在，因为没有对比，一件艺术作品就会变得难以察觉。这一原则与变化和强调密切相关，在大多数情况下，它们是同时应用的。通过创造明暗对比、利用色轮上的相反色调（如红色和绿色或橙色和蓝色）、安排不同大小或纹理等方式都可以实现对比。在艺术中，对比可以展现节奏并强化作品的重点。作为艺术作品的观赏者，我们的眼睛总是首先被对比强烈的区域所吸引。日本艺术中的“浓淡”（Notan）一词指的是明暗的组合，是对比的一个绝佳例子。这些艺术作品通过明暗的并置来暗示一种平衡与和谐的感觉。点击下面的复选框查看一些浓淡艺术作品！")
display = st.checkbox("Notan artworks")
if display:
    image_path='/Users/hanchang/mu_code/image.py/Notan_art.jpg'
    st.image(image_path, use_column_width=True)

st.write(" ")
st.write(" ")
st.write(" ")

st.divider()
st.subheader("References（参考文献）")
st.write("[1] Activity: Principles of Art - Movement. www.purchase.edu/live/profiles/3934-activity-principles-of-art-movement.")
st.write("[2] ARTMEDIA.BG. “Pattern in Art.” ARTMEDIA.BG, 28 May 2024, artmedia.bg/en/art-mentor/pattern-in-art.")
st.write("[3] DeGuzman, Kyle. “What Is Movement in Art — Composition Techniques Explained.” StudioBinder, 14 May 2025, www.studiobinder.com/blog/what-is-movement-in-art-definition.")
st.write("[4] Fine Art Tutorials. “Harmony in Art: Definition and Guide.” Fine Art Tutorials, 17 Feb. 2023, finearttutorials.com/guide/harmony-in-art.")
st.write("[5] ---. “Scale in Art: Definition and Guide.” Fine Art Tutorials, 17 Feb. 2023, finearttutorials.com/guide/scale-in-art.")
st.write("[6] Marder, Lisa. “The 7 Principles of Art and Design.” ThoughtCo, 2 May 2024, www.thoughtco.com/principles-of-art-and-design-2578740.")
st.write("[7] P, Silka. “What Is Contrast in Art? Examples and Definition.” Artsper Magazine, 27 Feb. 2025, blog.artsper.com/en/a-closer-look/contemporary-art/what-is-contrast-in-art-examples-and-definition.")
st.write("[8] “What Is Unity? - Unity - National 5 Art and Design Revision - BBC Bitesize.” BBC Bitesize, 3 Apr. 2023, www.bbc.co.uk/bitesize/guides/zy4mmnb/revision/1.")
st.write("[9] “What Is Variety in Art? - Variety - AQA - GCSE Art and Design Revision - AQA - BBC Bitesize.” BBC Bitesize, 9 Mar. 2023, www.bbc.co.uk/bitesize/guides/zq2mng8/revision/1.")
