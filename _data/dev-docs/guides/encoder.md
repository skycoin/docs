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

Package encoder binary implements translation between numbers and byte sequences and encoding and decoding of [varints][/en/glossary/varint]{:#term-varint}{:.term}.

Numbers are translated by reading and writing fixed-size values.

A fixed-size value is either a fixed-size arithmetic type (int8, uint8, int16, float32, complex64, ...) or an array or struct containing only fixed-size values.

### EncodeInt

The function `EncodeInt(b []byte, data interface{})` encodes an Integer type contained in `data` into buffer `b`. If `data` is not an Integer type, error message `log.Panic("PushAtomic, case not handled")` is logged.

### DecodeInt

The function `DecodeInt(in []byte, data interface{})` decodes `in` buffer into `data` parameter. If `data` is not an Integer type, error message `log.Panic("PushAtomic, case not handled")` is logged.
<!--This function doesn't check whether `in` param is a valid in. Must be fixed and updated accordingly. -->

### DeserializeAtomic

### DeserializeRaw

### Deserialize

### CanDeserialize

### DeserializeRawToValue

### DeserializeToValue

### SerializeAtomic

### Serialize

### Size


{{% subhead %}}
