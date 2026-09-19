# Natural Language & AI

**I believe natural language is becoming a new interface for doing science.**
Scientists can increasingly describe the analysis they want to perform in the
same language they use to think, discuss and write about their research, with
agentic AI translating those instructions into computational workflows.

For decades, turning a scientific idea into a computational analysis has
required expressing it through the technical syntax of programming languages and
software APIs. That syntax was never the science itself: it was the interface
between the scientist's ideas and the computer carrying them out. Removing that
barrier lets scientists spend less time translating their thinking into code and
more time thinking about the scientific questions they want to answer.

My aim is to make natural language the primary way scientists turn ideas into
research, with AI expanding what they can do while preserving their control and
autonomy. Natural language provides the interface; AI provides the capability;
the scientist provides the understanding, direction and judgement.

## Scientific assistants

**I am putting this vision into practice by redesigning my scientific
software around natural language input.**

The [PyAutoLens Assistant][lens-assistant] lets anyone investigate
gravitational lenses through natural language, even if they are new to the
science or have never used the software before. You describe what you want
to understand, and an AI coding agent turns that request into an interactive
analysis. You can inspect the data, ask questions, change the model and learn
what each step means as you go.

**You can measure the mass of a black hole yourself.** In
[Abell 1201][black-hole-paper], my collaborators and I used gravitational
lensing to discover a black hole around 33 billion times the mass of the Sun.
With the assistant, you can explore the observations and work through a
measurement of its mass, asking it to explain the lensing and guide you
through the modelling. You do not need to arrive knowing all the physics or
how to write the code: you can build that understanding through the analysis
itself.

**Try it yourself.** Follow the [assistant's setup guide][lens-assistant],
open Claude Code, Codex or another supported AI coding agent, and start with:

::: {.science-example}
![Abell 1201 with a bright arc of gravitationally lensed light.][abell-image]

::: {.science-request}
**Your starting prompt**

> I want to use the PyAutoLens Assistant:
> https://github.com/PyAutoLabs/autolens_assistant
>
> I'd like to understand how gravitational lensing can be used to measure the
> black hole in Abell 1201.
>
> Show me the data, explain what we are looking at, and walk me through
> modelling the black hole as a point mass. Let's estimate its mass and
> uncertainty and see how well the model reproduces the observations.
>
> Explain what we are doing as we go, and let me ask questions or change the
> analysis along the way.

:::
:::

::: {.image-credit}
Abell 1201. Image: Nightingale et al. (2023), via [Astrobites][astrobites].
The image shows the lens system; the black hole is not directly visible.
:::

That is what excites me about natural language as an interface to science:
you can go from asking “How do we weigh a black hole?” to working with real
observations and estimating its mass yourself. You remain part of the
analysis throughout, questioning the assumptions, exploring the results and
deciding what to investigate next.

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
