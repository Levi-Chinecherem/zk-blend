# ZK-BLEND
A zero-knowledge proof system using class groups of unknown order.

## Setup (Windows)
- Install Rust 1.88.0, Docker Desktop 28.0.1, Git 2.49.0, Visual Studio Build Tools, and vcpkg.
- Clone: `git clone https://github.com/<your-username>/zk-blend.git`
- Install GMP (optional for native build): `cd C:\vcpkg && .\vcpkg install gmp:x64-windows && .\vcpkg integrate install`
- Set environment (optional): `$env:LIB = "C:\vcpkg\installed\x64-windows\lib"; $env:INCLUDE = "C:\vcpkg\installed\x64-windows\include"; $env:VCPKG_ROOT = "C:\vcpkg"`
- Build (Docker recommended): `cd C:\Developments\Solutions\ZK-BLEND\zk-blend && docker build -t zk-blend . && docker run -it -v C:\Developments\Solutions\ZK-BLEND\zk-blend:/usr/src/zk-blend zk-blend cargo build`
- Run tests: `docker run -it -v C:\Developments\Solutions\ZK-BLEND\zk-blend:/usr/src/zk-blend zk-blend cargo test`

## Development
Follow the development plan in `docs/development_plan.md`.