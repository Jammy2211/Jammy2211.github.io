# Natural Language & AI

**I believe natural language is becoming the primary interface for doing science.**

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
science or software. You describe what you want to understand, and an AI
coding agent turns that request into an interactive analysis where you can
inspect the data, ask questions, change the model and learn as you go.

You can weigh a galaxy yourself. The COSMOS-Web Ring is one
of the most striking gravitational lenses the James Webb Space Telescope has
found. It was discovered in the COSMOS-Web survey by
[Mercier et al. (2024)][mercier] and is part of the
[COSMOS-Web Lens Survey (COWLS)][cowls], which I lead. A massive galaxy at
a redshift of about 2 bends the light of a more distant galaxy, at a
redshift of about 5.1, into an almost perfect ring. JWST imaged it in four
colours, and because gravitational lensing bends every colour of light in
the same way, the ring looks the same in all of them. With the assistant,
you can look at the JWST image, fit a lens model in a few minutes on a
laptop and measure the mass inside the ring: a few hundred billion times
the mass of the Sun. You do not need to know all the physics or write the
code beforehand: you can build that understanding through the analysis
itself.

The assistant starts by asking who you are, whether a curious reader, a
student or a researcher, and pitches the walkthrough to your background.

**Try it yourself.** Open Claude Code, Codex or another supported AI coding
agent and start with this prompt; the agent installs the
[assistant][lens-assistant] itself:

::: {.science-example}
![The COSMOS-Web Ring: a near-complete ring of lensed light around a massive galaxy, imaged by JWST.][ring-image]

::: {.science-request}
**Your starting prompt**

```{#starting-prompt .prompt-text}
I want to use the PyAutoLens Assistant:
https://github.com/PyAutoLabs/autolens_assistant
First clone that repository, cd into it and follow its AGENTS.md.

I'd like to understand how gravitational lensing works using the JWST image
of the COSMOS-Web Ring that ships with the assistant. Show me the picture,
explain what we are looking at, and walk me through fitting a lens model so
we can measure the mass inside the ring and see how well the model
reproduces the observations. Pitch it at my level: ask me what my background
is first. Explain what we are doing as we go, and let me ask questions or
change the analysis along the way.
```

:::
:::

::: {.image-credit}
The COSMOS-Web Ring (COSJ100024+015334), JWST NIRCam colour image from the
COSMOS-Web Lens Survey (COWLS). Credit: COWLS / Nightingale et al. (2025);
discovered by Mercier et al. (2024).
:::

::: {.science-request .route-card}
**Prefer a notebook?**

Open [the same analysis as a Google Colab notebook][colab-ring], with more
explanation. It is recommended if you are learning PyAutoLens and want to
see the code.
:::

That is what excites me about natural language as an interface to science:
you can go from asking “How do we weigh a galaxy?” to working with real
observations and measuring its mass yourself. You stay involved throughout,
questioning assumptions, exploring results and deciding what to investigate
next.

## Learning the science

Being able to measure a galaxy's mass through natural language does not remove
the need to understand the science
behind that measurement. To direct an analysis well, you still need to
understand the physics, the modelling
assumptions and how uncertainty is quantified. I design my natural-language
software with that in mind: easier access to
sophisticated analysis should make scientific understanding more important, not
less.

This is why I am building education directly into my natural-language software
ecosystem.
The [HowToLens Lectures][howtolens] teach gravitational lensing from first
principles, pairing explanations with Python
that readers can run and explore. The PyAutoLens Assistant can also act as a
teacher, explaining concepts, answering
questions and helping users understand the analysis they are directing.

The aim is that a researcher first develops the knowledge needed to understand
and direct an analysis, and can then use
natural language to put that knowledge into practice. You
can [try the first HowToLens science lecture in Google Colab][colab] in your
browser, where eligible users can also use
Colab's Gemini integration to ask questions about the science and code as they
work through it.

## Building software through natural language

I also use natural language to develop the software itself. Through
[PyAutoScientist][scientist], I describe scientific and software requirements
in plain English, with AI coding agents helping plan, implement, test and
document the changes. I set the direction and review the work, while the
code remains open and available to inspect. This connects how I build
scientific tools with how researchers learn to use them and carry out science.

## Teaching natural-language science

I teach these ideas through my workshop Using Natural Language to Do Science:
How Agentic AI Empowers Astronomers.
It shows researchers how natural language can become the starting point for
scientific work: understanding unfamiliar
software, developing analyses, running and debugging code, interrogating results
and refining scientific questions
with an AI coding assistant.

The message is the same as for my software: the scientist leads the research,
while AI removes technical friction between
an idea and putting it into practice. The aim is to help researchers work this
way confidently while retaining the
scientific understanding, judgement and autonomy needed to direct the science.

[Download the workshop slides (PowerPoint)][slides]. This version focuses
on PyAutoLens.

[slides]: NaturalLanguageLens.pptx
[lens-assistant]: https://github.com/PyAutoLabs/autolens_assistant
[galaxy-assistant]: https://github.com/PyAutoLabs/autogalaxy_assistant
[fit-assistant]: https://github.com/PyAutoLabs/autofit_assistant
[cti-assistant]: https://github.com/PyAutoLabs/autocti_assistant
[lens]: https://github.com/PyAutoLabs/PyAutoLens#getting-started
[ring-image]: ../assets/images/cosmos_web_ring_rgb.png
[cowls]: https://arxiv.org/abs/2503.08777
[mercier]: https://arxiv.org/abs/2309.15986
[colab-ring]: https://colab.research.google.com/github/PyAutoLabs/autolens_assistant/blob/main/docs/colab/cosmos_web_ring_colab.ipynb
[howtolens]: https://github.com/PyAutoLabs/HowToLens
[howtogalaxy]: https://github.com/PyAutoLabs/HowToGalaxy
[howtofit]: https://github.com/PyAutoLabs/HowToFit
[colab]: https://colab.research.google.com/github/PyAutoLabs/HowToLens/blob/2026.9.19.1/notebooks/chapter_1_introduction/tutorial_1_grids_and_galaxies.ipynb
[scientist]: https://github.com/PyAutoLabs/PyAutoScientist
