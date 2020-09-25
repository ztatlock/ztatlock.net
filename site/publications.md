% Publications

<style>
  h1 {
    font-size: 1.5rem;
  }
  #body-container {
    max-width: max-content;
    font-size: 0.95rem;
  }
  .abs-card, .bib-card {
    max-width: 40rem;
  }
</style>

# Publications

<!-- HERE -->


<!-- 2020-06 -->


::: {#pub-2020-pldi-szalinski-cad-eqsat .anchor}
::: {.pub-entry}
  **Synthesizing Structured CAD Models with Equality Saturation and Inverse Transformations** \
  [Chandrakana Nandi], [Max Willsey], [Adam Anderson], [James R. Wilcox], <br class='big-only'>
  [Eva Darulova], [Dan Grossman], [Zachary Tatlock] \
  Programming Language Design and Implementation (PLDI) 2020 \
  [paper](pubs/2020-pldi-szalinski-cad-eqsat.pdf) &nbsp;
  [teaser](https://www.youtube.com/watch?v=dnIWBnpZqSo&t=135) &nbsp;
  [talk](https://www.youtube.com/watch?v=2KA602M8t7c) &nbsp;
  [slides](pubs/2020-pldi-szalinski-cad-eqsat-slides.pdf) &nbsp;
  [poster](pubs/2020-pldi-szalinski-cad-eqsat-poster.png) &nbsp;
  [code](https://github.com/uwplse/szalinski/) &nbsp;
  [project](http://incarnate.uwplse.org/) &nbsp;
  [bib](#bib-2020-pldi-szalinski-cad-eqsat){aria-controls='bib-2020-pldi-szalinski-cad-eqsat' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2020-pldi-szalinski-cad-eqsat .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2020-pldi-szalinski-cad-eqsat,
  author    = {Chandrakana Nandi and
               Max Willsey and
               Adam Anderson and
               James R. Wilcox and
               Eva Darulova and
               Dan Grossman and
               Zachary Tatlock},
  editor    = {Alastair F. Donaldson and
               Emina Torlak},
  title     = {Synthesizing Structured {CAD} Models with Equality Saturation and
               Inverse Transformations},
  booktitle = {Proceedings of the 41st {ACM} {SIGPLAN} International Conference on
               Programming Language Design and Implementation, {PLDI} 2020,
               London, UK, June 15-20, 2020},
  pages     = {31--44},
  publisher = {{ACM}},
  year      = {2020},
  url       = {https://doi.org/10.1145/3385412.3386012},
  doi       = {10.1145/3385412.3386012},
}
```
:::
:::


<!-- 2019-11 -->


::: {#pub-2019-siga-carpentry-compiler .anchor}
::: {.pub-entry}
  **Carpentry Compiler** \
  [Chenming Wu], [Haisen Zhao], [Chandrakana Nandi], <br class='big-only'>
  [Jeffrey I. Lipton], [Zachary Tatlock], [Adriana Schulz] \
  ACM Transactions on Graphics (SIGGRAPH ASIA) 2019 \
  [abstract](#abs-2019-siga-carpentry-compiler){aria-controls='abs-2019-siga-carpentry-compiler' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [paper](pubs/2019-siga-carpentry-compiler.pdf) &nbsp;
  [appendix](pubs/2019-siga-carpentry-compiler-appendix.pdf) &nbsp;
  [teaser](https://www.youtube.com/watch?v=yaXKP7lv-CI) &nbsp;
  [slides](pubs/2019-siga-carpentry-compiler-slides.pptx) &nbsp;
  [code](https://github.com/helm-compiler) &nbsp;
  [project](https://grail.cs.washington.edu/projects/carpentrycompiler/) &nbsp;
  [bib](#bib-2019-siga-carpentry-compiler){aria-controls='bib-2019-siga-carpentry-compiler' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#abs-2019-siga-carpentry-compiler .collapse}
::: {.card .card-body .abs-card}

Traditional manufacturing workflows
  strongly decouple design and fabrication phases.
As a result, fabrication-related objectives
  such as manufacturing time and precision
  are difficult to optimize in the design space,
  and vice versa.

This paper presents HL-HELM,
  a high-level, domain-specific language for expressing abstract,
  parametric fabrication plans;
it also introduces LL-HELM,
  a low-level language for expressing concrete fabrication plans that
  take into account the physical constraints of
  available manufacturing processes.
We present a new compiler that supports
  the real-time, unoptimized translation of
  high-level, geometric fabrication operations into
  concrete, tool-specific fabrication instructions;
this gives users immediate feedback on
  the physical feasibility of plans as they design them.

HELM offers novel optimizations to
  improve accuracy and reduce fabrication time
  as well as material costs.
Optimized low-level plans can be interpreted as
  step-by-step instructions for users
  to actually fabricate a physical product.
We provide a variety of example fabrication plans
  in the carpentry domain that
  are designed using our high-level language,
  show how the compiler translates and optimizes
  these plans to generate concrete low-level instructions,
  and present the final physical products fabricated in wood.

<!--
See also:

-
-->

Press:

- [TechCrunch](https://techcrunch.com/2019/12/02/carpentry-compiler-turns-3d-models-to-instructions-on-how-to-build-them/)
- [Popular Woodworking](https://www.popularwoodworking.com/editors-blog/new-software-could-take-the-guesswork-out-of-your-project/)
- [i-programmer](https://www.i-programmer.info/news/98-languages/13310-carpentry-compiler-yes-the-target-is-wood.html)
- [The UW Daily](http://www.dailyuw.com/science/article_5a21a1ce-5c3a-11ea-bf1d-e3dabdecfbbc.html)
- [UW News](https://www.washington.edu/news/2019/12/02/carpentry-compiler/)

:::
:::
::: {#bib-2019-siga-carpentry-compiler .collapse}
::: {.card .card-body .bib-card}
```

@article{2019-siga-carpentry-compiler,
  author    = {Chenming Wu and
               Haisen Zhao and
               Chandrakana Nandi and
               Jeffrey I. Lipton and
               Zachary Tatlock and
               Adriana Schulz},
  title     = {Carpentry compiler},
  journal   = {{ACM} Transactions on Graphics},
  volume    = {38},
  number    = {6},
  pages     = {195:1--195:14},
  year      = {2019},
  url       = {https://doi.org/10.1145/3355089.3356518},
  doi       = {10.1145/3355089.3356518},
}
```
:::
:::


<!-- 2019-10 -->


::: {#pub-2019-oopsla-troika-modular-layout-verification .anchor}
::: {.pub-entry}
  **Modular Verification of Web Page Layout** \
  [Pavel Panchekha], [Michael D. Ernst], [Zachary Tatlock], [Shoaib Kamil] \
  Object-Oriented Programming, Systems, Languages & Applications (OOPSLA) 2019 \
  [paper](pubs/2019-oopsla-troika-modular-layout-verification.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=4nFuMh5y9F8) &nbsp;
  [slides](pubs/2019-oopsla-troika-modular-layout-verification-slides.pdf) &nbsp;
  [code](https://github.com/uwplse/cassius/) &nbsp;
  [project](https://cassius.uwplse.org/) &nbsp;
  [bib](#bib-2019-oopsla-troika-modular-layout-verification){aria-controls='bib-2019-oopsla-troika-modular-layout-verification' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2019-oopsla-troika-modular-layout-verification .collapse}
::: {.card .card-body .bib-card}
```

@article{2019-oopsla-troika-modular-layout-verification,
  author    = {Pavel Panchekha and
               Michael D. Ernst and
               Zachary Tatlock and
               Shoaib Kamil},
  title     = {Modular Verification of Web Page Layout},
  journal   = {Proceedings of the {ACM} on Programming Languages},
  volume    = {3},
  number    = {{OOPSLA}},
  pages     = {151:1--151:26},
  year      = {2019},
  url       = {https://doi.org/10.1145/3360577},
  doi       = {10.1145/3360577},
}
```
:::
:::


<!-- 2019-10 -->


::: {#pub-2019-splashe-theia-psv-viz .anchor}
::: {.pub-entry}
  **Theia: Automatically Generating Correct Program State Visualizations** \
  [Josh Pollock], [Jared Roesch], [Doug Woos], [Zachary Tatlock] \
  ACM SIGPLAN Symposium on SPLASH-E 2019 \
  [paper](pubs/2019-splashe-theia-psv-viz.pdf) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- 2019-09 -->


::: {#pub-2019-ftpl-qed-at-large .anchor}
::: {.pub-entry}
  **QED at Large: A Survey of Engineering of Formally Verified Software** \
  [Talia Ringer], [Karl Palmskog], [Ilya Sergey], [Milos Gligoric], [Zachary Tatlock] \
  Foundations and Trends in Programming Languages (FTPL) 2019 \
  [paper](pubs/2019-ftpl-qed-at-large.pdf) &nbsp;
  [errata](https://proofengineering.org/qed_errata.html) &nbsp;
  [project](https://proofengineering.org/) &nbsp;
  [bib](#bib-2019-ftpl-qed-at-large){aria-controls='bib-2019-ftpl-qed-at-large' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2019-ftpl-qed-at-large .collapse}
::: {.card .card-body .bib-card}
```

@article{2019-ftpl-qed-at-large,
  author    = {Talia Ringer and
               Karl Palmskog and
               Ilya Sergey and
               Milos Gligoric and
               Zachary Tatlock},
  title     = {{QED} at Large: {A} Survey of Engineering of Formally Verified Software},
  journal   = {Foundations and Trends in Programming Languages},
  volume    = {5},
  number    = {2-3},
  pages     = {102--281},
  year      = {2019},
  url       = {https://doi.org/10.1561/2500000045},
  doi       = {10.1561/2500000045},
}
```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Toward Multi-Precision, Multi-Format Numerics** \
  [David Thien], [Bill Zorn], [Pavel Panchekha], [Zachary Tatlock] \
  Software Correctness for HPC Applications (CORRECTNESS) 2019 \
  [paper](pubs/2019-correctness-mpmf.pdf) &nbsp;
  [slides](pubs/2019-correctness-mpmf-slides.pdf) &nbsp;
  [FPBench] &nbsp;
  [Titanic] &nbsp;
  [Herbie] &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Icing: Supporting Fast-Math Style Optimizations in a Verified Compiler** \
  [Heiko Becker], [Eva Darulova], [Magnus O. Myreen], [Zachary Tatlock] \
  Computer-Aided Verification (CAV) 2019 \
  [paper](pubs/2019-cav-icing-verified-fastmath.pdf) &nbsp;
  [slides](pubs/2019-cav-icing-verified-fastmath-slides.pdf) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Teaching Rigorous Distributed Systems With Efficient Model Checking** \
  [Ellis Michael], [Doug Woos], [Thomas E. Anderson], [Michael D. Ernst], [Zachary Tatlock] \
  European Conference on Computer Systems (EuroSys) 2019 \
  [paper](pubs/2019-eurosys-dslabs.pdf) &nbsp;
  [talk](https://youtu.be/zip-v2aR2WM?t=2693) &nbsp;
  [slides](pubs/2019-eurosys-dslabs-slides.pdf) &nbsp;
  [code](https://github.com/emichael/dslabs) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-2018-icfp-reincarnate-cad-decompiler .anchor}
::: {.pub-entry}
  **Functional Programming for Compiling and Decompiling Computer-aided Design** \
  [Chandrakana Nandi], [James R. Wilcox], [Pavel Panchekha], [Taylor Blau], <br class='big-only'>
  [Dan Grossman], [Zachary Tatlock] \
  International Conference on Functional Programming (ICFP) 2018 \
  [paper](pubs/2018-icfp-reincarnate-cad-decompiler.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=u3H70i4AUKs) &nbsp;
  [slides](pubs/2018-icfp-reincarnate-cad-decompiler-slides.pdf) &nbsp;
  [poster](pubs/2018-icfp-reincarnate-cad-decompiler-poster.pdf) &nbsp;
  [code](https://github.com/uwplse/szalinski) &nbsp;
  [project](http://reincarnate.uwplse.org) &nbsp;
  [I Am CSE](https://www.youtube.com/watch?v=G7v3kegE9_g) &nbsp;
  [bib](#bib-2018-icfp-reincarnate-cad-decompiler){aria-controls='bib-2018-icfp-reincarnate-cad-decompiler' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2018-icfp-reincarnate-cad-decompiler .collapse}
::: {.card .card-body .bib-card}
```

@article{2018-icfp-reincarnate-cad-decompiler,
  author    = {Chandrakana Nandi and
               James R. Wilcox and
               Pavel Panchekha and
               Taylor Blau and
               Dan Grossman and
               Zachary Tatlock},
  title     = {Functional Programming for Compiling and Decompiling Computer-aided Design},
  journal   = {Proceedings of the {ACM} on Programming Languages},
  volume    = {2},
  number    = {{ICFP}},
  pages     = {99:1--99:31},
  year      = {2018},
  url       = {https://doi.org/10.1145/3236794},
  doi       = {10.1145/3236794},
}
```
:::
:::



<!-- 2018-07 -->


::: {#pub-2018-fm-combining-fp-tools .anchor}
::: {.pub-entry}
  **Combining Tools for Optimization and Analysis of Floating-Point Computations** \
  [Heiko Becker], [Pavel Panchekha], [Eva Darulova], [Zachary Tatlock] \
  Formal Methods (FM) 2018 \
  [short paper](pubs/2018-fm-combining-fp-tools.pdf) &nbsp;
  [slides](pubs/2018-fm-combining-fp-tools-slides.pdf) &nbsp;
  [Daisy](https://github.com/malyzajko/daisy) &nbsp;
  [Herbie](http://herbie.uwplse.org/) &nbsp;
  [FPBench](http://fpbench.org/) &nbsp;
  [bib](#bib-2018-fm-combining-fp-tools){aria-controls='bib-2018-fm-combining-fp-tools' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2018-fm-combining-fp-tools .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2018-fm-combining-fp-tools,
  author    = {Heiko Becker and
               Pavel Panchekha and
               Eva Darulova and
               Zachary Tatlock},
  editor    = {Klaus Havelund and
               Jan Peleska and
               Bill Roscoe and
               Erik P. de Vink},
  title     = {Combining Tools for Optimization and Analysis of Floating-Point Computations},
  booktitle = {Formal Methods - 22nd International Symposium, {FM} 2018,
               Held as Part of the Federated Logic Conference, FloC 2018, Oxford, UK,
               July 15-17, 2018, Proceedings},
  series    = {Lecture Notes in Computer Science},
  volume    = {10951},
  pages     = {355--363},
  publisher = {Springer},
  year      = {2018},
  url       = {https://doi.org/10.1007/978-3-319-95582-7\_21},
  doi       = {10.1007/978-3-319-95582-7\_21},
}
```
:::
:::


<!-- 2018-07 -->


::: {#pub-2018-itp-binary-code-extraction .anchor}
::: {.pub-entry}
  **Software Verification with ITPs Should Use Binary Code Extraction to Reduce the TCB** \
  [Ramana Kumar], [Eric Mullen], [Zachary Tatlock], [Magnus O. Myreen] \
  Interactive Theorem Proving (ITP) 2018 \
  [short paper](pubs/2018-itp-binary-code-extraction.pdf) &nbsp;
  [slides](https://easychair.org/smart-slide/slide/pCvQ#) &nbsp;
  [CakeML](https://cakeml.org/) &nbsp;
  [Oeuf](http://oeuf.uwplse.org/) &nbsp;
  [bib](#bib-2018-itp-binary-code-extraction){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2018-itp-binary-code-extraction .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2018-itp-binary-code-extraction,
  author    = {Ramana Kumar and
               Eric Mullen and
               Zachary Tatlock and
               Magnus O. Myreen},
  editor    = {Jeremy Avigad and
               Assia Mahboubi},
  title     = {Software Verification with ITPs Should Use Binary Code Extraction
               to Reduce the {TCB} - (Short Paper)},
  booktitle = {Interactive Theorem Proving - 9th International Conference, {ITP} 2018,
               Held as Part of the Federated Logic Conference, FloC 2018,
               Oxford, UK, July 9-12, 2018, Proceedings},
  series    = {Lecture Notes in Computer Science},
  volume    = {10895},
  pages     = {362--369},
  publisher = {Springer},
  year      = {2018},
  url       = {https://doi.org/10.1007/978-3-319-94821-8\_21},
  doi       = {10.1007/978-3-319-94821-8\_21},
}
```
:::
:::


<!-- 2018-06 -->


::: {#pub-2018-pldi-vizassert-web-layout .anchor}
::: {.pub-entry}
  **Verifying that Web Pages have Accessible Layout** \
  [Pavel Panchekha], [Adam T. Geller], [Michael D. Ernst], [Zachary Tatlock], [Shoaib Kamil] \
  Programming Language Design and Implementation (PLDI) 2018 \
  [paper](pubs/2018-pldi-vizassert-web-layout.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=07efSFKC8XY) &nbsp;
  [slides](pubs/2018-pldi-vizassert-web-layout-slides.pdf) &nbsp;
  [code](https://github.com/uwplse/cassius/) &nbsp;
  [project](https://cassius.uwplse.org/) &nbsp;
  [bib](#bib-2018-pldi-vizassert-web-layout){aria-controls='bib-2018-pldi-vizassert-web-layout' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2018-pldi-vizassert-web-layout .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2018-pldi-vizassert-web-layout,
  author    = {Pavel Panchekha and
               Adam T. Geller and
               Michael D. Ernst and
               Zachary Tatlock and
               Shoaib Kamil},
  editor    = {Jeffrey S. Foster and
               Dan Grossman},
  title     = {Verifying that Web Pages have Accessible Layout},
  booktitle = {Proceedings of the 39th {ACM} {SIGPLAN} Conference on
               Programming Language Design and Implementation, {PLDI} 2018,
               Philadelphia, PA, USA,
               June 18-22, 2018},
  pages     = {1--14},
  publisher = {{ACM}},
  year      = {2018},
  url       = {https://doi.org/10.1145/3192366.3192407},
  doi       = {10.1145/3192366.3192407},
}
```
:::
:::


<!-- 2018-06 -->


::: {#pub-2018-pldi-herbgrind-fp-error .anchor}
::: {.pub-entry}
  **Finding Root Causes of Floating Point Error** \
  [Alex Sanchez-Stern], [Pavel Panchekha], [Sorin Lerner], [Zachary Tatlock] \
  Programming Language Design and Implementation (PLDI) 2018 \
  [paper](pubs/2018-pldi-herbgrind-fp-error.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=bFL6PaPrz8Y) &nbsp;
  [slides](http://herbgrind.ucsd.edu/pldi18-talk/) &nbsp;
  [code](https://github.com/uwplse/herbgrind) &nbsp;
  [project](http://herbgrind.ucsd.edu/) &nbsp;
  [bib](#bib-2018-pldi-herbgrind-fp-error){aria-controls='bib-2018-pldi-herbgrind-fp-error' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2018-pldi-herbgrind-fp-error .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2018-pldi-herbgrind-fp-error,
  author    = {Alex Sanchez{-}Stern and
               Pavel Panchekha and
               Sorin Lerner and
               Zachary Tatlock},
  editor    = {Jeffrey S. Foster and
               Dan Grossman},
  title     = {Finding root causes of floating point error},
  booktitle = {Proceedings of the 39th {ACM} {SIGPLAN} Conference on
               Programming Language Design and Implementation, {PLDI} 2018,
               Philadelphia, PA, USA,
               June 18-22, 2018},
  pages     = {256--269},
  publisher = {{ACM}},
  year      = {2018},
  url       = {https://doi.org/10.1145/3192366.3192411},
  doi       = {10.1145/3192366.3192411},
}
```
:::
:::


<!-- 2018-06 -->


::: {#pub-2018-mapl-relay-ir .anchor}
::: {.pub-entry}
  **Relay: a New IR for Machine Learning Frameworks** \
  [Jared Roesch], [Steven Lyubomirsky], [Logan Weber], [Josh Pollock], [Marisa Kirisame], <br class='big-only'>
  [Tianqi Chen], [Zachary Tatlock] \
  Machine Learning and Programming Languages (MAPL) 2018 \
  [paper](pubs/2018-mapl-relay-ir.pdf) &nbsp;
  [slides](pubs/2018-mapl-relay-ir-slides.pdf) &nbsp;
  [code](https://github.com/apache/incubator-tvm/issues/1673) &nbsp;
  [project](https://sampl.cs.washington.edu/projects/relay.html) &nbsp;
  [bib](#bib-2018-mapl-relay-ir){aria-controls='bib-2018-mapl-relay-ir' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2018-mapl-relay-ir .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2018-mapl-relay-ir,
  author    = {Jared Roesch and
               Steven Lyubomirsky and
               Logan Weber and
               Josh Pollock and
               Marisa Kirisame and
               Tianqi Chen and
               Zachary Tatlock},
  editor    = {Justin Gottschlich and
               Alvin Cheung},
  title     = {Relay: a New {IR} for Machine Learning Frameworks},
  booktitle = {Proceedings of the 2nd {ACM} {SIGPLAN} International Workshop on
               Machine Learning and Programming Languages, MAPL@PLDI 2018,
               Philadelphia, PA, USA,
               June 18-22, 2018},
  pages     = {58--68},
  publisher = {{ACM}},
  year      = {2018},
  url       = {https://doi.org/10.1145/3211346.3211348},
  doi       = {10.1145/3211346.3211348},
}
```
:::
:::


<!-- 2018-01 -->


::: {#pub-2018-popl-disel .anchor}
::: {.pub-entry}
  **Programming and Proving with Distributed Protocols** \
  [Ilya Sergey], [James R. Wilcox], [Zachary Tatlock] \
  Principles of Programming Languages (POPL) 2018 \
  [paper](pubs/2018-popl-disel.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=zuuBEXhM4tU) &nbsp;
  [slides](pubs/2018-popl-disel-slides.pdf) &nbsp;
  [code](https://github.com/DistributedComponents/disel) &nbsp;
  [project](https://distributedcomponents.net/) &nbsp;
  [bib](#bib-2018-popl-disel){aria-controls='bib-2018-popl-disel' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2018-popl-disel .collapse}
::: {.card .card-body .bib-card}
```

@article{2018-popl-disel,
  author    = {Ilya Sergey and
               James R. Wilcox and
               Zachary Tatlock},
  title     = {Programming and Proving with Distributed Protocols},
  journal   = {Proceedings of the {ACM} on Programming Languages},
  volume    = {2},
  number    = {{POPL}},
  pages     = {28:1--28:30},
  year      = {2018},
  url       = {https://doi.org/10.1145/3158116},
  doi       = {10.1145/3158116},
}
```
:::
:::


<!-- 2018-01 -->


::: {#pub-2018-cpp-oeuf-coq-compiler .anchor}
::: {.pub-entry}
  **Œuf: Minimizing the Coq Extraction TCB** \
  [Eric Mullen], [Stuart Pernsteiner], [James R. Wilcox], [Zachary Tatlock], [Dan Grossman] \
  Certified Programs and Proofs (CPP) 2018 \
  [paper](pubs/2018-cpp-oeuf-coq-compiler.pdf) &nbsp;
  [slides](pubs/2018-cpp-oeuf-coq-compiler-slides.pdf) &nbsp;
  [code](https://github.com/uwplse/oeuf) &nbsp;
  [project](http://oeuf.uwplse.org/) &nbsp;
  [bib](#bib-2018-cpp-oeuf-coq-compiler){aria-controls='bib-2018-cpp-oeuf-coq-compiler' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2018-cpp-oeuf-coq-compiler .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2018-cpp-oeuf-coq-compiler,
  author    = {Eric Mullen and
               Stuart Pernsteiner and
               James R. Wilcox and
               Zachary Tatlock and
               Dan Grossman},
  editor    = {June Andronick and
               Amy P. Felty},
  title     = {{\OE}uf: Minimizing the Coq Extraction {TCB}},
  booktitle = {Proceedings of the 7th {ACM} {SIGPLAN} International Conference on
               Certified Programs and Proofs, {CPP} 2018,
               Los Angeles, CA, USA,
               January 8-9, 2018},
  pages     = {172--185},
  publisher = {{ACM}},
  year      = {2018},
  url       = {https://doi.org/10.1145/3167089},
  doi       = {10.1145/3167089},
}
```
:::
:::


<!-- 2017-10 -->


::: {#pub-2017-icalepcs-epics-verification .anchor}
::: {.pub-entry}
  **Automatic Formal Verification for EPICS** \
  [Jonathan Jacky], [Stefani Banerian], [Michael D. Ernst], [Calvin Loncaric], <br class='big-only'>
  [Stuart Pernsteiner], [Zachary Tatlock], [Emina Torlak] \
  International Conference on Accelerator and Large Experimental Control Systems (ICALEPCS) 2017 \
  [abstract](#abs-2017-icalepcs-epics-verification){aria-controls='abs-2017-icalepcs-epics-verification' data-toggle='collapse' role='button' aria-expanded='false'} &nbsp;
  [paper](pubs/2017-icalepcs-epics-verification.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=CFSnkB5z0GA) &nbsp;
  [slides](pubs/2017-icalepcs-epics-verification-slides.pdf) &nbsp;
  [code](https://github.com/uwplse/neutrons) &nbsp;
  [project](http://neutrons.uwplse.org) &nbsp;
  [publisher](http://accelconf.web.cern.ch/icalepcs2017/doi/JACoW-ICALEPCS2017-TUDPL02.html) &nbsp;
  [bib](#bib-2017-icalepcs-epics-verification){aria-controls='bib-2017-icalepcs-epics-verification' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#abs-2017-icalepcs-epics-verification .collapse}
::: {.card .card-body .abs-card}

We built an EPICS-based radiation therapy machine control system,
  and are using it to treat patients at our hospital.
To help ensure safety,
  we use a restricted subset of EPICS constructs and programming techniques,
  and developed several new automated formal verification tools for them.
The Symbolic Evaluator checks properties of
  EPICS database programs (applications),
  using symbolic evaluation and satisfiability checking.
It found serious errors in our control program
  that were missed by reviews and testing.
Other tools are based on a formal semantics for database records,
  derived from EPICS documentation and expressed
  in the specification language of an automated theorem prover.
The Verified Interpreter is a re-implementation of
  the parts of the database engine we use,
  which is proved correct against the formal semantics.
We used it to check those parts of EPICS core by differential testing.
It found no significant errors
  (differences between EPICS behavior and the formal semantics).
A Verified Compiler is in development.
It will compile a database to a standalone program
  that does not use EPICS core,
  where the machine code is verified to conform to the formal semantics.

<!--

TODO

See also:

-

Press:

-

-->

:::
:::
::: {#bib-2017-icalepcs-epics-verification .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2017-icalepcs-epics-verification,
  author       = {Jonathan Jacky and
                  Stefani Banerian and
                  Michael D. Ernst and
                  Calvin Loncaric and
                  Stuart Pernsteiner and
                  Zachary Tatlock and
                  Emina Torlak},
  title        = {{A}utomatic {F}ormal {V}erification for {EPICS}},
  booktitle    = {Proc. of International Conference on Accelerator and Large Experimental Control Systems (ICALEPCS'17),
                  Barcelona, Spain, 8-13 October 2017},
  pages        = {285--291},
  paper        = {TUDPL02},
  language     = {english},
  keywords     = {ion, EPICS, controls, database, operation},
  venue        = {Barcelona, Spain},
  series       = {International Conference on Accelerator and Large Experimental Control Systems},
  number       = {16},
  publisher    = {JACoW},
  address      = {Geneva, Switzerland},
  month        = {January},
  year         = {2018},
  isbn         = {978-3-95450-193-9},
  doi          = {https://doi.org/10.18429/JACoW-ICALEPCS2017-TUDPL02},
  url          = {http://jacow.org/icalepcs2017/papers/tudpl02.pdf},
  note         = {https://doi.org/10.18429/JACoW-ICALEPCS2017-TUDPL02},
}
```
:::
:::


<!-- 2017-08 -->


::: {#pub-2017-icfp-spacesearch-verifying-solver-aided-tools .anchor}
::: {.pub-entry}
  **SpaceSearch: A Library for Building and Verifying Solver-aided Tools** \
  [Konstantin Weitz], [Steven Lyubomirsky], [Stefan Heule], <br class='big-only'>
  [Emina Torlak], [Michael D. Ernst], [Zachary Tatlock] \
  International Conference on Functional Programming (ICFP) 2017 \
  [paper](pubs/2017-icfp-spacesearch-verifying-solver-aided-tools.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=dCx_E2SqcWE) &nbsp;
  [slides](pubs/2017-icfp-spacesearch-verifying-solver-aided-tools-slides.pdf) &nbsp;
  [code](https://github.com/konne88/SpaceSearch) &nbsp;
  [project](TODO) &nbsp;
  [bib](#bib-2017-icfp-spacesearch-verifying-solver-aided-tools){aria-controls='bib-2017-icfp-spacesearch-verifying-solver-aided-tools' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2017-icfp-spacesearch-verifying-solver-aided-tools .collapse}
::: {.card .card-body .bib-card}
```

@article{2017-icfp-spacesearch-verifying-solver-aided-tools,
  author    = {Konstantin Weitz and
               Steven Lyubomirsky and
               Stefan Heule and
               Emina Torlak and
               Michael D. Ernst and
               Zachary Tatlock},
  title     = {SpaceSearch: A Library for Building and Verifying Solver-aided Tools},
  journal   = {Proceedings of the {ACM} on Programming Languages},
  volume    = {1},
  number    = {{ICFP}},
  pages     = {25:1--25:28},
  year      = {2017},
  url       = {https://doi.org/10.1145/3110269},
  doi       = {10.1145/3110269},
}
```
:::
:::


<!-- 2017-05 -->


::: {#pub-2017-snapl-incarnate-pl-for-3d-printing .anchor}
::: {.pub-entry}
  **Programming Language Tools and Techniques for 3D Printing** \
  [Chandrakana Nandi], [Anat Caspi], [Dan Grossman], [Zachary Tatlock] \
  Summit oN Advances in Programming Languages (SNAPL) 2017 \
  [paper](pubs/2017-snapl-incarnate-pl-for-3d-printing.pdf) &nbsp;
  [slides](pubs/2017-snapl-incarnate-pl-for-3d-printing-slides.pdf) &nbsp;
  [project](http://incarnate.uwplse.org/) &nbsp;
  [bib](#bib-2017-snapl-incarnate-pl-for-3d-printing){aria-controls='bib-2017-snapl-incarnate-pl-for-3d-printing' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2017-snapl-incarnate-pl-for-3d-printing .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2017-snapl-incarnate-pl-for-3d-printing,
  author    = {Chandrakana Nandi and
               Anat Caspi and
               Dan Grossman and
               Zachary Tatlock},
  editor    = {Benjamin S. Lerner and
               Rastislav Bod{\'{\i}}k and
               Shriram Krishnamurthi},
  title     = {Programming Language Tools and Techniques for 3D Printing},
  booktitle = {2nd Summit on Advances in Programming Languages, {SNAPL} 2017,
               May 7-10, 2017, Asilomar, CA, {USA}},
  series    = {LIPIcs},
  volume    = {71},
  pages     = {10:1--10:12},
  publisher = {Schloss Dagstuhl - Leibniz-Zentrum f{\"{u}}r Informatik},
  year      = {2017},
  url       = {https://doi.org/10.4230/LIPIcs.SNAPL.2017.10},
  doi       = {10.4230/LIPIcs.SNAPL.2017.10},
}
```
:::
:::


<!-- 2017-05 -->


::: {#pub-2017-snapl-disel-pl-for-distributed-systems .anchor}
::: {.pub-entry}
  **Programming Language Abstractions for Modularly Verified Distributed Systems** \
  [James R. Wilcox], [Ilya Sergey], [Zachary Tatlock] \
  Summit oN Advances in Programming Languages (SNAPL) 2017 \
  [paper](pubs/2017-snapl-disel-pl-for-distributed-systems.pdf) &nbsp;
  [slides](pubs/2017-snapl-disel-pl-for-distributed-systems-slides.pdf) &nbsp;
  [project](https://distributedcomponents.net) &nbsp;
  [bib](#bib-2017-snapl-disel-pl-for-distributed-systems){aria-controls='bib-2017-snapl-disel-pl-for-distributed-systems' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2017-snapl-disel-pl-for-distributed-systems .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2017-snapl-disel-pl-for-distributed-systems,
  author    = {James R. Wilcox and
               Ilya Sergey and
               Zachary Tatlock},
  editor    = {Benjamin S. Lerner and
               Rastislav Bod{\'{\i}}k and
               Shriram Krishnamurthi},
  title     = {Programming Language Abstractions for
               Modularly Verified Distributed Systems},
  booktitle = {2nd Summit on Advances in Programming Languages, {SNAPL} 2017,
               May 7-10, 2017, Asilomar, CA, {USA}},
  series    = {LIPIcs},
  volume    = {71},
  pages     = {19:1--19:12},
  publisher = {Schloss Dagstuhl - Leibniz-Zentrum f{\"{u}}r Informatik},
  year      = {2017},
  url       = {https://doi.org/10.4230/LIPIcs.SNAPL.2017.19},
  doi       = {10.4230/LIPIcs.SNAPL.2017.19},
}
```
:::
:::


<!-- 2016-07 -->


::: {#pub-2016-cav-neutrons-radiotherapy-safety .anchor}
::: {.pub-entry}
  **Investigating Safety of a Radiotherapy Machine Using System Models with Pluggable Checkers** \
  [Stuart Pernsteiner], [Calvin Loncaric], [Emina Torlak], [Zachary Tatlock], <br class='big-only'>
  [Xi Wang], [Michael D. Ernst], [Jonathan Jacky] \
  Computer-Aided Verification (CAV) 2016 \
  [paper](pubs/2016-cav-neutrons-radiotherapy-safety.pdf) &nbsp;
  [slides](pubs/2016-cav-neutrons-radiotherapy-safety-slides.pdf) &nbsp;
  [code](https://github.com/uwplse/neutrons) &nbsp;
  [project](http://neutrons.uwplse.org) &nbsp;
  [I Am CSE](https://www.youtube.com/watch?v=QdR9_TJ1br8) &nbsp;
  [bib](#bib-2016-cav-neutrons-radiotherapy-safety){aria-controls='bib-2016-cav-neutrons-radiotherapy-safety' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib-2016-cav-neutrons-radiotherapy-safety .collapse}
::: {.card .card-body .bib-card}
```

@inproceedings{2016-cav-neutrons-radiotherapy-safety,
  author    = {Stuart Pernsteiner and
               Calvin Loncaric and
               Emina Torlak and
               Zachary Tatlock and
               Xi Wang and
               Michael D. Ernst and
               Jonathan Jacky},
  editor    = {Swarat Chaudhuri and
               Azadeh Farzan},
  title     = {Investigating Safety of a Radiotherapy Machine Using System Models
               with Pluggable Checkers},
  booktitle = {Computer Aided Verification - 28th International Conference,
               {CAV} 2016, Toronto, ON, Canada, July 17-23, 2016, Proceedings, Part {II}},
  series    = {Lecture Notes in Computer Science},
  volume    = {9780},
  pages     = {23--41},
  publisher = {Springer},
  year      = {2016},
  url       = {https://doi.org/10.1007/978-3-319-41540-6\_2},
  doi       = {10.1007/978-3-319-41540-6\_2},
}
```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Toward a Standard Benchmark Format and Suite for Floating-Point Analysis** \
  [Nasrine Damouche], [Matthieu Martel], [Pavel Panchekha], <br class='big-only'>
  [Chen Qiu], [Alex Sanchez-Stern], [Zachary Tatlock] \
  Numerical Software Verification (NSV) 2016 \
  [paper](pubs/2016-nsv-fpbench.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=SRE2Gky381M) &nbsp;
  [slides](pubs/2016-nsv-fpbench-slides.pdf) &nbsp;
  [code](https://github.com/FPBench/FPBench) &nbsp;
  [project](http://fpbench.org/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Planning for Change in a Formal Verification of the Raft Consensus Protocol** \
  [Doug Woos], [James R. Wilcox], [Steve Anton], [Zachary Tatlock], [Michael D. Ernst], [Thomas E. Anderson] \
  Certified Programs and Proofs (CPP) 2016 \
  [paper](pubs/2016-cpp-verdi-raft-proof-engineering.pdf) &nbsp;
  [slides](pubs/2016-cpp-verdi-raft-proof-engineering-slides.pdf) &nbsp;
  [code](https://github.com/uwplse/verdi-raft) &nbsp;
  [Verdi](http://verdi.uwplse.org) &nbsp;
  [Proof Engineering](https://proofengineering.org) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Scalable Verification of Border Gateway Protocol Configurations with an SMT Solver** \
  [Konstantin Weitz], [Doug Woos], [Emina Torlak], [Michael D. Ernst], [Arvind Krishnamurthy], [Zachary Tatlock] \
  Object-Oriented Programming, Systems, Languages & Applications (OOPSLA) 2016 \
  [paper](pubs/2016-oopsla-bagpipe-scalable-bgp-verification-smt.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=ErvRZVNI3rc) &nbsp;
  [slides](pubs/2016-oopsla-bagpipe-scalable-bgp-verification-smt-slides.pdf) &nbsp;
  [code](https://github.com/uwplse/bagpipe) &nbsp;
  [project](http://bagpipe.uwplse.org/bagpipe/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Verified Peephole Optimizations for CompCert** \
  [Eric Mullen], [Daryl Zuniga], [Zachary Tatlock], [Dan Grossman] \
  Programming Language Design and Implementation (PLDI) 2016 \
  [paper](pubs/2016-pldi-peek-verified-peepholes-compcert.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=h4KoLyTh0zY) &nbsp;
  [code](https://github.com/uwplse/peek) &nbsp;
  [project](http://peek.uwplse.org/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Visual Robot Programming for Generalizable Mobile Manipulation Tasks (Extended Abstract)** \
  [Sonya Alexandrova], [Zachary Tatlock], [Maya Cakmak] \
  Human Robot Interaction (HRI) 2015 \
  [paper](pubs/2015-hri-roboflow-visual-robot-programming-language.pdf) &nbsp;
  [teaser](https://www.youtube.com/watch?v=CEKFUMBNEmU) &nbsp;
  [web GUI](http://cse512-15s.github.io/fp-fiannaca-sonyaa/roboflow.html) &nbsp;
  [code](https://github.com/sonyaa/roboflow) &nbsp;
  [project](https://homes.cs.washington.edu/~ztatlock/roboflow/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **RoboFlow: A Flow-based Visual Programming Language for Mobile Manipulation Tasks** \
  [Sonya Alexandrova], [Zachary Tatlock], [Maya Cakmak] \
  International Conference on Robotics and Automation (ICRA) 2015 \
  [paper](pubs/2015-icra-roboflow-visual-robot-programming-language.pdf) &nbsp;
  [teaser](https://www.youtube.com/watch?v=CEKFUMBNEmU) &nbsp;
  [web GUI](http://cse512-15s.github.io/fp-fiannaca-sonyaa/roboflow.html) &nbsp;
  [code](https://github.com/sonyaa/roboflow) &nbsp;
  [project](https://homes.cs.washington.edu/~ztatlock/roboflow/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Automatically Improving Accuracy for Floating Point Expressions** \
  [Pavel Panchekha], [Alex Sanchez-Stern], [James R. Wilcox], [Zachary Tatlock] \
  Programming Language Design and Implementation (PLDI) 2015 \
  [paper](pubs/2015-pldi-herbie-floating-point-accuracy.pdf) &nbsp;
  [teaser](https://www.youtube.com/watch?v=qnkElmpTtBw) &nbsp;
  [talk](https://www.youtube.com/watch?v=RNzsvp6NLOY) &nbsp;
  [slides](pubs/2015-pldi-herbie-floating-point-accuracy-slides.pdf) &nbsp;
  [code](https://github.com/uwplse/herbie) &nbsp;
  [project](http://herbie.uwplse.org/) &nbsp;
  <br> *Distinguished Paper Award*
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Verdi: A Framework for Implementing and Formally Verifying Distributed Systems** \
  [James R. Wilcox], [Doug Woos], [Pavel Panchekha], [Zachary Tatlock], <br class='big-only'>
  [Xi Wang], [Michael D. Ernst], [Thomas E. Anderson] \
  Programming Language Design and Implementation (PLDI) 2015 \
  [paper](pubs/2015-pldi-verdi-verifying-distributed-systems.pdf) &nbsp;
  [teaser](https://www.youtube.com/watch?v=r068lSNqQC4) &nbsp;
  [slides](pubs/2015-pldi-verdi-verifying-distributed-systems-slides.pdf) &nbsp;
  [poster](pubs/2015-pldi-verdi-verifying-distributed-systems-poster.pdf) &nbsp;
  [code](https://github.com/uwplse/verdi) &nbsp;
  [project](http://verdi.uwplse.org/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Toward a Dependability Case Language and Workflow for a Radiation Therapy System** \
  [Michael D. Ernst], [Dan Grossman], [Jonathan Jacky], [Calvin Loncaric], <br class='big-only'>
  [Stuart Pernsteiner], [Zachary Tatlock], [Emina Torlak], [Xi Wang] \
  Summit oN Advances in Programming Languages (SNAPL) 2015 \
  [paper](pubs/2015-snapl-neutrons-radiotherapy-safety.pdf) &nbsp;
  [slides](pubs/2015-snapl-neutrons-radiotherapy-safety-slides.pdf) &nbsp;
  [project](http://neutrons.uwplse.org/) &nbsp;
  [I Am CSE](https://www.youtube.com/watch?v=QdR9_TJ1br8) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **SafeDispatch: Securing C++ Virtual Calls from Memory Corruption Attacks** \
  [Dongseok Jang], [Zachary Tatlock], [Sorin Lerner] \
  Network and Distributed System Security (NDSS) 2014 \
  [paper](pubs/2014-ndss-safe-dispatch-vtable-hijacking-defense.pdf) &nbsp;
  [slides](pubs/2014-ndss-safe-dispatch-vtable-hijacking-defense-slides.pdf) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Jitk: A Trustworthy In-Kernel Interpreter Infrastructure** \
  [Xi Wang], [David Lazar], [Nickolai Zeldovich], [Adam Chlipala], [Zachary Tatlock] \
  Operating Systems Design and Implementation (OSDI) 2014 \
  [paper](pubs/2014-osdi-jitk-verified-bpf.pdf) &nbsp;
  [talk](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/wang_xi) &nbsp;
  [slides](pubs/2014-osdi-jitk-verified-bpf-slides.pdf) &nbsp;
  [code](https://css.csail.mit.edu/jitk/) &nbsp;
  [project](https://css.csail.mit.edu/jitk/) &nbsp;
  [bib](pubs/2014-osdi-jitk-verified-bpf.bib) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Automating Formal Proofs for Reactive Systems** \
  [Daniel Ricketts], [Valentin Robert], [Dongseok Jang], [Zachary Tatlock], [Sorin Lerner] \
  Programming Language Design and Implementation (PLDI) 2014 \
  [paper](pubs/2014-pldi-reflex-reactive-systems-coq.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=phwVo66aChc) &nbsp;
  [slides](pubs/2014-pldi-reflex-reactive-systems-coq-slides.pdf) &nbsp;
  [code](https://github.com/UCSD-PL/kraken) &nbsp;
  [project](http://goto.ucsd.edu/reflex/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Establishing Browser Security Guarantees through Formal Shim Verification** \
  [Dongseok Jang], [Zachary Tatlock], [Sorin Lerner] \
  USENIX Security Symposium 2012 \
  [paper](pubs/2012-usenix-security-quark-formal-shim-verifiction-web-browser.pdf) &nbsp;
  [extended](pubs/2012-usenix-security-quark-formal-shim-verifiction-web-browser-extended.pdf) &nbsp;
  [talk](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/jang) &nbsp;
  [slides](pubs/2012-usenix-security-quark-formal-shim-verifiction-web-browser-slides.pdf) &nbsp;
  [poster](pubs/2012-usenix-security-quark-formal-shim-verifiction-web-browser-poster.pdf) &nbsp;
  [code](http://goto.ucsd.edu/quark/quark-0807.tar.gz) &nbsp;
  [project](http://goto.ucsd.edu/quark/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Equality Saturation: A New Approach to Optimization** \
  [Ross Tate], [Michael Stepp], [Zachary Tatlock], [Sorin Lerner] \
  Logical Methods in Computer Science (LMCS) 2011 \
  [paper](pubs/2011-lmcs-equality-saturation-optimizations-egraphs.pdf) &nbsp;
  [project](https://www.cs.cornell.edu/~ross/publications/eqsat/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Bringing Extensibility to Verified Compilers** \
  [Zachary Tatlock], [Sorin Lerner] \
  Programming Language Design and Implementation (PLDI) 2010 \
  [paper](pubs/2010-pldi-xcert-extensible-verified-compilers.pdf) &nbsp;
  [slides](pubs/2010-pldi-xcert-extensible-verified-compilers-slides.pdf) &nbsp;
  [project](http://cseweb.ucsd.edu/~lerner/collider.html) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Equality Saturation: A New Approach to Optimization** \
  [Ross Tate], [Michael Stepp], [Zachary Tatlock], [Sorin Lerner] \
  Principles of Programming Languages (POPL) 2009 \
  [paper](pubs/2009-popl-equality-saturation-optimizations-egraphs.pdf) &nbsp;
  [talk](https://www.cs.cornell.edu/~ross/publications/eqsat/) &nbsp;
  [slides](pubs/2009-popl-equality-saturation-optimizations-egraphs-slides.pdf) &nbsp;
  [code](http://goto.ucsd.edu/~mstepp/peggy/) &nbsp;
  [project](https://www.cs.cornell.edu/~ross/publications/eqsat/) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Proving Optimizations Correct using Parameterized Program Equivalence** \
  [Sudipta Kundu], [Zachary Tatlock], [Sorin Lerner] \
  Programming Language Design and Implementation (PLDI) 2009 \
  [paper](pubs/2009-pldi-pec-compiler-optimization-verification.pdf) &nbsp;
  [talk](https://www.youtube.com/watch?v=H2H3tAv695A) &nbsp;
  [slides](pubs/2009-pldi-pec-compiler-optimization-verification-slides.pdf) &nbsp;
  [code](https://github.com/ztatlock/pec) &nbsp;
  [project](http://cseweb.ucsd.edu/~lerner/collider.html) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::


<!-- -->


::: {#pub-TODO .anchor}
::: {.pub-entry}
  **Deep Typechecking and Refactoring** \
  [Zachary Tatlock], [Chris Tucker], [David Shuffelton], [Ranjit Jhala], [Sorin Lerner] \
  Object-Oriented Programming, Systems, Languages & Applications (OOPSLA) 2008 \
  [paper](pubs/2008-oopsla-quail-deep-typechecking-and-refactoring.pdf) &nbsp;
  [slides](pubs/2008-oopsla-quail-deep-typechecking-and-refactoring-slides.pptx) &nbsp;
  [poster](pubs/2008-oopsla-quail-deep-typechecking-and-refactoring-poster.pdf) &nbsp;
  [project](http://cseweb.ucsd.edu/~lerner/quail.html) &nbsp;
  [bib](#bib-){aria-controls='bib-' data-toggle='collapse' role='button' aria-expanded='false'}
:::
:::
::: {#bib- .collapse}
::: {.card .card-body .bib-card}
```

```
:::
:::

&nbsp;

# Aggregators

- [DBLP](https://dblp.org/pers/t/Tatlock:Zachary.html)
- [Google Scholar](https://scholar.google.com/citations?user=jz2Tvk4AAAAJ&hl=en)
- [Semantic Scholar](https://www.semanticscholar.org/author/Zachary-Tatlock/2272813)
- [ResearchGate](https://www.researchgate.net/profile/Zachary_Tatlock)
- [ACM Digital Library](https://dl.acm.org/profile/81392605383)
- [Publications BibTeX](ztatlock-bib.html)

<!-- TODO ORCID -->
