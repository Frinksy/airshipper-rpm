Name:           airshipper
Version:        0.7.0
Release:        1%{?dist}
Summary:        Airshipper launcher for Veloren.

License:        GPLv3
URL:            https://github.com/veloren/Airshipper
Source0:        https://github.com/veloren/Airshipper/archive/v%{version}.tar.gz

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: rust
BuildRequires: cargo
BuildRequires: desktop-file-utils
BuildRequires: rust-packaging


%global __cargo_skip_build 0
%global debug_package %{nil}

%description
Airshipper is a launcher for the open-world, open-source multiplayer voxel RPG Veloren.

%prep
%autosetup -n Airshipper-%{version}


%build
cargo build --release --bin airshipper

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
cp target/release/airshipper %{buildroot}%{_bindir}/
desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications              \
client/assets/net.veloren.airshipper.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -D client/assets/net.veloren.airshipper.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -D client/assets/net.veloren.airshipper.metainfo.xml -t %{buildroot}%{_metainfodir}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/net.veloren.airshipper.desktop
%{_datadir}/icons/hicolor/256x256/apps/net.veloren.airshipper.png
%{_metainfodir}/net.veloren.airshipper.metainfo.xml



%changelog
* Sat Apr 09 2022 Adam Blanchet
- Update to airshipper 0.7.0

* Fri Mar 12 2021 Adam Blanchet
- First airshipper package
