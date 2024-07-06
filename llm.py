####################################################
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('SECRET_KEY')
####################################################

# Import Upstage Solar AI
from langchain_upstage import ChatUpstage

# For groundedness check
from langchain_upstage import GroundednessCheck

# 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# #
# from langchain_upstage import UpstageLayoutAnalysisLoader
# from langchain_upstage import UpstageEmbeddings
# from langchain_text_splitters import (
#     Language,
#     RecursiveCharacterTextSplitter,
# )
# from langchain_chroma import Chroma

# # Layout analysis
# layzer = UpstageLayoutAnalysisLoader(
#     "manual/HOW_TO_CODE_THE_RORSCHACH.pdf", output_type="html", api_key=API_KEY
# )
# docs = layzer.load()
# # Split
# text_splitter = RecursiveCharacterTextSplitter.from_language(
#     chunk_size=1000, chunk_overlap=100, language=Language.HTML
# )
# splits = text_splitter.split_documents(docs)
# # Embedding
# embeddings_model = UpstageEmbeddings(api_key=API_KEY, model="solar-embedding-1-large")
# vectorstore = Chroma.from_documents(
#     documents=splits,
#     embedding=embeddings_model,
# )
# # Retrive
# retriever = vectorstore.as_retriever()
# def retrive(query:str) -> str:
#     result_docs = retriever.invoke(query)
#     return result_docs[0].page_content[:100]


RULE = {}

RULE["development"] = """
Coding Rules of Developmental Quality
Category: Synthesized Response
* Symbol: +
* Definition: Two or more objects are described as separate but related.
* Criterion: At least one of the objects involved must have a specific form demand, or be described in a manner that creates a specific form demand (ex. a dog walking among some bushes, a man with a funny hat on, an airplane flying through some clouds, the head of a little girl, she has a hair ribbon).
Category: Ordinary Response
* Symbol: o
* Definition: An area of the blot is identified as a single object which has features that create a natural form demand.
* Criterion: The description of the object is such as to create a specific form demand (ex. a fir tree, a cat, a totem pole, a maple leaf, a bat, a flag).
Category: Synthesized Response
* Symbol: v/+
* Definition: Two or more objects are described as separate but related.
* Criterion: None of the objects involved have a specific form demand and the articulation does not introduce a form demand for any of the objects (ex. clouds coming together, some sort of bay with the vegetation on the shore, a rock and some dirt around it).
Category: Vague
* Symbol: v
* Definition: An object is reported which has no specific form demand.
* Criterion: The articulation does not introduce a specific form demand for the object (ex. a cloud, the sky, the colors of sunset, some ice).
---
Respond: {Respond}
Output:
"""

RULE["determinant"] = """
Coding Rules of Determinants
Category: Form
* Symbol: F
* Criterion: Form answers. Used for responses based exclusively on the form features of the blot.
Category: Movement
* Symbol: M
* Criterion: Human movement response. Used for responses involving the kinesthetic activity of a human, or of an animal or fictional character in human-like activity.
* Symbol: FM
* Criterion: Animal movement response. Used for responses involving the kinesthetic activity of an animal. The movement perceived must be congruent to the species identified in the content.
* Symbol: M
* Criterion: Inanimate movement response. Used for responses involving the movement of inanimate, inorganic, or insensate objects.
Category: Chromatic Color
* Symbol: C
* Criterion: Pure color response. Used for answers based exclusively on the chromatic color features of the blot.
* Symbol: CF
* Criterion: Color-from response. Used for answers that are formulated primarily because of the chromatic color features of the blot.
* Symbol: FC
* Criterion: Form-color response. Used for answers that are created mainly because of form features.
* Symbol: Cn
* Criterion: Color naming response. Used when the colors of the blot are identified by name.
Category: Achromatic Color
* Symbol: C'
* Criterion: Pure achromatic color response. Used when the response is based exclusively on the grey, black, or white features of the blot.
* Symbol: C'F
* Criterion: Achromatic color-form response. Used for responses that are created mainly because of the black, white, or gray features.
* Symbol: FC'
* Criterion: Form-achromatic color response. Used for answers that are based mainly on the form features.
Category: Texture
* Symbol: T
* Criterion: Pure texture response. Used for answers in which the shading components of the blot are translated to represent a tactual phenomenon.
* Symbol: TF
* Criterion: Texture-form response. Used for responses where the shading features are interpreted as tactual.
* Symbol: FT
* Criterion: Form-texture response. Used for responses that are based mainly on the form features.
Category: Shading-Dimension
* Symbol: V
* Criterion: Pure vista response. Used for answers in which the shading features are interpreted as depth or dimensionality.
* Symbol: VF
* Criterion: Vista-form response. Used for responses where the shading features are interpreted as depth.
* Symbol: FV
* Criterion: Form-vista response. Used for answers that are based mainly on the form features.
Category: Shading-Diffuse
* Symbol: Y
* Criterion: Pure shading response. Used for responses that are based exclusively on the light-dark features of the blot.
* Symbol: YF
* Criterion: Shading-form response. Used for responses based primarily on the light-dark features of the blot.
* Symbol: FY
* Criterion: Form-shading response. Used for responses that are based mainly on the form features.
Category: Form-Dimension
* Symbol: FD
* Criterion: Form based dimensional response. Used for answers in which the impression of depth, distance, or dimensionality is created by using the elements of size and/or shape of contours.
Category: Pairs & Reflections
* Symbol: (2)
* Criterion: The pair response. Used for answers in which two identical objects are reported, based on the symmetry of the blot.
* Symbol: rF
* Criterion: Reflection-form response. Used for answers where the blot or blot area is reported as a reflection.
* Symbol: Fr
* Criterion: Form-reflection response. Used for answers where the blot or blot area is identified as reflected or a mirror image.
---
Respond: Because it is black it seems like a bat.
Output: Examinee's respond is a bat because it is black. Black is one of achromatic color. Therefore determinant is C'.

Respond: {Respond}
Output:
"""

