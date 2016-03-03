Name:           libbpg
Version:        0.9.6
Release:        2%{?dist}
Summary:        A library of functions for manipulating BPG image format files

Group:          System Environment/Libraries
License:        LGPLv2 and BSD
URL:            http://bellard.org/bpg/
Source0:        http://bellard.org/bpg/%{name}-%{version}.tar.gz

BuildRequires:  libpng-devel, libjpeg-turbo-devel, SDL-devel, SDL_image-devel
BuildRequires:  numactl-libs, numactl-devel, yasm, cmake

%global debug_package %{nil}

%description
BPG (Better Portable Graphics) is a image format whose purpose is to
replace the JPEG image format when quality or file size is an issue. Its
main advantages are:
* High compression ratio. Files are much smaller than JPEG for similar quality.
* Supported by most Web browsers with a small Javascript decoder.
* Based on a subset of the HEVC open video compression standard.
* Supports the same chroma formats as JPEG (grayscale, YCbCr 4:2:0, 4:2:2,
4:4:4) to reduce the losses during the conversion. An alpha channel is
supported. The RGB, YCgCo and CMYK color spaces are also supported.
* Native support of 8 to 14 bits per channel for a higher dynamic range.
* Lossless compression is supported.
* Various metadata (such as EXIF, ICC profile, XMP) can be included.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
make %{?_smp_mflags} LIBS='-lnuma -pthread'

echo RPM_BUILD_ROOT=$RPM_BUILD_ROOT

%install
mkdir -p %{buildroot}%{_bindir}
install -s -m755 bpgdec bpgenc bpgview %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_includedir}
install -m644 bpgenc.h libbpg.h %{buildroot}%{_includedir}

mkdir -p %{buildroot}%{_libdir}
install -s -m644 %{name}.a %{buildroot}%{_libdir}

find %{buildroot} -name '*.la' -or -name '*.a' -delete

%files
%doc doc html post.js
%{_bindir}/bpgdec
%{_bindir}/bpgenc
%{_bindir}/bpgview

%files devel
%{_includedir}/*


%changelog
* Wed Feb 24 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.5-2
- Import from https://copr.fedorainfracloud.org/coprs/red/libbpg/
- Rework, clean.

* Tue Jan 13 2015 Sandro Mathys <red at fedoraproject dot org> - 0.9.5-1
- new upstream release
- partially incompatible with earlier versions, see ChangeLog
- new bpgview tool

* Thu Dec 11 2014 Sandro Mathys <red at fedoraproject dot org> - 0.9.2-1
- new upstream release
- include javascript decoder (post.js)

* Wed Dec 10 2014 Sandro Mathys <red at fedoraproject dot org> - 0.9.1-1
- initial release

