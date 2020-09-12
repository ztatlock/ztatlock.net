% Talks

# Talks

::: {#talk-2020-08-madpl-backward-geometry-synthesis .anchor}
::: {.talk-entry}

**Synthesizing Backward through the Geometry Pipeline** <br>
madPL Seminar, University of Wisconsin on 2020-08-19 <br>
[abstract](#abs-2020-08-madpl-backward-geometry-synthesis){aria-controls='abs-2020-08-madpl-backward-geometry-synthesis' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
[talk](https://www.youtube.com/watch?v=vOUP2wT-k1U) &nbsp;
[slides](talks/2020-08-madpl-backward-geometry-synthesis-slides.pdf) &nbsp;
[event](https://madpl.cs.wisc.edu/pl-seminar/20200819-zach_tatlock/)

:::
:::
::: {#abs-2020-08-madpl-backward-geometry-synthesis .collapse}
::: {.card .card-body .abs-card}

Most physical goods are actually program outputs: designers develop declarative
specifications of objects, such specifications are then compiled down to
control languages, and finally control programs are executed by fabrication
devices to physically implement the design.

Given the rise of "desktop manufacturing" in the form of affordable 3D
printers, laser cutters, and mini CNC mills, why does the design-to-prototype
workflow still require so much expertise, tinkering, and failure?

We are trying to figure that out. Our key hypothesis is that “designs are just
programs” and therefore we can bring all the powerful machinery of modern
Programming Languages research to bear on the problem: synthesis, language
design, and compiler optimizations all have a role to play.

In this talk, I describe some of our efforts to help users get more-editable
designs out of the low-level representations commonly shared online. This
"decompilation" starts with a description of an object’s surface as a set of
triangles and ends up with high-level CAD program that parameterizes over
repetitive design features. Along the way we’ll see some semantics for CAD,
domain-specific heuristics for geometry synthesis, and some new techniques that
extend equality saturation in addressing the dread "AC matching problem" that
makes trouble for all kinds of automated solvers. I highlight how the new
[egg] egraph library enables new kinds of synthesis by specializing egraphs to
equality saturation and enables greater flexibility via novel eclass analyses.

See also:

- [Synthesizing Structured CAD Models with Equality Saturation and Inverse Transformations](publications.html#pub-2020-pldi-szalinski-cad-eqsat)
<!-- TODO Reincarnate -->

:::
:::