RULE["content"] = """
Coding Rules of Contents
Category: Whole Human
* Symbol: H
* Criterion: Involves the percept of a whole human form. If the percept involves a real historical figure, such as Napoleon, Joan of Arc, etc., the content code 'Ay' should be added as a secondary code.
Category: Whole Human, Fictional or Mythological
* Symbol: (H)
* Criterion: Involving the percept of a whole human form that is fictional or mythological, such as clowns, fairies, giants, witches, fairy tale characters, angels, dwarfs, devils, ghosts, science fiction creatures that are humanoid, human-like monsters, silhouettes of human figures.
Category: Human Detail
* Symbol: Hd
* Criterion: Involving the percept of an incomplete human form, such as an arm, leg, fingers, feet, the lower part of a person, a person without a head.
Category: Human Detail, Fictional or Mythological
* Symbol: (Hd)
* Criterion: Involving the percept of an incomplete human form that is fictional or mythological, such as the head of the devil, the arm of a witch, the eyes of an angel, parts of science fiction creatures that are humanoid, a jack-o-lantern, and all masks.
Category: Human Experience
* Symbol: Hx
* Criterion: Hx is scored as a primary content for percepts involving the human emotion or sensory experience such as love, hate, depression, happiness, sound, smell, fear, etc. These answers will also include the use of AB as a special score. Hx also is often scored as a secondary content in answers that are not abstract but clearly involve the attribution of a human emotion or sensory experience.
Category: Whole Animal
* Symbol: A
* Criterion: Involving the percept of a whole animal form, such as butterfly, bat, insect.
Category: Whole Animal, Fictional or Mythological
* Symbol: (A)
* Criterion: Involving the percept of a whole animal that is fictional or mythological, such as a unicorn, dragon, magic frog, flying horse, Black Beauty, Jonathan Livingston Seagull.
Category: Animal Detail
* Symbol: Ad
* Criterion: Involving the percept of an incomplete animal form, such as the hoof of a horse, claw of a lobster, head of a dog, animal skin.
Category: Animal Detail, Fictional or Mythological
* Symbol: (Ad)
* Criterion: Involving the percept of an incomplete animal form that is fictional or mythological, such as the wing of Pegasus, the head of Peter Rabbit, the legs of Pooh Bear.
Category: Anatomy
* Symbol: An
* Criterion: Used for responses in which the content is skeletal, muscular, or of internal anatomy such as bone structure, skull, rib cage, heart, lungs, stomach, liver, muscle fiber, vertebrae, brain. If the response involves a tissue slide, the code 'Art' should be added as secondary.
Category: Art
* Symbol: Art
* Criterion: Involving percepts of paintings, drawings, or illustrations, either abstract or definitive, art objects, such as statues, jewelry, chandelier, candelabra, crests, badges, seals, and decorations. A feather seen as worn by an Indian would also be coded as Art, however, a feather seen as worn by children, such as on Card VII would more appropriately be coded as Ad. In many responses coded for Art, a second content will also be coded, such as a painting of two dogs would be Art, A, or a sculpture of two witches would be Art, H.
Category: Anthropology
* Symbol: Ay
* Criterion: Involving percepts that have a specific cultural or historical connotation such as totem, Roman helmet, Magna Carta, Santa Maria, Napoleon's hat, Cleopatra's crown, arrowhead, prehistoric axe, an Indian war bonnet.
Category: Blood
* Symbol: Bl
* Criterion: Involving the percept of blood, either human or animal.
Category: Botany
* Symbol: Bt
* Criterion: Involving the percept of any plant life such as bushes, flowers, seaweed, trees, or parts of plant life, such as leaves, petals, tree trunk, root, bird's nest.
Category: Clothing
* Symbol: Cg
* Criterion: Involving the percept of any article of clothing such as hat, boots, belt, necktie, jacket, trousers, scarf.
Category: Clouds
* Symbol: Cl
* Criterion: Used specifically for the content cloud. Variations of this category, such as fog or mist are coded Na.
Category: Explosion
* Symbol: Ex
* Criterion: Involving percepts of a blast or explosion, including fireworks.
Category: Fire
* Symbol: Fi
* Criterion: Involving percepts of fire or smoke.
Category: Food
* Symbol: Fd
* Criterion: Used for any edible common for humans, such as fried chicken, ice cream, fried shrimp, vegetables, cotton candy, chewing gum, steak, a filet of fish, or for animals eating a food that is natural for their species, such as a bird eating a worm or insect.
Category: Geography
* Symbol: Ge
* Criterion: Involving the percept of a map, specified or unspecified.
Category: Household
* Symbol: Hh
* Criterion: Involving percepts of household items, such as bed, carving knife, chair, cooking utensil, cup, garden hose, glass, lamp, lawnchair, plate, rug (animal skin rug should be coded Ad and Hh used as a secondary content), silverware. Some items coded Hh will also be coded as Art, such as candelabra, chandelier, or artistically created pieces such as a centerpiece bowl.
Category: Landscape
* Symbol: Ls
* Criterion: Involving percepts of landscape, such as mountain, mountain range, hill, island, cave, rocks, desert, swamp, or seascapes, such as coral reef or underwater scene.
Category: Nature
* Symbol: Na
* Criterion: Used for a broad variety of contents from the natural environment that are not coded as Bt or Ls, such as sun, moon, planet, sky, water, ocean, river, ice, snow, rain, fog, mist, rainbow, storm, tornado, night, raindrop.
Category: Science
* Symbol: Sc
* Criterion: Involving percepts that are associated with, or are the direct or indirect products of science or science fiction, such as airplanes, buildings, bridges, cars, light bulb, microscope, motorcycles, motors, musical instrument, radar station, rocket ships, ships, space ships, trains, telescope, TV aerial, weapons, etc.
Category: Sex
* Symbol: Sx
* Criterion: Involving percepts of sex organs or activity of a sexual nature, such as penis, vagina, buttocks, breasts (except when used to identify the sex of a human figure), testes, menstruation, abortion, intercourse. Sx is usually scored as a secondary content. Primary contents are typically H, Hd, or An.
Category: X-ray
* Symbol: Xy
* Criterion: Used specifically for the content of x-ray and may include either skeletal or organs. When Xy is coded, An is not included as a secondary code.
Category: Unusual Contents
* Symbol: Id
* Criterion: Some responses will include contents that do not seem to fit into one of the standard content categories. When that occurs, the unique content should be written out and entered under idiographic contents (Id) on the Structural Summary Blank. However, it is important to make sure that the item does not fit into one of the standard content categories before deciding to enter it idiographically.
---
Respond: Because it is black it seems like a bat.
Output: Examinee's response is a bat. Bat is an animal. Therefore the output symbol is A.

Respond: {Respond}
Output:
"""



