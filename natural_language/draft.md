# Natural Language & AI

I am pioneering ways for scientists to do research through natural language:
describing an idea, asking a question or requesting an analysis in the words
they already use to discuss their science. Agentic AI makes this possible by
turning those instructions into code and computational workflows. My aim is
to put more research capability into scientists' hands, while keeping them
in control of the questions, assumptions and interpretation.

## Scientific assistants

I am putting this approach into practice through dedicated scientific
assistants. The [PyAutoLens Assistant][lens-assistant] helps researchers
analyse gravitational lenses: systems in which a galaxy's gravity bends
the light from a more distant galaxy into arcs or multiple images.
Researchers describe the analysis they want, discuss choices with the
assistant, and inspect the code, figures and results it produces.

One example comes from my research on [Abell 1201][black-hole-paper], where
my collaborators and I discovered a black hole around 33 billion times
the mass of the Sun through its effect on gravitationally lensed light.
An instruction to investigate its mass could be:

::: {.science-example}
![Abell 1201 with a bright arc of gravitationally lensed light.][abell-image]

::: {.science-request}
**An example scientific instruction**

> Model the black hole at the centre of Abell 1201 as a point mass.
> Estimate its mass and uncertainty, and show how well the model fits
> the observations.

This example is being developed and validated as an assistant benchmark.
:::
:::

::: {.image-credit}
Abell 1201. Image: Nightingale et al. (2023), via [Astrobites][astrobites].
The image shows the lens system; the black hole is not directly visible.
:::

The scientist supplies the research direction and judges the result.
“Assistant” describes that relationship: the researcher leads and decides
what to delegate. I am extending this approach through the
[PyAutoGalaxy][galaxy-assistant], [PyAutoFit][fit-assistant] and
[PyAutoCTI][cti-assistant] assistants, for galaxy structure, statistical
inference and the correction of distortions introduced by telescope detectors.

This also changes how I introduce people to my software. The
[PyAutoLens getting-started guide][lens] begins with the assistant, making
scientific questions and natural-language instructions the entry point.
The Python API and worked Jupyter notebooks provide the next layer of
detail, so users can understand, inspect and adapt the underlying analysis.

## Learning the science

Directing an analysis requires understanding the science behind it. For
lensing, that includes gravity, galaxy structure and Bayesian inference:
how we use data to constrain models and quantify uncertainty. Easier access
to sophisticated tools makes the ability to question their results essential.

I build that education into the same ecosystem. [HowToLens][howtolens]
teaches gravitational lensing and lens modelling from first principles,
pairing explanations with Python that readers can run and explore.
[HowToGalaxy][howtogalaxy] and [HowToFit][howtofit] do the same for galaxy
modelling and statistical inference. Researchers can build their knowledge
while learning to direct an assistant and assess its work.

You can [try the first HowToLens science lecture in Google Colab][colab]
in your browser. Colab's Gemini integration lets eligible users ask
questions about the notebook's concepts and code as they read and run it.

## Building software through natural language

I also use natural language to develop the software itself. Through
[PyAutoScientist][scientist], I describe scientific and software requirements
in plain English, with AI coding agents helping plan, implement, test and
document the changes. I set the direction and review the work, while the
code remains open and available to inspect. This connects how I build
scientific tools with how researchers learn to use them and carry out science.

## Teaching natural-language science

I have delivered my workshop *Using Natural Language to Do Science: How
Agentic AI Empowers Astronomers* three times. It explores how researchers
can use conversation to understand software, develop analyses, investigate
results and refine their scientific questions, while retaining the knowledge
and judgement needed to lead the research.

[Download the workshop slides (PowerPoint)][slides]. This version focuses
on PyAutoLens.

[slides]: NaturalLanguageLens.pptx
[lens-assistant]: https://github.com/PyAutoLabs/autolens_assistant
[galaxy-assistant]: https://github.com/PyAutoLabs/autogalaxy_assistant
[fit-assistant]: https://github.com/PyAutoLabs/autofit_assistant
[cti-assistant]: https://github.com/PyAutoLabs/autocti_assistant
[lens]: https://github.com/PyAutoLabs/PyAutoLens#getting-started
[black-hole-paper]: https://arxiv.org/abs/2303.15514
[abell-image]: ../assets/images/abell_1201_astrobites.png
[astrobites]: https://astrobites.org/2023/04/05/gravitational-lensing-unveils-ultramassive-black-hole/
[howtolens]: https://github.com/PyAutoLabs/HowToLens
[howtogalaxy]: https://github.com/PyAutoLabs/HowToGalaxy
[howtofit]: https://github.com/PyAutoLabs/HowToFit
[colab]: https://colab.research.google.com/github/PyAutoLabs/HowToLens/blob/2026.9.19.1/notebooks/chapter_1_introduction/tutorial_1_grids_and_galaxies.ipynb
[scientist]: https://github.com/PyAutoLabs/PyAutoScientist
