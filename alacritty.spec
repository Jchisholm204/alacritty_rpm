Name:           alacritty
Version:        v0.16.1
Release:        1%{?dist}
Summary:        A cross-platform, OpenGL terminal emulator.

License:        ASL 2.0
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo rust cmake freetype-devel fontconfig-devel libxcb-devel libxkbcommon-devel g++
Requires:       freetype fontconfig libxcb libxkbcommon


%description
Alacritty is a modern terminal emulator that comes with sensible defaults, but allows for extensive configuration. By integrating with other applications, rather than reimplementing their functionality, it manages to provide a flexible set of features with high performance.

%prep
%autosetup


%build
cargo build --release --locked

%install
mkdir -p %{buildroot}%{_bindir}
cp target/release/alacritty %{buildroot}%{_bindir}/
# Add desktop integration
mkdir -p %{buildroot}%{_datadir}/applications
cp extra/linux/Alacritty.desktop %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp extra/logo/alacritty-term.svg %{buildroot}%{_datadir}/pixmaps/Alacritty.svg
cp extra/logo/alacritty-term.svg %{buildroot}%{_datadir}/pixmaps/alacritty-term.svg
cp extra/logo/alacritty-term+scanlines.svg %{buildroot}%{_datadir}/pixmaps/alacritty-term+scanlines.svg
cp extra/logo/alacritty-simple.svg %{buildroot}%{_datadir}/pixmaps/alacritty-simple.svg
# Install Man Pages
mkdir -p %{buildroot}%{_mandir}/man1
cp extra/man/alacritty.1.scd %{buildroot}%{_mandir}/man1/alacritty.1
cp extra/man/alacritty-msg.1.scd %{buildroot}%{_mandir}/man1/alacritty-msg.1
cp extra/man/alacritty.5.scd %{buildroot}%{_mandir}/man1/alacritty.5
cp extra/man/alacritty-bindings.5.scd %{buildroot}%{_mandir}/man1/alacritty-bindings.5

%files
# %license add-license-file-here
# %doc add-docs-here
%{_bindir}/alacritty
%{_datadir}/applications/Alacritty.desktop
%{_datadir}/pixmaps/Alacritty.svg
%{_datadir}/pixmaps/alacritty-term.svg
%{_datadir}/pixmaps/alacritty-term+scanlines.svg
%{_datadir}/pixmaps/alacritty-simple.svg
# Man Pages
%{_mandir}/man1/alacritty.1.gz
%{_mandir}/man1/alacritty-msg.1.gz
%{_mandir}/man1/alacritty.5.gz
%{_mandir}/man1/alacritty-bindings.5.gz

%changelog
* Sat Mar 21 2026 Jacob Chisholm <jacobchisholm1010@gmail.com>
- 
