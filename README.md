# alacritty_rpm
Custom RPM Generator for the Alacritty Terminal Client.


Do *NOT* use this if you are on a distro (fedora) that natively distributes Alacritty as an RPM package.
This repository is for my own personal repackaging to remove dependencies not present in RHEL 10.


## Current Deps
```sh
 ldd $(which alacritty)
        linux-vdso.so.1 (0x00007f63e6b88000)
        libfreetype.so.6 => /lib64/libfreetype.so.6 (0x00007f63e6a8a000)
        libfontconfig.so.1 => /lib64/libfontconfig.so.1 (0x00007f63e6a3a000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f63e6a0c000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f63e611c000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f63e5f2a000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f63e6b8a000)
        libz.so.1 => /lib64/libz.so.1 (0x00007f63e69e9000)
        libbz2.so.1 => /lib64/libbz2.so.1 (0x00007f63e69d5000)
        libpng16.so.16 => /lib64/libpng16.so.16 (0x00007f63e5ef0000)
        libharfbuzz.so.0 => /lib64/libharfbuzz.so.0 (0x00007f63e5dd4000)
        libbrotlidec.so.1 => /lib64/libbrotlidec.so.1 (0x00007f63e69c7000)
        libxml2.so.2 => /lib64/libxml2.so.2 (0x00007f63e5c75000)
        libglib-2.0.so.0 => /lib64/libglib-2.0.so.0 (0x00007f63e5b27000)
        libgraphite2.so.3 => /lib64/libgraphite2.so.3 (0x00007f63e5b07000)
        libbrotlicommon.so.1 => /lib64/libbrotlicommon.so.1 (0x00007f63e5ae4000)
        liblzma.so.5 => /lib64/liblzma.so.5 (0x00007f63e5ab0000)
        libpcre2-8.so.0 => /lib64/libpcre2-8.so.0 (0x00007f63e5a10000)
```
