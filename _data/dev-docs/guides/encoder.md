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

Function `EncodeInt(b []byte, data interface{})` encodes an Integer type contained in `data` into buffer `b`. If `data` is not an Integer type, error message `log.Panic("PushAtomic, case not handled")` is logged.

### DecodeInt

Function `DecodeInt(in []byte, data interface{})` decodes `in` buffer into `data` parameter. If `data` is not an Integer type, error message `log.Panic("PushAtomic, case not handled")` is logged.
<!--This function doesn't check whether `in` param is a valid integer. Must be fixed and updated accordingly. -->

### DeserializeAtomic

Function `DeserializeAtomic(in []byte, data interface{})` deserializes `in` buffer into `data` parameter. If `data` is not an atomic type (i.e., Integer type or Boolean type), error message `log.Panic("type not atomic")` is logged.
<!--This function doesn't check whether `in` param is a valid atomic type. Must be fixed and updated accordingly. -->

### DeserializeRaw

Function `DeserializeRaw(in []byte, data interface{}) error` deserializes `in` buffer into return parameter. If `data` is not either a Pointer type, a Slice type or a Struct type, error message `fmt.Errorf("Invalid type %s", reflect.TypeOf(v).String())` is returned. If `in` buffer can't be deserialized, error `errors.New("Deserialization failed")` is returned.

### Deserialize

Function `Deserialize((r io.Reader, dsize int, data interface{}) error` reads `dsize` bytes from `r` and deserializes the resulting buffer into return parameter. If `data` is not either a Pointer type, a Slice type or a Struct type, error `errors.New("binary.Read: invalid type " + reflect.TypeOf(d).String())` is returned. If `in` buffer can't be deserialized, error `errors.New("Deserialization failed")` is returned.

### CanDeserialize

Function `CanDeserialize(in []byte, dst reflect.Value) bool` returns true if `in` buffer can be deserialized into `dst`'s type. Returns false in any other case.

### DeserializeRawToValue

Function `DeserializeRawToValue(in []byte, dst reflect.Value) (int, error)` deserializes `in` buffer into `dst`'s type and returns the number of bytes used and the value of the buffer. If `data` is not either a Pointer type, a Slice type or a Struct type, 0 and error `errors.New("binary.Read: invalid type " + reflect.TypeOf(dst).String())` are returned. If `in` buffer can't be deserialized, 0 and error `errors.New("Deserialization failed")` are returned.

### DeserializeToValue

Function `(r io.Reader, dsize int, dst reflect.Value) error` reads `dsize` bytes from `r`, deserializes the resulting buffer into `dst`'s type and returns the value of the buffer. If `data` is not either a Pointer type, a Slice type or a Struct type, error `errors.New("binary.Read: invalid type " + reflect.TypeOf(dst).String())` is returned. If `in` buffer can't be deserialized, an error is returned.

### SerializeAtomic

Function `SerializeAtomic(data interface{}) []byte` returns serialization of `data` parameter. If `data` is not an atomic type, error message `log.Panic("type not atomic")` is logged.

### Serialize

Function `Serialize(data interface{}) []byte` returns serialized basic type-based `data` parameter. Encoding is reflect-based.

### Size

Function `Size(v interface{}) int` returns how many bytes would it take to encode the value v, which must be a fixed-size value (struct) or a slice of fixed-size values, or a pointer to such data. Reflect-based encoding is used.

{{% subhead %}}
