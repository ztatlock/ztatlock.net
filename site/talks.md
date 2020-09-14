% Talks

# Talks


<!-- -->


::: {#talk-2020-08-madpl-backward-geometry-synthesis .anchor}
::: {.talk-entry}
  **Synthesizing Backward through the Geometry Pipeline** \
  [Zachary Tatlock] \
  madPL Seminar, University of Wisconsin on 2020-08-19 \
  [abstract](#abs-2020-08-madpl-backward-geometry-synthesis){aria-controls='abs-2020-08-madpl-backward-geometry-synthesis' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [talk](https://www.youtube.com/watch?v=vOUP2wT-k1U) &nbsp;
  [slides](talks/2020-08-madpl-backward-geometry-synthesis-slides.pdf) &nbsp;
  [event](https://madpl.cs.wisc.edu/pl-seminar/20200819-zach_tatlock/) &nbsp;
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


<!-- -->


::: {#talk-2020-07-nsv-herbie-fpbench .anchor}
::: {.talk-entry}
  **Towards Numerical Assistants** \
  [Pavel Panchekha], [Zachary Tatlock] \
  Numerical Software Verification @ CAV on 2020-07-21 \
  [abstract](#abs-2020-07-nsv-herbie-fpbench){aria-controls='abs-2020-07-nsv-herbie-fpbench' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [talk](https://www.youtube.com/watch?v=m_tRUSCRM1M) &nbsp;
  [slides](talks/2020-07-nsv-herbie-fpbench-slides.pdf) &nbsp;
  [event](https://nsv2020.github.io/) &nbsp;
:::
:::
::: {#abs-2020-07-nsv-herbie-fpbench .collapse}
::: {.card .card-body .abs-card}

The last few years have seen an explosion of work on tools that address
numerical error in scientific, mathematical, and engineering software.
The resulting tools can provide essential guidance to expert non-experts:
scientists, mathematicians, and engineers for whom mathematical computation
is essential but who may have little formal training in numerical methods.
It is high time these tools move into practice.

Practitioners need a "numerical workbench" that not only succeeds as a research
artifact but as a daily tool. We describe our experience adapting [Herbie],
a tool for numerical error repair, from a research prototype to a reliable
workhorse for daily use. In particular, we focus on how we worked to increase
user trust and use internal measurement to polish the tool. Looking more
broadly, we show that community development and an investment in the generality
of our tools, such as through the [FPBench] project, will better support users
and strengthen our research community.

<!-- See also: -->
<!-- TODO NSV 2016 -->

:::
:::


<!-- -->


::: {#talk-2019-12-tvm-relay-release .anchor}
::: {.talk-entry}
  **TVM Relay: A Functional IR for Analysis and Optimization** \
  [Zachary Tatlock] \
  TVM Conference on 2019-12-05 \
  [abstract](#abs-2019-12-tvm-relay-release){aria-controls='abs-2019-12-tvm-relay-release' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [talk](https://www.youtube.com/watch?v=npqO0hVXZwU&t=1814) &nbsp;
  [slides](talks/2019-12-tvm-relay-release-slides.pdf) &nbsp;
  [event](https://sampl.cs.washington.edu/tvmconf/) &nbsp;
:::
:::
::: {#abs-2019-12-tvm-relay-release .collapse}
::: {.card .card-body .abs-card}

In this talk, I briefly sketch Relay's key design features
and survey all the amazing progress that's made using it
to develop and extend tools in the TVM ecosystem.

<!-- TODO flesh out abstract -->

<!-- See also: -->
<!-- TODO -->

:::
:::


<!-- -->



