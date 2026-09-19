# Natural Language as an Interface to Science

I believe natural language is becoming a new interface for doing science.
Scientists can increasingly describe the analysis they want to perform in the
same language they use to think, discuss and write about their research, with
agentic AI translating those instructions into computational workflows.

For decades, scientists have used programming languages, command-line tools and
software APIs to tell computers how to perform science. Doing so has required
researchers to learn the technical syntax needed to translate a scientific idea
into instructions a computer can execute. That syntax was never the science
itself: it was the interface between the scientist's ideas and the computer
carrying them out.

Natural language changes that interface. A scientist can now describe the
scientific task directly, while AI translates that intent into code,
calculations, figures and reproducible analyses. The scientist is still making
the computer do the science; what changes is the language used to express that
intent. Those who want to work directly with code still can, but increasingly
they will not need to.

My aim is to make natural language the primary way scientists turn ideas into
research: scientific idea → natural language → AI → scientific result. AI
provides the capability, natural language provides the interface, and the
scientist remains in control of the questions, decisions and interpretation.

## Scientific Assistants

I am putting this vision into practice by redesigning my scientific software
around natural language, via AI coding assistants.

The PyAutoLens Assistant allows a scientist to perform strong gravitational-lens
modelling by describing the analysis they want to carry out in natural language.
The AI coding assistant translates that scientific intent into the software,
code and computational steps needed to perform the analysis, while remaining
interactive throughout so the scientist can inspect the results and decide what
happens next. I am developing this same approach across my other scientific
software packages.

Assistant describes the relationship I want between the AI and the researcher:
the scientist leads, the AI helps make the science happen.

For example, I can use the PyAutoLens Assistant to reproduce the analysis that
led to my discovery of an ultramassive black hole in the strong gravitational
lens Abell 1201 with an instruction as concise as:

> Reproduce my Abell 1201 strong-lens analysis, fitting models with and without
> a central black hole. Compare the models and measure the black-hole mass.

Expressing the same analysis directly in Python requires translating this
scientific intent into many layers of syntax, classes and API calls. Natural
language makes the scientific intent itself the starting point, with the AI
coding assistant translating it into the detailed computational workflow.

This philosophy now shapes how my software is documented. The PyAutoLens
documentation and GitHub README encourage new users to begin with
natural-language prompts that describe the science they want to perform,
lowering the technical barrier between understanding a scientific analysis and
actually carrying it out.

The Python API is not hidden or replaced. All of my software packages continue
to document it explicitly — for example, the PyAutoFit Python API — and provide
Jupyter notebooks containing complete, end-to-end scientific analyses paired
directly with the Python that performs them. These are designed to be read and
understood by a scientist, providing a transparent path from natural-language
intent to the underlying implementation.

Natural language removes the syntax barrier, not the need to understand the
science. Being able to ask an AI coding assistant to fit a gravitational lens
does not remove the need to understand gravitational lensing, Bayesian
inference, galaxy structure or whether the resulting model makes scientific
sense. Making sophisticated tools easier to use makes that scientific
understanding more important, not less.

This is why I am building education directly into my natural-language software
ecosystem. HowToLens teaches strong gravitational lensing and lens modelling
from first principles, combining the underlying science with the Python used to
perform it. Companion HowTo lecture series do the same for the other scientific
areas covered by my software.

The aim is that a researcher first develops the knowledge needed to understand
and direct an analysis, and can then use natural language to put that knowledge
into practice. Learn the science → describe the analysis → use AI to help
perform it → inspect and interpret the result. Natural language lowers the
technical barrier to carrying out the science; it does not lower the
intellectual standard required to do it well.

The lectures can be run interactively in Google Colab, where Google's Gemini
integration allows a learner to read the material, run the Python and ask
questions about the science or code as they work through it.

Try the first HowToLens lecture in Google Colab →

The same AI that helps perform the research can therefore also help scientists
build the knowledge needed to lead it.

## Teaching Natural-Language Science

I am also teaching scientists how to work in this way through my workshop Using
Natural Language to Do Science: How Agentic AI Empowers Astronomers, which I
have delivered three times.

The workshop moves beyond using AI simply to write or explain code. It shows
researchers how natural language can become the starting point for scientific
work: understanding an unfamiliar codebase, developing an analysis, running and
debugging software, interrogating results and iterating on the science with an
AI coding assistant.

The central message is the same as for my software: the scientist leads the
research, while AI removes technical friction between an idea and putting that
idea into practice. My aim is to help researchers use these tools confidently
while retaining the scientific understanding, judgement and autonomy that
ultimately determine the quality of the research.

[View the workshop slides →]

## Natural Language Software Development

Natural language is also changing how I develop scientific software itself. In
March 2026, after more than a decade of writing scientific software largely by
hand, I transitioned the development of PyAutoLens-JAX to a natural-language,
agentic-AI ecosystem called PyAutoScientist. I can now describe what I want the
software to do in plain English, with AI coding agents helping plan, implement,
test and document the changes.

PyAutoScientist is organised as a software organism, with different repositories
playing roles analogous to human organs. PyAutoBrain is the reasoning centre,
interpreting development requests and coordinating specialist coding agents.
PyAutoMind records my scientific and software-development intent in natural
language and tracks ideas from their initial description through to
implementation. PyAutoMemory provides long-term scientific memory, connecting
the software to literature, documentation and verifiable citations.

Together, these tools allow me to carry out substantial software development
through natural language: idea → natural-language requirement → AI planning and
implementation → tested scientific software. The source code remains open,
inspectable and reproducible, but writing every line of it myself is no longer
the only way I can build scientific software.

For me, this completes the natural-language workflow: I can learn and
communicate the science in natural language, perform the science through
natural-language assistants, and now develop the scientific software itself in
the same way.

## Natural Language Software Development

Natural language is also changing how I develop scientific software itself. I
develop PyAutoScientist, a natural-language, agentic-AI development ecosystem in
which I describe scientific and software-development ideas in plain English and
AI coding agents help plan, implement, test and document them. PyAutoScientist
is organised as a software organism: PyAutoBrain acts as the reasoning centre,
interpreting requests and coordinating specialist coding agents; PyAutoMind
records scientific and development intent and tracks ideas through to
implementation; and PyAutoMemory provides long-term scientific memory through
literature, documentation and verifiable citations. Together, they let me carry
out substantial software development through natural language while keeping the
underlying code open, inspectable and reproducible. If that sounds interesting,
explore the PyAutoLabs GitHub organisation.
