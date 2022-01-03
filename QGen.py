# -*- coding: utf-8 -*-
from git import Repo
import pickle
Repo.clone_from("https://github.com/patil-suraj/question_generation.git",'/git')

# !pip install -U transformers==3.0.0
# python -m nltk.downloader punkt
# git clone https://github.com/patil-suraj/question_generation.git

text = "42 is the answer to life, universe and everything."

from pipelines import pipeline

nlp = pipeline("multitask-qa-qg", model="valhalla/t5-base-qa-qg-hl")

nlp(text)

# nlpS = pipeline("multitask-qa-qg")

# nlpS(text)

text2 = "Gravity from Latin gravitas, meaning 'weight', or gravitation, is a natural phenomenon by which all things with mass or energy—including planets, stars, galaxies, and even light—are brought toward (or gravitate toward) one another. On Earth, gravity gives weight to physical objects, and the Moon's gravity causes the ocean tides. The gravitational attraction of the original gaseous matter present in the Universe caused it to begin coalescing and forming stars and caused the stars to group together into galaxies, so gravity is responsible for many of the large-scale structures in the Universe. Gravity has an infinite range, although its effects become increasingly weaker as objects get further away"