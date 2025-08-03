# Class Group Arithmetic Design
## Overview
Describes the class group arithmetic module for ZK-BLEND, using ideal class groups of quadratic fields (\(\mathbb{Q}(\sqrt{-p})\)) for transparent polynomial commitments.

## Ideal Representation
- Ideals as \((a, b)\) pairs for \(a\mathbb{Z} + (b + \sqrt{-p})\mathbb{Z}\).
- Constraints: \(a\) divides \(b^2 + p\).
- Prime \(p\): 1000-bit, \(p \equiv 3 \pmod{4}\).

## Operations
- **Multiplication**: Algorithm for multiplying ideals, based on Cohen’s number theory.
- **Reduction**: Algorithm to reduce ideals to canonical form.
- **Prime Selection**: Criteria for choosing secure primes.

## Dependencies
- `num-bigint`: Large integer operations.
- `rug`: High-precision arithmetic (via `libgmp-dev`).
- `pari-sys`: Advanced number theory (via `libpari-dev`).

## Testing
- **Unit Tests**: Associativity, commutativity, identity, reduction correctness.
- **Property-Based Tests**: Random ideal testing with `proptest`.
- **Benchmarks**: Performance of multiplication and reduction with `criterion`.

## Implementation Notes
- Use Docker for builds: `docker run -it -v C:\Developments\Solutions\ZK-BLEND\zk-blend:/usr/src/zk-blend zk-blend cargo build`.
- Ensure 1000-bit primes for cryptographic security.