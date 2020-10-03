% Talks

# Talks


<!-- -->


::: {#talk-2020-08-madpl-backward-geometry-synthesis .anchor}
::: {.talk-entry}
  **Synthesizing Backward through the Geometry Pipeline** \
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


::: {#talk-2018-09-galois-verdi .anchor}
::: {.talk-entry}
  **Formally Verifying Implementations of Distributed Systems** \
  Galois Inc on 2018-09-13 \
  [abstract](#abs-2018-09-galois-verdi){aria-controls='abs-2018-09-galois-verdi' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [slides](talks/2018-09-galois-verdi-slides.pdf) &nbsp;
  [event](https://galois.com/blog/2018/09/public-tech-talk-formally-verifying-implementations-of-distributed-systems/) &nbsp;
:::
:::
::: {#abs-2018-09-galois-verdi .collapse}
::: {.card .card-body .abs-card}

Distributed systems are difficult to implement correctly because they must
handle both concurrency and failures: machines may crash at arbitrary points
and networks may reorder, drop, or duplicate packets. Further, their behavior
is often too complex to permit exhaustive testing. In this talk, we’ll survey
the [Verdi] project which provides a framework for implementing and formally
verifying implementations of distributed systems in Coq. Verdi eases the
verification burden by enabling developers to first verify their system under
an idealized fault model, then transfer the resulting correctness guarantees to
a more realistic fault model without any additional proof burden. Using this
approach, the Verdi team produced the first correctness proof for an
implementation of the Raft distributed consensus protocol.

<!-- See also: -->
<!-- TODO -->

:::
:::


<!-- -->


::: {#talk-2018-07-coqworkshop-verdi .anchor}
::: {.talk-entry}
  **Formally Verifying Distributed Systems in Coq** \
  Coq Workshop on 2018-07-08 \
  [abstract](#abs-2018-07-coqworkshop-verdi){aria-controls='abs-2018-07-coqworkshop-verdi' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [slides](https://easychair.org/smart-slide/slide/gJSP#) &nbsp;
  [event](https://coqworkshop2018.inria.fr/program/) &nbsp;
:::
:::
::: {#abs-2018-07-coqworkshop-verdi .collapse}
::: {.card .card-body .abs-card}

<!-- TODO update -->

Distributed systems are difficult to implement correctly because they must
handle both concurrency and failures: machines may crash at arbitrary points
and networks may reorder, drop, or duplicate packets. Further, their behavior
is often too complex to permit exhaustive testing. In this talk, we’ll survey
the [Verdi] project which provides a framework for implementing and formally
verifying implementations of distributed systems in Coq. Verdi eases the
verification burden by enabling developers to first verify their system under
an idealized fault model, then transfer the resulting correctness guarantees to
a more realistic fault model without any additional proof burden. Using this
approach, the Verdi team produced the first correctness proof for an
implementation of the Raft distributed consensus protocol.

<!-- See also: -->
<!-- TODO -->

:::
:::


<!-- -->


::: {#talk-2017-08-dagstuhl-fpbench .anchor}
::: {.talk-entry}
  **FPBench: Toward Standard Floating Point Benchmarks** \
  Dagstuhl on 2017-08-29 \
  MPI-SWS on 2017-08-25 \
  [abstract](#abs-2017-08-dagstuhl-fpbench){aria-controls='abs-2017-08-dagstuhl-fpbench' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [slides](talks/2017-08-dagstuhl-fpbench-slides.pdf) &nbsp;
  [event](https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=17352) &nbsp;
:::
:::
::: {#abs-2017-08-dagstuhl-fpbench .collapse}
::: {.card .card-body .abs-card}

[FPBench] is a standard format and common set of benchmarks for
  floating-point accuracy tests.
The goal of FPBench is to enable
  direct comparisons between competing tools,
  facilitate the composition of complementary tools, and
  lower the barrier to entry for new teams working on numerical tools.
FPBench collects benchmarks from published papers
  in a standard format and with standard accuracy measures and metadata.
As a single repository for benchmarks,
  FPBench can be used to guide the development of new tools,
  evaluate completed tools, or
  compare existing tools on identical inputs,
  all while avoiding duplication and the manual effort
  and inevitable errors of translating between input formats.

See also:

- [Pavel][Pavel Panchekha]'s
  [related talk](https://www.youtube.com/watch?v=WvDZ4m4fAF0)
  on combining [Herbie] and [Herbgrind] using [FPBench].

:::
:::


<!-- -->


::: {#talk-2017-02-utah-herbie-herbgrind-fpbench .anchor}
::: {.talk-entry}
  **Automatically Improving Accuracy for Floating Point Expressions** \
  University of Utah on 2017-02-03 \
  [abstract](#abs-2017-02-utah-herbie-herbgrind-fpbench){aria-controls='abs-2017-02-utah-herbie-herbgrind-fpbench' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [slides](talks/2017-02-utah-herbie-herbgrind-fpbench-slides.pdf) &nbsp;
  [event](https://www.cs.utah.edu/calendar/colloquium-zach-tatlock/) &nbsp;
:::
:::
::: {#abs-2017-02-utah-herbie-herbgrind-fpbench .collapse}
::: {.card .card-body .abs-card}

Most engineering and scientific computer programs follow mathematical models
described by real numbers, but use floating point arithmetic internally.
Sometimes the two number systems give rather different results, and when that
happens programmers are often ill-equipped to improve the accuracy of their
code. Experts in numerical methods can fix these problems by rearranging
computations, but acquiring that expertise can take years. My colleagues and I
are working to bridge this gap with [Herbie], a tool that automatically improves
the accuracy of floating point expressions.

In this talk I will describe the techniques Herbie uses to automatically
improve floating point accuracy using a guided, heuristic search. Herbie
applies algebraic rewrites and series expansions to generate
potentially-more-accurate versions of the program, then samples inputs to
evaluate, prune, and combine these candidates into a new, more-accurate
program. We’ve used Herbie on expressions found everywhere from textbooks to
large-scale surveys of open-source software, and consistently find good
results. I’ll also briefly discuss next steps for Herbie: scaling up to larger
codebases and a new format to standardize floating point benchmarks.

<!-- See also: -->
<!-- TODO -->

:::
:::


<!-- -->



