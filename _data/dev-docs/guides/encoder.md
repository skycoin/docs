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
<!--This function doesn't check whether `in` param is a valid integer. Must be fixed and updated accordingly. -->

### DeserializeAtomic

The function `DeserializeAtomic(in []byte, data interface{})` deserializes `in` buffer into `data` parameter. If `data` is not an atomic type (i.e., Integer type or Boolean type), error message `log.Panic("type not atomic")` is logged.
<!--This function doesn't check whether `in` param is a valid atomic type. Must be fixed and updated accordingly. -->

### DeserializeRaw

The function `DeserializeRaw(in []byte, data interface{}) error` deserializes `in` buffer into return parameter. If `data` is not either a Pointer type, a Slice type or a Struct type, error message `fmt.Errorf("Invalid type %s", reflect.TypeOf(v).String())` is returned. If `in` buffer can't be deserialized, error `errors.New("Deserialization failed")` is returned.

### Deserialize

The function `Deserialize((r io.Reader, dsize int, data interface{}) error` reads `dsize` bytes from `r` and deserializes the resulting buffer buffer into return parameter. If `data` is not either a Pointer type, a Slice type or a Struct type, error `errors.New("binary.Read: invalid type " + reflect.TypeOf(d).String())` is returned. If `in` buffer can't be deserialized, error `errors.New("Deserialization failed")` is returned.

### CanDeserialize

The function `CanDeserialize(in []byte, dst reflect.Value) bool` returns true if `in` buffer can be deserialized into `dst`'s type. Returns false in any other case.

### DeserializeRawToValue

The function `DeserializeRawToValue(in []byte, dst reflect.Value) (int, error)` deserializes `in` buffer into `dst`'s type and returns the number of bytes used and the value of the buffer. If `data` is not either a Pointer type, a Slice type or a Struct type, 0 and error `errors.New("binary.Read: invalid type " + reflect.TypeOf(dst).String())` are returned. If `in` buffer can't be deserialized, 0 and error `errors.New("Deserialization failed")` are returned.

### DeserializeToValue

### SerializeAtomic

### Serialize

### Size


{{% subhead %}}
