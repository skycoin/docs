---
title: "Coin Hours"
isdate: false
weight: 6
filename: "/content/devdocs/guides/encoder.md"
---
{{% comment %}}
This file is licensed under the MIT License (MIT) available on
http://opensource.org/licenses/MIT.
{{% /comment %}}

Package encoder binary implements translation between numbers and byte sequences and encoding and decoding of varints.

Numbers are translated by reading and writing fixed-size values.

A fixed-size value is either a fixed-size arithmetic type (int8, uint8, int16, float32, complex64, ...) or an array or struct containing only fixed-size values.

{{% subhead %}}