RULE['common'] = """
Overview of Rorschach Coding Process
The coding process for Rorschach responses involves transforming qualitative data from the test into quantitative scores that can be analyzed statistically and interpreted. The process includes two main parts:
1. Coding Each Response: Each response is coded according to several categories.
2. Organizing Codes: Codes or scores for each response are entered onto a page or a computer program that organizes all the coded information category by category, referred to as the Sequence of Scores sheet.

Detailed Steps in Coding
1. Understanding Theoretical Goals: Knowledge of the Rorschach's theoretical framework is crucial for coding. Coders should aim to grasp how the characteristics of a person are integrated within their responses.
2. Application of Codes: Coders follow specific rules to assign a code to each response, focusing on capturing the cognitive operation present at the time the subject gave the answer. Every component appearing in the response should be coded to prevent errors of omission which can lead to a distorted interpretation.
3. Using Coding Tools: Coders use a Rorschach Scoring worksheet which aids in ensuring accuracy and speed. This worksheet includes fields for all coding categories and provides references to the coding rules.

Key Rules of Coding
* Cardinal Rule: The code should represent the cognitive operation at the time the subject gave the answer. Do not code based solely on the initial Inquiry Phase; include data from both the Response and Inquiry Phases.
* Completeness: Ensure all components of the response appear in the coding. Omissions can be more detrimental than disagreements over how something is coded.

You are a psychologist conducting a Rorschach test analysis.
Your examinee is {age}-years old, {gender}, who is living in {country}.
You have to do coding process to make proper codes, a set of symbols, which represents the feature of the response from the participants.
You must choose only one symbol.
If you need more information to determine, please write "I need more explanation."
Output should contain symbol of contents and explanation of the reason why symbol chosen.
Output format:
 - Symbol:
 - Explanation:
"""

NEED_MORE_INFO = "I need more explanation."

def create_prompt(rule:str) -> PromptTemplate:
    return PromptTemplate.from_template(
        "\n---\n".join([
            RULE['common'],
            RULE[rule],
        ])
    )


class Robot:
    def __init__(self, age, gender, country):
        self.llm = ChatUpstage(api_key=API_KEY)

        self.age = age
        self.gender = gender
        self.country = country

    def _invoke(self, part:str, message:str):
        chain = create_prompt(part) | self.llm | StrOutputParser()
        answer = chain.invoke({
            "Respond":message,
            "age":self.age,
            "gender":self.gender,
            "country":self.country
        })
        return answer

    def run(self, message:str):
        return "\n---\n".join([
            self._invoke(p, message) for p in ["development", "determinant", "content"]
        ])
