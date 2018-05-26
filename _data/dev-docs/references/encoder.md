---
title: "Encoder"
isdate: false
weight: 5
filename: "/_data/dev-docs/references/encoder.md"
---
{{% comment %}}
This file is licensed under the MIT License (MIT) available on
<http://opensource.org/licenses/MIT.>
{{% /comment %}}

# Encoder

Package encoder binary implements translation between numbers and byte sequences and encoding and decoding of [varints][/en/glossary/varint]{:#term-varint}{:.term}.

Numbers are translated by reading and writing fixed-size values.

A fixed-size value is either a fixed-size arithmetic type (int8, uint8, int16, float32, complex64, ...) or an array or struct containing only fixed-size values.

## Numeric types

Integers, both `Int` types (`Int8`,`Int16`,`Int32`,`Int64`) and `Uint` types (`Uint8`,`Uint16`,`Uint32`,`Uint64`) are encoded in big-endian format.

Floats, both `Float32` and `Float64`, are encoded in IEEE 754 binary representation.

## Strings

For a string with `n` characters:

Bytes `0` - `3`: Integer `n` encoded in `Uint32` format.
Bytes `3` - `3+n`: Characters encoded in `Uint8` format.

## Booleans

Booleans are encoded as a byte, with `1` for `true` and `0` for `false`.

## Arrays

For an array of size `n`:

Bytes `0` - `n-1`: Encoded fixed-size elements.

## Slices

For a slice with `n` elements of size `s`:

Bytes `0` - `3`: Integer `n` encoded in `Uint32` format.
Bytes `3` - `3(s*n)`: Encoded fixed-size elements.

## Maps

For a map with `n` key-value pairs, with values of size `s`:

Bytes `0` - `3`: Integer `n` encoded in `Uint32` format.
Bytes `3` - `3(s*n)`: Encoded fixed-size values.

## Struct

Each field that can be setted, is not named `"_"`, and whose `"enc"` tag is not set as `"-"`, is encoded in order.

{{% subhead %}}
