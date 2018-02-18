---
title: "Introduction"
isdate: false
weight: 5
---


The Developer Reference aims to provide technical details and API information
to help you start building Skycoin-based applications, but it is [not a specification][]. To make the best use of
this documentation, you may want to install the current version of Skycoin core,
either from ```core git``` or from a <code>core executable</code>.

Questions about Skycoin development are best asked in one of the
[Skycoin community channels][dev communities].
Errors or suggestions related to
documentation on Skycoin.net can be [submitted as an issue][docs issue]
or posted to the [skycoin-docs mailing list][].

In the following documentation, some strings have been shortened or wrapped: "[...]"
indicates extra data was removed, and lines ending in a single backslash "\\"
are continued below. If you hover your mouse over a paragraph, cross-reference
links will be shown in blue.  If you hover over a cross-reference link, a brief
definition of the term will be displayed in a tooltip.


#### Not A Specification

The Skycoin.net Developer Documentation describes how Skycoin works to
help educate new Skycoin developers, but it is not a specification---and
it never will be.

Skycoin security depends on consensus. Should your program diverge from
consensus, its security is weakened or destroyed. The cause of the
divergence doesn't matter: it could be a bug in your program, it could
be an [error in this documentation][errors in docs] which you
implemented as described, or it could be you do everything right but
other software on the network behaves unexpectedly. The specific cause will not matter to the users of your software
whose wealth is lost.

The only correct specification of consensus behavior is the actual
behavior of programs on the network which maintain consensus. As that
behavior is subject to arbitrary inputs<!--noref--> in a large variety
of unique environments, it cannot ever be fully documented here or
anywhere else.

In addition, we also warn you that this documentation has not been
extensively reviewed by Skycoin experts and so likely contains numerous
errors. At the bottom of the menu on the left, you will find links that
allow you to report an issue or to edit the documentation on GitHub.
Please use those links if you find any errors or important missing
information.
