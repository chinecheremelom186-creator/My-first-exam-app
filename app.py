import streamlit as st

# Custom Branding
st.set_page_config(page_title="KanteChukwu Quiz App")
st.title("Medical Study Quiz")
st.sidebar.write("### Powered by KANTECHUKWU")
st.sidebar.write("Focus. Growth. Knowledge.")

# Your quiz_data list goes here...
quiz_data = [
    {"q": "Flowering plants are also known as?", "options": ["Gymnosperms", "Angiosperms", "Bryophytes", "Pteridophytes"], "answer": "Angiosperms", "exp": "Flowering plants are called angiosperms because their seeds are enclosed within fruits."},
    {"q": "The word 'angio' means?", "options": ["Root", "Flower", "Vessel or enclosure", "Leaf"], "answer": "Vessel or enclosure", "exp": "“Angio” refers to a vessel/enclosure, while “sperm” means seed."},
    {"q": "The reproductive structure of flowering plants is the?", "options": ["Root", "Stem", "Flower", "Leaf"], "answer": "Flower", "exp": "Flowers contain reproductive parts such as pollen, ovule, stamen, and carpel."},
    {"q": "After fertilization, the ovary develops into?", "options": ["Root", "Fruit", "Seed coat", "Stem"], "answer": "Fruit", "exp": "In angiosperms, the ovary becomes the fruit that surrounds the seed."},
    {"q": "Non-flowering plants reproduce mainly through?", "options": ["Flowers", "Fruits", "Spores or naked seeds", "Leaves"], "answer": "Spores or naked seeds", "exp": "Bryophytes and pteridophytes use spores, while gymnosperms produce naked seeds."},
    {"q": "Which of the following is a bryophyte?", "options": ["Pine", "Moss", "Fern", "Cycad"], "answer": "Moss", "exp": "Bryophytes include mosses and reproduce by spores."},
    {"q": "Gymnosperms are called 'naked seed plants' because?", "options": ["They lack roots", "Their seeds are exposed", "They have no leaves", "They produce flowers"], "answer": "Their seeds are exposed", "exp": "Gymnosperm seeds are not enclosed in fruits but are usually found in cones."},
    {"q": "Which group produces seeds enclosed within fruits?", "options": ["Angiosperms", "Gymnosperms", "Bryophytes", "Ferns"], "answer": "Angiosperms", "exp": "The defining feature of flowering plants is enclosed seeds inside fruits."},
    {"q": "The vascular tissues in plants are?", "options": ["Epidermis and cortex", "Xylem and phloem", "Root and stem", "Flower and fruit"], "answer": "Xylem and phloem", "exp": "The plant vascular system consists of xylem and phloem for transport."},
    {"q": "Non-vascular plants lack?", "options": ["Leaves", "Flowers", "Xylem and phloem", "Roots"], "answer": "Xylem and phloem", "exp": "Mosses and liverworts lack vascular tissues and depend on diffusion and osmosis."},
    {"q": "Xylem mainly transports?", "options": ["Sugars", "Water and minerals", "Oxygen", "Proteins"], "answer": "Water and minerals", "exp": "Xylem carries water and dissolved minerals from roots to aerial parts of the plant."},
    {"q": "The word xylem originates from the Greek word?", "options": ["Phloios", "Xylon", "Angio", "Sperm"], "answer": "Xylon", "exp": "Xylon means wood and relates to xylem’s role in woody support."},
    {"q": "Which cells are responsible for water conduction in xylem?", "options": ["Companion cells", "Sieve tubes", "Vessel elements and tracheids", "Phloem fibers"], "answer": "Vessel elements and tracheids", "exp": "These two xylem cell types conduct water through the plant."},
    {"q": "Vessel elements differ from tracheids because vessel elements are?", "options": ["Longer and thinner", "Wider and shorter", "Living cells with nuclei", "Found in phloem"], "answer": "Wider and shorter", "exp": "Vessel elements are wider and connect end-to-end through perforation plates."},
    {"q": "The process responsible for upward water movement in xylem is mainly explained by?", "options": ["Translocation theory", "Cohesion-tension theory", "Cell division theory", "Respiration theory"], "answer": "Cohesion-tension theory", "exp": "Transpiration creates tension that pulls water upward through xylem."},
    {"q": "Phloem transports?", "options": ["Water only", "Organic nutrients such as sugars", "Minerals only", "Oxygen only"], "answer": "Organic nutrients such as sugars", "exp": "Phloem transports food produced during photosynthesis from leaves to other parts."},
    {"q": "The movement of sugars through phloem is called?", "options": ["Transpiration", "Diffusion", "Translocation", "Respiration"], "answer": "Translocation", "exp": "Translocation is the movement of organic substances through phloem from source to sink."},
    {"q": "The cells that assist sieve tube elements are?", "options": ["Vessel elements", "Companion cells", "Tracheids", "Xylem fibers"], "answer": "Companion cells", "exp": "Companion cells regulate sugar transport and support sieve tubes."},
    {"q": "Girdling removes a ring of?", "options": ["Xylem", "Bark containing phloem", "Roots", "Leaves"], "answer": "Bark containing phloem", "exp": "Removing phloem interrupts sugar movement from leaves to roots."},
    {"q": "A major function of lignin is?", "options": ["Sugar production", "Providing rigidity and waterproofing", "Transporting food", "Producing flowers"], "answer": "Providing rigidity and waterproofing", "exp": "Lignin strengthens plant cell walls, especially in xylem."},
    {"q": "In dicot plants, vascular tissues are arranged?", "options": ["Randomly", "In bundles scattered throughout the stem", "In a ring", "Outside the plant"], "answer": "In a ring", "exp": "Dicots have xylem inside and phloem surrounding it in a ring arrangement."},
    {"q": "Monocots usually lack?", "options": ["Xylem", "Phloem", "Vascular cambium", "Roots"], "answer": "Vascular cambium", "exp": "Without vascular cambium, monocots usually do not increase in stem diameter."},
    {"q": "The animal circulatory system mainly transports?", "options": ["Only water", "Nutrients and gases", "Only hormones", "Only waste"], "answer": "Nutrients and gases", "exp": "Circulatory systems distribute nutrients, gases, and wastes throughout animals."},
    {"q": "A closed circulatory system is characterized by?", "options": ["Blood mixing with body cavity fluid", "Blood being contained inside vessels", "Absence of a heart", "Lack of circulation"], "answer": "Blood being contained inside vessels", "exp": "In closed systems, blood remains within vessels and circulates around the body."},
    {"q": "Arthropods usually possess?", "options": ["Closed circulatory systems", "Open circulatory systems", "No circulatory systems", "Plant-like vascular systems"], "answer": "Open circulatory systems", "exp": "Insects and many mollusks use open circulation where hemolymph enters body cavities."}
]
